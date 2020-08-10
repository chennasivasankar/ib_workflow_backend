from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.constants.exception_messages import USER_IS_NOT_ASSIGNED_TO_TASK
from ib_tasks.exceptions.custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter import \
    TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskDueDetailsDTO


class TaskDueDetailsPresenterImplementation(TaskDueDetailsPresenterInterface,
                                            HTTPResponseMixin):

    def response_for_invalid_task_id(self, err: InvalidTaskIdException):
        from ib_tasks.constants.exception_messages import INVALID_TASK_ID
        task_id = err.task_id
        response_message = INVALID_TASK_ID[0].format(task_id)
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_TASK_ID[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def response_for_user_is_not_assignee_for_task(self):
        response_message = USER_IS_NOT_ASSIGNED_TO_TASK[0]
        data = {
            "response": response_message,
            "http_status_code": 403,
            "res_status": USER_IS_NOT_ASSIGNED_TO_TASK[1]
        }
        response_object = self.prepare_403_forbidden_response(
            response_dict=data
        )
        return response_object

    def get_response_for_get_task_due_details(self, task_dtos: List[TaskDueDetailsDTO]):
        data = [{}]
        response_object = self.prepare_200_success_response(
            response_dict=data
        )
        return response_object
