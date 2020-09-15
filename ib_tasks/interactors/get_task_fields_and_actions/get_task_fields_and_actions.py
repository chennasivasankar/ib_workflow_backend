from typing import List

from ib_boards.interactors.dtos import StageActionDetailsDTO
from ib_tasks.constants.enum import ViewType
from ib_tasks.exceptions.stage_custom_exceptions import InvalidTaskStageIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
from ib_tasks.interactors.get_task_fields_and_actions.get_task_actions import GetTaskActionsInteractor
from ib_tasks.interactors.get_task_fields_and_actions.get_task_fields import GetTaskFieldsInteractor
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    (FieldDetailsDTO, TaskTemplateStageFieldsDTO,
     FieldDetailsDTOWithTaskId)
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


class GetTaskFieldsAndActionsInteractor:
    def __init__(self, task_storage: TaskStorageInterface,
                 field_storage: FieldsStorageInterface,
                 stage_storage: StageStorageInterface,
                 action_storage: ActionStorageInterface):
        self.field_storage = field_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.action_storage = action_storage

    def get_task_fields_and_action(self, task_dtos: List[GetTaskDetailsDTO],
                                   user_id: str, view_type: ViewType) -> \
            List[GetTaskStageCompleteDetailsDTO]:

        task_ids = self._validate_task_ids(task_dtos)
        stage_ids = self._validate_stage_ids(task_dtos)
        valid_stage_and_tasks = \
            self.task_storage.validate_task_related_stage_ids(
                task_dtos)
        self._validate_stage_and_tasks(valid_stage_and_tasks, task_dtos)

        stage_task_dtos = task_dtos

        task_stage_dtos = self.stage_storage.get_stage_details(stage_task_dtos)

        action_dtos, field_dtos, stage_fields_dtos = \
            self.get_fields_and_actions(
                stage_ids, task_ids,
                task_stage_dtos, user_id, view_type)

        task_details_dtos = self. \
            _map_fields_and_actions_based_on_their_stage_and_task_id(
                action_dtos, field_dtos, stage_fields_dtos)
        return task_details_dtos

    def get_fields_and_actions(self, stage_ids, task_ids,
                               task_stage_dtos, user_id, view_type):
        actions_interactor = GetTaskActionsInteractor(self.action_storage,
                                                      self.task_storage,
                                                      self.stage_storage)
        action_dtos = actions_interactor.get_task_actions(
                stage_ids=stage_ids,
                user_id=user_id,
                task_ids=task_ids)
        fields_interactor = GetTaskFieldsInteractor(self.field_storage,
                                                    self.task_storage)
        field_dtos, stage_fields_dtos = fields_interactor.get_task_fields(
                task_stage_dtos=task_stage_dtos,
                task_ids=task_ids,
                user_id=user_id,
                view_type=view_type)
        return action_dtos, field_dtos, stage_fields_dtos

    def _validate_stage_ids(self, task_dtos):
        stage_ids = [task.stage_id for task in task_dtos]
        unique_stage_ids = list(sorted(set(stage_ids)))

        valid_stage_ids = self.stage_storage.get_existing_stage_ids(
                unique_stage_ids)
        invalid_stage_ids = [
                stage_id for stage_id in stage_ids
                if stage_id not in valid_stage_ids
        ]

        if invalid_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                InvalidStageIdsListException
            raise InvalidStageIdsListException(invalid_stage_ids)
        return valid_stage_ids

    def _validate_task_ids(self, task_dtos):
        task_ids = [task.task_id for task in task_dtos]
        unique_task_ids = list(sorted(set(task_ids)))
        valid_task_ids = self.task_storage.get_valid_task_ids(unique_task_ids)
        invalid_task_ids = [
                task_id for task_id in task_ids if
                task_id not in valid_task_ids
        ]
        if invalid_task_ids:
            raise InvalidTaskIds(invalid_task_ids)
        return task_ids

    def _map_fields_and_actions_based_on_their_stage_and_task_id(
            self,
            action_dtos: List[ActionDetailsDTO],
            field_dtos: List[FieldDetailsDTOWithTaskId],
            task_stage_fields_dtos: List[TaskTemplateStageFieldsDTO]
    ):
        task_details_dtos = []
        for task_stage_dto in task_stage_fields_dtos:
            fields_dtos = self._get_list_of_fields_for_stage(
                    field_dtos, task_stage_dto)
            actions_dtos = self._get_list_of_actions_dtos_for_stage(
                    action_dtos, task_stage_dto)
            task_stage_dtos = self._get_task_stage_details(
                    actions_dtos, fields_dtos, task_stage_dto)
            task_details_dtos.append(task_stage_dtos)

        return task_details_dtos

    def _get_task_stage_details(
            self,
            action_dtos: List[StageActionDetailsDTO],
            field_dtos: List[FieldDetailsDTOWithTaskId],
            task_stage_dto: TaskTemplateStageFieldsDTO
    ):
        fields_dtos = self._get_fields_dtos(field_dtos)
        return GetTaskStageCompleteDetailsDTO(
                task_id=task_stage_dto.task_id,
                stage_id=task_stage_dto.stage_id,
                db_stage_id=task_stage_dto.db_stage_id,
                display_name=task_stage_dto.display_name,
                stage_color=task_stage_dto.stage_color,
                field_dtos=fields_dtos,
                action_dtos=action_dtos
        )

    @staticmethod
    def _get_fields_dtos(list_of_field_dtos):
        fields_dtos = [
                FieldDetailsDTO(
                        field_type=field.field_type,
                        value=field.value,
                        key=field.key,
                        field_id=field.field_id
                )
                for field in list_of_field_dtos
        ]
        return fields_dtos

    @staticmethod
    def _get_list_of_fields_for_stage(
            field_dtos: List[FieldDetailsDTOWithTaskId],
            stage: TaskTemplateStageFieldsDTO
    ):
        list_of_field_dtos = [
                field for field in field_dtos
                if field.field_id in stage.field_ids and
                   field.task_id == stage.task_id]

        return list_of_field_dtos

    @staticmethod
    def _get_list_of_actions_dtos_for_stage(action_dtos, stage):
        list_of_action_dtos = [action for action in action_dtos
                               if action.stage_id == stage.stage_id]
        return list_of_action_dtos

    def _validate_stage_and_tasks(self, valid_task_stage_ids, task_dtos):
        import copy
        invalid_task_stage_ids = copy.deepcopy(task_dtos)
        for task in task_dtos:
            self._validate_task_stages(invalid_task_stage_ids,
                                       task, valid_task_stage_ids)
        if invalid_task_stage_ids:
            raise InvalidTaskStageIds(invalid_task_stage_ids)
        return

    @staticmethod
    def _validate_task_stages(invalid_task_stage_ids, task,
                              valid_task_stage_ids):
        for valid_task in valid_task_stage_ids:
            task_id_condition = task.task_id == valid_task.task_id
            stage_id_condition = task.stage_id == valid_task.stage_id
            if task_id_condition and stage_id_condition:
                invalid_task_stage_ids.remove(task)
