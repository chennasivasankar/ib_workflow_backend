import enum
from ib_common.constants import BaseEnumClass


class StatusCode(BaseEnumClass, enum.Enum):
    SUCCESS = 200
    CREATE_SUCCESS = 201
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
