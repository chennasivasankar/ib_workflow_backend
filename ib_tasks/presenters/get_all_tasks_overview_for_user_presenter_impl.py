from datetime import datetime
from typing import Dict, Optional, List

from django.http import response
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.presenter_interfaces \
    .get_all_tasks_overview_for_user_presenter_interface import \
    GetAllTasksOverviewForUserPresenterInterface, \
    GetFilteredTasksOverviewForUserPresenterInterface
from ib_tasks.interactors.stage_dtos import TaskStageAssigneeTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskBaseDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO


class GetAllTasksOverviewForUserPresenterImpl(
    GetAllTasksOverviewForUserPresenterInterface, HTTPResponseMixin
):
    def raise_limit_should_be_greater_than_zero_exception(
            self) -> response.HttpResponse:
        from ib_tasks.constants.exception_messages import \
            LIMIT_SHOULD_BE_GREATER_THAN_ZERO
        response_dict = {
            "response": LIMIT_SHOULD_BE_GREATER_THAN_ZERO[0],
            "http_status_code": 400,
            "res_status": LIMIT_SHOULD_BE_GREATER_THAN_ZERO[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_offset_should_be_greater_than_zero_exception(
            self) -> response.HttpResponse:
        from ib_tasks.constants.exception_messages import \
            OFFSET_SHOULD_BE_GREATER_THAN_ZERO
        response_dict = {
            "response": OFFSET_SHOULD_BE_GREATER_THAN_ZERO[0],
            "http_status_code": 400,
            "res_status":
                OFFSET_SHOULD_BE_GREATER_THAN_ZERO[1]
        }

        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_stage_ids_empty_exception(self) -> response.HttpResponse:
        from ib_tasks.constants.exception_messages import \
            EMPTY_STAGE_IDS_ARE_INVALID
        response_dict = {
            "response": EMPTY_STAGE_IDS_ARE_INVALID[0],
            "http_status_code": 400,
            "res_status": EMPTY_STAGE_IDS_ARE_INVALID[1]
        }

        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def all_tasks_overview_details_response(self,
                                            all_tasks_overview_details_dto:
                                            AllTasksOverviewDetailsDTO) -> \
            response.HttpResponse:
        task_overview_details = self.get_task_overview_details(
            all_tasks_overview_details_dto)
        all_tasks_overview_details_response_dict = {
            'tasks': task_overview_details,
            'total_tasks': len(task_overview_details)
        }
        return self.prepare_200_success_response(
            response_dict=all_tasks_overview_details_response_dict)

    def get_task_overview_details(self, all_tasks_overview_details_dto):
        task_with_complete_stage_details_dtos = \
            all_tasks_overview_details_dto. \
            task_with_complete_stage_details_dtos
        task_fields_and_action_details_dtos = all_tasks_overview_details_dto. \
            task_fields_and_action_details_dtos
        task_base_details_dtos = all_tasks_overview_details_dto.task_base_details_dtos
        task_base_details_dtos_dict = {
            task_base_details_dto.task_id: task_base_details_dto
            for task_base_details_dto in task_base_details_dtos
        }
        task_fields_and_actions_dict = {}
        for task_fields_and_action_details_dto in task_fields_and_action_details_dtos:
            task_fields_and_actions_dict[
                task_fields_and_action_details_dto.stage_id
                + str(task_fields_and_action_details_dto.task_id)
            ] = task_fields_and_action_details_dto

        task_overview_details = []
        task_ids = []
        for task_with_complete_stage_details_dto in task_with_complete_stage_details_dtos:
            each_task_id_with_stage_details_dto = \
                task_with_complete_stage_details_dto.task_with_stage_details_dto
            task_id = each_task_id_with_stage_details_dto.task_id
            task_fields_and_action_details_dto = task_fields_and_actions_dict[
                each_task_id_with_stage_details_dto.stage_id
                + str(each_task_id_with_stage_details_dto.task_id)
            ]
            if task_id not in task_ids:
                task_overview_details_dict = self._get_task_overview_details_dict(
                    each_task_id_with_stage_details_dto,
                    task_fields_and_action_details_dto,
                    task_with_complete_stage_details_dto,
                    task_base_details_dtos_dict[task_id]
                )
                task_ids.append(task_id)
                task_overview_details.append(task_overview_details_dict)
        return task_overview_details

    def _get_task_overview_details_dict(
            self, each_task_id_with_stage_details_dto,
            task_fields_and_action_details_dto,
            task_with_complete_stage_details_dto, task_base_details_dto):
        task_overview_fields_details, actions_details = self. \
            task_fields_and_actions_details(
                task_fields_and_action_details_dto
            )
        assignee = self._get_assignee_details(
            task_with_complete_stage_details_dto.stage_assignee_dto
        )
        start_date, due_date = self._get_start_date_and_due_date(
            task_base_details_dto)
        task_overview_details_dict = {
            "template_id": task_base_details_dto.template_id,
            "task_id": each_task_id_with_stage_details_dto.task_display_id,
            "title": task_base_details_dto.title,
            "start_date": start_date,
            "due_date": due_date,
            "priority": task_base_details_dto.priority,
            "task_overview_fields": task_overview_fields_details,
            "stage_with_actions": {
                "stage_id":
                    each_task_id_with_stage_details_dto.db_stage_id,
                "stage_display_name":
                    each_task_id_with_stage_details_dto.stage_display_name,
                "stage_color":
                    each_task_id_with_stage_details_dto.stage_color,
                "assignee": assignee,
                "actions": actions_details
            }
        }
        return task_overview_details_dict

    def task_fields_and_actions_details(
            self, task_fields_and_action_details_dto: GetTaskStageCompleteDetailsDTO):
        task_overview_fields_details = self. \
            _get_task_overview_fields_details(task_fields_and_action_details_dto)
        action_details = self._get_actions_details_of_task_stage(
            task_fields_and_action_details_dto)
        return task_overview_fields_details, action_details

    @staticmethod
    def _get_task_overview_fields_details(
            each_task_fields_and_action_details_dto):

        field_dtos = each_task_fields_and_action_details_dto.field_dtos
        field_dtos.sort(key=lambda x: [x.order])
        task_overview_fields_details = [
            {
                "field_type": each_field_dto.field_type,
                "field_display_name": each_field_dto.key,
                "field_response": each_field_dto.value
            } for each_field_dto in field_dtos
        ]
        return task_overview_fields_details

    @staticmethod
    def _get_actions_details_of_task_stage(
            each_task_fields_and_action_details_dto):
        action_dtos = each_task_fields_and_action_details_dto.action_dtos
        action_dtos.sort(key=lambda x: [x.order])
        action_details = [{
            "action_id": each_action_dto.action_id,
            "button_text": each_action_dto.button_text,
            "button_color": each_action_dto.button_color,
            "action_type": each_action_dto.action_type,
            "transition_template_id": each_action_dto.transition_template_id
        } for each_action_dto in action_dtos]
        return action_details

    @staticmethod
    def _get_assignee_details(
            stage_assignee_dto: List[TaskStageAssigneeTeamDetailsDTO]
    ) -> Optional[Dict]:
        if stage_assignee_dto:
            assignee_details_dto = stage_assignee_dto[0].assignee_details
        else:
            return None
        if assignee_details_dto:
            assignee_details = {
                "assignee_id": assignee_details_dto.assignee_id,
                "name": assignee_details_dto.name,
                "profile_pic_url": assignee_details_dto.profile_pic_url
            }
            return assignee_details

    def _get_start_date_and_due_date(
            self, task_base_details_dto: TaskBaseDetailsDTO
    ):
        start_date, due_date = None, None
        if task_base_details_dto.start_date is not None:
            start_date = self._convert_datetime_object_to_string(
                task_base_details_dto.start_date
            )
        if task_base_details_dto.due_date is not None:
            due_date = self._convert_datetime_object_to_string(
                task_base_details_dto.due_date
            )
        return start_date, due_date

    @staticmethod
    def _convert_datetime_object_to_string(
            datetime_obj: datetime
    ) -> str:
        from ib_tasks.constants.constants import DATETIME_FORMAT
        datetime_in_string_format = datetime_obj.strftime(DATETIME_FORMAT)
        return datetime_in_string_format


class GetFilteredTasksOverviewForUserPresenterImplementation(
    GetAllTasksOverviewForUserPresenterImpl,
    GetFilteredTasksOverviewForUserPresenterInterface
):

    def get_response_for_filtered_tasks_overview_details_response(
            self,
            filtered_tasks_overview_details_dto: AllTasksOverviewDetailsDTO,
            total_tasks: int, column_task_count: int):
        task_overview_details = self.get_task_overview_details(
            filtered_tasks_overview_details_dto)
        all_tasks_overview_details_response_dict = {
            'tasks': task_overview_details,
            'total_tasks': total_tasks,
            "column_task_count": column_task_count
        }
        return self.prepare_200_success_response(
            response_dict=all_tasks_overview_details_response_dict)

    def get_response_for_invalid_project_id(
            self, err: InvalidProjectIdsException):
        from ib_tasks.constants.exception_messages import INVALID_PROJECT_ID
        project_id = err.invalid_project_ids[0]
        message = INVALID_PROJECT_ID[0].format(project_id)
        response_dict = {
            "response": message,
            "http_status_code": 404,
            "res_status": INVALID_PROJECT_ID[1]
        }

        response_object = self.prepare_404_not_found_response(response_dict)
        return response_object

    def get_response_for_user_not_in_project(self):
        from ib_tasks.constants.exception_messages import USER_NOT_IN_PROJECT
        response_dict = {
            "response": USER_NOT_IN_PROJECT[0],
            "http_status_code": 404,
            "res_status": USER_NOT_IN_PROJECT[1]
        }

        response_object = self.prepare_403_forbidden_response(response_dict)
        return response_object

    def get_response_for_invalid_filter_condition(self, error):
        from ib_tasks.constants.exception_messages import \
            FILTER_CONDITION_NOT_APPLICABLE_FOR_VALUE
        response_dict = {
            "response": FILTER_CONDITION_NOT_APPLICABLE_FOR_VALUE[0].format(
                error.condition),
            "http_status_code": 400,
            "res_status": FILTER_CONDITION_NOT_APPLICABLE_FOR_VALUE[1]
        }

        response_object = self.prepare_400_bad_request_response(response_dict)
        return response_object


