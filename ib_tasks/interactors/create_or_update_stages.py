from typing import List
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.dtos import StageDTO
from ib_tasks.exceptions.custom_exceptions import (
    InvalidStagesTaskTemplateId, InvalidStageValues, DuplicateStageIds,
    InvalidTaskTemplateIds, InvalidStageDisplayLogic)
from ib_tasks.interactors.storage_interfaces.dtos import TaskStagesDTO


class CreateOrUpdateStagesInterface:

    def __init__(self, stage_storage: TaskStorageInterface):
        self.stage_storage = stage_storage

    def create_or_update_stages_information(
            self,
            stages_information: List[StageDTO]):

        stage_ids = self._get_stage_ids(stages_information)
        self.check_for_duplicate_stage_ids(stage_ids)

        task_template_ids = self._get_valid_template_ids_in_given_template_ids(
            stages_information)
        self._validate_task_template_ids(task_template_ids)

        valid_stages_dtos = self._validate_stage_ids(stage_ids)
        self._validate_values_for_stages(stages_information)

        self._validate_stage_display_logic(stages_information)

        self._create_or_update_stages(valid_stages_dtos, stages_information)

    def _create_or_update_stages(self,
                                 valid_stages_dtos: List[str],
                                 stages_information: List[StageDTO]
                                 ):
        create_stages_dtos, update_stages_dtos = self._get_stages_dtos_based_on_their_state(
            valid_stages_dtos, stages_information)

        if update_stages_dtos:
            self.stage_storage.update_stages(
                update_stages_dtos)

        if create_stages_dtos:
            self.stage_storage.create_stages(
                create_stages_dtos)

    def _get_stages_dtos_based_on_their_state(self, valid_stages_dtos, stages_information):
        update_stages_information = []
        create_stages_information = []
        if valid_stages_dtos:
            valid_stages_info = self._get_valid_stages_details_dtos(
                stages_information, valid_stages_dtos)

            task_stages_dto = self._get_task_stages_dto(valid_stages_info)
            self._validate_stages_related_task_template_ids(task_stages_dto)

            for stage_information in stages_information:
                update_stages_information.append(stage_information)

        if len(valid_stages_dtos) != len(stages_information):
            valid_stage_ids = [stage.stage_id for stage in valid_stages_dtos]

            for stage_information in stages_information:
                if stage_information.stage_id not in valid_stage_ids:
                    create_stages_information.append(stage_information)
        return create_stages_information, update_stages_information

    def _get_valid_stages_details_dtos(self, stages_information, valid_stages_dtos):
        valid_stages_info = []
        for stage_dto in valid_stages_dtos:
            for stage in stages_information:
                if stage.stage_id == stage_dto.stage_id:
                    stage.id = stage_dto.id
                    valid_stages_info.append(stage)
        return valid_stages_info

    def _validate_stage_display_logic(self, stages_information):
        invalid_stage_display_logic_stages = [
            stage.stage_id for stage in stages_information
            if stage.stage_display_logic == ""
        ]
        if invalid_stage_display_logic_stages:
            raise InvalidStageDisplayLogic(invalid_stage_display_logic_stages)
        return

    def check_for_duplicate_stage_ids(self, stage_ids: List[str]):
        duplicate_stage_ids = list(set(
            [x for x in stage_ids if stage_ids.count(x) > 1]))

        if duplicate_stage_ids:
            raise DuplicateStageIds(duplicate_stage_ids)

    def _validate_stage_ids(self, stage_ids: List[str]):

        valid_stage_ids = self.stage_storage.get_valid_stage_ids(stage_ids)
        return valid_stage_ids

    def _get_valid_template_ids_in_given_template_ids(self, stages_information: List[StageDTO]):
        task_template_ids = [stage.task_template_id for stage in stages_information]
        return task_template_ids

    def _validate_task_template_ids(self, task_template_ids: List[str]):
        invalid_task_template_ids = []
        valid_task_template_ids = self.stage_storage.get_valid_template_ids_in_given_template_ids(task_template_ids)
        for task_template_id in task_template_ids:
            if task_template_id not in valid_task_template_ids:
                invalid_task_template_ids.append(task_template_id)

        if invalid_task_template_ids:
            raise InvalidTaskTemplateIds(invalid_task_template_ids)
        return

    def _validate_stages_related_task_template_ids(
            self,
            task_stages_dto: List[TaskStagesDTO]):
        invalid_stages_related_task_template_ids = self.stage_storage. \
            validate_stages_related_task_template_ids(task_stages_dto)

        if invalid_stages_related_task_template_ids:
            raise InvalidStagesTaskTemplateId(
                invalid_stages_related_task_template_ids)
        return

    def _get_stage_ids(self,
                       stages_information: List[StageDTO]):
        stage_ids = []
        for stage_information in stages_information:
            stage_ids.append(stage_information.stage_id)
        return stage_ids

    def _get_task_stages_dto(self,
                             stages_information: List[StageDTO]):
        task_stages_dto = []
        for stage_information in stages_information:
            task_stages_dto.append(TaskStagesDTO(
                stage_id=stage_information.stage_id,
                task_template_id=stage_information.task_template_id
            ))
        return task_stages_dto

    def _validate_values_for_stages(self,
                                    stages_information: List[StageDTO]):
        invalid_value_stages = []
        for stage in stages_information:
            if stage.value < 0:
                invalid_value_stages.append(stage.stage_id)

        if invalid_value_stages:
            raise InvalidStageValues(invalid_value_stages)
        return
