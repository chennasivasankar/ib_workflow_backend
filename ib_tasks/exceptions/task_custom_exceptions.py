import datetime
from typing import List

from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO


class InvalidTaskException(Exception):
    def __init__(self, task_id: int):
        self.task_id = task_id


class InvalidReasonIdException(Exception):
    pass


class InvalidTaskIdException(Exception):
    def __init__(self, task_id: int):
        self.task_id = task_id


class InvalidTaskTemplateId(Exception):
    def __init__(self, task_template_ids_dict: str):
        self.task_template_ids_dict = task_template_ids_dict


class InvalidStagesTaskTemplateId(Exception):
    def __init__(self, invalid_stages_task_template_ids: List[TaskStagesDTO]):
        self.invalid_stages_task_template_ids = \
            invalid_stages_task_template_ids

    def __str__(self):
        return self.invalid_stages_task_template_ids


class InvalidTaskTemplateIds(Exception):
    def __init__(self, invalid_task_template_ids: List[str]):
        self.invalid_task_template_ids = invalid_task_template_ids


class InvalidTaskTemplateDBId(Exception):
    def __init__(self, invalid_task_template_id: str):
        self.task_template_id = invalid_task_template_id


class DuplicateTaskStatusVariableIds(Exception):
    def __init__(self, duplicate_status_ids_for_tasks: List[str]):
        self.task_ids = duplicate_status_ids_for_tasks


class TaskTemplateIdCantBeEmpty(Exception):
    pass


class TemplateDoesNotExists(Exception):
    def __int__(self, message: str):
        self.message = message


class InvalidTemplateIds(Exception):
    def __int__(self, message: str):
        self.message = message


class TaskTemplatesDoesNotExists(Exception):
    pass


class InvalidTaskIds(Exception):
    def __init__(self, task_ids: List[str]):
        self.invalid_task_ids = task_ids


class InvalidTaskJson(Exception):
    def __init__(self, message: str):
        self.message = message


class TaskDoesNotExists(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidGoFsOfTaskTemplate(Exception):
    def __init__(self, invalid_gof_ids: List[str], task_template_id: str):
        self.gof_ids = invalid_gof_ids
        self.task_template_id = task_template_id


class InvalidFieldsOfGoF(Exception):
    def __init__(self, gof_id: str, invalid_field_ids: List[str]):
        self.gof_id = gof_id
        self.field_ids = invalid_field_ids


class ManyStagesToInitialTaskTemplate(Exception):
    def __init__(self, task_template_stages_dict: str):
        self.task_template_stages_dict = task_template_stages_dict


class InvalidTransitionChecklistTemplateId(Exception):

    def __init__(self, transition_checklist_template_id: str):
        self.transition_checklist_template_id = \
            transition_checklist_template_id


class TransitionTemplateDoesNotExist(Exception):
    def __init__(self, transition_template_id: str):
        self.transition_template_id = transition_template_id


class InvalidTransitionTemplateIds(Exception):
    def __init__(self, invalid_transition_ids: List[str]):
        self.invalid_transition_ids = invalid_transition_ids


class UserIsNotAssigneeToTask(Exception):
    pass


class InvalidStageIdsForTask(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidTaskDisplayId(Exception):
    def __init__(self, task_display_id: str):
        self.task_display_id = task_display_id


class UserPermissionDenied(Exception):
    pass


class UserNotInAnyTeamForGivenProjectException(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id

    pass


class InvalidTaskTemplateOfProject(Exception):
    def __init__(self, project_id: str, template_id: str):
        self.template_id = template_id
        self.project_id = project_id


class TaskIdsNotInProject(Exception):
    def __init__(self, invalid_task_ids: List[int]):
        self.invalid_task_ids = invalid_task_ids

    def __str__(self):
        return self.invalid_task_ids

class TaskDelayReasonIsNotUpdated(Exception):
    def __init__(
            self, due_date: datetime.datetime, task_display_id: str,
            stage_display_name: str
    ):
        self.due_date = due_date
        self.task_display_id = task_display_id
        self.stage_display_name = stage_display_name
