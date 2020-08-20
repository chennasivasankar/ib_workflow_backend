"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageValueWithTaskIdsDTO, TaskIdWithStageDetailsDTO, \
    TaskWithCompleteStageDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class GetTaskIdsOfUserBasedOnStagesInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 task_stage_storage: TaskStageStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.task_stage_storage = task_stage_storage

    def get_task_ids_of_user_based_on_stage_ids(
            self, user_id: str, stage_ids: List[str]) \
            -> List[TaskWithCompleteStageDetailsDTO]:
        given_stage_ids = stage_ids

        self._validate_given_stage_ids_list_empty(given_stage_ids)
        given_unique_stage_ids = sorted(list(set(given_stage_ids)))
        valid_stage_ids = self.stage_storage. \
            get_valid_stage_ids_in_given_stage_ids(given_unique_stage_ids)

        self._validate_stage_ids(valid_stage_ids, given_unique_stage_ids)
        task_id_with_max_stage_value_dtos = self.task_storage. \
            get_user_task_ids_and_max_stage_value_dto_based_on_given_stage_ids(
                user_id=user_id, stage_ids=valid_stage_ids)
        stage_values = [
            task_id_with_max_stage_value_dto.stage_value
            for task_id_with_max_stage_value_dto in
            task_id_with_max_stage_value_dtos
        ]
        stage_values = sorted(list(set(stage_values)))
        task_ids_group_by_stage_value_dtos = \
            self.get_task_ids_group_by_stage_value_dtos(
                stage_values, task_id_with_max_stage_value_dtos
            )
        task_id_with_stage_details_dtos = self. \
            stage_storage. \
            get_task_id_with_stage_details_dtos_based_on_stage_value(
                stage_values=stage_values,
                task_ids_group_by_stage_value_dtos=
                task_ids_group_by_stage_value_dtos,
                user_id=user_id
            )
        task_ids = []
        task_id_with_single_stage_details_dto = []
        for task_id_with_stage_details_dto in task_id_with_stage_details_dtos:
            if task_id_with_stage_details_dto.task_display_id not in task_ids:
                task_ids.append(task_id_with_stage_details_dto.task_display_id)
                task_id_with_single_stage_details_dto.append(
                    task_id_with_stage_details_dto)
        task_with_complete_stage_details_dtos = \
            self._get_task_with_complete_stage_details_dtos(
                task_id_with_stage_details_dtos=task_id_with_stage_details_dtos)
        return task_with_complete_stage_details_dtos

    def _get_task_with_complete_stage_details_dtos(
            self,
            task_id_with_stage_details_dtos: List[TaskIdWithStageDetailsDTO]
    ) -> List[TaskWithCompleteStageDetailsDTO]:
        from ib_tasks.interactors.get_stages_assignees_details_interactor \
            import GetStagesAssigneesDetailsInteractor
        get_stage_assignees_details_interactor = \
            GetStagesAssigneesDetailsInteractor(
                task_stage_storage=self.task_stage_storage
            )
        task_with_complete_stage_details_dtos = []
        for task_id_with_stage_details_dto in task_id_with_stage_details_dtos:
            stage_assignee_details_dtos = \
                get_stage_assignees_details_interactor. \
                    get_stages_assignee_details_dtos(
                        task_id=task_id_with_stage_details_dto.task_id,
                        stage_ids=[task_id_with_stage_details_dto.db_stage_id])
            task_with_complete_stage_details_dto = \
                TaskWithCompleteStageDetailsDTO(
                    task_with_stage_details_dto=task_id_with_stage_details_dto,
                    stage_assignee_dto=stage_assignee_details_dtos)
            task_with_complete_stage_details_dtos.append(
                task_with_complete_stage_details_dto)
        return task_with_complete_stage_details_dtos

    @staticmethod
    def get_task_ids_group_by_stage_value_dtos(
            stage_values: List[int], task_id_with_max_stage_value_dtos
    ) -> List[StageValueWithTaskIdsDTO]:
        task_ids_group_by_stage_value_dtos = []
        for each_value in stage_values:

            list_of_task_ids = []
            for each_task_id_with_max_stage_value_dto in \
                    task_id_with_max_stage_value_dtos:
                if each_task_id_with_max_stage_value_dto.stage_value == \
                        each_value:
                    list_of_task_ids.append(
                        each_task_id_with_max_stage_value_dto.task_id)
            each_stage_value_with_task_ids_dto = StageValueWithTaskIdsDTO(
                stage_value=each_value, task_ids=list_of_task_ids)
            task_ids_group_by_stage_value_dtos.append(
                each_stage_value_with_task_ids_dto)
        return task_ids_group_by_stage_value_dtos

    @staticmethod
    def _validate_given_stage_ids_list_empty(given_stage_ids: List[str]):
        if not given_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                StageIdsListEmptyException
            raise StageIdsListEmptyException

    @staticmethod
    def _validate_stage_ids(valid_stage_ids: List[str],
                            given_unique_stage_ids: List[str]):
        invalid_stage_ids = []
        for stage_id in given_unique_stage_ids:
            if stage_id not in valid_stage_ids:
                invalid_stage_ids.append(stage_id)

        if invalid_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                InvalidStageIdsListException
            raise InvalidStageIdsListException(
                invalid_stage_ids=invalid_stage_ids)
