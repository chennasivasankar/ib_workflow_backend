from typing import List


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


class InvalidRolesException(Exception):

    def __init__(self, roles):
        self.roles = roles
