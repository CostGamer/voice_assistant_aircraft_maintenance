from pydantic import UUID4
from sqlalchemy import and_, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.pydantic_models import GetSession, PostSession, StatusEnum
from app.core.models.sqlalchemy_models import Session, UsersAircrafts


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
        self, session_data: PostSession, users_aircrafts_id: UUID4
    ) -> UUID4:
        query = (
            insert(Session)
            .values(
                users_aircrafts_id=users_aircrafts_id,
                name=session_data.name,
                status=session_data.status,
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
