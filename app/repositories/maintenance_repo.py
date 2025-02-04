from logging import getLogger

from pydantic import UUID4
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.pydantic_models import AircraftPart as AirPart
from app.core.models.pydantic_models import Maintance
from app.core.models.sqlalchemy_models import (
    AircraftPart,
    Aircrafts,
    MaintenanceStep,
    UsersAircrafts,
)

logger = getLogger(__name__)


class MaintenanceRepo:
    def __init__(self, con: AsyncSession) -> None:
        self._con = con

    async def check_the_user_ability_to_fetch_aircraft(
        self, aircraft_registration_number: str, user_id: UUID4
    ) -> UUID4 | None:
        query = (
            select(Aircrafts.id)
            .join(UsersAircrafts)
            .where(
                and_(
                    UsersAircrafts.user_id == user_id,
                    Aircrafts.registration_number == aircraft_registration_number,
                )
            )
        )
        query_res = (await self._con.execute(query)).scalar_one_or_none()
        return query_res

    async def get_aircraft_parts(self, aircraft_id: UUID4) -> list[AirPart]:
        query = select(AircraftPart).where(AircraftPart.aircraft_id == aircraft_id)
        query_res = (await self._con.execute(query)).scalars().all()
        return [AirPart.model_validate(part) for part in query_res]

    async def get_maintenance_steps(self, aircraft_part_id: UUID4) -> list[Maintance]:
        query = select(MaintenanceStep).where(
            MaintenanceStep.part_id == aircraft_part_id
        )
        query_res = (await self._con.execute(query)).scalars().all()
        return [
            Maintance.model_validate(part_maintance) for part_maintance in query_res
        ]
