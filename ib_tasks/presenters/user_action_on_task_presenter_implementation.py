from typing import List, Dict
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO, ColumnStageDTO
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserActionPermissionDenied
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException
from ib_tasks.interactors.gofs_dtos import FieldDisplayDTO
from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO
from ib_tasks.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO
from ib_tasks.interactors.user_action_on_task_interactor import \
    InvalidBoardIdException


class UserActionOnTaskPresenterImplementation(PresenterInterface,
                                              HTTPResponseMixin):

    def raise_exception_for_invalid_task(
            self, error_obj: InvalidTaskException):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_ID

        response_message = INVALID_TASK_ID[0].format(
            str(error_obj.task_id)
        )
        response_dict = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_TASK_ID[1]
        }

        response_object = self.prepare_404_not_found_response(response_dict)
        return response_object

    def raise_exception_for_invalid_board(
            self, error_obj: InvalidBoardIdException):
        from ib_tasks.constants.exception_messages import \
            INVALID_BOARD_ID

        response_message = INVALID_BOARD_ID[0].format(
            str(error_obj.board_id)
        )
        response_dict = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_BOARD_ID[1]
        }

        response_object = self.prepare_404_not_found_response(response_dict)
        return response_object

    def raise_exception_for_invalid_action(
            self, error_obj: InvalidActionException):
        from ib_tasks.constants.exception_messages import \
            INVALID_ACTION_ID

        response_message = INVALID_ACTION_ID[0].format(
            str(error_obj.action_id)
        )
        response_dict = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_ACTION_ID[1]
        }

        response_object = self.prepare_404_not_found_response(response_dict)
        return response_object

    def raise_exception_for_user_action_permission_denied(
            self, error_obj: UserActionPermissionDenied):
        from ib_tasks.constants.exception_messages import \
            USER_DO_NOT_HAVE_ACCESS

        response_message = USER_DO_NOT_HAVE_ACCESS[0].format(
            str(error_obj.action_id)
        )
        response_dict = {
            "response": response_message,
            "http_status_code": 403,
            "res_status": USER_DO_NOT_HAVE_ACCESS[1]
        }

        response_object = self.prepare_403_forbidden_response(response_dict)
        return response_object

    def get_response_for_user_action_on_task(
            self, task_complete_details_dto: TaskCompleteDetailsDTO):

        task_id = task_complete_details_dto.task_id
        task_board_details = task_complete_details_dto.task_boards_details
        actions_dto = task_complete_details_dto.actions_dto
        fields_dto = task_complete_details_dto.field_dtos
        board_dto = task_board_details.board_dto
        response_dict = {
            "task_id": str(task_id),
            "current_board_details": {
                "board_id": board_dto.board_id,
                "board_name": board_dto.name,
                "column_details": self._get_column_details(
                    actions_dto, fields_dto, task_board_details
                )
            },
            "other_board_details": []
        }
        response_object = self.prepare_200_success_response(response_dict)
        return response_object

    def _get_column_details(self, actions_dto: List[ActionDTO],
                            fields_dto: List[FieldDisplayDTO],
                            task_board_details: TaskBoardsDetailsDTO):

        column_stage_dtos = task_board_details.column_stage_dtos
        stage_fields_dict = self._get_stage_fields_dict(fields_dto)
        stage_actions_dict = self._get_stage_actions_dict(actions_dto)
        column_fields_dict, column_actions_dict = \
            self._get_column_fields_and_actions_dicts(
                column_stage_dtos, stage_actions_dict, stage_fields_dict
            )

        column_dtos = task_board_details.columns_dtos
        return [
            {
                "column_id": column_dto.column_id,
                "column_name": column_dto.name,
                "actions": self._get_column_actions(
                    column_actions_dict[column_dto.column_id]
                ),
                "fields": self._get_column_fields(
                    column_fields_dict[column_dto.column_id]
                )
            }
            for column_dto in column_dtos
        ]

    @staticmethod
    def _get_column_fields_and_actions_dicts(
            column_stage_dtos: List[ColumnStageDTO],
            stage_actions_dict: Dict[str, List[ActionDTO]],
            stage_fields_dict: Dict[str, List[FieldDisplayDTO]]
    ):
        column_fields_dict = {}
        column_actions_dict = {}

        for column_stage_dto in column_stage_dtos:
            column_id = column_stage_dto.column_id
            stage_id = column_stage_dto.stage_id
            column_fields_dict[column_id] = stage_fields_dict[stage_id]
            column_actions_dict[column_id] = stage_actions_dict[stage_id]
        return column_fields_dict, column_actions_dict

    @staticmethod
    def _get_stage_fields_dict(fields_dto: List[FieldDisplayDTO]):

        from collections import defaultdict
        stage_fields_dict = defaultdict(list)
        for field_dto in fields_dto:
            stage_id = field_dto.stage_id
            stage_fields_dict[stage_id].append(field_dto)
        return stage_fields_dict

    @staticmethod
    def _get_stage_actions_dict(actions_dto: List[ActionDTO]):

        from collections import defaultdict
        stage_actions_dict = defaultdict(list)
        for action_dto in actions_dto:
            stage_id = action_dto.stage_id
            stage_actions_dict[stage_id].append(action_dto)
        return stage_actions_dict

    @staticmethod
    def _get_column_actions(actions_dto: List[ActionDTO]):

        return [
            {
                "action_id": str(action_dto.action_id),
                "name": action_dto.name,
                "button_text": action_dto.button_text,
                "button_color": action_dto.button_color
            }
            for action_dto in actions_dto
        ]

    @staticmethod
    def _get_column_fields(fields_dto: List[FieldDisplayDTO]):

        return [
            {
                "field_type": field_dto.field_type,
                "key": field_dto.key,
                "value": field_dto.value
            }
            for field_dto in fields_dto
        ]
