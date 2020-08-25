from datetime import datetime
from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.adapters.dtos import AssigneeDetailsDTO
from ib_tasks.constants.exception_messages import USER_IS_NOT_ASSIGNED_TO_TASK, \
    INVALID_DUE_DATE_TIME, INVALID_REASON_ID
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskDisplayId
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter import \
    TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskDueDetailsDTO

INVALID_STAGE_ID = ("please give a valid stage id",
                    "INVALID_STAGE_ID")


class TaskDueDetailsPresenterImplementation(TaskDueDetailsPresenterInterface,
                                            HTTPResponseMixin):

    def response_for_invalid_task_id(self, err: InvalidTaskDisplayId):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_DISPLAY_ID
        message = INVALID_TASK_DISPLAY_ID[0].format(err.task_display_id)
        data = {
            "response": message,
            "http_status_code": 404,
            "res_status": INVALID_TASK_DISPLAY_ID[1]
        }
        return self.prepare_404_not_found_response(data)

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
        data = self._convert_tasks_dtos_to_dict(task_dtos)
        response_object = self.prepare_200_success_response(
            response_dict=data
        )
        return response_object

    def _convert_tasks_dtos_to_dict(self, task_dtos: List[TaskDueDetailsDTO]):
        task_delay_details_list = []
        for task in task_dtos:
            task_details_dict = {'task_id': task.task_id,
                                 'reason': task.reason,
                                 'due_date_time': datetime.strftime(task.due_date_time, "%Y-%m-%d %H:%M:%S"),
                                 'due_missed_count': task.due_missed_count,
                                 'user': self._convert_user_dto_to_dict(task.user)}
            task_delay_details_list.append(
                task_details_dict
            )
        return task_delay_details_list

    @staticmethod
    def _convert_user_dto_to_dict(user: AssigneeDetailsDTO):
        user_dict = {'user_id': user.assignee_id,
                     'name': user.name,
                     'profile_pic': user.profile_pic_url}
        return user_dict

    def response_for_invalid_due_datetime(self):
        response_message = INVALID_DUE_DATE_TIME[0]
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_DUE_DATE_TIME[1]
        }
        response_object = self.prepare_400_bad_request_response(
            response_dict=data
        )
        return response_object

    def response_for_invalid_reason_id(self):
        response_message = INVALID_REASON_ID[0]
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_REASON_ID[1]
        }
        response_object = self.prepare_400_bad_request_response(
            response_dict=data
        )
        return response_object

    def response_for_invalid_stage_id(self):
        response_message = INVALID_STAGE_ID[0]
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_STAGE_ID[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object
