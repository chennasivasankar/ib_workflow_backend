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

    gof_id = factory.Sequence(lambda counter: "GOF_ID-{}".format(counter))
    gof_display_name = factory.Sequence(
        lambda counter: "GOF_DISPLAY_NAME-{}".format(counter)
    )
    max_columns = 2


class GoFRolesDTOFactory(factory.Factory):
    class Meta:
        model = GoFRolesDTO

    gof_id = factory.Sequence(lambda counter: "GOF_ID-{}".format(counter))
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

    gof_id = factory.Sequence(lambda counter: "GOF_ID-{}".format(counter))
    role = factory.Sequence(lambda counter: "ROLE-{}".format(counter))
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
