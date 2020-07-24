from typing import List



class InvalidTaskException(Exception):
    def __init__(self, task_id: str):
        self.task_id = task_id

class InvalidTaskIdException(Exception):
    def __init__(self, task_id: str):
        self.task_id = task_id


class InvalidTaskTemplateId(Exception):
    def __init__(self, task_template_ids_dict: str):
        self.task_template_ids_dict = task_template_ids_dict


class InvalidStagesTaskTemplateId(Exception):
    def __init__(self, invalid_stages_task_template_ids: List[str]):
        self.invalid_stages_task_template_ids = invalid_stages_task_template_ids


class InvalidTaskTemplateIds(Exception):
    def __init__(self, invalid_task_template_ids: List[str]):
        self.invalid_task_template_ids = invalid_task_template_ids


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
    def __init__(self, message: str):
        self.message = message


class InvalidTaskIds(Exception):
    def __init__(self, task_ids: List[str]):
        self.invalid_task_ids = task_ids


class InvalidStageIds(Exception):
    def __init__(self, stage_ids: List[str]):
        self.invalid_stage_ids = stage_ids
