import enum


class ViewType(enum.Enum):
    LIST = "LIST"
    KANBAN = "KANBAN"


class FieldTypes(enum.Enum):
    PLAIN_TEXT = "PLAIN_TEXT"
    PHONE_NUMBER = "PHONE_NUMBER"
    EMAIL = "EMAIL"
    URL = "URL"
    PASSWORD = "PASSWORD"
    NUMBER = "NUMBER"
    FLOAT = "FLOAT"
    LONG_TEXT = "LONG_TEXT"
    DROPDOWN = "DROPDOWN"
    GOF_SELECTOR = "GOF_SELECTOR"
    RADIO_GROUP = "RADIO_GROUP"
    CHECKBOX_GROUP = "CHECKBOX_GROUP"
    MULTI_SELECT_FIELD = "MULTI_SELECT_FIELD"
    MULTI_SELECT_LABELS = "MULTI_SELECT_LABELS"
    DATE = "DATE"
    TIME = "TIME"
    DATE_TIME = "DATE_TIME"
    IMAGE_UPLOADER = "IMAGE_UPLOADER"
    FILE_UPLOADER = "FILE_UPLOADER"
    SEARCHABLE = "SEARCHABLE"


class PermissionTypes(enum.Enum):
    WRITE = "WRITE"
    READ = "READ"


class Searchable(enum.Enum):
    CITY = "CITY"
    STATE = "STATE"
    COUNTRY = "COUNTRY"
    VENDOR = "VENDOR"
    USER = "USER"
    COMPANY = "COMPANY"
    TEAM = "TEAM"


class Operators(enum.Enum):
    GTE = "GTE"
    LTE = "LTE"
    GT = "GT"
    LT = "LT"
    NE = "NE"
    EQ = "EQ"
    CONTAINS = "CONTAINS"


class Status(enum.Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Priority(enum.Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class ValidationType(enum.Enum):
    NO_VALIDATIONS = "NO_VALIDATIONS"


class ActionTypes(enum.Enum):
    NO_VALIDATIONS = "NO_VALIDATIONS"


DELAY_REASONS = [
    {
        "id": 1,
        "reason": "wrong estimation of time"
    },
    {
        "id": 2,
        "reason": "Execution level plan fail"
    },
    {
        "id": 3,
        "reason": "No clarity in objective"
    },
    {
        "id": 4,
        "reason": "Doesn't follow Instructions"
    },
    {
        "id": -1,
        "reason": ""
    }
]
