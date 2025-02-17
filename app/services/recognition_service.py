from io import BytesIO

import speech_recognition as sr
from fastapi import UploadFile
from pydub import AudioSegment

from app.core.configs.settings import Settings
from app.core.custom_exceptions import FormatError, SpeachRecognitionError
from app.core.schemas.service_protocols import FileServiceProtocol


class RecognitionService:
    def __init__(self, settings: Settings, file_service: FileServiceProtocol) -> None:
        self._settings = settings
        self._file_service = file_service

    async def __call__(self, file: UploadFile) -> str:
        audio_data = await file.read()

        try:
            audio_segment = AudioSegment.from_file(BytesIO(audio_data))
            audio_segment = (
                audio_segment.set_frame_rate(16000).set_channels(1).set_sample_width(2)
            )
            wav_io = BytesIO()
            audio_segment.export(wav_io, format="wav")
            wav_io.seek(0)
        except Exception:
            raise FormatError

        res = await self.recognize(wav_io)
        await self.save_to_file(wav_io.getvalue())
        return res

    async def save_to_file(self, audio_data: bytes) -> None:
        await self._file_service.save_file(audio_data)

    async def recognize(self, audio_file: BytesIO) -> str:
        recognizer = sr.Recognizer()

        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            return text
        except sr.UnknownValueError:
            raise SpeachRecognitionError
