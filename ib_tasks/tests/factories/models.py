import json
from datetime import datetime, timedelta

import factory

from ib_tasks.constants.enum import PermissionTypes, FieldTypes, Operators, \
    Priority, ActionTypes, DELAY_REASONS
from ib_tasks.models import (
    Stage, ActionPermittedRoles, StageAction, TaskTemplateStatusVariable,
    UserTaskDelayReason, Task, TaskGoF, TaskGoFField,
    TaskTemplateGlobalConstants,
    TaskStatusVariable, Filter, FilterCondition, TaskLog,
    StagePermittedRoles, ElasticSearchTask, ProjectTaskTemplate, TaskStageRp,
    StageGoF, StageFlow)
from ib_tasks.models.current_task_stage import CurrentTaskStage
from ib_tasks.models.field import Field
from ib_tasks.models.field_role import FieldRole
from ib_tasks.models.global_constant import GlobalConstant
from ib_tasks.models.gof import GoF
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.models.task_stage_history import TaskStageHistory
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
from ib_tasks.models.task_template_initial_stages import \
    TaskTemplateInitialStage


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    task_display_id = factory.sequence(
        lambda counter: "IBWF-{}".format(counter + 1))
    project_id = factory.Sequence(
        lambda n: "project_id_%d" % (n + 1)
    )
    template_id = factory.Sequence(
        lambda counter: "template_{}".format(counter))
    created_by = "123e4567-e89b-12d3-a456-426614174000"
    title = factory.sequence(lambda counter: "title_{}".format(counter))
    description = factory.sequence(
        lambda counter: "description_{}".format(counter))
    start_date = datetime(2020, 10, 12, 4, 40)
    due_date = datetime(2020, 10, 12, 4, 40) + timedelta(10)
    priority = Priority.HIGH.value


class StageModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stage

    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)
    display_name = factory.Sequence(lambda n: "name_%d" % n)
    task_template_id = factory.Sequence(lambda n: "task_template_id_%d" % n)
    value = factory.Sequence(lambda n: n)
    stage_color = factory.Iterator(["blue", "orange", "green"])
    display_logic = factory.Sequence(lambda n: "status_id_%d==stage_id" % n)
    card_info_kanban = json.dumps(['field_id_1', "field_id_2"])
    card_info_list = json.dumps(['field_id_1', "field_id_2"])


class UserRpInTaskStageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskStageRp

    task = factory.SubFactory(TaskFactory)
    stage = factory.SubFactory(StageModelFactory)
    rp_id = factory.Sequence(
        lambda n: "123e4567-e89b-12d3-a456-42661417405%d" % n)


class TaskStageModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CurrentTaskStage

    task = factory.SubFactory(TaskFactory)
    stage = factory.SubFactory(StageModelFactory)


class TaskModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    project_id = factory.Sequence(lambda counter: "project_{}".format(counter))
    task_display_id = factory.sequence(lambda counter: "iB_{}".format(counter))
    template_id = factory.Sequence(lambda n: "template_%d" % (n + 1))
    project_id = factory.Sequence(lambda n: "project_id{}".format(n))
    created_by = factory.Sequence(lambda n: (n + 1))
    title = factory.Sequence(lambda c: "title_{}".format(c))
    description = factory.Sequence(lambda c: "description_{}".format(c))
    start_date = datetime.now()
    due_date = datetime.now() + timedelta(days=2)


class TaskTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskTemplate

    template_id = factory.sequence(lambda n: "template_{}".format(n + 1))
    name = factory.sequence(lambda n: "Template {}".format(n + 1))


class TaskTemplateWithTransitionFactory(TaskTemplateFactory):
    is_transition_template = factory.Iterator([True, False])


class TaskDueDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserTaskDelayReason

    task = factory.SubFactory(TaskFactory)
    due_datetime = datetime.now() + timedelta(days=2)
    stage = factory.SubFactory(StageModelFactory)
    count = factory.Sequence(lambda n: (n + 1))
    user_id = factory.Sequence(
        lambda n: "123e4567-e89b-12d3-a456-42661417400%d" % n)
    reason_id = DELAY_REASONS[0]['id']
    reason = DELAY_REASONS[0]['reason']


class StageActionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StageAction

    stage = factory.SubFactory(StageModelFactory)
    name = factory.Sequence(lambda n: "action_name_%d" % n)
    button_text = "hey"
    button_color = "#fafafa"
    logic = "Status1 = PR_PAYMENT_REQUEST_DRAFTS"
    py_function_import_path = "path"
    action_type = ActionTypes.NO_VALIDATIONS.value
    transition_template = factory.SubFactory(TaskTemplateFactory)


class StageActionWithTransitionFactory(StageActionFactory):
    action_type = "action_type"
    transition_template = factory.SubFactory(TaskTemplateWithTransitionFactory)


class ActionPermittedRolesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActionPermittedRoles

    action = factory.SubFactory(StageActionFactory)
    role_id = factory.Sequence(lambda n: "role_%d" % n)


class TaskTemplateStatusVariableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskTemplateStatusVariable

    task_template_id = factory.Sequence(lambda n: n)
    variable = factory.Sequence(lambda n: "status_id_%d" % n)
    value = factory.Sequence(lambda n: n)


class TaskStatusVariableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskStatusVariable

    task_id = factory.Sequence(lambda n: "%d" % n)
    variable = factory.Sequence(lambda n: "status_variable_%d" % n)
    value = factory.Sequence(lambda n: "value_%d" % n)


class TaskTemplateGlobalConstantsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskTemplateGlobalConstants

    task_template_id = factory.Sequence(lambda n: n)
    variable = factory.Sequence(lambda n: "variable%d" % n)
    value = factory.Sequence(lambda n: "value%d" % n)
    data_type = factory.Sequence(lambda n: "data_type_%d" % n)


class GoFFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoF

    gof_id = factory.Sequence(lambda counter: "gof_{}".format(counter + 1))
    display_name = factory.Sequence(
        lambda counter: "GOF_DISPLAY_NAME-{}".format(counter)
    )
    max_columns = 2


class FieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Field

    gof = factory.SubFactory(GoFFactory)
    field_id = factory.Sequence(lambda counter: "FIELD_ID-{}".format(counter))
    display_name = factory.Sequence(
        lambda counter: "DISPLAY_NAME-{}".format(counter)
    )
    field_type = FieldTypes.PLAIN_TEXT.value
    required = True
    order = factory.sequence(lambda counter: counter)

    class Params:
        optional = factory.Trait(
            field_values='["mr", "mrs"]'
        )


class GoFRoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoFRole

    gof = factory.SubFactory(GoFFactory)
    role = factory.Sequence(lambda counter: "ROLE-{}".format(counter))
    permission_type = PermissionTypes.READ.value


class FieldRoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FieldRole

    field = factory.SubFactory(FieldFactory)
    role = factory.Iterator(
        ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"]
    )
    permission_type = PermissionTypes.READ.value


class GlobalConstantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GlobalConstant

    name = factory.sequence(lambda n: "constant_{}".format(n + 1))
    value = factory.sequence(lambda n: (n + 1))
    task_template = factory.SubFactory(TaskTemplateFactory)


class GoFToTaskTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskTemplateGoFs

    task_template = factory.SubFactory(TaskTemplateFactory)
    gof = factory.SubFactory(GoFFactory)
    order = factory.sequence(lambda n: n)
    enable_add_another_gof = factory.Iterator([True, False])


class TaskTemplateWith2GoFsFactory(TaskTemplateFactory):
    gof1 = factory.RelatedFactory(
        GoFToTaskTemplateFactory, 'task_template', gof__gof_id='gof_1'
    )
    gof2 = factory.RelatedFactory(
        GoFToTaskTemplateFactory, 'task_template', gof__gof_id='gof_2'
    )


class TaskGoFFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskGoF

    same_gof_order = 1
    gof = factory.SubFactory(GoFFactory)
    task = factory.SubFactory(TaskFactory)


class TaskGoFFieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskGoFField

    task_gof = factory.SubFactory(TaskGoFFactory)
    field = factory.SubFactory(FieldFactory)
    field_response = factory.Sequence(
        lambda counter: "field_response_{}".format(counter)
    )


class TaskTemplateInitialStageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskTemplateInitialStage

    task_template = factory.SubFactory(TaskTemplateFactory)
    stage = factory.SubFactory(StageModelFactory)


class CurrentTaskStageModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CurrentTaskStage

    task = factory.SubFactory(TaskFactory)
    stage = factory.SubFactory(StageModelFactory)


class FilterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Filter

    created_by = factory.sequence(lambda n: "{}".format(n))
    name = factory.sequence(lambda n: "filter_name_{}".format(n))
    template = factory.SubFactory(TaskTemplateFactory)
    is_selected = "ENABLED"


class FilterConditionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FilterCondition

    filter = factory.SubFactory(FilterFactory)
    field = factory.SubFactory(FieldFactory)
    operator = Operators.GTE.value
    value = factory.sequence(lambda n: "value_{}".format(n))


class StagePermittedRolesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StagePermittedRoles

    stage = factory.SubFactory(StageModelFactory)
    role_id = factory.Iterator(
        ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"]
    )


class TaskStageHistoryModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskStageHistory

    task = factory.SubFactory(TaskFactory)
    stage = factory.SubFactory(StageModelFactory)
    assignee_id = factory.sequence(
        lambda n: "123e4567-e89b-12d3-a456-42661417400{}".format(n))
    joined_at = datetime(2012, 10, 10)
    left_at = datetime(2012, 10, 11)
    team_id = factory.Sequence(lambda n: "team_{}".format(n + 1))


class ElasticSearchTaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ElasticSearchTask

    elasticsearch_id = factory.sequence(
        lambda n: 'elastic_search_id_{}'.format(n))
    task_id = factory.sequence(lambda n: n)


class TaskLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskLog

    task = factory.SubFactory(TaskFactory)
    task_json = """ json """
    acted_at = "2020-08-11 12:00:00"
    action = factory.SubFactory(StageActionFactory)
    user_id = factory.Sequence(
        lambda n: "123e4567-e89b-12d3-a456-42661417400%d" % n)


class StageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stage

    stage_id = factory.Sequence(lambda c: "stage_{}".format(c))
    task_template_id = factory.Sequence(lambda c: "template_{}".format(c))
    display_name = factory.Sequence(lambda c: "display_name_{}".format(c))
    value = factory.Sequence(lambda c: c)
    stage_color = factory.Sequence(lambda counter: "#fff2f{}".format(counter))


class ProjectTaskTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectTaskTemplate

    task_template = factory.SubFactory(TaskTemplateFactory)
    project_id = factory.sequence(lambda counter: "project_{}".format(counter))


class TaskStageHistoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskStageHistory

    task = factory.SubFactory(TaskFactory)
    stage = factory.SubFactory(StageModelFactory)
    team_id = factory.Sequence(lambda n: "TEAM_ID_%d" % n)
    assignee_id = factory.sequence(
        lambda n: "123e4567-e89b-12d3-a456-42661417400{}".format(n))
    joined_at = datetime(2012, 10, 10)
    left_at = datetime(2012, 10, 11)


class StageFlowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StageFlow

    previous_stage = factory.SubFactory(StageModelFactory)
    action = factory.SubFactory(StageActionFactory)
    next_stage = factory.SubFactory(StageModelFactory)


class StageGoFFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StageGoF

    stage = factory.SubFactory(StageModelFactory)
    gof = factory.SubFactory(GoFFactory)
