import enum

from ib_common.constants import BaseEnumClass


class StatusCode(BaseEnumClass, enum.Enum):
    UNAUTHORIZED = 401
    BAD_REQUEST = 400
    NOT_FOUND = 404
    FORBIDDEN = 403
    SUCCESS = 200
    SUCCESS_CREATE = 201


class Searchable(enum.Enum):
    CITY = "CITY"
    STATE = "STATE"
    COUNTRY = "COUNTRY"
    VENDOR = "VENDOR"
    USER = "USER"
    COMPANY = "COMPANY"
    TEAM = "TEAM"
    DISTRICT = "DISTRICT"
