from drf_standardized_errors.handler import ExceptionHandler
from rest_framework.exceptions import APIException


class CustomExceptionHandler(ExceptionHandler):
    def format_exception(self, exc: APIException) -> dict:
        msg = "Internal Server Error"
        if exc.status_code == 500:
            exc = APIException(detail=msg)
        return super().format_exception(exc)
