from typing import List, Dict


class InvalidStageIdsException(Exception):
    def __init__(self, stage_ids_dict: str):
        self.stage_ids_dict = stage_ids_dict

    def __str__(self):
        return self.stage_ids_dict


class InvalidRolesException(Exception):
    def __init__(self, stage_roles_dict: str):
        self.stage_roles_dict = stage_roles_dict


class InvalidFormatException(Exception):
    def __init__(self, valid_format: str):
        self.valid_format = valid_format


class InvalidPythonCodeException(Exception):
    pass


class InvalidTaskIdException(Exception):
    def __init__(self, task_id: str):
        self.task_id = task_id


class InvalidTaskTemplateId(Exception):
    def __init__(self, task_template_ids_dict: str):
        self.task_template_ids_dict = task_template_ids_dict



class InvalidStagesTaskTemplateId(Exception):
    def __init__(self, invalid_stages_task_template_ids: List[str]):
        self.invalid_stages_task_template_ids = invalid_stages_task_template_ids


class InvalidStageValues(Exception):
    def __init__(self, invalid_value_stages: List[str]):
        self.invalid_value_stages = invalid_value_stages


class DuplicateStageIds(Exception):
    def __init__(self, duplicate_stage_ids: List[str]):
        self.duplicate_stage_ids = duplicate_stage_ids


class InvalidTaskTemplateIds(Exception):
    def __init__(self, invalid_task_template_ids: List[str]):
        self.invalid_task_template_ids = invalid_task_template_ids


class InvalidStageDisplayLogic(Exception):
    def __init__(self, invalid_stage_display_logic_stages: List[str]):
        self.invalid_stage_display_logic_stages = invalid_stage_display_logic_stages


class InvalidStagesDisplayName(Exception):
    def __init__(self, invalid_stages_display_name: List[str]):
        self.invalid_stages_display_name = invalid_stages_display_name


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


class FieldIdEmptyValueException(Exception):
    def __init__(self, message: str):
        self.message = message


class DuplicationOfFieldIdsExist(Exception):

    def __init__(self, field_ids: List[str]):
        self.field_ids = field_ids


class DuplicationOfFieldValuesForFieldTypeMultiValues(Exception):

    def __init__(self, message: str):
        self.message = message


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
        super().__init__(self.message)


class DuplicateTaskStatusVariableIds(Exception):
    def __init__(self, duplicate_status_ids_for_tasks: List[str]):
        self.task_ids = duplicate_status_ids_for_tasks


class DuplicationOfPermissionRoles(Exception):

    def __init__(self, message: str):
        self.message = message


class EmptyValuesForFieldValues(Exception):

    def __init__(self, message: str):
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


class EmptyValuesForAllowedFormats(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidValueForSearchable(Exception):
    def __init__(self, message: str):
        self.message = message
