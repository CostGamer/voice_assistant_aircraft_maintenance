from io import BytesIO
from typing import Protocol

from fastapi import UploadFile


class RecognitionServiceProtocol(Protocol):
    async def __call__(self, file: UploadFile) -> str:
        """Process the downloaded audio file and return its text transcript"""
        pass

    async def recognize(self, audio_data: BytesIO) -> str:
        """Send an audio file to the Yandex server and receive the recognition result"""
        pass

    async def save_to_file(self, audio_data: bytes) -> None:
        """Save audio file locally"""
        pass
