from http import HTTPStatus
from typing import Any


def create_error_responses(
    error_responses: dict[int, dict[str, dict[str, Any]]]
) -> dict:
    """Generates error response schemas for an API based on provided error examples.

    This function takes a dictionary of error status codes and their associated examples,
    then constructs a response schema for each status code in a format compatible with OpenAPI.

    Args:
        error_responses (dict[int, dict[str, dict[str, Any]]]): A dictionary where the keys are
                                                              HTTP status codes (integers) and the values
                                                              are dictionaries containing response examples
                                                              for each status code.

    Returns:
        dict: A dictionary of response schemas for each error status code, where the keys are status codes
              and the values are response descriptions and examples formatted for OpenAPI specification.
    """
    responses = {}

    for status_code, examples in error_responses.items():
        description = HTTPStatus(status_code).phrase
        responses[status_code] = {
            "description": description,
            "content": {"application/json": {"examples": examples}},
        }

    return responses


get_user_register_exceptions = {
    400: {
        "user_already_exists_error": {
            "summary": "UserWithThisLoginExistsError",
            "value": {"detail": "This login already in the system"},
        },
    }
}

get_user_login_exceptions = {
    400: {
        "invalid_username_password_error": {
            "summary": "InvalidUsernameOrPasswordError",
            "value": {"detail": "Invalid password or username"},
        },
    }
}

get_token_reissue_exceptions = {
    400: {
        "invalid_jwt_error": {
            "summary": "InvalidTokenError",
            "value": {"detail": "Invalid jwt"},
        },
    },
    409: {
        "refresh_token_expect_error": {
            "summary": "ExpectRefreshTokenError",
            "value": {"detail": "Expect refresh jwt"},
        },
    },
}

post_synthesize_exceptions = {
    400: {
        "speach_generation_error": {
            "summary": "SpeachGenerationError",
            "value": {"detail": "Speach can not generated"},
        },
        "expect_access_token_error": {
            "summary": "ExpectAccessTokenError",
            "value": {"detail": "Invalid JWT type"},
        },
        "is_directory_error": {
            "summary": "IsADirectoryError",
            "value": {"detail": "Is a directory, not a file"},
        },
    },
    401: {
        "invalid_token_error": {
            "summary": "InvalidTokenError",
            "value": {"detail": "Invalid JWT"},
        },
        "missing_or_bad_jwt_error": {
            "summary": "MissingOrBadJWTError",
            "value": {"detail": "Invalid JWT"},
        },
    },
}

get_user_info_exceptions = {
    400: {
        "expect_access_token_error": {
            "summary": "ExpectAccessTokenError",
            "value": {"detail": "Invalid JWT type"},
        },
    },
    401: {
        "invalid_token_error": {
            "summary": "InvalidTokenError",
            "value": {"detail": "Invalid JWT"},
        },
        "missing_or_bad_jwt_error": {
            "summary": "MissingOrBadJWTError",
            "value": {"detail": "Invalid JWT"},
        },
    },
}


get_user_register_responses = create_error_responses(get_user_register_exceptions)
get_user_login_responses = create_error_responses(get_user_login_exceptions)
get_token_reissue_responses = create_error_responses(get_token_reissue_exceptions)
post_synthesize_responses = create_error_responses(post_synthesize_exceptions)
get_user_info_responses = create_error_responses(get_user_info_exceptions)
