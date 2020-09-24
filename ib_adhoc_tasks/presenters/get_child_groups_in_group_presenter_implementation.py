from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.presenter_interfaces.get_child_groups_in_group_presenter_interface import \
    GetChildGroupsInGroupPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO
from ib_adhoc_tasks.presenters.mixins.tasks_details_mixin import \
    TaskDetailsMixin


class GetChildGroupsInGroupPresenterImplementation(
    GetChildGroupsInGroupPresenterInterface, HTTPResponseMixin, TaskDetailsMixin
):

    def prepare_response_for_get_child_groups_in_group(
            self, group_details_dtos: List[GroupDetailsDTO],
            total_child_groups_count: int,
            task_details_dto: TasksCompleteDetailsDTO
    ):
        child_groups = []
        for group_details_dto in group_details_dtos:
            task_ids = group_details_dto.task_ids
            tasks = self.get_tasks_details(
                task_ids, task_details_dto)
            each_group_details = {
                "group_by_value": group_details_dto.child_group_by_value,
                "group_by_display_name":
                    group_details_dto.child_group_by_display_name,
                "total_tasks": group_details_dto.total_tasks,
                "tasks": tasks
            }
            child_groups.append(each_group_details)
        response_dict = {
            "total_child_groups": total_child_groups_count,
            "child_groups": child_groups
        }
        response_object = self.prepare_200_success_response(
            response_dict=response_dict
        )
        return response_object
