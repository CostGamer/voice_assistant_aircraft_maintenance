from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Request
from pydantic import UUID4

from app.api.exception_responses.responses import (
    get_completed_sessions_responses,
    get_current_session_responses,
    patch_complete_session_responses,
    patch_maintenance_step_responses,
    post_session_responses,
)
from app.core.models.pydantic_models import (
    GetComplitedSession,
    GetSession,
    PostSession,
    PutStepSession,
)
from app.core.schemas.service_protocols import (
    GetCompletedUserSessionServiceProtocol,
    GetCurrentSessionServiceProtocol,
    PatchCompletedSessionServiceProtocol,
    PatchStepSessionServiceProtocol,
    PostSessionServiceProtocol,
)

session_router = APIRouter(prefix="/session", tags=["session"])


@session_router.post(
    "/generate",
    response_model=UUID4,
    responses=post_session_responses,
    description="Generate a new session",
)
@inject
async def post_session(
    request: Request,
    session_data: PostSession,
    get_session_service: FromDishka[PostSessionServiceProtocol],
) -> UUID4:
    return await get_session_service(request, session_data)


@session_router.get(
    "/current",
    response_model=GetSession,
    responses=get_current_session_responses,
    description="Fetch current session",
)
@inject
async def get_current_session(
    request: Request,
    get_session_service: FromDishka[GetCurrentSessionServiceProtocol],
) -> GetSession:
    return await get_session_service(request)


@session_router.get(
    "/complited",
    response_model=list[GetSession],
    responses=get_completed_sessions_responses,
    description="Fetch all complited sessions",
)
@inject
async def get_completed_sessions(
    request: Request,
    get_session_service: FromDishka[GetCompletedUserSessionServiceProtocol],
) -> list[GetSession]:
    return await get_session_service(request)


@session_router.patch(
    "/step",
    response_model=GetSession,
    responses=patch_maintenance_step_responses,
    description="Post step info of the complited maintenance step",
)
@inject
async def post_maintenance_step(
    request: Request,
    step_data: PutStepSession,
    get_session_service: FromDishka[PatchStepSessionServiceProtocol],
) -> GetSession:
    return await get_session_service(request, step_data)


@session_router.patch(
    "/complete",
    response_model=GetComplitedSession,
    responses=patch_complete_session_responses,
    description="Finish current session",
)
@inject
async def complete_session(
    request: Request,
    get_session_service: FromDishka[PatchCompletedSessionServiceProtocol],
) -> GetComplitedSession:
    return await get_session_service(request)
