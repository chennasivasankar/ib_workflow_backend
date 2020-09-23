import datetime

import factory

from ib_adhoc_tasks.adapters.dtos import FieldDetailsDTO, \
    StageActionDetailsDTO, GetTaskStageCompleteDetailsDTO, \
    AssigneeDetailsDTO, \
    TaskStageAssigneeDetailsDTO, TaskBaseDetailsDTO, TasksCompleteDetailsDTO, \
    TeamDetailsDTO, TaskIdWithSubTasksCountDTO, \
    TaskIdWithCompletedSubTasksCountDTO
from ib_adhoc_tasks.constants.enum import ActionTypes, Priority


class FieldDetailsDTOFactory(factory.Factory):
    class Meta:
        model = FieldDetailsDTO

    field_type = factory.sequence(
        lambda counter: "field_type{}".format(counter))
    field_id = factory.sequence(lambda counter: "field_{}".format(counter))
    key = factory.sequence(lambda counter: "key_{}".format(counter))
    value = factory.sequence(lambda counter: "value_{}".format(counter))


class StageActionDetailsDTOFactory(factory.Factory):
    class Meta:
        model = StageActionDetailsDTO

    action_id = factory.sequence(lambda counter: "action{}".format(counter))
    name = factory.sequence(lambda counter: "name{}".format(counter))
    stage_id = factory.sequence(lambda counter: "stage_id{}".format(counter))
    button_text = factory.sequence(
        lambda counter: "button_text{}".format(counter))
    button_color = factory.sequence(
        lambda counter: "button_color{}".format(counter))
    action_type = factory.Iterator([ActionTypes.NO_VALIDATIONS.value])
    transition_template_id = factory.sequence(
        lambda counter: "transition_template_{}".format(counter))


class GetTaskStageCompleteDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GetTaskStageCompleteDetailsDTO

    task_id = factory.sequence(lambda counter: counter)
    stage_id = factory.sequence(lambda counter: "stage_{}".format(counter))
    stage_color = factory.sequence(
        lambda counter: "stage_color{}".format(counter))
    display_name = factory.sequence(
        lambda counter: "stage_name{}".format(counter))
    db_stage_id = factory.sequence(lambda counter: counter)

    @factory.lazy_attribute
    def field_dtos(self):
        return [FieldDetailsDTOFactory()]

    @factory.lazy_attribute
    def action_dtos(self):
        return [StageActionDetailsDTOFactory()]


class AssigneeDetailsDTOFactory(factory.Factory):
    class Meta:
        model = AssigneeDetailsDTO

    assignee_id = factory.sequence(
        lambda counter: "assignee_{}".format(counter))
    name = factory.sequence(lambda counter: "name_{}".format(counter))
    profile_pic_url = factory.sequence(
        lambda counter: "profile_pic_{}".format(counter))


class TeamDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TeamDetailsDTO

    team_id = factory.sequence(lambda counter: "team_{}".format(counter))
    name = factory.sequence(lambda counter: "name_{}".format(counter))


class TaskStageAssigneeDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskStageAssigneeDetailsDTO

    task_id = factory.sequence(lambda counter: counter)
    stage_id = factory.sequence(lambda counter: "stage_{}".format(counter))

    @factory.lazy_attribute
    def assignee_details(self):
        return AssigneeDetailsDTOFactory()

    @factory.lazy_attribute
    def team_details(self):
        return TeamDetailsDTOFactory()


class TaskBaseDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskBaseDetailsDTO

    template_id = factory.sequence(
        lambda counter: "template_{}".format(counter))
    project_id = factory.sequence(lambda counter: "project_{}".format(counter))
    task_id = factory.sequence(lambda counter: counter)
    task_display_id = factory.sequence(
        lambda counter: "task_display{}".format(counter))
    title = factory.sequence(lambda counter: "title_{}".format(counter))
    description = factory.sequence(
        lambda counter: "description_{}".format(counter))
    start_date = datetime.datetime(2020, 9, 10, 5, 30)
    due_date = datetime.datetime(2020, 10, 10, 5, 30)
    priority = factory.Iterator(
        [Priority.HIGH.value, Priority.LOW.value, Priority.MEDIUM.value])


class TasksCompleteDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TasksCompleteDetailsDTO

    @factory.lazy_attribute
    def task_base_details_dtos(self):
        return [TaskBaseDetailsDTOFactory()]

    @factory.lazy_attribute
    def task_stage_details_dtos(self):
        return [GetTaskStageCompleteDetailsDTOFactory()]

    @factory.lazy_attribute
    def task_stage_assignee_dtos(self):
        return [TaskStageAssigneeDetailsDTOFactory()]


class TaskIdWithSubTasksCountDTOFactory(factory.Factory):
    class Meta:
        model = TaskIdWithSubTasksCountDTO

    task_id = factory.sequence(lambda counter: "task_{}".format(counter))
    sub_tasks_count = factory.Iterator([0, 1, 2, 3])


class TaskIdWithCompletedSubTasksCountDTOFactory(factory.Factory):
    class Meta:
        model = TaskIdWithCompletedSubTasksCountDTO

    task_id = factory.sequence(lambda counter: "task_{}".format(counter))
    completed_sub_tasks_count = factory.Iterator([0, 1, 2, 3])
