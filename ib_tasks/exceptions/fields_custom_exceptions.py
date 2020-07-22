from typing import List


class InvalidValueForField(Exception):
    def __init__(self, message: str):
        self.message = message


class DuplicatedFieldIds(Exception):
    pass


class InvalidFieldIds(Exception):

    def __init__(self, invalid_field_ids: List[str]):
        self.field_ids = invalid_field_ids


class InvalidFieldIdException(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message


class DuplicationOfFieldIdsExist(Exception):
    def __init__(self, field_ids: List[str]):
        self.field_ids = field_ids


class FieldsDuplicationOfDropDownValues(Exception):
    def __init__(self, fieds_with_dropdown_duplicate_values):
        self.fieds_with_dropdown_duplicate_values = \
            fieds_with_dropdown_duplicate_values


class InvalidValueForFieldDisplayName(Exception):

    def __init__(self, message: str):
        self.message = message


class InvalidValueForFieldType(Exception):

    def __init__(self, message: str):
        self.message = message
