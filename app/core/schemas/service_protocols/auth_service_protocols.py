from typing import Protocol

from fastapi import Response
from pydantic import UUID4

from app.core.models.pydantic_models import JWTTokenInfo, RegisterUser


class RegisterAuthServiceProtocol(Protocol):
    async def __call__(self, user_data: RegisterUser) -> UUID4:
        """Handle user registration by validating and saving the user data, and return the unique ID of the registered user"""
        pass


class LoginAuthServiceProtocol(Protocol):
    async def __call__(
        self,
        login: str,
        password: str,
        response: Response,
    ) -> JWTTokenInfo:
        """Authenticate a user by validating the provided login and password, and return JWT token information if successful"""
        pass


class ReissueTokenServiceProtocol(Protocol):
    async def __call__(
        self,
        token: str,
        response: Response,
    ) -> JWTTokenInfo:
        """Reissue a new JWT token based on the provided token (e.g., a refresh token) and return the updated token information"""
        pass
