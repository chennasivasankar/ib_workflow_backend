from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .subtask_presenter_interface import GetSubTasksPresenterInterface
from ib_adhoc_tasks.presenters.mixins.tasks_details_mixin import \
    TaskDetailsMixin


class GetSubTasksPresenterImplementation(
    GetSubTasksPresenterInterface, HTTPResponseMixin, TaskDetailsMixin
):

    def get_response_for_get_subtasks_of_task(
            self, subtask_ids: List[int],
            complete_subtasks_details_dto: TasksCompleteDetailsDTO
    ):
        complete_task_details = self.get_tasks_details(
            task_ids=subtask_ids,
            task_details_dto=complete_subtasks_details_dto
        )
        complete_task_details_dict = {
            "total_tasks": len(subtask_ids),
            "tasks": complete_task_details
        }
        return self.prepare_200_success_response(
            response_dict=complete_task_details_dict
        )
