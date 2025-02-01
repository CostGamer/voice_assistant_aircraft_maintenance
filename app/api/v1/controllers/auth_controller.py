from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Response
from pydantic import UUID4

from app.api.exception_responses.responses import (
    get_token_reissue_responses,
    get_user_login_responses,
    get_user_register_responses,
)
from app.core.models.pydantic_models import JWTTokenInfo, RegisterUser
from app.core.schemas.service_protocols import (
    LoginAuthServiceProtocol,
    RegisterAuthServiceProtocol,
    ReissueTokenServiceProtocol,
)

auth_router = APIRouter(prefix="/auth", tags=["jwt"])


@auth_router.post(
    "/register",
    response_model=UUID4,
    responses=get_user_register_responses,
    description="Registration for users",
)
@inject
async def register_user(
    user_data: RegisterUser,
    register_service: FromDishka[RegisterAuthServiceProtocol],
) -> UUID4:
    return await register_service(user_data)


@auth_router.get(
    "/login",
    response_model=JWTTokenInfo,
    responses=get_user_login_responses,
    description="Login into your account",
)
@inject
async def login_user(
    login: str,
    password: str,
    response: Response,
    login_service: FromDishka[LoginAuthServiceProtocol],
) -> JWTTokenInfo:
    return await login_service(login, password, response)


@auth_router.post(
    "/token/reissue",
    response_model=JWTTokenInfo,
    responses=get_token_reissue_responses,
    description="Generate new access JWT by refresh",
)
@inject
async def get_new_access(
    token: str,
    response: Response,
    login_service: FromDishka[ReissueTokenServiceProtocol],
) -> JWTTokenInfo:
    return await login_service(token, response)
