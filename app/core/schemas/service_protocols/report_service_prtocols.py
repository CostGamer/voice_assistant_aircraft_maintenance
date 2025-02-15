from typing import Protocol

from fastapi import Request
from pydantic import UUID4

from app.core.models.pydantic_models import ReportBase


class PostReportServiceProtocol(Protocol):
    async def __call__(self, report_data: ReportBase) -> UUID4:
        """Generate report"""
        pass


class GetReportServiceProtocol(Protocol):
    async def __call__(
        self, session_id: UUID4 | None = None, report_id: UUID4 | None = None
    ) -> ReportBase:
        """Fetch report by ID of the session or report itself"""
        pass


class GetAllUserReportsServiceProtocol(Protocol):
    async def __call__(self, request: Request) -> list[ReportBase]:
        """Fetch all users reports"""
        pass
