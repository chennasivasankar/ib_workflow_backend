import factory

from ib_tasks.interactors.dtos import TaskStatusVariableDTO
from ib_tasks.interactors.stages_dtos import StageDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import TaskTemplateStatusDTO, StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageActionNamesDTO, TaskStagesDTO, ValidStageDTO
from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, FieldRolesDTO, FieldRoleDTO, FieldValueDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, GoFRolesDTO, GoFRoleDTO, CompleteGoFDetailsDTO, \
    GroupOfFieldsDTO, GOFMultipleEnableDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import (TaskStagesDTO)
from ib_tasks.interactors.storage_interfaces.status_dtos import (
    TaskTemplateStatusDTO)
from ib_tasks.constants.enum import FieldTypes, PermissionTypes
from ib_tasks.models import StageAction

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
    status_id = factory.Sequence(lambda n: (n+1))
    status_variable = factory.Sequence(lambda n: 'status_variable_%d' % (n+1))
    value = factory.Sequence(lambda n: 'value_%d' % (n+1))


class GroupOfFieldsDTOFactory(factory.Factory):
    class Meta:
        model = GroupOfFieldsDTO
    database_id = factory.Sequence(lambda n: 'gof_database_%d' % (n+1))
    group_of_field_id = factory.Sequence(lambda n: 'group_of_field_%d' % (n+1))


class GOFMultipleStatusDTOFactory(factory.Factory):
    class Meta:
        model = GOFMultipleEnableDTO
    multiple_status = True
    group_of_field_id = factory.Sequence(lambda n: 'group_of_field_%d' % (n+1))


class ActionDTOFactory(factory.Factory):
    class Meta:
        model = ActionDTO

    action_id = factory.Sequence(lambda n: (n+1))
    name = factory.Sequence(lambda n: 'name_%d' % (n+1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n+1))
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n+1))
    button_color = None


class StageDTOFactory(factory.Factory):
    class Meta:
        model = StageDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    value = factory.Iterator([-1, 1, 2, 3, 4, 5, 0, 6])
    id = None
    stage_display_name = factory.Sequence(
        lambda n: 'stage_display_name_%d' % n)
    stage_display_logic = factory.Sequence(
        lambda n: 'Value[stage%d]==Value[other_stage]' % n)

    class Params:
        id_value = factory.Trait(
            id=factory.Sequence(lambda n: n)
        )

class TaskStagesDTOFactory(factory.Factory):
    class Meta:
        model = TaskStagesDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)

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


class TaskTemplateStatusDTOFactory(factory.Factory):
    class Meta:
        model = TaskTemplateStatusDTO

    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    status_variable_id = factory.Sequence(lambda n: 'status_id_%d' % n)


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

    gof_dto = factory.SubFactory(GoFDTOFactory)
    gof_roles_dto = factory.SubFactory(GoFRolesDTOFactory)


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
    help_text = None
    tooltip = None
    placeholder_text = None
    error_message = None
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



class TaskStatusVariableDTOFactory(factory.Factory):
    class Meta:
        model = TaskStatusVariableDTO
    task_id = factory.Sequence(lambda n: "%d" % n)
    variable = factory.Sequence(lambda n: "status_variable_%d" % n)
    value = factory.Sequence(lambda n: "value_%d" % n)
