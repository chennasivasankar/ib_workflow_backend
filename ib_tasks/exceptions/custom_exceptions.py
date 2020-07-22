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


class InvalidFormatException(Exception):

    def __init__(self, valid_format: str):
        self.valid_format = valid_format

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


class DuplicateTaskStatusVariableIds(Exception):
    def __init__(self, duplicate_status_ids_for_tasks: List[str]):
        self.task_ids = duplicate_status_ids_for_tasks


from typing import List


class DuplicateGoFIds(Exception):
    def __init__(self, gof_ids: List[str]):
        self.message = "Given duplicate gof ids {}".format(gof_ids)
        super().__init__(self.message)

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
    def __init__(self, constant_names: List[str]):
        self.message = \
            "Existing constants with constant names: {} of template not in " \
            "given data".format(constant_names)
        super().__init__(self.message)


class TemplateDoesNotExists(Exception):
    def __init__(self, template_id: str):
        self.message = "The template with template id: {}, does not exists". \
            format(template_id)
        super().__init__(self.message)


class DuplicateConstantNames(Exception):
    def __init__(self, constant_names: List[str]):
        self.message = \
            "Given duplicate constant names {}".format(constant_names)
        super().__init__(self.message)


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


class DuplicateGoFIds(Exception):
    def __init__(self, gof_ids: List[str]):
        self.message = "Given duplicate gof ids {}".format(gof_ids)
        super().__init__(self.message)


class ExistingGoFsNotInGivenGoFs(Exception):
    def __init__(self,
                 gof_of_template_not_in_given_gof: List[str],
                 given_gof_ids: List[str]):
        self.message = \
            "Existing gof ids: {} of template not in given gof ids: {}". \
                format(gof_of_template_not_in_given_gof, given_gof_ids)
        super().__init__(self.message)


class InvalidValueForField(Exception):
    def __init__(self, field: str):
        self.message = "Invalid value for field: {}".format(field)
        super().__init__(self.message)

class DuplicateTaskStatusVariableIds(Exception):
    def __init__(self, duplicate_status_ids_for_tasks: List[str]):
        self.task_ids = duplicate_status_ids_for_tasks
