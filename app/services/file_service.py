import os
from datetime import datetime

import aiofiles

from app.core.configs import all_settings


class FileService:
    def __init__(self) -> None:
        self.storage_path = os.path.expanduser(
            all_settings.yandex.yandex_voice_temporary_storage
        )

    async def _ensure_directory_exists(self) -> None:
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path, exist_ok=True)

    async def _validate_file_path(self, file_path: str) -> None:
        if os.path.isdir(file_path):
            raise IsADirectoryError

    async def save_file(self, data: bytes) -> str:
        await self._ensure_directory_exists()

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{timestamp}.mp3"
        file_path = os.path.join(self.storage_path, file_name)

        await self._validate_file_path(file_path)

        async with aiofiles.open(file_path, "wb") as f:
            await f.write(data)

        return file_path
