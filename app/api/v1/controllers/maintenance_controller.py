from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Request

from app.api.exception_responses.responses import (
    get_aircraft_maintenance_info_responses,
)
from app.core.models.pydantic_models import GetAircraftParts
from app.core.schemas.service_protocols import (
    MaintenanceServiceProtocol,
)

maintenance_router = APIRouter(prefix="/maintenance", tags=["maintenance"])


@maintenance_router.get(
    "/aircraft_maintenance",
    response_model=list[GetAircraftParts],
    responses=get_aircraft_maintenance_info_responses,
    description="Info about aircraft maintenance",
)
@inject
async def get_aircraft_maintenance_info(
    request: Request,
    aircraft_registration_number: str,
    get_maintenance_service: FromDishka[MaintenanceServiceProtocol],
) -> list[GetAircraftParts]:
    return await get_maintenance_service(aircraft_registration_number, request)
