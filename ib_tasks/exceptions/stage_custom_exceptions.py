from typing import List

from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


class InvalidStageIdsException(Exception):
    def __init__(self, stage_ids_dict: str):
        self.stage_ids_dict = stage_ids_dict

    def __str__(self):
        return self.stage_ids_dict


class InvalidStageIdsListException(Exception):
    def __init__(self, invalid_stage_ids: List[str]):
        self.invalid_stage_ids = invalid_stage_ids

    def __str__(self):
        return self.invalid_stage_ids


class InvalidDbStageIdsListException(Exception):
    def __init__(self, invalid_stage_ids: List[int]):
        self.invalid_stage_ids = invalid_stage_ids


class StageIdsWithInvalidPermissionForAssignee(Exception):
    def __init__(self, invalid_stage_ids: List[int]):
        self.invalid_stage_ids = invalid_stage_ids


class InvalidStageValues(Exception):
    def __init__(self, invalid_value_stages: List[str]):
        self.invalid_value_stages = invalid_value_stages


class DuplicateStageIds(Exception):
    def __init__(self, duplicate_stage_ids: List[int]):
        self.duplicate_stage_ids = duplicate_stage_ids


class InvalidStageDisplayLogic(Exception):
    def __init__(self, invalid_stage_display_logic_stages: List[str]):
        self.invalid_stage_display_logic_stages = \
            invalid_stage_display_logic_stages


class InvalidStagesDisplayName(Exception):
    def __init__(self, invalid_stages_display_name: List[str]):
        self.invalid_stages_display_name = invalid_stages_display_name


class InvalidPythonCodeException(Exception):
    pass


class InvalidTaskStageIds(Exception):
    def __init__(self, invalid_task_stage_ids: List[GetTaskDetailsDTO]):
        self.invalid_task_stage_ids = invalid_task_stage_ids


class StageIdsListEmptyException(Exception):
    pass


class InvalidStageId(Exception):

    def __init__(self, stage_id: int):
        self.stage_id = stage_id


class InvalidStageIdException(Exception):
    pass


class TransitionTemplateIsNotRelatedToGivenStageAction(Exception):

    def __init__(self, transition_checklist_template_id, action_id, stage_id):
        self.stage_id = stage_id
        self.action_id = action_id
        self.transition_checklist_template_id = \
            transition_checklist_template_id


class VirtualStageIdsException(Exception):
    def __init__(self, virtual_stage_ids: List[int]):
        self.virtual_stage_ids = virtual_stage_ids
