from typing import Protocol

from pydantic import UUID4

from app.core.models.pydantic_models import AircraftPart as AirPart
from app.core.models.pydantic_models import Maintance


class MaintenanceRepoProtocol(Protocol):
    async def check_the_user_ability_to_fetch_aircraft(
        self, aircraft_registration_number: str, user_id: UUID4
    ) -> UUID4 | None:
        """Check if the user has access to the aircraft"""
        pass

    async def get_aircraft_parts(self, aircraft_id: UUID4) -> list[AirPart]:
        """Retrieve aircraft parts by aircraft ID"""
        pass

    async def get_maintenance_steps(self, aircraft_part_id: UUID4) -> list[Maintance]:
        """Retrieve maintenance steps for a specific aircraft part"""
        pass
