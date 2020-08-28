from typing import List, Optional, Dict

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.datetime_custom_exceptions import \
    InvalidDueTimeFormat, StartDateIsAheadOfDueDate, \
    DueDateIsBehindStartDate, \
    DueTimeHasExpiredForToday, DueDateHasExpired
from ib_tasks.exceptions.field_values_custom_exceptions import \
    EmptyValueForRequiredField, InvalidPhoneNumberValue, \
    InvalidEmailFieldValue, InvalidURLValue, NotAStrongPassword, \
    InvalidNumberValue, InvalidFloatValue, InvalidValueForDropdownField, \
    IncorrectNameInGoFSelectorField, IncorrectRadioGroupChoice, \
    IncorrectCheckBoxOptionsSelected, IncorrectMultiSelectOptionsSelected, \
    IncorrectMultiSelectLabelsSelected, InvalidDateFormat, InvalidTimeFormat, \
    InvalidUrlForImage, InvalidImageFormat, InvalidUrlForFile, \
    InvalidFileFormat
from ib_tasks.exceptions.fields_custom_exceptions import InvalidFieldIds, \
    DuplicateFieldIdsToGoF
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission, \
    UserBoardPermissionDenied, UserActionPermissionDenied
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsWithInvalidPermissionForAssignee, InvalidStageId
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskTemplateIds, \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.presenter_interfaces \
    .save_and_act_on_task_presenter_interface import \
    SaveAndActOnATaskPresenterInterface
from ib_tasks.interactors.stage_dtos import TaskStageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO


class SaveAndActOnATaskPresenterImplementation(
    SaveAndActOnATaskPresenterInterface, HTTPResponseMixin
):

    def raise_duplicate_same_gof_orders_for_a_gof(self, err):
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF
        response_message = DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF[0].format(
            err.gof_id, err.same_gof_orders
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_stage_id(self, err: InvalidStageId):
        from ib_tasks.constants.exception_messages import INVALID_STAGE_ID
        message = INVALID_STAGE_ID[0].format(err.stage_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_STAGE_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_due_date_has_expired(self, err: DueDateHasExpired):
        from ib_tasks.constants.exception_messages import \
            DUE_DATE_HAS_EXPIRED
        message = DUE_DATE_HAS_EXPIRED[0].format(err.due_date)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": DUE_DATE_HAS_EXPIRED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_task_display_id(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_DISPLAY_ID
        message = INVALID_TASK_DISPLAY_ID[0].format(err.task_display_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_DISPLAY_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

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

    def raise_exception_for_invalid_present_stage_actions(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_PRESENT_STAGE_ACTION
        message = INVALID_PRESENT_STAGE_ACTION[0].format(err.action_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_PRESENT_STAGE_ACTION[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_due_time_format(self, err: InvalidDueTimeFormat):
        from ib_tasks.constants.exception_messages import \
            INVALID_DUE_TIME_FORMAT
        message = INVALID_DUE_TIME_FORMAT[0].format(err.due_time)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_DUE_TIME_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_start_date_is_ahead_of_due_date(self,
                                              err: StartDateIsAheadOfDueDate):
        from ib_tasks.constants.exception_messages import \
            START_DATE_IS_AHEAD_OF_DUE_DATE
        message = START_DATE_IS_AHEAD_OF_DUE_DATE[0].format(
            str(err.given_start_date), str(err.given_due_date)
        )
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": START_DATE_IS_AHEAD_OF_DUE_DATE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_due_time_has_expired_for_today(self,
                                             err: DueTimeHasExpiredForToday):
        from ib_tasks.constants.exception_messages import \
            DUE_TIME_HAS_EXPIRED_FOR_TODAY
        message = DUE_TIME_HAS_EXPIRED_FOR_TODAY[0].format(err.due_time)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": DUE_TIME_HAS_EXPIRED_FOR_TODAY[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_stage_ids_with_invalid_permission_for_assignee_exception(
            self, err: StageIdsWithInvalidPermissionForAssignee
    ):
        from ib_tasks.constants.exception_messages import \
            STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE
        response_dict = {
            "response": STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE[0].
                format(err.invalid_stage_ids),
            "http_status_code": 400,
            "res_status": STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE[1]
        }
        response_object = self.prepare_400_bad_request_response(response_dict)
        return response_object

    def get_save_and_act_on_task_response(
            self, task_current_stage_details_dto: TaskCurrentStageDetailsDTO,
            all_tasks_overview_dto: AllTasksOverviewDetailsDTO
    ):
        data = {
            "task_current_stages_details": {
                "task_id": task_current_stage_details_dto.task_display_id,
                "stages": [],
                "user_has_permission":
                    task_current_stage_details_dto.user_has_permission
            },
            "task_details": None
        }
        for stage_dto in task_current_stage_details_dto.stage_details_dtos:
            stage = {
                "stage_id": stage_dto.stage_id,
                "stage_display_name": stage_dto.stage_display_name
            }
            data['task_current_stages_details']['stages'].append(stage)
        task_overview_details_dict = \
            self._prepare_task_overview_details_dict(all_tasks_overview_dto)
        data['task_details'] = task_overview_details_dict
        return self.prepare_200_success_response(response_dict=data)

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

    def raise_invalid_task_id(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_ID
        response_message = INVALID_TASK_ID[0].format(
            err.task_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_action_id(self, err: InvalidActionException):
        from ib_tasks.constants.exception_messages import INVALID_ACTION_ID
        response_message = INVALID_ACTION_ID[0].format(err.action_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_ACTION_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_task_template_ids(self, err: InvalidTaskTemplateIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_TEMPLATE_IDS
        response_message = INVALID_TASK_TEMPLATE_IDS[0].format(
            err.invalid_task_template_ids
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_TEMPLATE_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_gof_ids(self, err: InvalidGoFIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_GOF_IDS
        response_message = INVALID_GOF_IDS[0].format(str(err.gof_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_GOF_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_field_ids(self, err: InvalidFieldIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_FIELD_IDS
        response_message = INVALID_FIELD_IDS[0].format(str(err.field_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FIELD_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_gofs_given_to_a_task_template(
            self, err: InvalidGoFsOfTaskTemplate
    ):
        from ib_tasks.constants.exception_messages import \
            INVALID_GOFS_OF_TASK_TEMPLATE
        response_message = INVALID_GOFS_OF_TASK_TEMPLATE[0].format(
            str(err.gof_ids), err.task_template_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_GOFS_OF_TASK_TEMPLATE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_duplicate_field_ids_to_a_gof(self, err: DuplicateFieldIdsToGoF):
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF
        response_message = DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF[0].format(
            err.gof_id, str(err.field_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_fields_given_to_a_gof(self, err: InvalidFieldsOfGoF):
        from ib_tasks.constants.exception_messages import \
            INVALID_FIELDS_OF_GOF
        response_message = INVALID_FIELDS_OF_GOF[0].format(
            str(err.field_ids), err.gof_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FIELDS_OF_GOF[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_user_needs_gof_writable_permission(
            self, err: UserNeedsGoFWritablePermission):
        from ib_tasks.constants.exception_messages import \
            USER_NEEDS_GOF_WRITABLE_PERMISSION
        response_message = USER_NEEDS_GOF_WRITABLE_PERMISSION[0].format(
            err.user_id, err.gof_id, str(err.required_roles))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": USER_NEEDS_GOF_WRITABLE_PERMISSION[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_user_needs_field_writable_permission(
            self, err: UserNeedsFieldWritablePermission
    ):
        from ib_tasks.constants.exception_messages import \
            USER_NEEDS_FILED_WRITABLE_PERMISSION
        response_message = USER_NEEDS_FILED_WRITABLE_PERMISSION[0].format(
            err.user_id, err.field_id, str(err.required_roles))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": USER_NEEDS_FILED_WRITABLE_PERMISSION[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_empty_value_in_required_field(
            self, err: EmptyValueForRequiredField):
        from ib_tasks.constants.exception_messages import \
            EMPTY_VALUE_FOR_REQUIRED_FIELD
        response_message = EMPTY_VALUE_FOR_REQUIRED_FIELD[0].format(
            err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": EMPTY_VALUE_FOR_REQUIRED_FIELD[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_phone_number_value(
            self, err: InvalidPhoneNumberValue):
        from ib_tasks.constants.exception_messages import \
            INVALID_PHONE_NUMBER_VALUE
        response_message = INVALID_PHONE_NUMBER_VALUE[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_PHONE_NUMBER_VALUE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_email_address(self,
                                                  err: InvalidEmailFieldValue):
        from ib_tasks.constants.exception_messages import \
            INVALID_EMAIL
        response_message = INVALID_EMAIL[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_EMAIL[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_url_address(self, err: InvalidURLValue):
        from ib_tasks.constants.exception_messages import INVALID_URL
        response_message = INVALID_URL[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_URL[1]
        }
        return self.prepare_400_bad_request_response(response_dict=data)

    def raise_exception_for_weak_password(self, err: NotAStrongPassword):
        from ib_tasks.constants.exception_messages import NOT_A_STRONG_PASSWORD
        response_message = NOT_A_STRONG_PASSWORD[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": NOT_A_STRONG_PASSWORD[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_number_value(self,
                                                 err: InvalidNumberValue):
        from ib_tasks.constants.exception_messages import INVALID_NUMBER_VALUE
        response_message = INVALID_NUMBER_VALUE[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_NUMBER_VALUE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_float_value(self, err: InvalidFloatValue):
        from ib_tasks.constants.exception_messages import INVALID_FLOAT_VALUE
        response_message = INVALID_FLOAT_VALUE[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FLOAT_VALUE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_dropdown_value(
            self, err: InvalidValueForDropdownField):
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_DROPDOWN
        response_message = INVALID_VALUE_FOR_DROPDOWN[0].format(
            err.field_value, err.field_id, err.valid_values
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_VALUE_FOR_DROPDOWN[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_name_in_gof_selector_field_value(
            self, err: IncorrectNameInGoFSelectorField):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_NAME_IN_GOF_SELECTOR_FIELD
        response_message = INCORRECT_NAME_IN_GOF_SELECTOR_FIELD[0].format(
            err.field_value, err.field_id, err.valid_gof_selector_names
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_NAME_IN_GOF_SELECTOR_FIELD[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_choice_in_radio_group_field(
            self, err: IncorrectRadioGroupChoice):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_RADIO_GROUP_CHOICE
        response_message = INCORRECT_RADIO_GROUP_CHOICE[0].format(
            err.field_value, err.field_id, err.valid_radio_group_options
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_RADIO_GROUP_CHOICE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_checkbox_group_options_selected(
            self, err: IncorrectCheckBoxOptionsSelected):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_CHECK_BOX_OPTIONS_SELECTED
        response_message = INCORRECT_CHECK_BOX_OPTIONS_SELECTED[0].format(
            err.invalid_checkbox_options, err.field_id,
            err.valid_check_box_options
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_CHECK_BOX_OPTIONS_SELECTED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_multi_select_options_selected(
            self, err: IncorrectMultiSelectOptionsSelected):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_MULTI_SELECT_OPTIONS_SELECTED
        response_message = INCORRECT_MULTI_SELECT_OPTIONS_SELECTED[0].format(
            err.invalid_multi_select_options, err.field_id,
            err.valid_multi_select_options
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_MULTI_SELECT_OPTIONS_SELECTED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_multi_select_labels_selected(
            self, err: IncorrectMultiSelectLabelsSelected):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_MULTI_SELECT_LABELS_SELECTED
        response_message = INCORRECT_MULTI_SELECT_LABELS_SELECTED[0].format(
            err.invalid_multi_select_labels, err.field_id,
            err.valid_multi_select_labels
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_MULTI_SELECT_LABELS_SELECTED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_date_format(self, err: InvalidDateFormat):
        from ib_tasks.constants.exception_messages import INVALID_DATE_FORMAT
        response_message = INVALID_DATE_FORMAT[0].format(
            err.field_value, err.field_id, err.expected_format
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_DATE_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_time_format(self, err: InvalidTimeFormat):
        from ib_tasks.constants.exception_messages import INVALID_TIME_FORMAT
        response_message = INVALID_TIME_FORMAT[0].format(
            err.field_value, err.field_id, err.expected_format
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_TIME_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_image_url(self, err: InvalidUrlForImage):
        from ib_tasks.constants.exception_messages import INVALID_IMAGE_URL
        response_message = INVALID_IMAGE_URL[0].format(
            err.image_url, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_IMAGE_URL[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_not_acceptable_image_format(
            self, err: InvalidImageFormat):
        from ib_tasks.constants.exception_messages import INVALID_IMAGE_FORMAT
        response_message = INVALID_IMAGE_FORMAT[0].format(
            err.given_format, err.field_id, err.allowed_formats
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_IMAGE_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_file_url(self, err: InvalidUrlForFile):
        from ib_tasks.constants.exception_messages import INVALID_FILE_URL
        response_message = INVALID_FILE_URL[0].format(
            err.file_url, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FILE_URL[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_not_acceptable_file_format(self,
                                                       err: InvalidFileFormat):
        from ib_tasks.constants.exception_messages import \
            INVALID_FILE_FORMAT
        response_message = INVALID_FILE_FORMAT[0].format(
            err.given_format, err.field_id, err.allowed_formats
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FILE_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(data)

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
