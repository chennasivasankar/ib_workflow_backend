"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""

from typing import List

from django.http import response

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetBoardsPresenterInterface, GetBoardsDetailsPresenterInterface, \
    GetColumnTasksPresenterInterface, TaskCompleteDetailsDTO
from ib_boards.interactors.storage_interfaces.dtos import BoardDTO
from ib_boards.constants.exception_messages import (
    INVALID_BOARD_ID, INVALID_OFFSET_VALUE, INVALID_LIMIT_VALUE, USER_DONOT_HAVE_ACCESS)
from ib_boards.interactors.dtos import TaskColumnDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskFieldsDTO, TaskActionsDTO, ColumnDetailsDTO)


class GetBoardsPresenterImplementation(
    GetBoardsPresenterInterface, HTTPResponseMixin):

    def get_response_for_user_have_no_access_for_boards(
            self) -> response.HttpResponse:
        from ib_boards.constants.exception_messages import \
            USER_NOT_HAVE_ACCESS_TO_BOARDS
        response_dict = {
            "response": USER_NOT_HAVE_ACCESS_TO_BOARDS[0],
            "http_status_code": 403,
            "res_status": USER_NOT_HAVE_ACCESS_TO_BOARDS[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )

    def get_response_for_invalid_offset(self) -> response.HttpResponse:
        from ib_boards.constants.exception_messages import INVALID_OFFSET_VALUE
        response_dict = {
            "response": INVALID_OFFSET_VALUE[0],
            "http_status_code": 400,
            "res_status": INVALID_OFFSET_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_invalid_limit(self) -> response.HttpResponse:
        from ib_boards.constants.exception_messages import INVALID_LIMIT_VALUE
        response_dict = {
            "response": INVALID_LIMIT_VALUE[0],
            "http_status_code": 400,
            "res_status": INVALID_LIMIT_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_get_boards(
            self, board_dtos: List[BoardDTO], total_boards: int) \
            -> response.HttpResponse:
        board_details_dict = {
            "total_boards_count": total_boards,
            "boards_details": []
        }
        for board_dto in board_dtos:
            board_dict = self._convert_board_dto_to_dict(board_dto=board_dto)
            board_details_dict["boards_details"].append(board_dict)

        return self.prepare_200_success_response(
            response_dict=board_details_dict
        )

    @staticmethod
    def _convert_board_dto_to_dict(board_dto):
        return {
            "board_id": board_dto.board_id,
            "display_name": board_dto.display_name
        }

    def get_response_for_offset_exceeds_total_tasks(self):
        pass


class GetBoardsDetailsPresenterImplementation(
    GetBoardsDetailsPresenterInterface, HTTPResponseMixin):

    def get_response_for_invalid_board_ids(
            self, error) -> response.HttpResponse:
        from ib_boards.constants.exception_messages import INVALID_BOARD_IDS
        response_dict = {
            "response": f"{INVALID_BOARD_IDS[0]}: {error.board_ids}",
            "http_status_code": 404,
            "res_status": INVALID_BOARD_IDS[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def get_response_for_board_details(
            self, board_dtos: List[BoardDTO]) -> response.HttpResponse:
        board_details_dict = []
        for board_dto in board_dtos:
            board_dict = self._convert_board_dto_to_dict(board_dto=board_dto)
            board_details_dict.append(board_dict)

        return self.prepare_200_success_response(
            response_dict=board_details_dict
        )

    @staticmethod
    def _convert_board_dto_to_dict(board_dto: BoardDTO):
        return {
            "board_id": board_dto.board_id,
            "display_name": board_dto.display_name
        }


class GetColumnTasksPresenterImplementation(
    GetColumnTasksPresenterInterface, HTTPResponseMixin):

    def get_response_for_the_invalid_column_id(self):
        from ib_boards.constants.exception_messages import INVALID_COLUMN_ID
        response_dict = {
            "response": INVALID_COLUMN_ID[0],
            "http_status_code": 404,
            "res_status": INVALID_COLUMN_ID[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def get_response_for_invalid_stage_ids(self, error):
        pass

    def get_response_column_tasks(
            self, task_complete_details_dto: TaskCompleteDetailsDTO):
        pass

    def get_response_for_invalid_offset(self):
        pass

    def get_response_for_invalid_limit(self):
        pass

    def get_response_for_offset_exceeds_total_tasks(self):
        pass

    def get_response_for_invalid_stage_ids(self, error):
        pass

    def get_response_for_user_have_no_access_for_column(self):
        from ib_boards.constants.exception_messages import \
            USER_NOT_HAVE_ACCESS_TO_COLUMN
        response_dict = {
            "response": USER_NOT_HAVE_ACCESS_TO_COLUMN[0],
            "http_status_code": 403,
            "res_status": USER_NOT_HAVE_ACCESS_TO_COLUMN[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):

    def response_for_invalid_board_id(self) -> response.HttpResponse:
        response_object = {"response": INVALID_BOARD_ID[0],
                           "http_status_code": 404,
                           "res_status": INVALID_BOARD_ID[1]}
        return self.prepare_404_not_found_response(response_dict=response_object)

    def response_for_invalid_offset_value(self):
        response_object = {"response": INVALID_OFFSET_VALUE[0],
                           "http_status_code": 400,
                           "res_status": INVALID_OFFSET_VALUE[1]}
        return self.prepare_400_bad_request_response(response_object)

    def response_for_invalid_limit_value(self):
        response_object = {"response": INVALID_LIMIT_VALUE[0],
                           "http_status_code": 400,
                           "res_status": INVALID_LIMIT_VALUE[1]}
        return self.prepare_400_bad_request_response(response_object)

    def response_for_user_donot_have_access_for_board(self):
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
        return list_of_tasks

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
                    "total_tasks_count": len(list_of_tasks),
                    "tasks": task_details_dict
                }
            )
        columns_dict = {
            "total_columns_count": len(column_details),
            "columns": list_of_columns
        }
        return columns_dict

    def get_response_for_offset_exceeds_total_tasks(self):
        pass
