import enum


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
    DATE = "DATE"
    TIME = "TIME"
    DATE_TIME = "DATE_TIME"


class PermissionTypes(enum.Enum):
    WRITE = "WRITE"
    READ = "READ"