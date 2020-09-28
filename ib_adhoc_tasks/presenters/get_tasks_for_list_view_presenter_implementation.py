from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_tasks_for_list_view_presenter_interface import \
    GetTasksForListViewPresenterInterface, \
    TaskDetailsWithGroupInfoForListViewDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupByResponseDTO
from ib_adhoc_tasks.presenters.mixins.tasks_details_mixin import \
    TaskDetailsMixin
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_tasks_for_list_view_presenter_interface import \
    GetTasksForListViewPresenterInterface, \
    TaskDetailsWithGroupInfoForListViewDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupByResponseDTO
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
            self, task_details_with_group_info_list_view_dto:
            TaskDetailsWithGroupInfoForListViewDTO,
            group_by_response_dto: GroupByResponseDTO
    ):
        group_details_dtos = \
            task_details_with_group_info_list_view_dto.group_details_dtos
        task_details_dto = task_details_with_group_info_list_view_dto\
            .task_details_dto
        total_groups_count = \
            task_details_with_group_info_list_view_dto.total_groups_count
        sub_tasks_count_dtos = \
            task_details_with_group_info_list_view_dto\
                .task_with_sub_tasks_count_dtos
        completed_sub_tasks_count_dtos = \
            task_details_with_group_info_list_view_dto\
                .task_completed_sub_tasks_count_dtos

        groups = []
        for group_details_dto in group_details_dtos:
            task_ids = group_details_dto.task_ids
            tasks = self.get_tasks_details(
                task_ids, task_details_dto, sub_tasks_count_dtos,
                completed_sub_tasks_count_dtos
            )
            group_by_display_name = "Empty value for " + group_by_response_dto.group_by_key
            if group_details_dto.group_by_value:
                group_by_display_name = self._get_group_by_display_name(
                    group_by_response_dto=group_by_response_dto,
                    group_by_display_name=group_details_dto.group_by_display_name
                )
            each_group_details = {
                "group_by_value": group_details_dto.group_by_value,
                "group_by_display_name": group_by_display_name,
                "total_tasks": group_details_dto.total_tasks,
                "tasks": tasks
            }
            groups.append(each_group_details)
        all_group_details = {
            "group_by_key": {
                "group_by_key": group_by_response_dto.group_by_key,
                "display_name": group_by_response_dto.display_name,
                "order": group_by_response_dto.order
            },
            "total_groups": total_groups_count,
            "groups": groups
        }
        response_object = self.prepare_200_success_response(
            response_dict=all_group_details
        )
        return response_object

    def _get_group_by_display_name(self, group_by_response_dto: GroupByResponseDTO, group_by_display_name):
        from ib_adhoc_tasks.constants.enum import GroupByKey
        if group_by_response_dto.group_by_key in [GroupByKey.START_DATE.value, GroupByKey.DUE_DATE.value]:
            return self._convert_milliseconds_epoch_time_to_datetime_sting(
                epoch_time=group_by_display_name
            )
        return group_by_display_name

    @staticmethod
    def _convert_milliseconds_epoch_time_to_datetime_sting(epoch_time: int):
        import datetime
        datetime_object = datetime.datetime.fromtimestamp(epoch_time / 1000.0)
        from ib_adhoc_tasks.constants.constants import DISPLAY_DATE_FORMAT
        datetime_string = datetime_object.strftime(DISPLAY_DATE_FORMAT)
        return datetime_string
