from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_tasks_for_list_view_presenter_interface import \
    GetTasksForListViewPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO
from ib_adhoc_tasks.presenters.mixins.tasks_details_mixin import \
    TaskDetailsMixin


class GetTasksForListViewPresenterImplementation(
        GetTasksForListViewPresenterInterface,
        HTTPResponseMixin,
        TaskDetailsMixin
):

    def raise_invalid_offset_value(self):
        from ib_adhoc_tasks.constants.exception_messages import \
            INVALID_OFFSET_VALUE
        response_message = INVALID_OFFSET_VALUE[0]
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_OFFSET_VALUE[1]
        }
        response_object = self.prepare_400_bad_request_response(
            response_dict=data
        )
        return response_object

    def raise_invalid_limit_value(self):
        from ib_adhoc_tasks.constants.exception_messages import \
            INVALID_LIMIT_VALUE
        response_message = INVALID_LIMIT_VALUE[0]
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_LIMIT_VALUE[1]
        }
        response_object = self.prepare_400_bad_request_response(
            response_dict=data
        )
        return response_object

    def raise_invalid_project_id(self):
        from ib_adhoc_tasks.constants.exception_messages import \
            INVALID_PROJECT_ID
        response_message = INVALID_PROJECT_ID[0]
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_PROJECT_ID[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def raise_invalid_user_id(self):
        from ib_adhoc_tasks.constants.exception_messages import \
            INVALID_USER_ID
        response_message = INVALID_USER_ID[0]
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_USER_ID[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def raise_invalid_user_for_project(self):
        from ib_adhoc_tasks.constants.exception_messages import \
            INVALID_USER_ID_FOR_PROJECT
        response_message = INVALID_USER_ID_FOR_PROJECT[0]
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_USER_ID_FOR_PROJECT[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def get_task_details_group_by_info_response(
            self,
            group_details_dtos: List[GroupDetailsDTO],
            task_details_dto: TasksCompleteDetailsDTO,
            total_groups_count: int
    ):
        groups = []
        for group_details_dto in group_details_dtos:
            task_ids = group_details_dto.task_ids
            tasks = self.get_tasks_details(task_ids, task_details_dto)
            each_group_details = {
                "group_by_value": group_details_dto.group_by_value,
                "group_by_display_name":
                    group_details_dto.group_by_display_name,
                "total_tasks": group_details_dto.total_tasks,
                "tasks": tasks
            }
            groups.append(each_group_details)
        all_group_details = {
            "total_groups": total_groups_count,
            "groups": groups
        }
        response_object = self.prepare_200_success_response(
            response_dict=all_group_details
        )
        return response_object
