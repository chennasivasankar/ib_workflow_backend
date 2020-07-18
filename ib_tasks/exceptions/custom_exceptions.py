from typing import List


class InvalidValueForField(Exception):
    def __init__(self, err_msg: str):
        super().__init__(err_msg)


class GOFIdCantBeEmpty(Exception):
    pass


class GOFDisplayNameCantBeEmpty(Exception):
    pass


class GOFReadPermissionsCantBeEmpty(Exception):
    pass


class GOFWritePermissionsCantBeEmpty(Exception):
    pass


class GOFFieldIdsCantBeEmpty(Exception):
    pass


class DuplicatedFieldIds(Exception):
    pass


class InvalidReadPermissionRoles(Exception):
    pass


class InvalidWritePermissionRoles(Exception):
    pass


class DifferentDisplayNamesForSameGOF(Exception):
    pass


class InvalidOrderValues(Exception):

    def __init__(self, invalid_order_values: List[int]):
        self.order_values = invalid_order_values


class InvalidFieldIds(Exception):

    def __init__(self, invalid_field_ids: List[str]):
        self.field_ids = invalid_field_ids


class GoFIDsAlreadyExists(Exception):

    def __init__(self, existing_gof_ids: List[str]):
        self.gof_ids = existing_gof_ids


class InvalidTaskTemplateIds(Exception):

    def __init__(self, invalid_task_template_ids: List[str]):
        self.task_template_ids = invalid_task_template_ids


class ExistingGlobalConstantNamesNotInGivenData(Exception):
    def __init__(self, err_msg: str):
        super().__init__(err_msg)


class TemplateDoesNotExists(Exception):
    def __init__(self, err_msg: str):
        super().__init__(err_msg)


class DuplicateConstantNames(Exception):
    def __init__(self, err_msg: str):
        super().__init__(err_msg)


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


class EmptyValueForPermissions(Exception):

    def __init__(self, message: str):
        self.message = message


class InvalidValueForFieldDisplayName(Exception):

    def __init__(self, message: str):
        self.message = message


class InvalidValueForFieldType(Exception):

    def __init__(self, message: str):
        self.message = message


class InvalidGOFIds(Exception):
    def __int__(self, message: str):
        self.message = message
