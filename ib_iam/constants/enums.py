from enum import Enum


class StatusCode(Enum):
    NOT_FOUND = 404
    BAD_REQUEST = 400
    FORBIDDEN = 403
    SUCCESS = 200
