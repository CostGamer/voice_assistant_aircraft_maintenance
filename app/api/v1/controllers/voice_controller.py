from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.api.exception_responses.responses import (
    post_synthesize_responses,
)
from app.core.schemas.service_protocols import (
    SynthesizeServiceProtocol,
)

voice_router = APIRouter(prefix="/voice", tags=["voice"])


@voice_router.post(
    "/synthesize",
    responses=post_synthesize_responses,
    description="Synthesize the speach",
)
@inject
async def register_user(
    text: str,
    synthesize_service: FromDishka[SynthesizeServiceProtocol],
) -> None:
    await synthesize_service(text)
