from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Request

from app.api.exception_responses.responses import (
    get_user_info_responses,
)
from app.core.models.pydantic_models import GetUser
from app.core.schemas.service_protocols import (
    GetUserServiceProtocol,
)

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get(
    "/user",
    response_model=GetUser,
    responses=get_user_info_responses,
    description="Info about user",
)
@inject
async def get_user_info(
    request: Request,
    get_user_service: FromDishka[GetUserServiceProtocol],
) -> GetUser:
    return await get_user_service(request)
