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
            "value": {"detail": "Speach can not be generated"},
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

post_recognition_exceptions = {
    400: {
        "speach_recognition_error": {
            "summary": "SpeachRecognitionError",
            "value": {"detail": "The file can not be recognized"},
        },
        "expect_access_token_error": {
            "summary": "ExpectAccessTokenError",
            "value": {"detail": "Invalid JWT type"},
        },
        "format_error": {
            "summary": "FormatError",
            "value": {"detail": "The file format is incorrect"},
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

get_aircraft_maintenance_info_exceptions = {
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
    403: {
        "no_permission_error": {
            "summary": "UserHasNotPermissionToAircraftError",
            "value": {"detail": "User has not permission to this aircraft"},
        },
    },
}

post_session_exceptions = {
    400: {
        "expect_access_token_error": {
            "summary": "ExpectAccessTokenError",
            "value": {"detail": "Invalid JWT type"},
        },
        "open_session_error": {
            "summary": "HaveOpenSessionError",
            "value": {"detail": "You already have open session"},
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
    403: {
        "no_permission_error": {
            "summary": "UserHasNotPermissionToAircraftError",
            "value": {"detail": "User has not permission to this aircraft"},
        },
    },
}

get_current_session_exceptions = {
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
    404: {
        "session_not_found_error": {
            "summary": "UserHasNoSessionError",
            "value": {"detail": "This user has no open session right now"},
        },
    },
}

get_completed_sessions_exceptions = {
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

patch_maintenance_step_exceptions = {
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
    404: {
        "step_not_found_error": {
            "summary": "StepNotExistsError",
            "value": {"detail": "This maintenance steps does not exist"},
        },
        "aircraft_part_not_found_error": {
            "summary": "AircraftPartNotExistsError",
            "value": {"detail": "This aircraft part does not exist"},
        },
    },
}

patch_complete_session_exceptions = {
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
    404: {
        "no_open_session_error": {
            "summary": "NoResultFound",
            "value": {"detail": "There is no open session"},
        },
    },
}

post_report_exceptions = {
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
    404: {
        "session_not_found_error": {
            "summary": "SessionNotExistsError",
            "value": {"detail": "This session does not exist"},
        },
    },
    409: {
        "report_exists_error": {
            "summary": "ReportExistsError",
            "value": {"detail": "Report for this session is already exists"},
        },
    },
}

get_report_exceptions = {
    400: {
        "expect_access_token_error": {
            "summary": "ExpectAccessTokenError",
            "value": {"detail": "Invalid JWT type"},
        },
        "fill_some_gap_error": {
            "summary": "FillSomeIDError",
            "value": {"detail": "You have to fill one of two params"},
        },
        "fill_only_one_gap_error": {
            "summary": "FillOnlyOneParamError",
            "value": {"detail": "You have to fill only one param"},
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
    404: {
        "session_not_found_error": {
            "summary": "SessionNotExistsError",
            "value": {"detail": "This session does not exist"},
        },
        "report_not_found_error": {
            "summary": "ReportNotExistsError",
            "value": {"detail": "This report does not exist"},
        },
    },
}

get_all_report_exceptions = {
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
post_recognition_responses = create_error_responses(post_recognition_exceptions)
get_aircraft_maintenance_info_responses = create_error_responses(
    get_aircraft_maintenance_info_exceptions
)
post_session_responses = create_error_responses(post_session_exceptions)
get_current_session_responses = create_error_responses(get_current_session_exceptions)
get_completed_sessions_responses = create_error_responses(
    get_completed_sessions_exceptions
)
patch_maintenance_step_responses = create_error_responses(
    patch_maintenance_step_exceptions
)
patch_complete_session_responses = create_error_responses(
    patch_complete_session_exceptions
)
post_report_responses = create_error_responses(post_report_exceptions)
get_report_responses = create_error_responses(get_report_exceptions)
get_all_report_exceptions_responses = create_error_responses(get_all_report_exceptions)
