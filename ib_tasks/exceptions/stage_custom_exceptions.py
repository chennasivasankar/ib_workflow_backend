from typing import List

from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


class InvalidStageIdsException(Exception):
    def __init__(self, stage_ids_dict: str):
        self.stage_ids_dict = stage_ids_dict

    def __str__(self):
        return self.stage_ids_dict


class InvalidStageValues(Exception):
    def __init__(self, invalid_value_stages: List[str]):
        self.invalid_value_stages = invalid_value_stages


class DuplicateStageIds(Exception):
    def __init__(self, duplicate_stage_ids: List[str]):
        self.duplicate_stage_ids = duplicate_stage_ids


class InvalidStageDisplayLogic(Exception):
    def __init__(self, invalid_stage_display_logic_stages: List[str]):
        self.invalid_stage_display_logic_stages = invalid_stage_display_logic_stages


class InvalidStagesDisplayName(Exception):
    def __init__(self, invalid_stages_display_name: List[str]):
        self.invalid_stages_display_name = invalid_stages_display_name


class InvalidFormatException(Exception):
    def __init__(self, valid_format: str):
        self.valid_format = valid_format


class InvalidPythonCodeException(Exception):
    pass


class InvalidTaskStageIds(Exception):
    def __init__(self, invalid_task_stage_ids: List[GetTaskDetailsDTO]):
        self.invalid_task_stage_ids = invalid_task_stage_ids
