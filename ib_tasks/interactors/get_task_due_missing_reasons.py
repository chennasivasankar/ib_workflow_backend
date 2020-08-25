from typing import List

from ib_tasks.adapters.service_adapter import get_service_adapter
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId, InvalidStageIdException
from ib_tasks.exceptions.task_custom_exceptions import UserIsNotAssigneeToTask, \
    InvalidTaskDisplayId
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter \
    import TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskDueMissingDTO, \
    TaskDueDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class GetTaskDueMissingReasonsInteractor(GetTaskIdForTaskDisplayIdMixin):
    def __init__(self, task_storage: TaskStorageInterface,
                 storage: StorageInterface):
        self.storage = storage
        self.task_storage = task_storage

    def get_task_due_missing_reasons_wrapper(
            self,
            presenter: TaskDueDetailsPresenterInterface,
            task_display_id: str, user_id: str, stage_id: str) \
            -> List[TaskDueDetailsDTO]:
        try:
            task_dtos = self.get_task_due_missing_reasons(
                task_display_id=task_display_id, user_id=user_id,
                stage_id=stage_id)
        except InvalidTaskDisplayId as err:
            return presenter.response_for_invalid_task_id(err)
        except UserIsNotAssigneeToTask as err:
            return presenter.response_for_user_is_not_assignee_for_task()
        except InvalidStageIdException:
            return presenter.response_for_invalid_stage_id()
        return presenter.get_response_for_get_task_due_details(task_dtos)

    def get_task_due_missing_reasons(self, task_display_id: str,
                                     user_id: str, stage_id: str) -> \
            List[TaskDueDetailsDTO]:
        task_id = self.get_task_id_for_task_display_id(
            task_display_id=task_display_id)
        self._validate_stage_id(stage_id)
        self._validate_if_task_is_assigned_to_user(task_id=task_id,
                                                   user_id=user_id, stage_id=stage_id)
        task_dtos = self._get_task_reasons(task_id=task_id, stage_id=stage_id)
        return task_dtos

    def _validate_stage_id(self, stage_id: str):
        is_valid = self.storage.validate_stage_id(stage_id)
        if not is_valid:
            raise InvalidStageIdException

    def _validate_if_task_is_assigned_to_user(self, task_id: int,
                                              user_id: str, stage_id: str):
        is_assigned = self.storage.validate_if_task_is_assigned_to_user_in_given_stage(
            task_id=task_id, user_id=user_id, stage_id=stage_id
        )
        is_not_assigned = not is_assigned
        if is_not_assigned:
            raise UserIsNotAssigneeToTask

    def _get_task_reasons(self, task_id: int, stage_id: str)\
            -> List[TaskDueDetailsDTO]:
        task_details = self.storage.get_task_due_details(task_id=task_id,
                                                         stage_id=stage_id)
        user_ids = [task.user_id for task in task_details]
        unique_user_ids = list(set(user_ids))
        user_service = get_service_adapter().assignee_details_service
        user_dtos = user_service.get_assignees_details_dtos(unique_user_ids)
        users_dict = {}
        for user in user_dtos:
            users_dict[user.assignee_id] = user

        task_dtos = self._map_user_and_tasks(task_details=task_details,
                                             users_dict=users_dict)
        return task_dtos

    @staticmethod
    def _map_user_and_tasks(task_details: List[TaskDueMissingDTO],
                            users_dict) -> List[TaskDueDetailsDTO]:
        tasks_dtos = []
        for task in task_details:
            tasks_dtos.append(
                TaskDueDetailsDTO(
                    task_id=task.task_id,
                    reason=task.reason,
                    due_date_time=task.due_date_time,
                    due_missed_count=task.due_missed_count,
                    user=users_dict[task.user_id]
                )
            )
        return tasks_dtos
