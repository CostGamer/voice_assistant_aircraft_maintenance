from typing import Protocol

from fastapi import Request

from app.core.models.pydantic_models import GetAircraftParts


class MaintenanceServiceProtocol(Protocol):
    async def __call__(
        self, aircraft_registration_number: str, request: Request
    ) -> list[GetAircraftParts]:
        """Retrieve maintaince plan for the aircraft"""
        pass
