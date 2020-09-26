from collections import defaultdict
from typing import List, Dict

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_tasks_for_kanban_view_presenter_interface import \
    GetTasksForKanbanViewPresenterInterface, TaskDetailsWithGroupByInfoDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupDetailsDTO, \
    ChildGroupCountDTO, GroupByResponseDTO
from ib_adhoc_tasks.presenters.mixins.tasks_details_mixin import \
    TaskDetailsMixin


class GetTasksForKanbanViewPresenterImplementation(
    GetTasksForKanbanViewPresenterInterface,
    HTTPResponseMixin,
    TaskDetailsMixin

):

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
            task_details_with_group_by_info_dto: TaskDetailsWithGroupByInfoDTO,
            group_by_response_dtos: List[GroupByResponseDTO]
    ):
        group_details_dtos = \
            task_details_with_group_by_info_dto.group_details_dtos
        total_groups_count = \
            task_details_with_group_by_info_dto.total_groups_count
        child_group_count_dtos = \
            task_details_with_group_by_info_dto.child_group_count_dtos
        task_details_dto = \
            task_details_with_group_by_info_dto.task_details_dtos

        group_by_parent_dict = self._get_group_by_parent_dict(
            group_details_dtos)
        group_by_child_dict = self._get_group_by_child_dict(group_details_dtos)
        groups = []
        for group_by_value, dto in group_by_parent_dict.items():
            total_child_groups = self._get_total_child_groups(
                dto.group_by_value, child_group_count_dtos
            )
            child_group_dtos = group_by_child_dict[group_by_value]
            child_groups = self._get_child_groups_details_for_each_group(
                child_group_dtos, task_details_dto)
            each_group = {
                "total_groups": total_child_groups,
                "group_by_value": dto.group_by_value,
                "group_by_display_name": dto.group_by_display_name,
                "child_groups": child_groups
            }
            groups.append(each_group)

        group_by_keys = [
            {
                "group_by_key": group_by_response_dto.group_by_key,
                "display_name": group_by_response_dto.display_name,
                "order": group_by_response_dto.order
            }
            for group_by_response_dto in group_by_response_dtos
        ]

        all_group_details = {
            "group_by_keys": group_by_keys,
            "total_groups": total_groups_count,
            "groups": groups
        }
        response_object = self.prepare_200_success_response(
            response_dict=all_group_details
        )
        return response_object

    @staticmethod
    def _get_group_by_parent_dict(
            group_details_dtos: List[GroupDetailsDTO]
    ) -> Dict:
        group_by_parent_dict = {}
        for group_details_dto in group_details_dtos:
            group_by_value = group_details_dto.group_by_value
            group_by_parent_dict[group_by_value] = group_details_dto
        return group_by_parent_dict

    @staticmethod
    def _get_group_by_child_dict(
            group_details_dtos: List[GroupDetailsDTO]
    ) -> Dict:
        group_by_child_dict = defaultdict(list)
        for group_details_dto in group_details_dtos:
            group_by_value = group_details_dto.group_by_value
            group_by_child_dict[group_by_value].append(group_details_dto)
        return group_by_child_dict

    @staticmethod
    def _get_total_child_groups(
            group_by_value: str,
            child_group_count_dtos: List[ChildGroupCountDTO]
    ) -> int:
        total_child_groups = 0
        for dto in child_group_count_dtos:
            if dto.group_by_value == group_by_value:
                total_child_groups = dto.total_child_groups
        return total_child_groups

    def _get_child_groups_details_for_each_group(
            self, child_group_dtos: List[GroupDetailsDTO],
            task_details_dto: TasksCompleteDetailsDTO
    ) -> List[Dict]:
        child_groups = []
        for child_group_dto in child_group_dtos:
            task_ids = child_group_dto.task_ids
            tasks = self.get_tasks_details(task_ids, task_details_dto)
            each_group_details = {
                "group_by_value": child_group_dto.child_group_by_value,
                "group_by_display_name":
                    child_group_dto.child_group_by_display_name,
                "total_tasks": child_group_dto.total_tasks,
                "tasks": tasks
            }
            child_groups.append(each_group_details)
        return child_groups
