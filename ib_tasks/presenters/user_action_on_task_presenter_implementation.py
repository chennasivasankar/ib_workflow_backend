from typing import List, Dict

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO, ColumnStageDTO
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserActionPermissionDenied, UserBoardPermissionDenied
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException
from ib_tasks.interactors.gofs_dtos import FieldDisplayDTO
from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO
from ib_tasks.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO
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

    def raise_exception_for_invalid_present_actions(self, error_obj):
        pass

    def raise_exception_for_user_board_permission_denied(
            self, error_obj: UserBoardPermissionDenied):
        from ib_tasks.constants.exception_messages import \
            USER_DO_NOT_HAVE_BOARD_ACCESS

        response_message = USER_DO_NOT_HAVE_BOARD_ACCESS[0].format(
            str(error_obj.board_id)
        )
        response_dict = {
            "response": response_message,
            "http_status_code": 403,
            "res_status": USER_DO_NOT_HAVE_BOARD_ACCESS[1]
        }

        response_object = self.prepare_403_forbidden_response(response_dict)
        return response_object

    def get_response_for_user_action_on_task(
            self, task_complete_details_dto: TaskCompleteDetailsDTO,
            task_current_stage_details_dto: TaskCurrentStageDetailsDTO
    ):

        task_id = task_complete_details_dto.task_id
        is_board_id_none = not task_complete_details_dto.task_boards_details
        if is_board_id_none:
            current_board_details = {}
        else:
            current_board_details = \
                self._get_current_board_details(task_complete_details_dto)

        response_dict = {
            "task_id": str(task_id),
            "current_board_details": current_board_details,
            "other_board_details": [],
            "task_current_stages_details": dict()
        }
        task_current_stages_data = {
            "task_id": task_current_stage_details_dto.task_display_id,
            "stages": [],
            "user_has_permission":
                task_current_stage_details_dto.user_has_permission
        }
        for stage_dto in task_current_stage_details_dto.stage_details_dtos:
            stage = {
                "stage_id": stage_dto.stage_id,
                "stage_display_name": stage_dto.stage_display_name
            }
            task_current_stages_data['stages'].append(stage)
        response_dict["task_current_stages_details"] = task_current_stages_data
        response_object = self.prepare_200_success_response(response_dict)
        return response_object

    def _get_current_board_details(
            self, task_complete_details_dto: TaskCompleteDetailsDTO):
        actions_dto = task_complete_details_dto.actions_dto
        fields_dto = task_complete_details_dto.field_dtos
        task_board_details = task_complete_details_dto.task_boards_details
        board_dto = task_board_details.board_dto

        return {
            "board_id": board_dto.board_id,
            "board_name": board_dto.name,
            "column_details": self._get_column_details(
                actions_dto, fields_dto, task_board_details
            )
        }

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
        from collections import defaultdict
        column_fields_dict = defaultdict(lambda: list())
        column_actions_dict = defaultdict(lambda: list())

        for column_stage_dto in column_stage_dtos:
            column_id = column_stage_dto.column_id
            stage_id = column_stage_dto.stage_id
            column_fields_dict[column_id] += stage_fields_dict[stage_id]
            column_actions_dict[column_id] += stage_actions_dict[stage_id]
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

    def raise_invalid_key_error(self):
        from ib_tasks.constants.exception_messages import \
            INVALID_KEY_ERROR
        data = {
            "response": INVALID_KEY_ERROR[0],
            "http_status_code": 400,
            "res_status": INVALID_KEY_ERROR[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_custom_logic_function_exception(self):
        from ib_tasks.constants.exception_messages import \
            INVALID_CUSTOM_LOGIC
        data = {
            "response": INVALID_CUSTOM_LOGIC[0],
            "http_status_code": 400,
            "res_status": INVALID_CUSTOM_LOGIC[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_path_not_found_exception(self, path_name):
        from ib_tasks.constants.exception_messages import \
            PATH_NOT_FOUND
        data = {
            "response": PATH_NOT_FOUND[0],
            "http_status_code": 400,
            "res_status": PATH_NOT_FOUND[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_method_not_found_exception(self, method_name):
        from ib_tasks.constants.exception_messages import \
            METHOD_NOT_FOUND
        data = {
            "response": METHOD_NOT_FOUND[0],
            "http_status_code": 400,
            "res_status": METHOD_NOT_FOUND[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_duplicate_stage_ids_not_valid(self, duplicate_stage_ids):
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_STAGE_IDS
        data = {
            "response": DUPLICATE_STAGE_IDS[0].format(duplicate_stage_ids),
            "http_status_code": 400,
            "res_status": DUPLICATE_STAGE_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_stage_ids_exception(self, invalid_stage_ids):
        from ib_tasks.constants.exception_messages import \
            INVALID_STAGE_IDS
        data = {
            "response": INVALID_STAGE_IDS[0].format(invalid_stage_ids),
            "http_status_code": 400,
            "res_status": INVALID_STAGE_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_stage_ids_with_invalid_permission_for_assignee_exception(
            self, invalid_stage_ids):
        from ib_tasks.constants.exception_messages import \
            STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE
        data = {
            "response": STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE[
                0].format(invalid_stage_ids),
            "http_status_code": 400,
            "res_status": STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE[1]
        }
        return self.prepare_400_bad_request_response(data)
