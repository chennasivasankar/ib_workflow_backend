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
