from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Query, Request
from pydantic import UUID4

from app.api.exception_responses.responses import (
    get_all_report_exceptions_responses,
    get_report_responses,
    post_report_responses,
)
from app.core.models.pydantic_models import ReportBase
from app.core.schemas.service_protocols import (
    GetAllUserReportsServiceProtocol,
    GetReportServiceProtocol,
    PostReportServiceProtocol,
)

report_router = APIRouter(prefix="/report", tags=["report"])


@report_router.post(
    "/generate",
    response_model=UUID4,
    responses=post_report_responses,
    description="Generate and insert report after session completion",
)
@inject
async def post_report(
    report_data: ReportBase,
    get_report_service: FromDishka[PostReportServiceProtocol],
) -> UUID4:
    return await get_report_service(report_data)


@report_router.get(
    "/get",
    response_model=ReportBase,
    responses=get_report_responses,
    description="Get exact report by session_id or report_id",
)
@inject
async def get_report(
    get_report_service: FromDishka[GetReportServiceProtocol],
    session_id: UUID4 | None = Query(None, description="Session ID of the report"),
    report_id: UUID4 | None = Query(None, description="Report ID"),
) -> ReportBase:
    return await get_report_service(session_id, report_id)


@report_router.get(
    "/all",
    response_model=list[ReportBase],
    responses=get_all_report_exceptions_responses,
    description="Get all user reports",
)
@inject
async def get_all_user_report(
    request: Request,
    get_report_service: FromDishka[GetAllUserReportsServiceProtocol],
) -> list[ReportBase]:
    return await get_report_service(request)
