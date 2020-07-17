from typing import List
from django.http import response
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_boards.constants.exception_messages import (
    INVALID_BOARD_ID, INVALID_OFFSET_VALUE, INVALID_LIMIT_VALUE, USER_DONOT_HAVE_ACCESS)
from ib_boards.interactors.dtos import TaskColumnDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskFieldsDTO, TaskActionsDTO, ColumnDetailsDTO)


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
                                      task_details: List[TaskColumnDTO]) -> \
            response.HttpResponse:

        task_details_list = self._convert_task_details_into_dict(
            task_details=task_details, task_fields_dto=task_fields_dto,
            task_actions_dto=task_actions_dto
        )
        task_details_dict = {
            "total_tasks_count": len(task_details),
            "tasks": task_details_list
        }
        return self.prepare_200_success_response(task_details_dict)

    def _convert_task_details_into_dict(self,
                                        task_fields_dto: List[TaskFieldsDTO],
                                        task_actions_dto: List[TaskActionsDTO],
                                        task_details: List[TaskColumnDTO]
                                        ):
        list_of_tasks = []
        for task_dto in task_details:
            list_of_fields = self._get_list_of_task_fields(task_dto.task_id,
                                                           task_fields_dto)

            list_of_actions = self._get_task_actions_dict(task_actions_dto,
                                                          task_dto.task_id)
            list_of_tasks.append(
                {
                    "task_id": task_dto.task_id,
                    "fields": list_of_fields,
                    "actions": list_of_actions
                }
            )
        return  list_of_tasks

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

    def get_response_for_column_details(self,
                                        column_details: List[ColumnDetailsDTO],
                                        task_fields_dto: List[TaskFieldsDTO],
                                        task_actions_dto: List[TaskActionsDTO],
                                        task_details: List[TaskColumnDTO]
                                        ) -> response.HttpResponse:
        column_details = self._convert_column_details_into_dict(
            column_details=column_details, task_fields_dto=task_fields_dto,
            task_actions_dto=task_actions_dto, task_details=task_details
        )

        return self.prepare_200_success_response(column_details)

    def _convert_column_details_into_dict(self,
                                          column_details: List[ColumnDetailsDTO],
                                          task_fields_dto: List[TaskFieldsDTO],
                                          task_actions_dto: List[TaskActionsDTO],
                                          task_details: List[TaskColumnDTO]
                                          ):
        list_of_columns = []
        for column_dto in column_details:
            list_of_tasks = []
            for task_dto in task_details:
                if task_dto.column_id == column_dto.column_id:
                    list_of_tasks.append(task_dto)
            print(list_of_tasks)
            task_details_dict = self._convert_task_details_into_dict(
                task_details=list_of_tasks, task_actions_dto=task_actions_dto,
                task_fields_dto=task_fields_dto
            )
            list_of_columns.append(
                {
                    "column_id": column_dto.column_id,
                    "name": column_dto.name,
                    "tasks": task_details_dict
                }
            )
        columns_dict = {
            "total_columns_count": len(column_details),
            "columns": list_of_columns
        }
        return  columns_dict