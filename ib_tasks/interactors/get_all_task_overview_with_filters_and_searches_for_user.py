"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""

from dataclasses import dataclass
from typing import List

from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageDetailsDTO, GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


@dataclass
class UserIdPaginationDTO:
    user_id: str
    limit: int
    offset: int


class GetTasksOverviewForUserInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 field_storage: FieldsStorageInterface,
                 action_storage: ActionStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.field_storage = field_storage
        self.action_storage = action_storage

    def get_filtered_tasks_overview_for_user(
            self, user_id: str, task_ids: List[int]):
        stage_ids = self._get_allowed_stage_ids_of_user(user_id=user_id)
        task_id_with_stage_ids_dtos = self._get_task_ids_of_user(
            user_id=user_id,
            stage_ids=stage_ids
        )
        task_id_with_stage_details_dtos = [
            task_id_with_stage_ids_dto
            for task_id_with_stage_ids_dto in task_id_with_stage_ids_dtos
            if task_id_with_stage_ids_dto.task_id in task_ids
        ]
        from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
        task_id_with_stage_id_dtos = [
            GetTaskDetailsDTO(
                stage_id=each_task_id_with_stage_details_dto.stage_id,
                task_id=each_task_id_with_stage_details_dto.task_id)
            for each_task_id_with_stage_details_dto in
            task_id_with_stage_details_dtos
        ]
        task_fields_and_action_details_dtos = self._get_task_fields_and_action(
            task_id_with_stage_id_dtos, user_id)
        from ib_tasks.interactors.presenter_interfaces.dtos import \
            AllTasksOverviewDetailsDTO
        all_tasks_overview_details_dto = AllTasksOverviewDetailsDTO(
            task_id_with_stage_details_dtos=task_id_with_stage_details_dtos,
            task_fields_and_action_details_dtos=
            task_fields_and_action_details_dtos)
        return all_tasks_overview_details_dto

    def _get_allowed_stage_ids_of_user(self, user_id: str) -> List[str]:
        from ib_tasks.interactors.get_allowed_stage_ids_of_user_interactor \
            import \
            GetAllowedStageIdsOfUserInteractor
        get_allowed_stage_ids_of_user_interactor \
            = GetAllowedStageIdsOfUserInteractor(storage=self.stage_storage)
        stage_ids = get_allowed_stage_ids_of_user_interactor. \
            get_allowed_stage_ids_of_user(user_id=user_id)
        return stage_ids

    def _get_task_ids_of_user(
            self, user_id: str, stage_ids: List[str]) -> List[TaskIdWithStageDetailsDTO]:
        from ib_tasks.interactors. \
            get_valid_task_ids_for_user_based_on_stage_ids import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        task_ids_of_user_based_on_stage_ids_interactor = \
            GetTaskIdsOfUserBasedOnStagesInteractor(
                stage_storage=self.stage_storage,
                task_storage=self.task_storage
            )
        task_id_with_stage_ids_dtos = task_ids_of_user_based_on_stage_ids_interactor. \
            get_task_ids_of_user_based_on_stage_ids(
                user_id=user_id, stage_ids=stage_ids
            )
        return task_id_with_stage_ids_dtos

    def _get_task_fields_and_action(
            self, task_id_with_stage_id_dtos: List[GetTaskDetailsDTO],
            user_id: str
    ) -> List[GetTaskStageCompleteDetailsDTO]:
        from ib_tasks.interactors.get_task_fields_and_actions import \
            GetTaskFieldsAndActionsInteractor
        get_task_fields_and_actions_interactor = \
            GetTaskFieldsAndActionsInteractor(stage_storage=self.stage_storage,
                                              field_storage=self.field_storage,
                                              task_storage=self.task_storage,
                                              action_storage=self.action_storage)
        task_details_dtos = get_task_fields_and_actions_interactor. \
            get_task_fields_and_action(task_dtos=task_id_with_stage_id_dtos,
                                       user_id=user_id)
        return task_details_dtos

    @staticmethod
    def _get_filtered_task_id_with_stage_details_dtos(
            task_id_with_stage_details_dtos: List[TaskIdWithStageDetailsDTO],
            task_ids: List[str]) -> List[TaskIdWithStageDetailsDTO]:
        new_task_id_with_stage_details_dtos = [
            task_id_with_stage_details_dto
            for task_id_with_stage_details_dto in
            task_id_with_stage_details_dtos
            if task_id_with_stage_details_dto.task_id in task_ids
        ]
        return new_task_id_with_stage_details_dtos
