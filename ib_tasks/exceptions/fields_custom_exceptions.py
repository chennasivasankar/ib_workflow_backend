from typing import List

from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldIdWithFieldDisplayNameDTO


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


class SearchableTypeDoesNotExistException(Exception):
    pass


class LimitShouldBeGreaterThanZeroException(Exception):
    pass


class OffsetShouldBeGreaterThanOrEqualToMinusOneException(Exception):
    pass


class OffsetShouldBeGreaterThanZeroException(Exception):
    pass


class OffsetShouldBeGreaterThanOrEqualToZeroException(Exception):
    pass


class DuplicateFieldIdsToGoF(Exception):

    def __init__(self, gof_id: str, duplicate_field_ids: List[str]):
        self.gof_id = gof_id
        self.field_ids = duplicate_field_ids


class OrderForFieldShouldNotBeNegativeException(Exception):
    def __init__(self, message: str):
        self.message = message


class DuplicateOrdersForFieldsOfGoFException(Exception):
    def __init__(self, message: str):
        self.message = message


class UserDidNotFillRequiredFields(Exception):

    def __init__(
            self, unfilled_field_dtos: List[FieldIdWithFieldDisplayNameDTO]):
        self.unfilled_field_dtos = unfilled_field_dtos
