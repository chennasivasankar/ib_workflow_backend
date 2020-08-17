"""
Created on: 14/08/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass
from typing import List

from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface


class ValidateStageIdsWithTemplateIdsInteractor:

    def __init__(self, stage_storage: StageStorageInterface):
        self.stage_storage = stage_storage

    def validate_stages_with_task_template_ids(
            self, template_stages: List[TaskStagesDTO]):
        invalid_stage_ids = self.stage_storage.validate_stages_related_task_template_ids(
            task_stages_dto=template_stages
        )
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidStagesTaskTemplateId
        raise InvalidStagesTaskTemplateId(
            invalid_stages_task_template_ids=invalid_stage_ids
        )
