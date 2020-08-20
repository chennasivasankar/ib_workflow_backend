from enum import Enum

from ib_common.constants import BaseEnumClass


class EntityType(BaseEnumClass, Enum):
    TASK = "TASK"
    COLUMN = "COLUMN"
    BOARD = "BOARD"


class TimerEntityType(BaseEnumClass, Enum):
    STAGE_TASK = "STAGE_TASK"
    STAGE = "STAGE"


class StatusCode(Enum):
    SUCCESS = 200
    NOT_FOUND = 404
    BAD_REQUEST = 400
    FORBIDDEN = 403
    CREATED = 201
