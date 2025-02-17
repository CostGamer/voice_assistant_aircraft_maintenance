import asyncio

from fastapi import Request

from app.core.custom_exceptions import UserHasNotPermissionToAircraftError
from app.core.models.pydantic_models import GetAircraftParts
from app.core.schemas.repo_protocols import MaintenanceRepoProtocol
from app.core.schemas.service_protocols import CommonServiceProtocol


class MaintenanceService:
    def __init__(
        self,
        maintenance_repo: MaintenanceRepoProtocol,
        common_service: CommonServiceProtocol,
    ) -> None:
        self._maintenance_repo = maintenance_repo
        self._common_service = common_service

    async def __call__(
        self, aircraft_registration_number: str, request: Request
    ) -> list[GetAircraftParts]:
        user_id = await self._common_service._get_user_id(request)
        aircraft_id = (
            await self._maintenance_repo.check_the_user_ability_to_fetch_aircraft(
                aircraft_registration_number, user_id
            )
        )

        if not aircraft_id:
            raise UserHasNotPermissionToAircraftError

        all_aircraft_parts = await self._maintenance_repo.get_aircraft_parts(
            aircraft_id
        )

        maintenance_tasks = await asyncio.gather(
            *(
                self._maintenance_repo.get_maintenance_steps(part.id)
                for part in all_aircraft_parts
            )
        )

        return [
            GetAircraftParts(
                id=part.id,
                name=part.name,
                description=part.description,
                serial_number=part.serial_number,
                maintaince_steps=steps,
            )
            for part, steps in zip(all_aircraft_parts, maintenance_tasks)
        ]
