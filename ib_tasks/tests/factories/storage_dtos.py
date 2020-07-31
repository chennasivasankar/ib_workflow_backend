import json

import factory

from ib_tasks.constants.constants import VALID_FIELD_TYPES
from ib_tasks.constants.enum import FieldTypes, PermissionTypes
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.stages_dtos import StageDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO, \
    ActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionsOfTemplateDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldRolesDTO, FieldRoleDTO, FieldTypeDTO, UserFieldPermissionDTO, \
    FieldDetailsDTO, StageTaskFieldsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldValueDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import (
    TaskGoFFieldDTO,
    TaskGoFDTO
)
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageActionNamesDTO, ValidStageDTO, TaskTemplateStageDTO, \
    StageActionNamesDTO, ValidStageDTO, TaskStageIdsDTO, StageValueDTO, StageDisplayValueDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFRolesDTO, GoFRoleDTO, CompleteGoFDetailsDTO, GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import (TaskStagesDTO)
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFRolesDTO, GoFRoleDTO, CompleteGoFDetailsDTO, GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GroupOfFieldsDTO, \
    GOFMultipleEnableDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import (
    TaskStagesDTO,
    StageActionNamesDTO,
    StageValueDTO,
    ValidStageDTO,
    TaskStageIdsDTO)
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskTemplateStageDTO,\
    StageActionNamesDTO, ValidStageDTO, TaskTemplateStageDTO, \
    StageActionNamesDTO, ValidStageDTO, TaskStageIdsDTO, StageValueDTO, StageDetailsDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFRolesDTO, GoFRoleDTO, CompleteGoFDetailsDTO, GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import (TaskStagesDTO,
    TaskTemplateStageDTO)
from ib_tasks.interactors.storage_interfaces.stage_dtos import (TaskStagesDTO)
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import (
    TaskTemplateStatusDTO)
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TaskTemplateDTO
from ib_tasks.interactors.task_dtos import TaskStatusVariableDTO
from ib_tasks.models import StageAction

from ib_tasks.interactors.storage_interfaces.get_task_dtos import (
    TaskGoFFieldDTO,
    TaskGoFDTO
)


class StageDetailsDTOFactory(factory.Factory):
    class Meta:
        model = StageDetailsDTO

    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)
    name = factory.Sequence(lambda n: "name_%d" % n)


class FieldValueDTOFactory(factory.Factory):
    class Meta:
        model = FieldValueDTO

    database_id = factory.Sequence(lambda n: (n + 1))
    gof_database_id = factory.Sequence(lambda n: 'gof_database_%d' % (n + 1))
    field_id = factory.Sequence(lambda n: 'field_%d' % (n + 1))
    value = factory.Sequence(lambda n: 'value_%d' % (n + 1))


class StatusVariableDTOFactory(factory.Factory):
    class Meta:
        model = StatusVariableDTO

    status_id = factory.Sequence(lambda n: (n + 1))
    status_variable = factory.Sequence(lambda n: 'status_variable_%d' %
                                                 (n + 1))
    value = factory.Sequence(lambda n: 'value_%d' % (n + 1))


class GroupOfFieldsDTOFactory(factory.Factory):
    class Meta:
        model = GroupOfFieldsDTO

    database_id = factory.Sequence(lambda n: 'gof_database_%d' % (n + 1))
    group_of_field_id = factory.Sequence(lambda n: 'group_of_field_%d' %
                                                   (n + 1))


class GOFMultipleStatusDTOFactory(factory.Factory):
    class Meta:
        model = GOFMultipleEnableDTO

    multiple_status = True
    group_of_field_id = factory.Sequence(lambda n: 'gof%d' % (n + 1))


class ActionDTOFactory(factory.Factory):
    class Meta:
        model = ActionDTO

    action_id = factory.Sequence(lambda n: (n + 1))
    name = factory.Sequence(lambda n: 'name_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n + 1))
    button_color = None


class ActionDetailsDTOFactory(factory.Factory):
    class Meta:
        model = ActionDetailsDTO

    action_id = factory.Sequence(lambda n: (n + 1))
    name = factory.Sequence(lambda n: 'name_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % (n + 1))
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n + 1))
    button_color = None


class TaskStagesDTOFactory(factory.Factory):
    class Meta:
        model = TaskStagesDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % (n + 1))
    task_template_id = factory.Sequence(
        lambda n: 'task_template_id_%d' % (n + 1))


class TaskTemplateStagesDTOFactory(factory.Factory):
    class Meta:
        model = TaskTemplateStageDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % (n + 1))
    task_id = factory.Sequence(lambda n: n + 1)
    task_template_id = factory.Sequence(
        lambda n: 'task_template_id_%d' % (n + 1))


class TaskFieldsDTOFactory(factory.Factory):
    class Meta:
        model = StageTaskFieldsDTO

    field_ids = ['FIELD-ID-1', 'FIELD-ID-2']
    task_id = factory.Sequence(lambda n: n + 1)


class TemplateStagesDTOFactory(factory.Factory):
    class Meta:
        model = TaskTemplateStageDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_id = factory.Sequence(lambda n: n)
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


class StageDTOFactory(factory.Factory):
    class Meta:
        model = StageDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    value = factory.Sequence(lambda n: n)
    id = None
    card_info_kanban = json.dumps(['field_id_1', "field_id_2"])
    card_info_list = json.dumps(['field_id_1', "field_id_2"])
    stage_display_name = factory.Sequence(lambda n: 'name_%d' % n)
    stage_display_logic = factory.Sequence(
        lambda n: 'status_id_%d==stage_id' % n)

    class Params:
        id_value = factory.Trait(id=factory.Sequence(lambda n: n))


class StageValueDTOFactory(factory.Factory):
    class Meta:
        model = StageValueDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    value = factory.Sequence(lambda n: n)


class ValidStageDTOFactory(factory.Factory):
    class Meta:
        model = ValidStageDTO

    id = factory.Sequence(lambda n: (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)


class GOFMultipleEnableDTOFactory(factory.Factory):
    class Meta:
        model = GOFMultipleEnableDTO

    group_of_field_id = factory.Sequence(lambda n: 'gof_%d' % n)
    multiple_status = True


class TaskStageDTOFactory(factory.Factory):
    class Meta:
        model = TaskStagesDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)


class GoFDTOFactory(factory.Factory):
    class Meta:
        model = GoFDTO

    gof_id = factory.Sequence(lambda counter: "gof_{}".format(counter))
    gof_display_name = factory.Sequence(
        lambda counter: "GOF_DISPLAY_NAME-{}".format(counter))
    max_columns = 2


class GoFRolesDTOFactory(factory.Factory):
    class Meta:
        model = GoFRolesDTO

    gof_id = factory.Sequence(lambda counter: "gof_{}".format(counter))
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

    gof_id = factory.Sequence(lambda counter: "gof_{}".format(counter))
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


class FieldTypeDTOFactory(factory.Factory):
    class Meta:
        model = FieldTypeDTO

    field_id = factory.Sequence(lambda counter: "FIELD_ID-{}".format(counter))
    field_type = factory.Iterator(VALID_FIELD_TYPES)


class TaskTemplateDTOFactory(factory.Factory):
    class Meta:
        model = TaskTemplateDTO

    template_id = factory.Sequence(lambda n: 'template_{}'.format(n + 1))
    template_name = \
        factory.sequence(lambda n: 'Task Template {}'.format(n + 1))


class ActionsOfTemplateDTOFactory(factory.Factory):
    class Meta:
        model = ActionsOfTemplateDTO

    template_id = factory.Sequence(lambda n: 'template_{}'.format(n + 1))
    action_id = factory.Sequence(lambda n: n + 1)
    button_text = factory.Sequence(lambda n: 'button_text__{}'.format(n + 1))
    button_color = factory.Sequence(lambda n: 'button_color_{}'.format(n + 1))


class UserFieldPermissionDTOFactory(factory.Factory):
    class Meta:
        model = UserFieldPermissionDTO

    field_id = factory.Sequence(lambda n: 'field_{}'.format(n + 1))
    permission_type = factory.Iterator(["READ", "WRITE"])


class GoFToTaskTemplateDTOFactory(factory.Factory):
    class Meta:
        model = GoFToTaskTemplateDTO

    gof_id = factory.Sequence(lambda n: 'gof_{}'.format(n + 1))
    template_id = factory.Sequence(lambda n: 'template_{}'.format(n + 1))
    order = factory.Sequence(lambda n: n)
    enable_add_another = factory.Iterator([True, False])


class TaskGoFDTOFactory(factory.Factory):
    class Meta:
        model = TaskGoFDTO

    task_gof_id = factory.Sequence(lambda n: n)
    gof_id = factory.Sequence(lambda n: "gof{}".format(n))
    same_gof_order = 0


class FieldDetailsDTOFactory(factory.Factory):
    class Meta:
        model = FieldDetailsDTO

    field_id = factory.Sequence(lambda n: "FIELD-ID-%d" % (n + 1))
    field_type = "Drop down"
    key = "key"
    value = "value"



class TaskGoFFieldDTOFactory(factory.Factory):
    class Meta:
        model = TaskGoFFieldDTO

    task_gof_id = factory.Sequence(lambda n: n)
    field_id = factory.Sequence(lambda n: "field{}".format(n))
    field_response = factory.Sequence(lambda n: "field_response{}".format(n))


class GlobalConstantDTOFactory(factory.Factory):
    class Meta:
        model = GlobalConstantsDTO

    constant_name = factory.sequence(lambda n: "constant_{}".format(n + 1))
    value = factory.sequence(lambda n: (n + 1))


class TaskStageIdsDTOFactory(factory.Factory):
    class Meta:
        model = TaskStageIdsDTO

    task_id = factory.Sequence(lambda n: f'TASK_ID_{n + 1}')
    stage_id = factory.Sequence(lambda n: f'STAGE_ID_{n + 1}')


class StageDisplayValueDTOFactory(factory.Factory):

    class Meta:
        model = StageDisplayValueDTO
    stage_id = factory.sequence(lambda n: "stage_{}".format(n + 1))
    display_logic = factory.sequence(lambda n: "variable_{} == stage_{}".format((n+1), (n+1)))
    value = factory.sequence(lambda n: (n+1))
