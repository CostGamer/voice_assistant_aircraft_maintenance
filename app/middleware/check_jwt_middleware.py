from typing import Any

import jwt
from fastapi import Request, status
from jwt.exceptions import InvalidTokenError
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from starlette.types import ASGIApp

from app.core.configs import all_settings
from app.core.configs.settings import ACCESS_TOKEN, TOKEN_TYPE_FIELD
from app.core.custom_exceptions import ExpectAccessTokenError, MissingOrBadJWTError


class CheckJWTAccessMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)
        self.excluded_paths = ["/docs", "/openapi.json", "/v1/auth"]

    async def dispatch(self, request: Request, call_next: Any) -> Any:
        if any(request.url.path.startswith(path) for path in self.excluded_paths):
            return await call_next(request)

        try:
            token = request.headers.get("Authorization")
            if not token or not token.startswith("Bearer "):
                raise MissingOrBadJWTError
            token = token.split(" ", 1)[1]

            try:
                token_payload: dict = await jwt.decode(
                    token, all_settings.jwt.jwt_secret, all_settings.jwt.jwt_algorithm
                )
            except Exception:
                raise InvalidTokenError

            token_type = token_payload.get(TOKEN_TYPE_FIELD)
            if token_type != ACCESS_TOKEN:
                raise ExpectAccessTokenError

        except (InvalidTokenError, MissingOrBadJWTError):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Invalid JWT"},
            )
        except ExpectAccessTokenError:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"detail": "Invalid JWT type"},
            )

        response = await call_next(request)
        return response
