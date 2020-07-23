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


class InvalidValueForFieldDisplayName(Exception):

    def __init__(self, message: str):
        self.message = message


class InvalidValueForFieldType(Exception):

    def __init__(self, message: str):
        self.message = message


class FieldIdEmptyValueException(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidGOFIds(Exception):

    def __int__(self, message: str):
        self.message = message


class InvalidJsonForFieldValue(Exception):
    def __init__(self, message: str):
        self.message = message


class EmptyValuesForGoFNames(Exception):
    def __init__(self, message: str):
        self.message = message


class DuplicationOfGoFNamesForFieldValues(Exception):
    def __init__(self, message: str):
        self.message = message


class AllowedFormatsEmptyValueException(Exception):
    def __init__(self, message: str):
        self.message = message


class FieldsDuplicationOfAllowedFormatsValues(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidValueForSearchable(Exception):
    def __init__(self, message: str):
        self.message = message


class EmptyValuesForFieldValues(Exception):

    def __init__(self, message: str):
        self.message = message


class DuplicationOfFieldValuesForFieldTypeMultiValues(Exception):

    def __init__(self, message: str):
        self.message = message


class EmptyValueForPermissions(Exception):

    def __init__(self, message: str):
        self.message = message


class InvalidFieldRolesException(Exception):

    def __init__(self, roles):
        self.roles = roles


class DuplicationOfPermissionRoles(Exception):

    def __init__(self, message: str):
        self.message = message


class EmptyValuesForAllowedFormats(Exception):
    def __init__(self, message: str):
        self.message = message

