from fastapi import Request
from pydantic import UUID4

from app.core.custom_exceptions import (
    FillOnlyOneParamError,
    FillSomeIDError,
    ReportExistsError,
    ReportNotExistsError,
    SessionNotExistsError,
)
from app.core.models.pydantic_models import ReportBase
from app.core.schemas.repo_protocols import (
    ReportRepoProtocol,
)
from app.core.schemas.service_protocols import CommonServiceProtocol


class PostReportService:
    def __init__(
        self,
        report_repo: ReportRepoProtocol,
    ) -> None:
        self._report_repo = report_repo

    async def __call__(self, report_data: ReportBase) -> UUID4:
        check_session_exists = await self._report_repo.check_session_exists(
            report_data.session_id
        )
        if not check_session_exists:
            raise SessionNotExistsError

        check_report_for_session_exists = (
            await self._report_repo.check_report_for_session_exists(
                report_data.session_id
            )
        )
        if check_report_for_session_exists:
            raise ReportExistsError

        return await self._report_repo.create_report(report_data)


class GetReportService:
    def __init__(self, report_repo: ReportRepoProtocol) -> None:
        self._report_repo = report_repo

    async def __call__(
        self, session_id: UUID4 | None = None, report_id: UUID4 | None = None
    ) -> ReportBase:
        if session_id and report_id:
            raise FillOnlyOneParamError
        if not session_id and not report_id:
            raise FillSomeIDError

        if session_id:
            if not await self._report_repo.check_session_exists(session_id):
                raise SessionNotExistsError

            report = await self._report_repo.get_report_by_id(session_id=session_id)
        elif report_id:
            if not await self._report_repo.check_report_exists(report_id):
                raise ReportNotExistsError

            report = await self._report_repo.get_report_by_id(report_id=report_id)

        if not report:
            raise ReportNotExistsError

        return ReportBase.model_validate(report)


class GetAllUserReportsService:
    def __init__(
        self,
        report_repo: ReportRepoProtocol,
        common_service: CommonServiceProtocol,
    ) -> None:
        self._report_repo = report_repo
        self._common_service = common_service

    async def __call__(self, request: Request) -> list[ReportBase]:
        user_id = await self._common_service._get_user_id(request)

        reports = await self._report_repo.get_all_user_reports(user_id)
        return reports
