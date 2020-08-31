from typing import List, Dict, Optional

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.adapters.dtos import ColumnStageDTO, AssigneeDetailsDTO
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserActionPermissionDenied, UserBoardPermissionDenied
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException
from ib_tasks.interactors.gofs_dtos import FieldDisplayDTO
from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO, AllTasksOverviewDetailsDTO
from ib_tasks.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_tasks.interactors.stage_dtos import TaskStageDTO, \
    TaskStageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO
from ib_tasks.interactors.user_action_on_task_interactor import \
    InvalidBoardIdException


class UserActionOnTaskPresenterImplementation(PresenterInterface,
                                              HTTPResponseMixin):

    def raise_invalid_task_display_id(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_DISPLAY_ID
        message = INVALID_TASK_DISPLAY_ID[0].format(err.task_display_id)
        data = {
            "response": message,
            "http_status_code": 404,
            "res_status": INVALID_TASK_DISPLAY_ID[1]
        }
        return self.prepare_404_not_found_response(data)

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
        from ib_tasks.constants.exception_messages import \
            INVALID_PRESENT_STAGE_ACTION
        message = INVALID_PRESENT_STAGE_ACTION[0].format(
            str(error_obj.action_id))
        data = {
            "response": message,
            "http_status_code": 403,
            "res_status": INVALID_PRESENT_STAGE_ACTION[1]
        }
        return self.prepare_403_forbidden_response(data)

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
            task_current_stage_details_dto: TaskCurrentStageDetailsDTO,
            all_tasks_overview_dto: AllTasksOverviewDetailsDTO
    ):

        is_board_id_none = not task_complete_details_dto.task_boards_details
        if is_board_id_none:
            current_board_details = None
        else:
            current_board_details = \
                self._get_current_board_details(task_complete_details_dto)

        response_dict = {
            "task_id": task_current_stage_details_dto.task_display_id,
            "current_board_details": current_board_details,
            "other_board_details": [],
            "task_current_stages_details": dict(),
            "task_details": None
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
        task_overview_details_dict = \
            self._prepare_task_overview_details_dict(all_tasks_overview_dto)
        response_dict['task_details'] = task_overview_details_dict
        response_object = self.prepare_200_success_response(response_dict)
        return response_object

    def _prepare_task_overview_details_dict(
            self, all_tasks_overview_dto: AllTasksOverviewDetailsDTO
    ):
        task_stages_has_no_actions = \
            not all_tasks_overview_dto.task_with_complete_stage_details_dtos
        if task_stages_has_no_actions:
            return None
        complete_task_stage_details_dto = \
            all_tasks_overview_dto.task_with_complete_stage_details_dtos[0]
        task_fields_action_details_dtos = \
            all_tasks_overview_dto.task_fields_and_action_details_dtos
        task_stage_details_dto = \
            complete_task_stage_details_dto.task_with_stage_details_dto
        task_overview_fields_details, actions_details = \
            self.task_fields_and_actions_details(
                task_stage_details_dto.task_id, task_fields_action_details_dtos
            )
        assignee = self._get_assignee_details(
            complete_task_stage_details_dto.stage_assignee_dto)
        task_overview_details_dict = {
            "task_id": task_stage_details_dto.task_display_id,
            "task_overview_fields": task_overview_fields_details,
            "stage_with_actions": {
                "stage_id":
                    task_stage_details_dto.db_stage_id,
                "stage_display_name":
                    task_stage_details_dto.stage_display_name,
                "stage_color":
                    task_stage_details_dto.stage_color,
                "assignee": assignee,
                "actions": actions_details
            }
        }
        return task_overview_details_dict

    @staticmethod
    def _get_assignee_details(
            stage_assignee_dto: List[TaskStageAssigneeDetailsDTO]
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

    def task_fields_and_actions_details(
            self, given_task_id: int,
            task_fields_and_action_details_dtos: List[
                GetTaskStageCompleteDetailsDTO]):
        for each_task_fields_and_action_details_dto in \
                task_fields_and_action_details_dtos:
            if given_task_id == \
                    each_task_fields_and_action_details_dto.task_id:
                task_overview_fields_details = self. \
                    _get_task_overview_fields_details(
                    each_task_fields_and_action_details_dto)
                action_details = self._get_actions_details_of_task_stage(
                    each_task_fields_and_action_details_dto)
                return task_overview_fields_details, action_details
        return [], []

    @staticmethod
    def _get_task_overview_fields_details(
            each_task_fields_and_action_details_dto):
        task_overview_fields_details = [
            {
                "field_type": each_field_dto.field_type,
                "field_display_name": each_field_dto.key,
                "field_response": each_field_dto.value
            } for each_field_dto in
            each_task_fields_and_action_details_dto.field_dtos
        ]
        return task_overview_fields_details

    @staticmethod
    def _get_actions_details_of_task_stage(
            each_task_fields_and_action_details_dto):
        action_details = [{
            "action_id": each_action_dto.action_id,
            "button_text": each_action_dto.button_text,
            "button_color": each_action_dto.button_color,
            "action_type": each_action_dto.action_type,
            "transition_template_id": each_action_dto.transition_template_id
        } for each_action_dto in
            each_task_fields_and_action_details_dto.action_dtos]
        return action_details

    def _get_current_board_details(
            self, task_complete_details_dto: TaskCompleteDetailsDTO):
        task_board_details = task_complete_details_dto.task_boards_details
        board_dto = task_board_details.board_dto
        return {
            "board_id": board_dto.board_id,
            "board_name": board_dto.name,
            "column_details": self._get_column_details(
                task_complete_details_dto=task_complete_details_dto
            )
        }

    def _get_column_details(self,
                            task_complete_details_dto: TaskCompleteDetailsDTO):
        actions_dto = task_complete_details_dto.actions_dto
        fields_dto = task_complete_details_dto.field_dtos
        task_board_details = task_complete_details_dto.task_boards_details
        task_stage_dtos = task_complete_details_dto.task_stage_details
        assignee_dtos = task_complete_details_dto.assignees_details
        column_stage_dtos = task_board_details.column_stage_dtos
        stage_fields_dict = self._get_stage_fields_dict(fields_dto)
        stage_actions_dict = self._get_stage_actions_dict(actions_dto)
        column_fields_dict, column_actions_dict = \
            self._get_column_fields_and_actions_dicts(
                column_stage_dtos, stage_actions_dict, stage_fields_dict
            )

        assignees_dict, task_stages_dict = \
            self._get_stage_details_and_assignees_details_dict(
            column_stage_dtos, assignee_dtos, task_stage_dtos
        )

        column_dtos = task_board_details.columns_dtos
        return [
            {
                "column_id": column_dto.column_id,
                "column_name": column_dto.name,
                "stage_with_actions": self._get_stages_with_column_actions(
                    column_actions_dict[column_dto.column_id],
                    assignees_dict[column_dto.column_id],
                    task_stages_dict[column_dto.column_id]
                ),
                "task_overview_fields": self._get_column_fields(
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

    def _get_stages_with_column_actions(
            self, actions_dto: List[ActionDTO],
            assignee_dto: AssigneeDetailsDTO, task_stage_dto: TaskStageDTO):

        return {
            "stage_id": task_stage_dto.db_stage_id,
            "stage_display_name": task_stage_dto.display_name,
            "stage_color": task_stage_dto.stage_colour,
            "assignee": self._get_assignee_details_dict(assignee_dto),
            "actions": self._get_actions_dict(actions_dto)
        }

    @staticmethod
    def _get_assignee_details_dict(assignee_dto: AssigneeDetailsDTO):

        if assignee_dto:
            return {
                "assignee_id": assignee_dto.assignee_id,
                "name": assignee_dto.name,
                "profile_pic_url": assignee_dto.profile_pic_url
            }

    @staticmethod
    def _get_actions_dict(actions_dto: List[ActionDTO]):
        return [
            {
                "action_id": str(action_dto.action_id),
                "name": action_dto.name,
                "action_type": action_dto.action_type,
                "transition_template_id": action_dto.transition_template_id,
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
                "field_display_name": field_dto.key,
                "field_response": field_dto.value
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

    @staticmethod
    def _get_stage_details_and_assignees_details_dict(
            column_stage_dtos: List[ColumnStageDTO],
            assignee_dtos: List[TaskStageAssigneeDetailsDTO],
            task_stage_dtos: List[TaskStageDTO]):

        assignee_dtos_dict = {}
        for assignee_dto in assignee_dtos:
            assignee_dtos_dict[
                assignee_dto.stage_id] = assignee_dto.assignee_details

        task_stages_dict = {}
        for task_stage_dto in task_stage_dtos:
            task_stages_dict[task_stage_dto.stage_id] = task_stage_dto

        assignees_dict = {}
        task_stages_dtos_dict = {}
        for column_stage_dto in column_stage_dtos:
            column_id = column_stage_dto.column_id
            stage_id = column_stage_dto.stage_id
            try:
                assignees_dict[column_id] = assignee_dtos_dict[stage_id]
            except KeyError:
                assignees_dict[column_id] = None
            task_stages_dtos_dict[column_id] = task_stages_dict[stage_id]
        return assignees_dict, task_stages_dtos_dict
