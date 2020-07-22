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

    def get_response_column_tasks(
            self, task_complete_details_dto: TaskCompleteDetailsDTO):
        pass

    def get_response_for_invalid_offset(self):
        pass

    def get_response_for_invalid_limit(self):
        pass

    def get_response_for_offset_exceeds_total_tasks(self):
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
