from typing import List


class InvalidGoFIDsInGoFSelectorField(Exception):

    def __init__(self, gof_ids: List[str]):
        self.gof_ids = gof_ids


class EmptyValueForPlainTextField(Exception):

    def __init__(self, field_id: str):
        self.field_id = field_id


class InvalidPhoneNumberValue(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidEmailFieldValue(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidURLValue(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class NotAStrongPassword(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidNumberValue(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidFloatValue(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidValueForLongText(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidValueForDropdownField(Exception):

    def __init__(self, field_id: str, field_value: str,
                 valid_values: List[str]):
        self.field_id = field_id
        self.field_value = field_value
        self.valid_values = valid_values
