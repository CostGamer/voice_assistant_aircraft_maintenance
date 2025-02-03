from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, UploadFile

from app.api.exception_responses.responses import (
    post_recognition_responses,
    post_synthesize_responses,
)
from app.core.schemas.service_protocols import (
    RecognitionServiceProtocol,
    SynthesizeServiceProtocol,
)

voice_router = APIRouter(prefix="/voice", tags=["voice"])


@voice_router.post(
    "/synthesize",
    responses=post_synthesize_responses,
    description="Synthesize the speach",
)
@inject
async def synthesize_speach(
    text: str,
    synthesize_service: FromDishka[SynthesizeServiceProtocol],
) -> None:
    await synthesize_service(text)


@voice_router.post(
    "/recognize",
    responses=post_recognition_responses,
    response_model=str,
    description="Recognize speach",
)
@inject
async def recognize_speach(
    file: UploadFile,
    recognize_service: FromDishka[RecognitionServiceProtocol],
) -> str:
    return await recognize_service(file)
