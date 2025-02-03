from typing import Protocol

from fastapi import Request

from app.core.models.pydantic_models import GetUser


class GetUserServiceProtocol(Protocol):
    async def __call__(self, request: Request) -> GetUser:
        """Retrieve user's info"""
        pass
