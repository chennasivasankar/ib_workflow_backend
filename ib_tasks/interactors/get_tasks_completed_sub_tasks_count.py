from collections import defaultdict
from typing import List

from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskWithSubTaskDTO
from ib_tasks.interactors.task_dtos import TaskWithAllSubTaskDTO, \
    TaskWithCompletedSubTasksCountDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class GetTasksCompletedSubTasksCount:

    def __init__(
            self, task_stage_storage: TaskStageStorageInterface,
            task_storage: TaskStorageInterface
    ):
        self.task_stage_storage = task_stage_storage
        self.task_storage = task_storage

    def get_tasks_completed_sub_tasks_count(self, task_ids: List[int]):
        self._validate_task_ids(task_ids)
        task_with_sub_task_dtos = \
            self.task_storage.get_task_with_sub_task_dtos(
                task_ids)
        sub_tasks_count_dtos = self._get_sub_tasks_count_dtos(
            task_ids, task_with_sub_task_dtos
        )
        task_with_all_sub_tasks_dtos = self._get_task_with_all_sub_tasks_dtos(
            task_with_sub_task_dtos
        )
        from ib_tasks.constants.constants import ADHOC_TEMPLATE_ID
        adhoc_task_template_id = ADHOC_TEMPLATE_ID
        max_stage_value = \
            self.task_stage_storage.get_max_stage_value_for_the_given_template(
                adhoc_task_template_id)
        task_with_completed_sub_tasks_count_dtos = \
            self._get_task_with_completed_sub_tasks_count_dtos_based_on_max_stage_value(
                task_with_all_sub_tasks_dtos, max_stage_value
            )
        task_with_completed_sub_tasks_count_dtos += sub_tasks_count_dtos
        return task_with_completed_sub_tasks_count_dtos

    def _get_sub_tasks_count_dtos(
            self, task_ids: List[int],
            task_with_sub_task_dtos: List[TaskWithSubTaskDTO]
    ) -> List[TaskWithCompletedSubTasksCountDTO]:
        sub_task_ids = []
        sub_tasks_count_dtos = []
        for task_id in task_ids:
            is_sub_task = self._check_is_sub_task(
                task_id, task_with_sub_task_dtos
            )
            if is_sub_task:
                sub_task_ids.append(task_id)
        for sub_task_id in sub_task_ids:
            sub_tasks_count_dto = TaskWithCompletedSubTasksCountDTO(
                task_id=sub_task_id, completed_sub_tasks_count=0
            )
            sub_tasks_count_dtos.append(sub_tasks_count_dto)
        return sub_tasks_count_dtos

    @staticmethod
    def _check_is_sub_task(
            task_id: int,
            task_with_sub_task_dtos: List[TaskWithSubTaskDTO]
    ) -> bool:
        for dto in task_with_sub_task_dtos:
            if dto.task_id == task_id:
                return False
        return True

    def _get_task_with_completed_sub_tasks_count_dtos_based_on_max_stage_value(
            self, task_with_all_sub_tasks_dtos: List[TaskWithAllSubTaskDTO],
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
            self, task_with_all_sub_tasks_dtos: List[TaskWithAllSubTaskDTO],
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
            task_with_all_sub_tasks_dto: TaskWithAllSubTaskDTO,
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
            task_with_all_sub_tasks_dtos: List[TaskWithAllSubTaskDTO]
    ) -> List[int]:
        all_sub_task_ids = []
        for dto in task_with_all_sub_tasks_dtos:
            sub_task_ids = dto.sub_task_ids
            all_sub_task_ids += sub_task_ids
        return all_sub_task_ids

    @staticmethod
    def _get_task_with_all_sub_tasks_dtos(
            task_with_sub_task_dtos: List[TaskWithSubTaskDTO]
    ) -> List[TaskWithAllSubTaskDTO]:
        task_with_sub_tasks_dict = defaultdict(list)
        for dto in task_with_sub_task_dtos:
            task_id = dto.task_id
            sub_task_id = dto.sub_task_id
            task_with_sub_tasks_dict[task_id].append(sub_task_id)
        task_with_all_sub_tasks_dtos = []
        for task_id, sub_task_ids in task_with_sub_tasks_dict.items():
            task_with_all_sub_tasks_dto = TaskWithAllSubTaskDTO(
                task_id=task_id, sub_task_ids=sub_task_ids
            )
            task_with_all_sub_tasks_dtos.append(task_with_all_sub_tasks_dto)
        return task_with_all_sub_tasks_dtos

    def _validate_task_ids(self, task_ids: List[int]):
        valid_task_ids = self.task_storage.get_valid_task_ids(task_ids)
        invalid_task_ids = []
        for task_id in task_ids:
            if task_id not in valid_task_ids:
                invalid_task_ids.append(task_id)

        if invalid_task_ids:
            from ib_tasks.exceptions.task_custom_exceptions import \
                InvalidTaskException
            raise InvalidTaskException()
