import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_user_info(set_auth_headers: AsyncClient) -> None:
    response = await set_auth_headers.get(
        "/v1/user/user",
    )

    assert response.status_code == 200, (
        f"Expected status code 200, but got {response.status_code}. "
        f"Response: {response.text}"
    )

    user_data = response.json()

    assert user_data["login"] == "test"
    assert user_data["name"] == "test"
    assert "airlines" in user_data
    assert "aircrafts" in user_data
