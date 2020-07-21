import factory

from ib_tasks.interactors.dtos import StageDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    TaskStatusDTO, ValidStageDTO, TaskStagesDTO, StageActionNamesDTO)
from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.storage_interfaces.dtos import (
    CompleteGoFDetailsDTO, GoFDTO, GoFRolesDTO, GoFRoleDTO
)
from ib_tasks.interactors.storage_interfaces.dtos import (
    CompleteGoFDetailsDTO, GoFDTO, GoFRolesDTO,
    FieldDTO, FieldRolesDTO, FieldRoleDTO
)
from ib_tasks.constants.enum import FieldTypes, PermissionTypes
from ib_tasks.models import StageAction


class StageActionsDTOFactory(factory.Factory):
    class Meta:
        model = StageActionNamesDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    action_names = factory.Sequence(lambda n: [f"name_{n}"])


class StageActionModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StageAction

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    name = factory.Sequence(lambda n: "name_%d" % n)
    logic = factory.Sequence(lambda n: 'status_id_%d==stage_id' % n)
    py_function_import_path = "ib_tasks.interactors.storage_interfaces.storage_interface.StorageInterface"
    button_text = "text"
    button_color = None

    class Params:
        color = factory.Trait(button_color="#ffffff")


class TaskStatusDTOFactory(factory.Factory):
    class Meta:
        model = TaskStatusDTO

    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    status_variable_id = factory.Sequence(lambda n: 'status_id_%d' % n)


class StageDTOFactory(factory.Factory):
    class Meta:
        model = StageDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    value = factory.Sequence(lambda n: n)
    id = None
    stage_display_name = factory.Sequence(lambda n: 'name_%d' % n)
    stage_display_logic = factory.Sequence(lambda n: 'status_id_%d==stage_id' % n)

    class Params:
        id_value = factory.Trait(id=factory.Sequence(lambda n: n))


class ValidStageDTOFactory(factory.Factory):
    class Meta:
        model = ValidStageDTO

    id = factory.Sequence(lambda n: (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)


class TaskStageDTOFactory(factory.Factory):
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
