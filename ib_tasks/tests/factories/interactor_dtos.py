from datetime import timedelta, datetime

import factory

from ib_tasks.adapters.dtos import UserDTO
from ib_tasks.constants.enum import Searchable, Priority
from ib_tasks.interactors.field_dtos import SearchableFieldTypeDTO, \
    SearchableFieldDetailDTO
from ib_tasks.interactors.get_stage_searchable_possible_assignees_interactor \
    import SearchQueryWithPaginationDTO
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.gofs_dtos \
    import GoFWithOrderAndAddAnotherDTO, GoFsWithTemplateIdDTO, FieldDisplayDTO
from ib_tasks.interactors.stage_dtos import TaskStageDTO
from ib_tasks.interactors.stages_dtos import TaskTemplateStageActionDTO, \
    StageActionDTO, StagesActionDTO, TaskIdWithStageAssigneeDTO, \
    UserStagesWithPaginationDTO, StageAssigneeDTO, \
    StageAssigneeWithTeamDetailsDTO, AssigneeWithTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldDetailsDTO, FieldWritePermissionRolesDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFWritePermissionRolesDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    CurrentStageDetailsDTO, StageIdWithValueDTO, StageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskDueDetailsDTO
from ib_tasks.interactors.task_dtos import GoFFieldsDTO, \
    TaskDueParametersDTO, \
    FieldValuesDTO, GetTaskDetailsDTO, StatusOperandStageDTO, \
    CreateTaskLogDTO, \
    CreateTaskDTO, UpdateTaskDTO, StageIdWithAssigneeDTO, \
    SaveAndActOnTaskDTO, TaskCurrentStageDetailsDTO, \
    TaskDelayParametersDTO, UpdateTaskWithTaskDisplayIdDTO, \
    SaveAndActOnTaskWithTaskDisplayIdDTO, SearchableDTO, SearchQueryDTO
from ib_tasks.interactors.task_template_dtos import \
    CreateTransitionChecklistTemplateDTO, \
    CreateTransitionChecklistTemplateWithTaskDisplayIdDTO
from ib_tasks.tests.factories.adapter_dtos import AssigneeDetailsDTOFactory, \
    UserDetailsDTO, TeamInfoDTOFactory


class GetTaskDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GetTaskDetailsDTO

    task_id = factory.Sequence(lambda n: n + 1)
    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % (n + 1))


class UserDetailsDTOFactory(factory.Factory):
    class Meta:
        model = UserDetailsDTO

    user_id = factory.Sequence(lambda n: "user_id_%d" % n)
    user_name = factory.Sequence(lambda n: "name_%d" % n)
    profile_pic_url = "pic_url"


class GetTaskDueDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskDueDetailsDTO

    user = factory.SubFactory(AssigneeDetailsDTOFactory)
    task_id = factory.Sequence(lambda n: 'task_id_%d' % (n + 1))
    due_date_time = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%z")
    due_missed_count = factory.Sequence(lambda n: n)
    reason = factory.Sequence(lambda n: "reason_id_%d" % n)


class StageActionDTOFactory(factory.Factory):
    class Meta:
        model = StageActionDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % (n + 1))
    action_name = factory.Sequence(lambda n: 'action_name_%d' % (n + 1))
    logic = factory.Sequence(lambda n: 'logic%d' % (n + 1))
    roles = factory.Sequence(lambda n: [f'ROLE_{n + 1}', f'ROLE_{n + 2}'])
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n + 1))
    action_type = "action_type"
    transition_template_id = factory.Sequence(
        lambda n: "template_%d" % (n + 1))
    button_color = factory.Sequence(lambda n: 'button_color_%d' % (n + 1))
    function_path = "sample_function_path"


class TaskTemplateStageActionDTOFactory(factory.Factory):
    class Meta:
        model = TaskTemplateStageActionDTO

    task_template_id = factory.Sequence(lambda n: "task_template_%d" % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    action_name = factory.Sequence(lambda n: 'action_name_%d' % (n + 1))
    logic = factory.Sequence(lambda n: 'logic%d' % (n + 1))
    roles = factory.Sequence(lambda n: [f'ROLE_{n + 1}', f'ROLE_{n + 2}'])
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n + 1))
    button_color = factory.Sequence(lambda n: 'button_color_%d' % (n + 1))
    function_path = "sample_function_path"
    action_type = "action_type"
    transition_template_id = factory.Sequence(
        lambda n: "transition_template_id_%d" % (n + 1))


class TaskStageDTOFactory(factory.Factory):
    class Meta:
        model = TaskStageDTO

    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    db_stage_id = factory.Sequence(lambda n: 'db_stage_%d' % (n + 1))
    display_name = factory.Sequence(lambda n: 'display_name_%d' % (n + 1))
    stage_colour = factory.Sequence(lambda n: 'stage_color_%d' % (n + 1))


class FieldDisplayDTOFactory(factory.Factory):
    class Meta:
        model = FieldDisplayDTO

    field_id = factory.Sequence(lambda n: '%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    field_type = factory.Sequence(lambda n: 'field_type_%d' % (n + 1))
    key = factory.Sequence(lambda n: 'key_%d' % (n + 1))
    value = factory.Sequence(lambda n: 'value_%d' % (n + 1))


class GlobalConstantsDTOFactory(factory.Factory):
    class Meta:
        model = GlobalConstantsDTO

    constant_name = factory.sequence(lambda n: "Constant_{}".format(n + 1))
    value = factory.sequence(lambda n: n)


class FieldDetailsDTOFactory(factory.Factory):
    class Meta:
        model = FieldDetailsDTO

    field_type = factory.Sequence(lambda n: 'field_type_%d' % (n + 1))
    field_id = factory.Sequence(lambda n: "%d" % (n + 1))
    key = factory.Sequence(lambda n: 'key_%d' % (n + 1))
    value = factory.Sequence(lambda n: 'value_%d' % (n + 1))


class ActionDetailsDTOFactory(factory.Factory):
    class Meta:
        model = ActionDetailsDTO

    action_id = factory.Sequence(lambda n: (n + 1))
    name = factory.Sequence(lambda n: 'name_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n + 1))
    button_color = None


class GoFWithOrderAndAddAnotherDTOFactory(factory.Factory):
    class Meta:
        model = GoFWithOrderAndAddAnotherDTO

    gof_id = factory.sequence(lambda n: "gof_{}".format(n + 1))
    order = factory.sequence(lambda n: n)
    enable_add_another_gof = factory.Iterator([True, False])


class GoFsWithTemplateIdDTOFactory(factory.Factory):
    class Meta:
        model = GoFsWithTemplateIdDTO

    template_id = factory.sequence(lambda n: "template_{}".format(n + 1))
    gof_dtos = factory.SubFactory(GoFWithOrderAndAddAnotherDTOFactory)


class ActionDTOFactory(factory.Factory):
    class Meta:
        model = StagesActionDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    action_name = factory.Sequence(lambda n: "name_%d" % n)
    function_path = "path"
    logic = factory.Sequence(lambda n: 'status_id_%d==stage_id' % n)
    roles = ['Role_1', 'Role_2']
    button_text = "text"
    button_color = None

    class Params:
        color = factory.Trait(button_color="#ffffff")


class FieldValuesDTOFactory(factory.Factory):
    class Meta:
        model = FieldValuesDTO

    field_id = factory.Sequence(lambda counter: "field{}".format(counter))
    field_response = factory.Sequence(
        lambda counter: "field_response{}".format(counter))


class GoFFieldsDTOFactory(factory.Factory):
    class Meta:
        model = GoFFieldsDTO

    gof_id = factory.sequence(lambda counter: "gof_{}".format(counter))
    same_gof_order = 1

    @factory.LazyAttribute
    def field_values_dtos(self):
        field_values_dtos = FieldValuesDTOFactory.create_batch(size=2)
        return field_values_dtos


class SearchableFieldTypeDTOFactory(factory.Factory):
    class Meta:
        model = SearchableFieldTypeDTO

    searchable_type = Searchable.USER.value
    limit = factory.Sequence(lambda n: n + 1)
    offset = factory.Sequence(lambda n: n + 1)
    search_query = ""


class SearchableFieldUserDetailDTOFactory(factory.Factory):
    class Meta:
        model = SearchableFieldDetailDTO

    id = factory.sequence(lambda n: "user_{}".format(n + 1))
    name = factory.sequence(lambda n: "user_name_{}".format(n + 1))


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    user_id = factory.sequence(lambda n: "user_{}".format(n + 1))
    name = factory.sequence(lambda n: "user_name_{}".format(n + 1))


class UserStagesWithPaginationDTOFactory(factory.Factory):
    class Meta:
        model = UserStagesWithPaginationDTO

    stage_ids = ["stage_id_1", "stage_id_2"]
    user_id = factory.sequence(lambda n: "user_{}".format(n + 1))
    limit = factory.Sequence(lambda n: n + 1)
    offset = factory.Sequence(lambda n: n + 1)


class StatusOperandStageDTOFactory(factory.Factory):
    class Meta:
        model = StatusOperandStageDTO

    variable = factory.sequence(lambda n: "variable_{}".format(n + 1))
    operator = "=="
    stage = factory.sequence(lambda n: "stage_{}".format(n + 1))


class CreateTaskLogDTOFactory(factory.Factory):
    class Meta:
        model = CreateTaskLogDTO

    task_json = factory.sequence(lambda n: "{{'task_json'_'{}'}}".format(n))
    task_id = factory.sequence(lambda n: n)
    user_id = factory.sequence(lambda n: "user_{}".format(n))
    action_id = factory.sequence(lambda n: n)


class TaskIdWithStageAssigneeDTOFactory(factory.Factory):
    class Meta:
        model = TaskIdWithStageAssigneeDTO

    task_id = factory.sequence(lambda n: n + 1)
    db_stage_id = factory.Sequence(lambda n: n + 1)
    assignee_id = factory.sequence(lambda n: "user_{}".format(n))
    team_id = factory.sequence(lambda n: "team_{}".format(n + 1))


class StageAssigneeDetailsDTOFactory(factory.Factory):
    class Meta:
        model = StageAssigneeDetailsDTO

    task_stage_id = factory.sequence(lambda counter: counter + 1)
    stage_id = factory.sequence(lambda counter: counter)

    @factory.lazy_attribute
    def assignee_details_dto(self):
        return [AssigneeDetailsDTOFactory()]


class StageAssigneeDetailsWithOneAssigneeDTOFactory(factory.Factory):
    class Meta:
        model = StageAssigneeDetailsDTO

    task_stage_id = factory.sequence(lambda counter: counter + 1)
    stage_id = factory.sequence(lambda counter: counter)

    @factory.lazy_attribute
    def assignee_details_dto(self):
        return AssigneeDetailsDTOFactory()


class SearchQueryDTOFactory(factory.Factory):
    class Meta:
        model = SearchQueryDTO

    user_id = factory.sequence(lambda n: n)
    offset = factory.sequence(lambda n: n - 1)
    limit = factory.sequence(lambda n: n)
    search_query = factory.sequence(lambda n: "value_{}" % n)


class TaskDueParametersDTOFactory(factory.Factory):
    class Meta:
        model = TaskDueParametersDTO

    user_id = factory.Sequence(lambda n: "user_id_%d" % n)
    due_date_time = datetime.now() + timedelta(days=2)
    reason_id = factory.Iterator([1, 2, 3, 4, -1])
    stage_id = factory.Sequence(lambda n: "stage_id_%d" % (n + 1))
    reason = "reason"


class TaskDelayParametersDTOFactory(factory.Factory):
    class Meta:
        model = TaskDelayParametersDTO

    user_id = factory.Sequence(lambda n: "user_id_%d" % n)
    task_id = factory.sequence(lambda n: (n + 1))
    due_date_time = datetime.now() + timedelta(days=2)
    reason_id = factory.Iterator([1, 2, 3, 4, -1])
    reason = "reason"


class CreateTaskDTOFactory(factory.Factory):
    class Meta:
        model = CreateTaskDTO

    project_id = factory.Sequence(lambda c: "project_id_{}".format(c))
    task_template_id = factory.Sequence(lambda c: "task_template_{}".format(c))
    created_by_id = "123e4567-e89b-12d3-a456-426614174000"
    action_id = factory.Sequence(lambda c: "action_id_{}".format(c))
    title = factory.Sequence(lambda c: "title_{}".format(c))
    description = factory.Sequence(lambda c: "description{}".format(c))
    start_date = datetime.today().date()
    due_date = datetime.today().date() + timedelta(days=2)
    due_time = "12:30:20"
    priority = Priority.HIGH.value

    @factory.lazy_attribute
    def gof_fields_dtos(self):
        return [GoFFieldsDTOFactory(), GoFFieldsDTOFactory()]


class StageIdWithAssigneeDTOFactory(factory.Factory):
    class Meta:
        model = StageIdWithAssigneeDTO

    stage_id = factory.Sequence(lambda c: "stage_{}".format(c))
    assignee_id = factory.Sequence(lambda c: "assignee_{}".format(c))
    team_id = factory.Sequence(lambda c: "team_{}".format(c))


class UpdateTaskDTOFactory(factory.Factory):
    class Meta:
        model = UpdateTaskDTO

    task_id = factory.Sequence(lambda c: c)
    created_by_id = "123e4567-e89b-12d3-a456-426614174000"
    title = factory.Sequence(lambda c: "title_{}".format(c))
    description = factory.Sequence(lambda c: "description{}".format(c))
    start_date = datetime.today().date()
    due_date = datetime.today().date() + timedelta(days=2)
    due_time = "12:30:20"
    priority = Priority.HIGH.value
    stage_assignee = factory.SubFactory(StageIdWithAssigneeDTOFactory)

    @factory.lazy_attribute
    def gof_fields_dtos(self):
        return [GoFFieldsDTOFactory(), GoFFieldsDTOFactory()]


class UpdateTaskWithTaskDisplayIdDTOFactory(factory.Factory):
    class Meta:
        model = UpdateTaskWithTaskDisplayIdDTO

    task_display_id = factory.Sequence(
        lambda c: "task_display_id_{}".format(c))
    created_by_id = "123e4567-e89b-12d3-a456-426614174000"
    title = factory.Sequence(lambda c: "title_{}".format(c))
    description = factory.Sequence(lambda c: "description{}".format(c))
    start_date = datetime.today().date()
    due_date = datetime.today().date() + timedelta(days=2)
    due_time = "12:30:20"
    priority = Priority.HIGH.value
    stage_assignee = factory.SubFactory(StageIdWithAssigneeDTOFactory)

    @factory.lazy_attribute
    def gof_fields_dtos(self):
        return [GoFFieldsDTOFactory(), GoFFieldsDTOFactory()]


class SaveAndActOnTaskDTOFactory(factory.Factory):
    class Meta:
        model = SaveAndActOnTaskDTO

    task_id = factory.Sequence(lambda c: "task_{}".format(c))
    created_by_id = "123e4567-e89b-12d3-a456-426614174000"
    action_id = factory.Sequence(lambda c: c)
    title = factory.Sequence(lambda c: "title_{}".format(c))
    description = factory.Sequence(lambda c: "description{}".format(c))
    start_date = datetime.today().date()
    due_date = datetime.today().date() + timedelta(days=2)
    due_time = "12:30:20"
    priority = Priority.HIGH.value
    stage_assignee = factory.SubFactory(StageIdWithAssigneeDTOFactory)

    @factory.lazy_attribute
    def gof_fields_dtos(self):
        return [GoFFieldsDTOFactory(), GoFFieldsDTOFactory()]


class SaveAndActOnTaskWithTaskDisplayIdDTOFactory(factory.Factory):
    class Meta:
        model = SaveAndActOnTaskWithTaskDisplayIdDTO

    task_display_id = factory.Sequence(lambda c: "task_{}".format(c))
    created_by_id = "123e4567-e89b-12d3-a456-426614174000"
    action_id = factory.Sequence(lambda c: c)
    title = factory.Sequence(lambda c: "title_{}".format(c))
    description = factory.Sequence(lambda c: "description{}".format(c))
    start_date = datetime.today().date()
    due_date = datetime.today().date() + timedelta(days=2)
    due_time = "12:30:20"
    priority = Priority.HIGH.value
    stage_assignee = factory.SubFactory(StageIdWithAssigneeDTOFactory)

    @factory.lazy_attribute
    def gof_fields_dtos(self):
        return [GoFFieldsDTOFactory(), GoFFieldsDTOFactory()]


class SearchDTOFactory(factory.Factory):
    class Meta:
        model = SearchQueryWithPaginationDTO

    limit = factory.Sequence(lambda number: number)
    offset = factory.Sequence(lambda number: number)
    search_query = factory.Sequence(lambda number: 'user_{}'.format(number))


class CurrentStageDetailsDTOFactory(factory.Factory):
    class Meta:
        model = CurrentStageDetailsDTO

    stage_id = factory.Sequence(lambda c: "stage_{}".format(c))
    stage_display_name = factory.Sequence(
        lambda c: "stage_display_name_{}".format(c))


class TaskCurrentStageDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskCurrentStageDetailsDTO

    task_display_id = factory.Sequence(lambda c: "task_display_{}".format(c))
    user_has_permission = True

    @factory.lazy_attribute
    def stage_details_dtos(self):
        return [CurrentStageDetailsDTOFactory(),
                CurrentStageDetailsDTOFactory()]


class GoFWritePermissionRolesDTOFactory(factory.Factory):
    class Meta:
        model = GoFWritePermissionRolesDTO

    gof_id = factory.sequence(lambda counter: "gof_{}".format(counter))
    write_permission_roles = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC']


class FieldWritePermissionRolesDTOFactory(factory.Factory):
    class Meta:
        model = FieldWritePermissionRolesDTO

    field_id = factory.sequence(lambda counter: "field_{}".format(counter))
    write_permission_roles = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC']


class CreateTransitionChecklistTemplateDTOFactory(factory.Factory):
    class Meta:
        model = CreateTransitionChecklistTemplateDTO

    task_id = factory.Sequence(lambda c: c)
    created_by_id: str
    transition_checklist_template_id: factory.Sequence(
        lambda c: "transition_checklist_template_".format(c))
    action_id: factory.Sequence(lambda c: c)
    stage_id: factory.Sequence(lambda c: c)

    @factory.lazy_attribute
    def transition_checklist_gofs(self):
        return [GoFFieldsDTOFactory(), GoFFieldsDTOFactory()]


class CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
    factory.Factory
):
    class Meta:
        model = CreateTransitionChecklistTemplateWithTaskDisplayIdDTO

    task_display_id = factory.Sequence(
        lambda c: "task_display_id_{}".format(c))
    created_by_id = "123e4567-e89b-12d3-a456-426614174000"
    transition_checklist_template_id = factory.Sequence(
        lambda c: "transition_checklist_template_".format(c))
    action_id = factory.Sequence(lambda c: c)
    stage_id = factory.Sequence(lambda c: c)

    @factory.lazy_attribute
    def transition_checklist_gofs(self):
        return [GoFFieldsDTOFactory(), GoFFieldsDTOFactory()]


class StageAssigneeDTOFactory(factory.Factory):
    class Meta:
        model = StageAssigneeDTO

    db_stage_id = factory.Sequence(lambda n: n + 1)
    assignee_id = factory.sequence(lambda n: "user_{}".format(n + 1))
    team_id = factory.Sequence(lambda n: "team_{}".format(n + 1))


class SearchableDTOFactory(factory.Factory):
    class Meta:
        model = SearchableDTO

    search_type = Searchable.TEAM.value
    id = "team1"


class StageIdWithValueDTOFactory(factory.Factory):
    class Meta:
        model = StageIdWithValueDTO

    db_stage_id = factory.Sequence(lambda n: n + 1)
    stage_value = factory.Sequence(lambda n: n)


class StageAssigneeWithTeamDetailsDTOFactory(factory.Factory):
    class Meta:
        model = StageAssigneeWithTeamDetailsDTO

    task_stage_id = factory.sequence(lambda counter: counter + 1)
    stage_id = factory.sequence(lambda counter: counter + 1)

    @factory.lazy_attribute
    def assignee_details_dto(self):
        return AssigneeWithTeamDetailsDTOFactory()


class AssigneeWithTeamDetailsDTOFactory(factory.Factory):
    class Meta:
        model = AssigneeWithTeamDetailsDTO

    assignee_id = factory.sequence(
        lambda counter: "123e4567-e89b-12d3-a456-42661417400{}".format(
            counter))
    name = factory.sequence(lambda counter: "name_{}".format(counter))
    profile_pic_url = "https://www.google.com/search?q=ibhubs&client=ubuntu" \
                      "&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved" \
                      "=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw" \
                      "=1848&bih=913#imgrc=Kg3TRY0jmx3udM"

    @factory.lazy_attribute
    def team_info_dto(self):
        return TeamInfoDTOFactory()
