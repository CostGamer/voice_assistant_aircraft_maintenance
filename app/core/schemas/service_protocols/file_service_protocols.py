from typing import Protocol


class FileServiceProtocol(Protocol):
    async def save_file(self, data: bytes) -> str:
        """Save audio data to a file and return the file path"""
        pass

    async def _ensure_directory_exists(self) -> None:
        """Ensure the directory for file storage exists"""
        pass

    async def _validate_file_path(self, file_path: str) -> None:
        """Validate that the file path is not a directory"""
        pass
