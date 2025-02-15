from typing import Protocol

from pydantic import UUID4

from app.core.models.pydantic_models import ReportBase
from app.core.models.sqlalchemy_models.report_sql_models import Report


class ReportRepoProtocol(Protocol):
    async def create_report(self, report_data: ReportBase) -> UUID4:
        """Generate report"""
        pass

    async def check_session_exists(self, session_id: UUID4) -> bool:
        """Check the correctness of the session ID"""
        pass

    async def get_report_by_id(
        self, session_id: UUID4 | None = None, report_id: UUID4 | None = None
    ) -> Report | None:
        """Fetch the report by session or report ID"""
        pass

    async def get_all_user_reports(self, user_id: UUID4) -> list[ReportBase]:
        """Fetch all possible user reports"""
        pass

    async def check_report_exists(self, report_id: UUID4) -> bool:
        """Check the correctness of the report ID"""
        pass

    async def check_report_for_session_exists(self, session_id: UUID4) -> bool:
        """Check if the report for session is already exists"""
        pass
