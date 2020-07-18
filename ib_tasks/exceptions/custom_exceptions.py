from typing import List


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
    pass


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


class ConflictingGoFOrder(Exception):

    def __init__(self, invalid_order_gof_ids: List[str]):
        self.gof_ids = invalid_order_gof_ids
