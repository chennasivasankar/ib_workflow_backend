from typing import List

from ib_tasks.interactors.storage_interfaces.task_dtos import SubTasksIdsDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskWithCompletedSubTasksCountDTO


class GetTasksCompletedSubTasksCount:

    def __init__(
            self, task_stage_storage: TaskStageStorageInterface,
            task_storage: TaskStorageInterface
    ):
        self.task_stage_storage = task_stage_storage
        self.task_storage = task_storage

    def get_tasks_completed_sub_tasks_count(self, task_ids: List[int]):
        self._validate_task_ids(task_ids)
        task_with_all_sub_tasks_dtos = \
            self.task_storage.get_sub_task_ids_to_tasks(task_ids=task_ids)
        from ib_tasks.constants.constants import ADHOC_TEMPLATE_ID
        adhoc_task_template_id = ADHOC_TEMPLATE_ID
        max_stage_value = \
            self.task_stage_storage.get_max_stage_value_for_the_given_template(
                adhoc_task_template_id)
        task_with_completed_sub_tasks_count_dtos = \
            self._get_task_with_completed_sub_tasks_count_dtos_based_on_max_stage_value(
                task_with_all_sub_tasks_dtos, max_stage_value
            )
        return task_with_completed_sub_tasks_count_dtos

    def _get_task_with_completed_sub_tasks_count_dtos_based_on_max_stage_value(
            self, task_with_all_sub_tasks_dtos: List[SubTasksIdsDTO],
            max_stage_value: int
    ) -> List[TaskWithCompletedSubTasksCountDTO]:
        all_sub_task_ids = self._get_all_sub_task_ids(
            task_with_all_sub_tasks_dtos)
        completed_sub_task_ids = \
            self.task_stage_storage.get_completed_sub_task_ids(
                all_sub_task_ids, max_stage_value)
        task_with_completed_sub_task_count_dtos = \
            self._get_task_with_completed_sub_task_count_dtos(
                task_with_all_sub_tasks_dtos, completed_sub_task_ids
            )
        return task_with_completed_sub_task_count_dtos

    def _get_task_with_completed_sub_task_count_dtos(
            self, task_with_all_sub_tasks_dtos: List[SubTasksIdsDTO],
            completed_sub_task_ids: List[int]
    ) -> List[TaskWithCompletedSubTasksCountDTO]:
        task_with_completed_sub_task_count_dtos = []
        for task_with_all_sub_tasks_dto in task_with_all_sub_tasks_dtos:
            completed_sub_tasks_count = self._get_completed_sub_tasks_count(
                task_with_all_sub_tasks_dto, completed_sub_task_ids
            )
            task_with_completed_sub_task_count_dtos.append(
                completed_sub_tasks_count)
        return task_with_completed_sub_task_count_dtos

    @staticmethod
    def _get_completed_sub_tasks_count(
            task_with_all_sub_tasks_dto: SubTasksIdsDTO,
            completed_sub_task_ids: List[int]
    ) -> TaskWithCompletedSubTasksCountDTO:
        count = 0
        sub_task_ids = task_with_all_sub_tasks_dto.sub_task_ids
        for sub_task_id in sub_task_ids:
            if sub_task_id in completed_sub_task_ids:
                count += 1

        return TaskWithCompletedSubTasksCountDTO(
            task_id=task_with_all_sub_tasks_dto.task_id,
            completed_sub_tasks_count=count
        )

    @staticmethod
    def _get_all_sub_task_ids(
            task_with_all_sub_tasks_dtos: List[SubTasksIdsDTO]
    ) -> List[int]:
        all_sub_task_ids = []
        for dto in task_with_all_sub_tasks_dtos:
            sub_task_ids = dto.sub_task_ids
            all_sub_task_ids += sub_task_ids
        return all_sub_task_ids

    def _validate_task_ids(self, task_ids: List[int]):
        valid_task_ids = self.task_storage.get_valid_task_ids(task_ids)
        invalid_task_ids = []
        for task_id in task_ids:
            if task_id not in valid_task_ids:
                invalid_task_ids.append(task_id)

        if invalid_task_ids:
            from ib_tasks.exceptions.task_custom_exceptions import \
                InvalidTaskIds
            raise InvalidTaskIds(invalid_task_ids)
