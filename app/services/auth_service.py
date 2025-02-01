from fastapi import Response
from jwt.exceptions import InvalidTokenError
from pydantic import UUID4

from app.core.configs.settings import REFRESH_TOKEN
from app.core.custom_exceptions import (
    ExpectRefreshTokenError,
    UserWithThisLoginExistsError,
)
from app.core.models.pydantic_models import JWTTokenInfo, RegisterUser
from app.core.schemas.repo_protocols import AuthRepoProtocol, CommonRepoProtocol
from app.core.schemas.service_protocols import JWTServiceProtocol


class RegisterAuthService:
    def __init__(
        self, auth_repo: AuthRepoProtocol, common_repo: CommonRepoProtocol
    ) -> None:
        self._auth_repo = auth_repo
        self._common_repo = common_repo

    async def __call__(self, user_data: RegisterUser) -> UUID4:
        check_user_exists_by_login = await self._common_repo.check_user_exists_by_login(
            user_data.login
        )
        if check_user_exists_by_login:
            raise UserWithThisLoginExistsError

        res = await self._auth_repo.register_user(user_data)
        return res


class LoginAuthService:
    def __init__(self, jwt_service: JWTServiceProtocol) -> None:
        self._jwt_service = jwt_service

    async def __call__(
        self,
        login: str,
        password: str,
        response: Response,
    ) -> JWTTokenInfo:
        user = await self._jwt_service.validate_auth_user(login, password)
        access_token = await self._jwt_service.create_access_token(user.id)
        refresh_token = await self._jwt_service.create_refresh_token(user.id)

        response.set_cookie(
            key="access_token",
            value=f"Bearer {access_token}",
            httponly=True,
            secure=False,
            samesite="lax",
            max_age=3600,
        )
        response.set_cookie(
            key="refresh_token",
            value=f"Bearer {refresh_token}",
            httponly=True,
            secure=False,
            samesite="lax",
            max_age=86400,
        )

        return JWTTokenInfo(access_token=access_token, refresh_token=refresh_token)


class ReissueTokenService:
    def __init__(
        self,
        jwt_service: JWTServiceProtocol,
        common_repo: CommonRepoProtocol,
    ) -> None:
        self._jwt_service = jwt_service
        self._common_repo = common_repo

    async def __call__(
        self,
        token: str,
        response: Response,
    ) -> JWTTokenInfo:
        try:
            token_payload = await self._jwt_service.decode_jwt(token)
        except Exception:
            raise InvalidTokenError

        if not await self._jwt_service.validation_token_type(
            REFRESH_TOKEN, token_payload
        ):
            raise ExpectRefreshTokenError

        user_data = await self._common_repo.get_user_data_by_token_sub(token_payload)
        access_token = await self._jwt_service.create_access_token(user_data.id)

        response.set_cookie(
            key="access_token",
            value=f"Bearer {access_token}",
            httponly=True,
            secure=False,
            samesite="lax",
            max_age=3600,
        )

        return JWTTokenInfo(access_token=access_token)
