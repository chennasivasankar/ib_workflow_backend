import json
from datetime import datetime, timedelta

import factory

from ib_tasks.adapters.dtos import UserDetailsDTO
from ib_tasks.constants.constants import VALID_FIELD_TYPES
from ib_tasks.constants.enum import Priority, ValidationType, FieldTypes, \
    PermissionTypes, Status, Operators, Searchable
from ib_tasks.interactors.field_dtos import FieldIdWithTaskGoFIdDTO
from ib_tasks.interactors.filter_dtos import FilterDTO, ConditionDTO
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.gofs_dtos import GoFIdWithSameGoFOrderDTO
from ib_tasks.interactors.stages_dtos import StageDTO, StageRolesDTO, \
    TaskStageHistoryDTO, LogDurationDTO, \
    StageMinimalDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO, \
    StageActionDetailsDTO, ActionDetailsDTO, ActionWithStageIdDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldCompleteDetailsDTO, FieldRolesDTO, FieldRoleDTO, \
    UserFieldPermissionDTO, FieldDetailsDTOWithTaskId, FieldDetailsDTO, \
    StageTaskFieldsDTO, FieldPermissionDTO, FieldValueDTO, FieldNameDTO, \
    FieldIdWithFieldDisplayNameDTO, FieldTypeDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import (
    TaskGoFFieldDTO,
    TaskGoFDTO, TaskDetailsDTO, TaskBaseDetailsDTO, FieldSearchableDTO
)
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFRolesDTO, GoFRoleDTO, CompleteGoFDetailsDTO, GoFToTaskTemplateDTO, \
    GroupOfFieldsDTO, GOFMultipleEnableDTO, TaskTemplateGofsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageActionNamesDTO, ValidStageDTO, TaskStageIdsDTO, StageValueDTO, \
    StageDetailsDTO, StageDisplayValueDTO, StageIdWithTemplateIdDTO, \
    StageRoleDTO, TaskStagesDTO, \
    TaskTemplateStageDTO, TaskStageAssigneeDTO, TaskStageHavingAssigneeIdDTO, \
    CurrentStageDetailsDTO, StageIdActionNameDTO, StageActionIdDTO, StageDisplayDTO, StageFlowDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    StatusVariableDTO, TaskTemplateStatusDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO, TaskDueMissingDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO, ProjectIdWithTaskTemplateIdDTO, ProjectTemplateDTO
from ib_tasks.interactors.task_dtos import TaskStatusVariableDTO
from ib_tasks.models import StageAction


class StageDetailsDTOFactory(factory.Factory):
    class Meta:
        model = StageDetailsDTO

    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)
    name = factory.Sequence(lambda n: "name_%d" % n)
    db_stage_id = factory.Sequence(lambda n: (n + 1))
    color = factory.Sequence(lambda counter: "color{}".format(counter))


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
    status_variable = factory.Sequence(lambda n: 'variable_%d' %
                                                 (n + 1))
    value = factory.Sequence(lambda n: 'stage_%d' % (n + 1))


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
    action_type = factory.Sequence(lambda n: "action_type_%d" % (n + 1))
    name = factory.Sequence(lambda n: 'name_%d' % (n + 1))
    transition_template_id = factory.Sequence(
        lambda n: 'template_id_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % (n + 1))
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


class StageActionDetailsDTOFactory(factory.Factory):
    class Meta:
        model = StageActionDetailsDTO

    action_id = factory.Sequence(lambda n: (n + 1))
    name = factory.Sequence(lambda n: 'name_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % (n + 1))
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n + 1))
    button_color = None
    action_type = factory.Sequence(lambda n: "action_type_%d" % (n + 1))
    transition_template_id = factory.Sequence(
        lambda n: 'template_id_%d' % (n + 1))


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
    stage_id = factory.Sequence(lambda n: "stage_id_%d" % (n + 1))
    task_id = factory.Sequence(lambda n: n + 1)


class TaskWithFieldsDTOFactory(factory.Factory):
    class Meta:
        model = StageTaskFieldsDTO

    field_ids = ['FIELD_ID-1', 'FIELD_ID-2']
    stage_id = factory.Sequence(lambda n: "stage_id_%d" % (n + 1))
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
    py_function_import_path = \
        "ib_tasks.interactors.storage_interfaces.storage_interface" \
        ".StorageInterface"
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

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % (n + 1))
    task_template_id = factory.Sequence(
        lambda n: 'task_template_id_%d' % (n + 1))
    value = factory.Sequence(lambda n: (n + 1))
    card_info_kanban = json.dumps(["field_id_1", "field_id_2"])
    card_info_list = json.dumps(["field_id_1", "field_id_2"])
    stage_display_name = factory.Sequence(lambda n: 'name_%d' % (n + 1))
    stage_display_logic = factory.Sequence(
        lambda n: 'status_id_%d==stage_id' % (n + 1))
    stage_color = factory.Iterator(["blue", "orange", "green"])
    roles = factory.Sequence(lambda n: "role_id_0\nrole_id_%d" % (n + 1))


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
    order = factory.sequence(lambda counter: counter)


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

    field_id = factory.Sequence(lambda counter: "field{}".format(counter))
    field_type = factory.Iterator(VALID_FIELD_TYPES)


class FieldCompleteDetailsDTOFactory(factory.Factory):
    class Meta:
        model = FieldCompleteDetailsDTO

    required = True
    field_values = None
    allowed_formats = None
    validation_regex = None


class TaskTemplateDTOFactory(factory.Factory):
    class Meta:
        model = TemplateDTO

    template_id = factory.Sequence(lambda n: 'template_{}'.format(n + 1))
    template_name = \
        factory.sequence(lambda n: 'Task Template {}'.format(n + 1))


class ProjectTemplateDTOFactory(factory.Factory):
    class Meta:
        model = ProjectTemplateDTO

    project_id = factory.Sequence(lambda n: 'project_{}'.format(n))
    template_id = factory.Sequence(lambda n: 'template_{}'.format(n))
    template_name = \
        factory.sequence(lambda n: 'Task Template {}'.format(n))



class ActionWithStageIdDTOFactory(factory.Factory):
    class Meta:
        model = ActionWithStageIdDTO

    stage_id = factory.Sequence(lambda n: n)
    action_id = factory.Sequence(lambda n: n)
    button_text = factory.Sequence(lambda n: 'button_text__{}'.format(n))
    button_color = factory.Sequence(lambda n: 'button_color_{}'.format(n))
    action_type = ValidationType.NO_VALIDATIONS.value
    transition_template_id = \
        factory.Sequence(lambda n: 'transition_template_{}'.format(n))


class UserFieldPermissionDTOFactory(factory.Factory):
    class Meta:
        model = UserFieldPermissionDTO

    field_id = factory.Sequence(lambda n: 'field_{}'.format(n + 1))
    permission_type = factory.Iterator(["READ", "WRITE"])


class StageRolesDTOFactory(factory.Factory):
    class Meta:
        model = StageRolesDTO

    stage_id = factory.Sequence(lambda n: 'stage_{}'.format(n))
    role_ids = factory.Sequence(
        lambda n: ['ROLE_{}'.format(n), 'ROLE_{}'.format(n + 1)])


class GoFToTaskTemplateDTOFactory(factory.Factory):
    class Meta:
        model = GoFToTaskTemplateDTO

    gof_id = factory.Sequence(lambda n: 'gof_{}'.format(n + 1))
    template_id = factory.Sequence(lambda n: 'template_{}'.format(n + 1))
    order = factory.Sequence(lambda n: n)
    enable_add_another = factory.Iterator([True, False])


class TaskTemplateGofsDTOFactory(factory.Factory):
    class Meta:
        model = TaskTemplateGofsDTO

    template_id = factory.Sequence(lambda n: 'template_{}'.format(n))
    gof_ids = factory.Sequence(
        lambda n: ['gof_{}'.format(n), 'gof_{}'.format(n + 1)])


class FieldNameDTOFactory(factory.Factory):
    class Meta:
        model = FieldNameDTO

    field_id = factory.Sequence(lambda n: 'field_{}'.format(n))
    gof_id = factory.Sequence(lambda n: 'gof_{}'.format(n))
    field_display_name = factory.Sequence(
        lambda n: 'display_name_{}'.format(n))


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


class FieldDetailsDTOWithTaskIdFactory(factory.Factory):
    class Meta:
        model = FieldDetailsDTOWithTaskId

    field_id = factory.Sequence(lambda n: "FIELD-ID-%d" % (n + 1))
    task_id = factory.Sequence(lambda n: (n + 1))
    field_type = "Drop down"
    key = "key"
    value = "value"


class TaskGoFWithTaskIdDTOFactory(factory.Factory):
    class Meta:
        model = TaskGoFWithTaskIdDTO

    task_id = factory.Sequence(lambda counter: counter)
    gof_id = factory.Sequence(lambda counter: "gof_{}".format(counter))
    same_gof_order = 0


class TaskGoFDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskGoFDetailsDTO

    task_gof_id = factory.Sequence(lambda counter: counter)
    gof_id = factory.Sequence(lambda counter: "gof_{}".format(counter))
    same_gof_order = 1


class TaskGoFFieldDTOFactory(factory.Factory):
    class Meta:
        model = TaskGoFFieldDTO

    field_id = factory.Sequence(lambda n: "field{}".format(n))
    field_response = factory.Sequence(lambda n: "field_response{}".format(n))
    task_gof_id = factory.Sequence(lambda n: n)


class GlobalConstantDTOFactory(factory.Factory):
    class Meta:
        model = GlobalConstantsDTO

    constant_name = factory.sequence(lambda n: "constant_{}".format(n + 1))
    value = factory.sequence(lambda n: (n + 1))


class TaskStageIdsDTOFactory(factory.Factory):
    class Meta:
        model = TaskStageIdsDTO

    task_id = factory.Sequence(lambda n: (n + 1))
    stage_id = factory.Sequence(lambda n: f'STAGE_ID_{n + 1}')
    task_display_id = factory.Sequence(lambda n: f'TASK_ID_{n + 1}')


class StageDisplayValueDTOFactory(factory.Factory):
    class Meta:
        model = StageDisplayValueDTO

    stage_id = factory.sequence(lambda n: "stage_{}".format(n + 1))
    display_logic = factory.sequence(
        lambda n: "variable_{} == stage_{}".format((n + 1), (n + 1)))
    value = factory.sequence(lambda n: (n + 1))


class StageDisplayDTOFactory(factory.Factory):
    class Meta:
        model = StageDisplayDTO
    stage_id = factory.sequence(lambda n: "stage_{}".format(n + 1))
    display_value = factory.sequence(
        lambda n: "variable_{} == stage_{}".format((n + 1), (n + 1)))


class FieldPermissionDTOFactory(factory.Factory):
    class Meta:
        model = FieldPermissionDTO

    field_dto = factory.SubFactory(FieldDTOFactory)
    is_field_writable = factory.Iterator([True, False])

    # display_logic = factory.sequence(lambda n: "variable_{} == stage_{
    # }".format((n+1), (n+1)))
    # value = factory.sequence(lambda n: (n+1))


class StageIdWithTemplateIdDTOFactory(factory.Factory):
    class Meta:
        model = StageIdWithTemplateIdDTO

    template_id = factory.sequence(lambda n: "template_{}".format(n))
    stage_id = factory.Sequence(lambda n: n)


class FilterDTOFactory(factory.Factory):
    class Meta:
        model = FilterDTO

    filter_id = factory.sequence(lambda n: n)
    filter_name = factory.sequence(lambda n: "filter_name_{}".format(n))
    user_id = factory.sequence(lambda n: "{}".format(n))
    is_selected = Status.ENABLED.value
    template_id = factory.sequence(lambda n: "template_{}".format(n))
    template_name = factory.sequence(lambda n: "Template {}".format(n))


class ConditionDTOFactory(factory.Factory):
    class Meta:
        model = ConditionDTO

    filter_id = factory.sequence(lambda n: n)
    condition_id = factory.sequence(lambda n: n)
    field_id = factory.sequence(lambda n: "FIELD_ID-{}".format(n))
    field_name = factory.sequence(lambda n: "DISPLAY_NAME-{}".format(n))
    operator = Operators.GTE.value
    value = factory.sequence(lambda n: "value_{}".format(n))


class TaskBaseDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskBaseDetailsDTO

    template_id = factory.sequence(
        lambda counter: "template_{}".format(counter))
    project_id = factory.sequence(
        lambda counter: "project_id{}".format(counter))
    task_display_id = factory.sequence(
        lambda counter: "IBWF-{}".format(counter + 1))
    title = factory.sequence(lambda counter: "title_{}".format(counter))
    description = factory.sequence(
        lambda counter: "description_{}".format(counter))
    start_date = datetime(2020, 4, 5, 4, 50, 40)
    due_date = datetime(2020, 4, 5, 4, 50, 40) + timedelta(10)
    priority = Priority.HIGH.value


class TaskDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskDetailsDTO

    @factory.lazy_attribute
    def task_base_details_dto(self):
        return TaskBaseDetailsDTOFactory()

    @factory.lazy_attribute
    def task_gof_dtos(self):
        return [TaskGoFDTOFactory()]

    @factory.lazy_attribute
    def task_gof_field_dtos(self):
        return [TaskGoFFieldDTOFactory()]

    @factory.lazy_attribute
    def project_details_dto(self):
        from ib_tasks.tests.factories.adapter_dtos \
            import ProjectDetailsDTOFactory
        return ProjectDetailsDTOFactory()


class StageRoleDTOFactory(factory.Factory):
    class Meta:
        model = StageRoleDTO

    db_stage_id = factory.Sequence(lambda n: n + 1)
    role_id = factory.Iterator(
        ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"]
    )


class TaskDueMissingDTOFactory(factory.Factory):
    class Meta:
        model = TaskDueMissingDTO

    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    due_missed_count = factory.Sequence(lambda n: n)
    due_date_time = datetime.today().date() + timedelta(days=2)
    user_id = factory.Sequence(
        lambda counter: "123e4567-e89b-12d3-a456-42661417400{}".format(
            counter))
    reason = "reason"


class UserDetailsDTOFactory(factory.Factory):
    class Meta:
        model = UserDetailsDTO

    user_id = factory.Sequence(
        lambda n: "123e4567-e89b-12d3-a456-42661417400%d" % (n + 1))
    user_name = factory.Sequence(lambda n: "user_name_%d" % (n + 1))
    profile_pic_url = factory.Sequence(lambda n: "profile_pic_%d" % (n + 1))


class TaskStageAssigneeDTOFactory(factory.Factory):
    class Meta:
        model = TaskStageAssigneeDTO

    task_stage_id = factory.sequence(lambda counter: counter + 1)
    stage_id = factory.Sequence(lambda counter: counter + 1)
    team_id = factory.Sequence(lambda counter: "team{}".format(counter))
    assignee_id = factory.sequence(
        lambda counter: "123e4567-e89b-12d3-a456-42661417400{}".format(
            counter))


class TaskStageHistoryDTOFactory(factory.Factory):
    class Meta:
        model = TaskStageHistoryDTO

    log_id = factory.sequence(lambda n: n)
    task_id = factory.sequence(lambda n: n)
    stage_id = factory.sequence(lambda n: n)
    stage_duration = None
    started_at = datetime(2012, 10, 10)
    assignee_id = factory.sequence(lambda n: "%d" % n)
    left_at = datetime(2012, 10, 11)


class StageMinimalDTOFactory(factory.Factory):
    class Meta:
        model = StageMinimalDTO

    stage_id = factory.sequence(lambda n: n)
    name = factory.sequence(lambda n: "stage_%d" % n)
    color = None

    class Params:
        stage_color = factory.Trait(color="#ffffff")


class StageFlowDTOFactory(factory.Factory):
    class Meta:
        model = StageFlowDTO
    previous_stage_id = factory.sequence(lambda n: n)
    action_name = factory.sequence(lambda n: "action_name_%d" % n)
    next_stage_id = factory.sequence(lambda n: n)


class LogDurationDTOFactory(factory.Factory):
    class Meta:
        model = LogDurationDTO

    entity_id = factory.sequence(lambda n: n)
    duration = timedelta(days=1)


class TaskStageHavingAssigneeIdDTOFactory(factory.Factory):
    class Meta:
        model = TaskStageHavingAssigneeIdDTO

    db_stage_id = factory.Sequence(lambda counter: counter + 1)
    assignee_id = factory.sequence(
        lambda counter: "123e4567-e89b-12d3-a456-42661417400{}".format(
            counter))
    stage_display_name = factory.Sequence(lambda n: "name_%d" % n)


class GoFIdWithSameGoFOrderDTOFactory(factory.Factory):
    class Meta:
        model = GoFIdWithSameGoFOrderDTO

    gof_id = factory.Sequence(lambda c: "gof_{}".format(c))
    same_gof_order = factory.Sequence(lambda c: c)


class FieldIdWithTaskGoFIdDTOFactory(factory.Factory):
    class Meta:
        model = FieldIdWithTaskGoFIdDTO

    field_id = factory.Sequence(lambda c: "field_{}".format(c))
    task_gof_id = factory.Sequence(lambda c: c)


class CurrentStageDetailsDTOFactory(factory.Factory):
    class Meta:
        model = CurrentStageDetailsDTO

    stage_id = factory.sequence(lambda counter: "stage_{}".format(counter))
    stage_display_name = factory.sequence(
        lambda counter: "name_{}".format(counter))


class FieldSearchableDTOFactory(factory.Factory):
    class Meta:
        model = FieldSearchableDTO

    task_gof_id = factory.sequence(lambda counter: counter)
    field_id = factory.sequence(lambda counter: "field{}".format(counter))
    field_value = Searchable.CITY.value
    field_response = "1"


class ProjectIdWithTaskTemplateIdDTOFactory(factory.Factory):
    class Meta:
        model = ProjectIdWithTaskTemplateIdDTO

    project_id = factory.sequence(lambda counter: "project_{}".format(counter))
    task_template_id = factory.sequence(
        lambda counter: "template_{}".format(counter))


class FieldIdWithFieldDisplayNameDTOFactory(factory.Factory):
    class Meta:
        model = FieldIdWithFieldDisplayNameDTO

    field_id = factory.Sequence(lambda c: "field_id_{}".format(c))
    gof_display_name = factory.Sequence(
        lambda c: "gof_display_name{}".format(c))
    field_display_name = factory.Sequence(
        lambda c: "field_display_name_{}".format(c))


class StageIdActionNameDTOFactory(factory.Factory):
    class Meta:
        model = StageIdActionNameDTO

    stage_id = factory.sequence(lambda counter: "stage_{}".format(counter))
    action_name = factory.sequence(lambda counter: "action_name_{}".format(counter))


class StageActionIdDTOFactory(factory.Factory):
    class Meta:
        model = StageActionIdDTO

    action_id = factory.sequence(lambda counter: counter)
    stage_id = factory.sequence(lambda counter: "stage_{}".format(counter))
    action_name = factory.sequence(lambda counter: "action_name_{}".format(counter))