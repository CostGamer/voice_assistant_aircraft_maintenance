from typing import Protocol

from app.core.models.pydantic_models import JWTUser


class CommonRepoProtocol(Protocol):
    async def check_user_exists_by_login(self, login: str) -> bool:
        """Check login already in DB"""
        pass

    async def get_user_data(self, login: str) -> JWTUser:
        """Retrieve user's data for JWT"""
        pass

    async def get_user_data_by_token_sub(self, payload: dict) -> JWTUser:
        """Retrieve uses's data from JWT"""
        pass
