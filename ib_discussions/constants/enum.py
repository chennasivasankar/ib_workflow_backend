from enum import Enum


class EntityType(Enum):
    TASK = "TASK"
    COLUMN = "COLUMN"
    BOARD = "BOARD"


class StatusCode(Enum):
    SUCCESS = 200
    NOT_FOUND = 404
    BAD_REQUEST = 400
    FORBIDDEN = 403
    CREATED = 201
