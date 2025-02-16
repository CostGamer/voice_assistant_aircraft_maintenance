from collections.abc import AsyncIterator
from typing import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.pool import NullPool

from app.core.configs import all_settings
from app.core.models.sqlalchemy_models import Base
from app.main import setup_app


@pytest.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    print(f"DB URI: {all_settings.database.db_uri}")
    app = setup_app()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        yield ac


@pytest.fixture(scope="session")
async def async_engine() -> AsyncIterator[AsyncEngine]:
    engine = create_async_engine(
        all_settings.database.db_uri, echo=True, future=True, poolclass=NullPool
    )
    try:
        yield engine
    finally:
        await engine.dispose()


@pytest.fixture(autouse=True, scope="session")
async def prepare_database(async_engine: AsyncEngine) -> AsyncGenerator:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
async def register_token(
    async_client: AsyncClient,
) -> AsyncGenerator[tuple[str, str], None]:
    login, password, name = ["test", "test", "test"]
    register_data = {"login": login, "password": password, "name": name}

    login_response = await async_client.post("/v1/auth/register", json=register_data)

    assert login_response.status_code == 200, (
        f"Unexpected status code: {login_response.status_code}. "
        f"Response: {login_response.text}"
    )

    yield login, password


@pytest.fixture(scope="session")
async def authenticated_token(
    async_client: AsyncClient, register_token: tuple[str, str]
) -> AsyncGenerator[str, None]:
    login_response = await async_client.get(
        "/v1/auth/login",
        params={"login": register_token[0], "password": register_token[1]},
    )

    assert login_response.status_code == 200, (
        f"Unexpected status code: {login_response.status_code}. "
        f"Response: {login_response.text}"
    )

    response_json = login_response.json()

    assert response_json, "No tokens found in response"

    api_key_token = response_json.get("access_token")
    assert api_key_token, "API key token not found in response"

    yield api_key_token


@pytest.fixture(scope="session", autouse=True)
async def set_auth_headers(
    async_client: AsyncClient, authenticated_token: str
) -> AsyncGenerator[AsyncClient, None]:
    async_client.headers.update({"Authorization": f"Bearer {authenticated_token}"})
    yield async_client
