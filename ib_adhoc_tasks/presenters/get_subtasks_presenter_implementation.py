from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.presenter_interfaces.subtask_presenter_interface import \
    GetSubTasksPresenterInterface


class GetSubTasksPresenterImplementation(
    GetSubTasksPresenterInterface, HTTPResponseMixin
):

    def get_response_for_get_subtasks_of_task(
            self, complete_subtasks_details_dto: TasksCompleteDetailsDTO
    ):
        pass
