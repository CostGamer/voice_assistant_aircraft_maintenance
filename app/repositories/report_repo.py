from datetime import datetime, timezone

from pydantic import UUID4
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.pydantic_models import ReportBase
from app.core.models.sqlalchemy_models import (
    Report,
    Session,
    UsersAircrafts,
)


class ReportRepo:
    def __init__(self, con: AsyncSession) -> None:
        self._con = con

    async def create_report(self, report_data: ReportBase) -> UUID4:
        query = (
            insert(Report)
            .values(
                session_id=report_data.session_id,
                report_type=report_data.report_type,
                content=report_data.content,
                created_at=datetime.now(timezone.utc).isoformat(),
            )
            .returning(Report.id)
        )
        query_res = (await self._con.execute(query)).scalar_one()
        return query_res

    async def check_session_exists(self, session_id: UUID4) -> bool:
        query = select(Session).where(Session.id == session_id)
        query_res = (await self._con.execute(query)).scalar_one_or_none()
        return query_res is not None

    async def get_report_by_id(
        self, session_id: UUID4 | None = None, report_id: UUID4 | None = None
    ) -> Report | None:
        if not session_id and not report_id:
            return None

        query = select(Report).where(
            Report.session_id == session_id if session_id else Report.id == report_id
        )
        return (await self._con.execute(query)).scalar_one_or_none()

    async def get_all_user_reports(self, user_id: UUID4) -> list[ReportBase]:
        query = (
            select(Report)
            .join(Session)
            .join(UsersAircrafts)
            .where(UsersAircrafts.user_id == user_id)
        )
        query_res = (await self._con.execute(query)).scalars().all()
        return [ReportBase.model_validate(res) for res in query_res]

    async def check_report_exists(self, report_id: UUID4) -> bool:
        query = select(Report).where(Report.id == report_id)
        query_res = (await self._con.execute(query)).scalar_one_or_none()
        return query_res is not None

    async def check_report_for_session_exists(self, session_id: UUID4) -> bool:
        query = select(Report).where(Report.session_id == session_id)
        query_res = (await self._con.execute(query)).scalar_one_or_none()
        return query_res is not None
