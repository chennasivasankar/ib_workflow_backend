import factory
from ib_tasks.interactors.storage_interfaces.dtos import (
    FieldValueDTO, StatusVariableDTO, GroupOfFieldsDTO,
    GOFMultipleStatusDTO, ActionDTO
)


class FieldValueDTOFactory(factory.Factory):
    class Meta:
        model = FieldValueDTO

    database_id = factory.Sequence(lambda n: 'database_%d' % (n+1))
    gof_database_id = factory.Sequence(lambda n: 'gof_database_%d' % (n+1))
    field_id = factory.Sequence(lambda n: 'field_%d' % (n+1))
    value = factory.Sequence(lambda n: 'value_%d' % (n+1))


class StatusVariableDTOFactory(factory.Factory):
    class Meta:
        model = StatusVariableDTO
    status_id = factory.Sequence(lambda n: 'status_%d' % (n+1))
    status_variable = factory.Sequence(lambda n: 'status_variable_%d' % (n+1))
    value = factory.Sequence(lambda n: 'value_%d' % (n+1))


class GroupOfFieldsDTOFactory(factory.Factory):
    class Meta:
        model = GroupOfFieldsDTO
    database_id = factory.Sequence(lambda n: 'gof_database_%d' % (n+1))
    group_of_field_id = factory.Sequence(lambda n: 'group_of_field_%d' % (n+1))


class GOFMultipleStatusDTOFactory(factory.Factory):
    class Meta:
        model = GOFMultipleStatusDTO
    multiple_status = True
    group_of_field_id = factory.Sequence(lambda n: 'group_of_field_%d' % (n+1))


class ActionDTOFactory(factory.Factory):
    class Meta:
        model = ActionDTO

    action_id = factory.Sequence(lambda n: 'action_%d' % (n+1))
    name = factory.Sequence(lambda n: 'name_%d' % (n+1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n+1))
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n+1))
    button_color = None

import factory

from ib_tasks.constants.enum import FieldTypes, PermissionTypes
from ib_tasks.interactors.dtos import StageDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    CompleteGoFDetailsDTO, GoFDTO, GoFRolesDTO,
    FieldDTO, FieldRolesDTO, FieldRoleDTO, GoFRoleDTO
)
from ib_tasks.interactors.storage_interfaces.dtos import (TaskStagesDTO)
from ib_tasks.interactors.storage_interfaces.dtos import (
    TaskStatusDTO)


class StageDTOFactory(factory.Factory):
    class Meta:
        model = StageDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    value = factory.Iterator([-1, 1, 2, 3, 4, 5, 0, 6])
    stage_display_name = factory.Sequence(
        lambda n: 'stage_display_name_%d' % n)
    stage_display_logic = factory.Sequence(
        lambda n: 'Value[stage%d]==Value[other_stage]' % n)


class TaskStagesDTOFactory(factory.Factory):
    class Meta:
        model = TaskStagesDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)


class GoFDTOFactory(factory.Factory):
    class Meta:
        model = GoFDTO

    gof_id = factory.Iterator(
        [
            'FIN_REQUEST_DETAILS', 'FIN_VENDOR_BASIC_DETAILS'
        ]
    )
    gof_display_name = factory.Iterator(
        [
            'Request Details', 'Vendor Basic Details'
        ]
    )
    task_template_id = factory.Iterator(
        [
            "FIN_PR", "FIN_VENDOR"
        ]
    )
    order = factory.Sequence(lambda counter: counter)
    max_columns = 2
    enable_multiple_gofs = False


class GoFRolesDTOFactory(factory.Factory):
    class Meta:
        model = GoFRolesDTO

    gof_id = factory.Iterator(
        [
            'FIN_REQUEST_DETAILS', 'FIN_VENDOR_BASIC_DETAILS'
        ]
    )
    read_permission_roles = ['ALL_ROLES']
    write_permission_roles = ['ALL_ROLES']


class CompleteGoFDetailsDTOFactory(factory.Factory):
    class Meta:
        model = CompleteGoFDetailsDTO

    gof_dto = GoFDTOFactory()
    gof_roles_dto = GoFRolesDTOFactory()


class GoFRoleDTOFactory(factory.Factory):
    class Meta:
        model = GoFRoleDTO

    gof_id = factory.Iterator(
        [
            'FIN_REQUEST_DETAILS', 'FIN_VENDOR_BASIC_DETAILS'
        ]
    )
    role = factory.Iterator(
        [
            "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"
        ]
    )
    permission_type = PermissionTypes.READ.value


class FieldDTOFactory(factory.Factory):
    class Meta:
        model = FieldDTO

    gof_id = "FIN_VENDOR_BASIC_DETAILS"
    field_id = factory.Sequence(lambda n: 'field%d' % n)
    field_display_name = "field name"
    field_type = FieldTypes.DROPDOWN.value
    field_values = ["Mr", "Mrs", "Ms"]
    required = True
    help_text = "Verify the code"
    tool_tip = "Request"
    placeholder_text = "select vendor"
    error_message = "error message"
    allowed_formats = None
    validation_regex = None


class FieldRolesDTOFactory(factory.Factory):
    class Meta:
        model = FieldRolesDTO

    field_id = factory.Sequence(lambda n: 'field%d' % n)
    read_permission_roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]
    write_permission_roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]


class FieldRoleDTOFactory(factory.Factory):
    class Meta:
        model = FieldRoleDTO

    field_id = factory.Sequence(lambda n: 'field%d' % n)
    role = "FIN_PAYMENT_REQUESTER"
    permission_type = PermissionTypes.READ.value


class TaskStatusDTOFactory(factory.Factory):
    class Meta:
        model = TaskStatusDTO

    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    status_variable_id = factory.Sequence(
        lambda n: 'status_variable_id_%d' % n)
