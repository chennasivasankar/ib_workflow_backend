"""
Created on: 14/08/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass
from typing import List

from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface


class BasicValidationsInteractor:

    def __init__(self, storage: StageStorageInterface):
        self.storage = storage

    def validate_stages_with_task_template_ids(
            self, template_stages: List[TaskStagesDTO]):
        invalid_stage_ids = self.storage.validate_stages_related_task_template_ids(
            task_stages_dto=template_stages
        )
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidStagesTaskTemplateId
        if invalid_stage_ids:
            raise InvalidStagesTaskTemplateId(
                invalid_stages_task_template_ids=invalid_stage_ids
            )

    def validate_template_ids(self, template_ids: List[str]) -> List[str]:
        return self.storage.get_valid_template_ids(
            template_ids=template_ids
        )
