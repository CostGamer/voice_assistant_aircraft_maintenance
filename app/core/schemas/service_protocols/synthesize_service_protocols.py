from typing import Protocol


class SynthesizeServiceProtocol(Protocol):
    async def __call__(self, text: str) -> None:
        """Save generated audio to file"""
        pass

    async def synthesize(self, text: str) -> bytes:
        """Synthesize speech and return audio data"""
        pass

    async def save_to_file(self, audio_data: bytes) -> None:
        """Save audio file locally"""
        pass

    def play_audio(self, audio_data: bytes) -> None:
        """Play generated audio"""
        pass
