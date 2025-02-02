from io import BytesIO

import aiohttp
from pydub import AudioSegment
from pydub.playback import play

from app.core.configs.settings import Settings, YandexSettings
from app.core.custom_exceptions import SpeachGenerationError
from app.core.schemas.service_protocols import FileServiceProtocol


class SynthesizeService:
    def __init__(self, settings: Settings, file_service: FileServiceProtocol) -> None:
        self._yandex_settings: YandexSettings = settings.yandex
        self._file_service = file_service

    async def __call__(self, text: str) -> None:
        audio_data = await self.synthesize(text)
        await self.save_to_file(audio_data)
        self.play_audio(audio_data)

    async def synthesize(self, text: str) -> bytes:
        url = self._yandex_settings.yandex_synthesize_url
        headers = {"Authorization": f"Api-Key {self._yandex_settings.yandex_api_key}"}
        data = {
            "text": text,
            "format": self._yandex_settings.yandex_format,
            "lang": "ru-RU",
            "voice": self._yandex_settings.yandex_voice,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=data) as resp:
                if resp.status != 200:
                    raise SpeachGenerationError
                return await resp.read()

    async def save_to_file(self, audio_data: bytes) -> None:
        await self._file_service.save_file(audio_data)

    # TODO: в будущем нужен асинхронный вариант
    def play_audio(self, audio_data: bytes) -> None:
        audio = AudioSegment.from_file(BytesIO(audio_data), format="mp3")
        play(audio)
