from typing import Protocol

from fastapi import Request
from pydantic import UUID4

from app.core.models.pydantic_models import GetSession, PostSession, PutStepSession


class PostSessionServiceProtocol(Protocol):
    async def __call__(self, request: Request, session_data: PostSession) -> UUID4:
        """Generate session while calling"""
        pass


class GetCurrentSessionServiceProtocol(Protocol):
    async def __call__(self, request: Request) -> GetSession:
        """Show current user session"""
        pass


class GetCompletedUserSessionServiceProtocol(Protocol):
    async def __call__(self, request: Request) -> list[GetSession]:
        """Show session's that user is already complited"""
        pass


class PatchStepSessionServiceProtocol(Protocol):
    async def __call__(
        self,
        request: Request,
        step_data: PutStepSession,
    ) -> GetSession:
        """Update steps and content JSON"""
        pass

    async def _update_content_json(
        self, dialog_history: dict, step_data: PutStepSession
    ) -> dict:
        """Update the JSON od the dialog"""
        pass


class PatchCompletedSessionServiceProtocol(Protocol):
    async def __call__(
        self,
        request: Request,
    ) -> GetSession:
        """Service that complete current session"""
        pass
