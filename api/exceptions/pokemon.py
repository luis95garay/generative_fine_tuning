from exceptions.base import HTTPException
from responses.response import Responses


class NotProcessingException(HTTPException):
    def __init__(self) -> None:
        super().__init__("Not found", Responses.not_found)


class StillProcessingException(HTTPException):
    def __init__(self) -> None:
        super().__init__("Not ready", Responses.accepted)