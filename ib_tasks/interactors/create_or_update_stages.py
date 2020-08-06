import json
from typing import List

from ib_boards.exceptions.custom_exceptions import InvalidTemplateFields
from ib_tasks.exceptions.roles_custom_exceptions import InvalidStageRolesException
from ib_tasks.exceptions.stage_custom_exceptions import (
    InvalidStageValues, DuplicateStageIds, InvalidStageDisplayLogic,
    InvalidStagesDisplayName)
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidStagesTaskTemplateId, InvalidTaskTemplateIds
from ib_tasks.interactors.stages_dtos import StageLogicAttributes, StageDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface import \
    TaskTemplateStorageInterface


class CreateOrUpdateStagesInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 task_template_storage: TaskTemplateStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.task_template_storage = task_template_storage

    def create_or_update_stages(
            self,
            stages_details: List[StageDTO]):
        stage_ids = self._get_stage_ids(stages_details)
        self.check_for_duplicate_stage_ids(stage_ids)
        self._validate_stage_display_name(stages_details)
        self._validate_stage_roles(stages_details)

        task_template_ids = self._get_task_template_ids(stages_details)
        self._validate_task_template_ids(task_template_ids)

        existing_stage_ids = self._get_existing_stage_ids(stage_ids)
        self._validate_values_for_stages(stages_details)

        self._validate_stage_display_logic(stages_details)

        task_fields_dtos = self.task_storage.get_field_ids_for_given_task_template_ids(
            task_template_ids)
        self._validate_task_related_field_ids(stages_details, task_fields_dtos)
        self._create_or_update_stages(existing_stage_ids, stages_details)

    def _validate_task_related_field_ids(self, stage_details,
                                         task_fields_dtos):

        if not task_fields_dtos:
            task_template_ids = [stage.task_template_id
                                 for stage in stage_details]
            raise InvalidTemplateFields(task_template_ids)

        stages_dict = {}
        for stage in stage_details:
            stages_dict[stage.task_template_id] = stage

        tasks_dict = {}
        for task in task_fields_dtos:
            tasks_dict[task.task_template_id] = task.field_ids

        invalid_template_ids = []
        for stage in stages_dict:
            kanban, list_value, task_template_id, template_id = self._get_required_constants(
                stage, stages_dict)
            if not kanban.issubset(set(tasks_dict[task_template_id])):
                invalid_template_ids.append(template_id.task_template_id)
            if not list_value.issubset(set(tasks_dict[task_template_id])):
                invalid_template_ids.append(template_id.task_template_id)

        if invalid_template_ids:
            raise InvalidTemplateFields(list(set(invalid_template_ids)))

    @staticmethod
    def _validate_stage_roles(stage_details: List[StageDTO]):
        all_roles = []
        for stage in stage_details:
            roles = stage.roles.split('\n')
            for role in roles:
                all_roles.append(role)

        all_unique_roles = list(set(all_roles))
        from ib_tasks.adapters.service_adapter import get_service_adapter
        db_roles = get_service_adapter().roles_service.\
            get_valid_role_ids_in_given_role_ids(all_unique_roles)

        invalid_role_ids = []
        for role in all_unique_roles:
            if role not in db_roles:
                invalid_role_ids.append(role)

        if invalid_role_ids:
            raise InvalidStageRolesException(invalid_role_ids)

    @staticmethod
    def _get_required_constants(stage, stages_dict):
        template_id = stages_dict[stage]
        task_template_id = stages_dict[stage].task_template_id
        kanban = set(json.loads(template_id.card_info_kanban))
        list_value = set(json.loads(template_id.card_info_list))
        return kanban, list_value, task_template_id, template_id

    def _create_or_update_stages(self,
                                 existing_stage_ids: List[str],
                                 stages_details: List[StageDTO]
                                 ):
        update_stages_details = []
        create_stages_details = []
        for stage_information in stages_details:
            if stage_information.stage_id not in existing_stage_ids:
                create_stages_details.append(stage_information)
            else:
                update_stages_details.append(stage_information)

        task_stages_dto = self._get_task_stages_dto(update_stages_details)

        self._validate_stages_related_task_template_ids(task_stages_dto)

        if update_stages_details:
            self.stage_storage.update_stages(
                update_stages_details)

        if create_stages_details:
            self.stage_storage.create_stages(
                create_stages_details)

    @staticmethod
    def _validate_stage_display_logic(stages_details):
        list_of_logic_attributes = []
        invalid_stage_display_logic_stages = [
            stage.stage_id for stage in stages_details
            if stage.stage_display_logic == ""
        ]
        if invalid_stage_display_logic_stages:
            raise InvalidStageDisplayLogic(invalid_stage_display_logic_stages)

        # TODO: validate stage display logic
        # for stage in stages_details:
        #     logic_interactor = StageDisplayLogicInteractor()
        #     stage_logic_attributes_dto = logic_interactor.get_stage_display_logic_attributes(
        #         stage.stage_display_logic
        #     )
        #     list_of_logic_attributes.append(stage_logic_attributes_dto)
        #
        # self._validate_stage_display_logic_attributes(list_of_logic_attributes)

    def _validate_stage_display_logic_attributes(
            self, list_of_logic_attributes: List[StageLogicAttributes]):

        invalid_stage_display_logic_stages = []

        list_of_stage_ids = [attribute.stage_id
                             for attribute in list_of_logic_attributes]

        valid_stage_ids = self.stage_storage.get_existing_stage_ids(
            list(set(list_of_stage_ids)))

        for attribute in list_of_logic_attributes:
            if attribute.stage_id not in valid_stage_ids:
                invalid_stage_display_logic_stages.append(attribute.stage_id)

        if invalid_stage_display_logic_stages:
            raise InvalidStageDisplayLogic(invalid_stage_display_logic_stages)
        return

    @staticmethod
    def _validate_stage_display_name(stages_details):
        invalid_stage_display_name_stages = [
            stage.stage_id for stage in stages_details if
            stage.stage_display_name == ""
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
        task_template_ids = [stage.task_template_id for stage in
                             stages_details]
        return task_template_ids

    def _validate_task_template_ids(self, task_template_ids: List[str]):
        invalid_task_template_ids = []
        valid_task_template_ids = self.task_template_storage. \
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
