from typing import List

from ib_tasks.interactors.dtos import StageLogicAttributes, StageDTO
from ib_tasks.interactors.stage_display_logic import StageDisplayLogicInteractor

from ib_tasks.exceptions.custom_exceptions import (
    InvalidStagesTaskTemplateId, InvalidStageValues, DuplicateStageIds,
    InvalidTaskTemplateIds, InvalidStageDisplayLogic, InvalidStagesDisplayName)
from ib_tasks.interactors.storage_interfaces.dtos import TaskStagesDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class CreateOrUpdateStagesInterface:
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def create_or_update_stages(
            self,
            stages_details: List[StageDTO]):

        stage_ids = self._get_stage_ids(stages_details)
        self.check_for_duplicate_stage_ids(stage_ids)
        self._validate_stage_display_name(stages_details)

        task_template_ids = self._get_task_template_ids(stages_details)
        self._validate_task_template_ids(task_template_ids)

        existing_stage_ids = self._get_existing_stage_ids(stage_ids)
        self._validate_values_for_stages(stages_details)

        self._validate_stage_display_logic(stages_details)

        self._create_or_update_stages(existing_stage_ids, stages_details)

    def _create_or_update_stages(self,
                                 existing_stage_ids: List[str],
                                 stages_details: List[StageDTO]
                                 ):
        update_stages_details = []
        create_stages_details = []
        if existing_stage_ids:
            task_stages_dto = self._get_task_stages_dto(stages_details)
            self._validate_stages_related_task_template_ids(task_stages_dto)

            for stage_information in stages_details:
                update_stages_details.append(stage_information)

        else:
            for stage_information in stages_details:
                if stage_information.stage_id not in existing_stage_ids:
                    create_stages_details.append(stage_information)

        if update_stages_details:
            self.stage_storage.update_stages(
                update_stages_details)

        if create_stages_details:
            self.stage_storage.create_stages(
                create_stages_details)

    def _validate_stage_display_logic(self, stages_details):
        list_of_logic_attributes = []
        invalid_stage_display_logic_stages = [
            stage.stage_id for stage in stages_details if stage.stage_display_logic == ""
        ]
        if invalid_stage_display_logic_stages:
            raise InvalidStageDisplayLogic(invalid_stage_display_logic_stages)

        for stage in stages_details:
            logic_interactor = StageDisplayLogicInteractor()
            stage_logic_attributes_dto = logic_interactor.get_stage_display_logic_attributes(
                stage.stage_display_logic
            )
            list_of_logic_attributes.append(stage_logic_attributes_dto)

        self._validate_stage_display_logic_attributes(list_of_logic_attributes)

    def _validate_stage_display_logic_attributes(
            self, list_of_logic_attributes: List[StageLogicAttributes]):

        invalid_stage_display_logic_stages = []

        list_of_status_ids = [attribute.status_id
                             for attribute in list_of_logic_attributes]

        valid_status_ids = self.stage_storage.get_valid_status_ids(
            list_of_status_ids)

        for attribute in list_of_logic_attributes:
            if attribute.status_id not in valid_status_ids:

                invalid_stage_display_logic_stages.append(attribute.stage_id)

        if invalid_stage_display_logic_stages:
            raise InvalidStageDisplayLogic(invalid_stage_display_logic_stages)
        return

    @staticmethod
    def _validate_stage_display_name(stages_details):
        invalid_stage_display_name_stages = [
            stage.stage_id for stage in stages_details if stage.stage_display_name == ""
        ]
        if invalid_stage_display_name_stages:
            raise InvalidStagesDisplayName(invalid_stage_display_name_stages)
        return

    @staticmethod
    def check_for_duplicate_stage_ids(stage_ids: List[str]):
        duplicate_stage_ids = list(set(
            [x for x in stage_ids if stage_ids.count(x) > 1]))
        if duplicate_stage_ids:
            raise DuplicateStageIds(duplicate_stage_ids)

    def _get_existing_stage_ids(self, stage_ids: List[str]):

        existing_stage_ids = self.stage_storage.get_existing_stage_ids(
            stage_ids)
        return existing_stage_ids

    @staticmethod
    def _get_task_template_ids(stages_details: List[StageDTO]):
        task_template_ids = [stage.task_template_id for stage in stages_details]
        return task_template_ids

    def _validate_task_template_ids(self, task_template_ids: List[str]):
        invalid_task_template_ids = []
        valid_task_template_ids = self.task_storage.\
            get_valid_template_ids_in_given_template_ids(
                task_template_ids)
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

    @staticmethod
    def _get_stage_ids(stages_details: List[StageDTO]):
        stage_ids = []
        for stage_information in stages_details:
            stage_ids.append(stage_information.stage_id)
        return stage_ids

    @staticmethod
    def _get_task_stages_dto(stages_details: List[StageDTO]):
        task_stages_dto = []
        for stage_information in stages_details:
            task_stages_dto.append(TaskStagesDTO(
                stage_id=stage_information.stage_id,
                task_template_id=stage_information.task_template_id
            ))
        return task_stages_dto

    @staticmethod
    def _validate_values_for_stages(stages_details: List[StageDTO]):
        invalid_value_stages = []
        for stage in stages_details:
            if stage.value < -1:
                invalid_value_stages.append(stage.stage_id)

        if invalid_value_stages:
            raise InvalidStageValues(invalid_value_stages)
        return
