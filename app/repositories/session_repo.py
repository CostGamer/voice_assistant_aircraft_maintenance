from pydantic import UUID4
from sqlalchemy import and_, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.pydantic_models import (
    GetSession,
    PostSession,
    StatusEnum,
)
from app.core.models.sqlalchemy_models import (
    AircraftPart,
    MaintenanceStep,
    Session,
    UsersAircrafts,
)


class SessionRepo:
    def __init__(self, con: AsyncSession) -> None:
        self._con = con

    async def check_user_active_session(self, user_id: UUID4) -> Session | None:
        query = (
            select(Session)
            .join(UsersAircrafts)
            .where(
                and_(
                    UsersAircrafts.user_id == user_id,
                    Session.status != StatusEnum.COMPLETED,
                )
            )
        )
        query_res = (await self._con.execute(query)).scalar_one_or_none()
        return query_res

    async def create_session(
        self,
        session_data: PostSession,
        users_aircrafts_id: UUID4,
        content: dict,
    ) -> UUID4:
        query = (
            insert(Session)
            .values(
                users_aircrafts_id=users_aircrafts_id,
                name=session_data.name,
                status=session_data.status,
                dialog_history=content,
            )
            .returning(Session.id)
        )
        query_res = (await self._con.execute(query)).scalar_one()
        return query_res

    async def get_current_user_session(self, user_id: UUID4) -> Session | None:
        query = (
            select(Session)
            .join(UsersAircrafts)
            .where(
                and_(
                    UsersAircrafts.user_id == user_id,
                    Session.status != StatusEnum.COMPLETED,
                )
            )
        )
        query_res = (await self._con.execute(query)).scalar_one_or_none()
        return query_res

    async def get_all_completed_session(self, user_id: UUID4) -> list[GetSession]:
        query = (
            select(Session)
            .join(UsersAircrafts)
            .where(
                and_(
                    UsersAircrafts.user_id == user_id,
                    Session.status == StatusEnum.COMPLETED,
                )
            )
        )
        query_res = (await self._con.execute(query)).scalars().all()
        return [GetSession.model_validate(res) for res in query_res]

    async def update_session_info(
        self, user_id: UUID4, current_step_id: UUID4, content: dict
    ) -> GetSession:
        subquery = (
            select(Session.id)
            .join(UsersAircrafts)
            .where(
                and_(
                    UsersAircrafts.user_id == user_id,
                    Session.status != StatusEnum.COMPLETED,
                )
            )
            .scalar_subquery()
        )

        query = (
            update(Session)
            .where(Session.id == subquery)
            .values(current_step_id=current_step_id, dialog_history=content)
            .execution_options(synchronize_session="fetch")
            .returning(Session)
        )

        query_res = (await self._con.execute(query)).scalar_one()
        return GetSession.model_validate(query_res)

    async def check_step_exists(self, step_id: UUID4) -> bool:
        query = select(MaintenanceStep).where(MaintenanceStep.id == step_id)
        query_res = (await self._con.execute(query)).scalar_one_or_none()
        return query_res is not None

    async def check_aircraft_part_exists(self, part_name: str) -> bool:
        query = select(AircraftPart).where(AircraftPart.name == part_name)
        query_res = (await self._con.execute(query)).scalar_one_or_none()
        return query_res is not None

    async def completed_session(self, user_id: UUID4) -> GetSession:
        subquery = (
            select(Session.id)
            .join(UsersAircrafts)
            .where(
                and_(
                    UsersAircrafts.user_id == user_id,
                    Session.status != StatusEnum.COMPLETED,
                )
            )
            .scalar_subquery()
        )

        query = (
            update(Session)
            .where(Session.id == subquery)
            .values(status=StatusEnum.COMPLETED, current_step_id=None)
            .execution_options(synchronize_session="fetch")
            .returning(Session)
        )

        query_res = (await self._con.execute(query)).scalar_one()
        return GetSession.model_validate(query_res)
