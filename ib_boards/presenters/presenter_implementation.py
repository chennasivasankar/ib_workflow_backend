from typing import List
from django.http import response
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_boards.constants.exception_messages import (
    INVALID_BOARD_ID, INVALID_OFFSET_VALUE, INVALID_LIMIT_VALUE, USER_DONOT_HAVE_ACCESS)
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import TaskFieldsDTO, TaskActionsDTO


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):

    def raise_exception_for_invalid_board_id(self) -> response.HttpResponse:
        response_object = {"response": INVALID_BOARD_ID[0],
                           "http_status_code": 404,
                           "res_status": INVALID_BOARD_ID[1]}
        return self.prepare_404_not_found_response(response_dict=response_object)

    def raise_exception_for_invalid_offset_value(self):
        response_object = {"response": INVALID_OFFSET_VALUE[0],
                           "http_status_code": 400,
                           "res_status": INVALID_OFFSET_VALUE[1]}
        return self.prepare_400_bad_request_response(response_object)

    def raise_exception_for_invalid_limit_value(self):
        response_object = {"response": INVALID_LIMIT_VALUE[0],
                           "http_status_code": 400,
                           "res_status": INVALID_LIMIT_VALUE[1]}
        return self.prepare_400_bad_request_response(response_object)

    def raise_exception_for_user_donot_have_access_for_board(self):
        response_object = {"response": USER_DONOT_HAVE_ACCESS[0],
                           "http_status_code": 403,
                           "res_status": USER_DONOT_HAVE_ACCESS[1]}
        return self.prepare_403_forbidden_response(response_object)

    def get_response_for_task_details(self,
                                      task_fields_dto: List[TaskFieldsDTO],
                                      task_actions_dto: List[TaskActionsDTO],
                                      task_ids: List[str]) -> response.HttpResponse:

        task_details_list = self._convert_task_details_into_list_of_dicts(
            task_ids=task_ids, task_fields_dto=task_fields_dto,
            task_actions_dto=task_actions_dto
        )
        return self.prepare_200_success_response(task_details_list)

    def _convert_task_details_into_list_of_dicts(self,
                                                 task_fields_dto: List[TaskFieldsDTO],
                                                 task_actions_dto: List[TaskActionsDTO],
                                                 task_ids: List[str]
                                                 ):
        list_of_tasks = []
        for task_id in task_ids:
            list_of_fields = self._get_list_of_task_fields(task_id, task_fields_dto)

            list_of_actions = self._get_task_actions_dict(task_actions_dto, task_id)
            list_of_tasks.append(
                {
                    "task_id": task_id,
                    "fields": list_of_fields,
                    "actions": list_of_actions
                }
            )
        return {
            "total_tasks_count": len(task_ids),
            "tasks": list_of_tasks
        }

    def _get_task_actions_dict(self, task_actions_dto, task_id):
        task_actions = []
        for task_action_dto in task_actions_dto:
            if task_action_dto.task_id == task_id:
                task_actions.append(task_action_dto)
        list_of_actions = self._convert_task_actions_dtos_into_list_of_dict(
            task_actions
        )
        return list_of_actions

    def _get_list_of_task_fields(self, task_id: str,
                                 task_fields_dto: List[TaskFieldsDTO]):
        task_fields = []
        for task_field in task_fields_dto:
            if task_field.task_id == task_id:
                task_fields.append(task_field)
        list_of_fields = self._convert_task_fields_dtos_into_list_of_dict(
            task_fields)

        return list_of_fields

    @staticmethod
    def _convert_task_fields_dtos_into_list_of_dict(task_fields_dto: List[TaskFieldsDTO]):
        list_of_task_fields = []
        for field_dto in task_fields_dto:
            list_of_task_fields.append(
                {
                    "field_type": field_dto.field_type,
                    "key": field_dto.key,
                    "value": field_dto.value
                }
            )
        return list_of_task_fields

    @staticmethod
    def _convert_task_actions_dtos_into_list_of_dict(task_actions_dto: List[TaskActionsDTO]):

        list_of_task_actions = []
        for action_dto in task_actions_dto:
            list_of_task_actions.append(
                {
                    "action_id": action_dto.action_id,
                    "name": action_dto.name,
                    "button_text": action_dto.button_text,
                    "button_color": action_dto.button_color
                }
            )
        return list_of_task_actions
