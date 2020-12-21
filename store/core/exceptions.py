class ApiError(Exception):
    """Generica API Exception"""


class MethodNotAllowed(ApiError):
    """Exceptin raised if the HTTP Method is not allowed"""
