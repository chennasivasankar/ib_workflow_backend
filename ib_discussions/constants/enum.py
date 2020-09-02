from enum import Enum

from ib_common.constants import BaseEnumClass


class EntityType(BaseEnumClass, Enum):
    TASK = "TASK"
    COLUMN = "COLUMN"
    BOARD = "BOARD"


class StatusCode(Enum):
    SUCCESS = 200
    NOT_FOUND = 404
    BAD_REQUEST = 400
    FORBIDDEN = 403
    CREATED = 201


class SortByEnum(Enum):
    LATEST = "LATEST"


class FilterByEnum(Enum):
    ALL = "ALL"
    POSTED_BY_ME = "POSTED_BY_ME"
    CLARIFIED = "CLARIFIED"
    NOT_CLARIFIED = "NOT_CLARIFIED"


class OrderByEnum(Enum):
    ASC = "ASC"
    DESC = "DESC"


class MultimediaFormat(Enum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
