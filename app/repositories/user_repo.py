from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.pydantic_models import Aircrafts as AircraftsPydantic
from app.core.models.pydantic_models import Airlines as AirlinesPydantic
from app.core.models.pydantic_models import User
from app.core.models.sqlalchemy_models import (
    Aircrafts,
    Airlines,
    Users,
    UsersAircrafts,
    UsersAirlines,
)


class UserRepo:
    def __init__(self, con: AsyncSession) -> None:
        self._con = con

    async def get_user_data(self, user_id: UUID4) -> User:
        query = select(Users).where(Users.id == user_id)
        query_res = (await self._con.execute(query)).scalar_one_or_none()
        return User.model_validate(query_res)

    async def get_all_airlines_related_to_user(
        self, user_id: UUID4
    ) -> list[AirlinesPydantic]:
        query = (
            select(Airlines).join(UsersAirlines).where(UsersAirlines.user_id == user_id)
        )
        query_res = (await self._con.execute(query)).scalars().all()
        return [AirlinesPydantic.model_validate(airline) for airline in query_res]

    async def get_all_aircraft_related_to_user(
        self, user_id: UUID4
    ) -> list[AircraftsPydantic]:
        query = (
            select(Aircrafts)
            .join(UsersAircrafts)
            .where(UsersAircrafts.user_id == user_id)
        )
        query_res = (await self._con.execute(query)).scalars().all()
        return [AircraftsPydantic.model_validate(airline) for airline in query_res]
