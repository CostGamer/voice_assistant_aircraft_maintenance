class UserWithThisLoginExistsError(Exception):
    pass


class ExpectRefreshTokenError(Exception):
    pass


class InvalidUsernameOrPasswordError(Exception):
    pass
