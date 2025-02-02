from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.core.custom_exceptions import (
    ExpectRefreshTokenError,
    InvalidUsernameOrPasswordError,
    SpeachGenerationError,
    UserWithThisLoginExistsError,
)


async def invalid_username_password_error(
    request: Request, exc: InvalidUsernameOrPasswordError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Invalid password or username"},
    )


async def user_already_exists_error(
    request: Request, exc: UserWithThisLoginExistsError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "This login already in the system"},
    )


async def refresh_token_expect_error(
    request: Request, exc: ExpectRefreshTokenError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": "Expect refresh jwt"},
    )


async def speach_generation_error(
    request: Request, exc: SpeachGenerationError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Speach can not generated"},
    )


async def is_directory_error(request: Request, exc: IsADirectoryError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Is a directory, not a file"},
    )
