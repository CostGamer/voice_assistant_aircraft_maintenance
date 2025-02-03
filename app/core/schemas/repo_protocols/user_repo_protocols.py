from typing import Protocol
from uuid import UUID

from app.core.models.pydantic_models import Aircrafts, Airlines, User


class UserRepoProtocol(Protocol):
    async def get_user_data(self, user_id: UUID) -> User:
        """Get user data by user ID"""
        pass

    async def get_all_airlines_related_to_user(self, user_id: UUID) -> list[Airlines]:
        """Get all airlines associated with the user"""
        pass

    async def get_all_aircraft_related_to_user(self, user_id: UUID) -> list[Aircrafts]:
        """Get all aircraft associated with the user"""
        pass
