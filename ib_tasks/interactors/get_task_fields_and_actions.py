from typing import List

from ib_tasks.exceptions.stage_custom_exceptions import InvalidTaskStageIds
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    StageTaskFieldsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


class GetTaskFieldsAndActionsInteractor:
    def __init__(self, storage: FieldsStorageInterface,
                 stage_storage: StageStorageInterface):
        self.storage = storage
        self.stage_storage = stage_storage

    def get_task_fields_and_action(self, task_dtos: List[GetTaskDetailsDTO], user_id: str) -> \
            List[GetTaskStageCompleteDetailsDTO]:
        # TODO: validate user tasks
        task_ids = [task.task_id for task in task_dtos]
        stage_ids = [task.stage_id for task in task_dtos]

        valid_task_ids = self.storage.get_valid_task_ids(task_ids)
        self._validate_task_ids(task_ids, valid_task_ids)
        stage_task_dtos = task_dtos
        valid_stage_ids = self.stage_storage.get_existing_stage_ids(stage_ids)
        self._validate_stage_ids(stage_ids, valid_stage_ids)
        valid_stage_and_tasks = self.storage.validate_task_related_stage_ids(
            task_dtos)
        self._validate_stage_and_tasks(valid_stage_and_tasks, task_dtos)

        task_stage_dtos = self.storage.get_stage_details(stage_task_dtos)

        action_dtos = self.storage.get_actions_details(stage_ids)

        stage_fields_dtos = self.storage.get_field_ids(task_stage_dtos)
        task_fields_dtos = self._map_task_and_their_fields(
            stage_fields_dtos, task_stage_dtos)
        field_dtos = self.storage.get_fields_details(task_fields_dtos)

        task_details_dtos = self._map_fields_and_actions_based_on_their_stage_and_task_id(
            action_dtos, field_dtos, stage_fields_dtos)
        return task_details_dtos

    def _map_task_and_their_fields(self, stage_fields_dtos, task_stage_dtos):
        list_of_stage_fields = []
        for task in task_stage_dtos:
            for stage in stage_fields_dtos:
                task_template_condition = stage.task_template_id == task.task_template_id
                stage_condition = stage.stage_id == task.stage_id
                if stage_condition and task_template_condition:
                    list_of_stage_fields.append(
                        self._get_task_fields(stage, task))
        return list_of_stage_fields

    @staticmethod
    def _get_task_fields(stage, task):
        return StageTaskFieldsDTO(task_id=task.task_id,
                                  field_ids=stage.field_ids)

    @staticmethod
    def _validate_stage_ids(stage_ids, valid_stage_ids):
        invalid_stage_ids = [
            stage_id for stage_id in stage_ids
            if stage_id not in valid_stage_ids
        ]
        if invalid_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                InvalidStageIdsListException
            raise InvalidStageIdsListException(invalid_stage_ids)
        return

    @staticmethod
    def _validate_task_ids(task_ids, valid_task_ids):
        invalid_task_ids = [
            task_id for task_id in task_ids if task_id not in valid_task_ids
        ]
        if invalid_task_ids:
            raise InvalidTaskIds(invalid_task_ids)
        return

    def _map_fields_and_actions_based_on_their_stage_and_task_id(
            self, action_dtos, field_dtos, stage_fields_dtos):
        list_of_task_details_dtos = []
        for task in stage_fields_dtos:
            list_of_field_dtos = self._get_list_of_fields_for_stage(
                field_dtos, task)
            list_of_action_dtos = self._get_list_of_actions_dtos_for_stage(
                action_dtos, task)
            task_stage_dtos = self._get_task_stage_details(
                list_of_action_dtos, list_of_field_dtos, task)
            list_of_task_details_dtos.append(task_stage_dtos)

        return list_of_task_details_dtos

    @staticmethod
    def _get_task_stage_details(list_of_action_dtos, list_of_field_dtos, task):
        return GetTaskStageCompleteDetailsDTO(task_id=task.task_id,
                                              stage_id=task.stage_id,
                                              field_dtos=list_of_field_dtos,
                                              action_dtos=list_of_action_dtos)

    @staticmethod
    def _get_list_of_fields_for_stage(field_dtos, task):
        list_of_field_dtos = []
        if field_dtos:
            for field in field_dtos:
                if field.field_id in task.field_ids:
                    list_of_field_dtos.append(field)
        return list_of_field_dtos

    @staticmethod
    def _get_list_of_actions_dtos_for_stage(action_dtos, task):
        list_of_action_dtos = []
        if action_dtos:
            for action in action_dtos:
                if action.stage_id == task.stage_id:
                    list_of_action_dtos.append(action)
        return list_of_action_dtos

    @staticmethod
    def _validate_stage_and_tasks(valid_task_stage_ids, task_dtos):
        import copy
        invalid_task_stage_ids = copy.deepcopy(task_dtos)
        for task in task_dtos:
            for valid_task in valid_task_stage_ids:
                task_id_condition = task.task_id == valid_task.task_id
                stage_id_condition = task.stage_id == valid_task.stage_id
                if task_id_condition and stage_id_condition:
                    invalid_task_stage_ids.remove(task)
        if invalid_task_stage_ids:
            raise InvalidTaskStageIds(invalid_task_stage_ids)
        return
