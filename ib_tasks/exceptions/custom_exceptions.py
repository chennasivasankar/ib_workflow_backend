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
from typing import List


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


class InvalidGoFIds(Exception):

    def __init__(self, invalid_gof_ids: List[str]):
        self.gof_ids = invalid_gof_ids


class DuplicateGoFIds(Exception):
    def __init__(self, gof_ids: List[str]):
        self.message = "Given duplicate gof ids {}".format(gof_ids)
        super().__init__(self.message)


class InvalidStageDisplayLogic(Exception):
    def __init__(self, invalid_stage_display_logic_stages: List[str]):
        self.invalid_stage_display_logic_stages = invalid_stage_display_logic_stages


class InvalidStagesDisplayName(Exception):
    def __init__(self, invalid_stages_display_name: List[str]):
        self.invalid_stages_display_name = invalid_stages_display_name


class ExistingGoFsNotInGivenGoFs(Exception):
    def __init__(self,
                 gof_of_template_not_in_given_gof: List[str],
                 given_gof_ids: List[str]):
        self.message = \
            "Existing gof ids: {} of template not in given gof ids: {}". \
                format(gof_of_template_not_in_given_gof, given_gof_ids)
        super().__init__(self.message)


class InvalidValueForField(Exception):
    def __init__(self, err_msg: str):
        super().__init__(err_msg)


class GOFIdCantBeEmpty(Exception):
    pass


class GOFDisplayNameCantBeEmpty(Exception):
    pass


class MaxColumnsCantBeEmpty(Exception):
    pass


class MaxColumnsMustBeANumber(Exception):

    def __init__(self, invalid_max_column_value: str):
        self.max_column = invalid_max_column_value


class MaxColumnsMustBeAPositiveInteger(Exception):

    def __init__(self, invalid_max_column_value: str):
        self.max_column = invalid_max_column_value


class TaskTemplateIdCantBeEmpty(Exception):
    pass


class GOFReadPermissionsCantBeEmpty(Exception):
    pass


class GOFWritePermissionsCantBeEmpty(Exception):
    pass


class GOFFieldIdsCantBeEmpty(Exception):
    pass


class DuplicatedFieldIds(Exception):

    def __init__(self, duplicated_field_ids: List[str]):
        self.field_ids = duplicated_field_ids


class InvalidReadPermissionRoles(Exception):

    def __init__(self, invalid_read_permission_roles: List[str]):
        self.read_permission_roles = invalid_read_permission_roles


class InvalidWritePermissionRoles(Exception):

    def __init__(self, invalid_write_permission_roles: List[str]):
        self.write_permission_roles = invalid_write_permission_roles


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


class DuplicateTaskStatusVariableIds(Exception):
    def __init__(self, duplicate_status_ids_for_tasks: List[str]):
        self.task_ids = duplicate_status_ids_for_tasks


class ConflictingGoFOrder(Exception):

    def __init__(self, invalid_order_gof_ids: List[str]):
        self.gof_ids = invalid_order_gof_ids


class EmptyValueForPlainTextField(Exception):
    pass
