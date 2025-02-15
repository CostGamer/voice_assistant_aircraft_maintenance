from typing import Protocol

from pydantic import UUID4

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

    async def get_user_aircraft(
        self, aircraft_registration_number: str | None, user_id: UUID4
    ) -> list | None:
        """Check the user ability to maintaince this aircraft & fetch user_aircraft_id"""
        pass
