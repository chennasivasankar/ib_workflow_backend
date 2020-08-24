"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""

from dataclasses import dataclass
from typing import List

from ib_tasks.constants.enum import ViewType
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageDetailsDTO, GetTaskStageCompleteDetailsDTO, \
    TaskWithCompleteStageDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
from ib_tasks.interactors.user_role_validation_interactor import UserRoleValidationInteractor


@dataclass
class UserIdPaginationDTO:
    user_id: str
    limit: int
    offset: int


class GetTasksOverviewForUserInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 field_storage: FieldsStorageInterface,
                 action_storage: ActionStorageInterface,
                 task_stage_storage: TaskStageStorageInterface):
        self.task_stage_storage = task_stage_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.field_storage = field_storage
        self.action_storage = action_storage

    def get_filtered_tasks_overview_for_user(
            self, user_id: str, task_ids: List[int],
            view_type: ViewType, project_id: str
    ) -> \
            AllTasksOverviewDetailsDTO:
        stage_ids = self._get_allowed_stage_ids_of_user(
            user_id=user_id, project_id=project_id
        )
        task_with_complete_stage_details_dtos = \
            self._get_task_with_complete_stage_details_dtos(
                user_id=user_id,
                stage_ids=stage_ids,
                task_ids=task_ids
            )
        task_id_with_stage_details_dtos = [
            task_with_complete_stage_details_dto.task_with_stage_details_dto
            for task_with_complete_stage_details_dto in
            task_with_complete_stage_details_dtos
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
            task_id_with_stage_id_dtos, user_id, view_type=view_type)

        task_with_stage_details_having_actions_dtos = \
            self._filter_tasks_with_stage_details_having_actions(
                task_with_complete_stage_details_dtos=
                task_with_complete_stage_details_dtos,
                task_fields_and_action_details_dtos=
                task_fields_and_action_details_dtos
            )

        from ib_tasks.interactors.presenter_interfaces.dtos import \
            AllTasksOverviewDetailsDTO
        all_tasks_overview_details_dto = AllTasksOverviewDetailsDTO(
            task_with_complete_stage_details_dtos=task_with_stage_details_having_actions_dtos,
            task_fields_and_action_details_dtos=
            task_fields_and_action_details_dtos,
        )
        return all_tasks_overview_details_dto

    def _get_allowed_stage_ids_of_user(self, user_id: str,
                                       project_id: str) -> List[str]:
        user_interactor = UserRoleValidationInteractor()
        stage_ids = user_interactor. \
            get_permitted_stage_ids_given_user_id(user_id=user_id,
                                                  stage_storage=self.stage_storage,
                                                  project_id=project_id)
        return stage_ids

    def _get_task_with_complete_stage_details_dtos(
            self, user_id: str, stage_ids: List[str], task_ids: List[int],
    ) -> List[TaskWithCompleteStageDetailsDTO]:
        from ib_tasks.interactors. \
            get_valid_task_ids_for_user_based_on_stage_ids import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        task_ids_of_user_based_on_stage_ids_interactor = \
            GetTaskIdsOfUserBasedOnStagesInteractor(
                stage_storage=self.stage_storage,
                task_storage=self.task_storage,
                task_stage_storage=self.task_stage_storage
            )
        task_id_with_stage_ids_dtos = task_ids_of_user_based_on_stage_ids_interactor. \
            get_task_ids_of_user_based_on_stage_ids(
                user_id=user_id, stage_ids=stage_ids, task_ids=task_ids
            )
        return task_id_with_stage_ids_dtos

    def _get_task_fields_and_action(
            self, task_id_with_stage_id_dtos: List[GetTaskDetailsDTO],
            user_id: str, view_type: ViewType
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
                                       user_id=user_id, view_type=view_type)
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

    def _filter_tasks_with_stage_details_having_actions(
            self,
            task_with_complete_stage_details_dtos: List[
                TaskWithCompleteStageDetailsDTO],
            task_fields_and_action_details_dtos: List[
                GetTaskStageCompleteDetailsDTO]
    ) -> List[TaskWithCompleteStageDetailsDTO]:
        task_with_stage_details_having_actions_dtos = []

        for task_with_complete_stage_details_dto in task_with_complete_stage_details_dtos:
            task_id_with_stage_details_dto = \
                task_with_complete_stage_details_dto.task_with_stage_details_dto
            is_task_has_actions = self._check_is_task_having_actions(
                task_id=task_id_with_stage_details_dto.task_id,
                task_fields_and_action_details_dtos=
                task_fields_and_action_details_dtos)
            if is_task_has_actions:
                task_with_stage_details_having_actions_dtos.append(
                    task_with_complete_stage_details_dto
                )

        return task_with_stage_details_having_actions_dtos

    @staticmethod
    def _check_is_task_having_actions(
            task_id: int,
            task_fields_and_action_details_dtos:
            List[GetTaskStageCompleteDetailsDTO]) -> bool:
        for task_fields_and_action_details_dto in task_fields_and_action_details_dtos:
            task_id_in_task_fields_and_actions_dto = \
                task_fields_and_action_details_dto.task_id
            is_task_id_same = task_id == task_id_in_task_fields_and_actions_dto
            is_task_having_actions = \
                task_fields_and_action_details_dto.action_dtos
            is_given_task_having_actions = \
                is_task_id_same and is_task_having_actions
            if is_given_task_having_actions:
                return True

        return False
