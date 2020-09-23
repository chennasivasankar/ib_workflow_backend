from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.custom_exceptions import InvalidProjectId, \
    InvalidModulePathFound, InvalidMethodFound
from ib_tasks.exceptions.datetime_custom_exceptions import \
    StartDateIsAheadOfDueDate, \
    DueTimeHasExpiredForToday, DueDateTimeHasExpired, DueDateTimeIsRequired, \
    StartDateTimeIsRequired, DueDateTimeWithoutStartDateTimeIsNotValid
from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidDateFormat
from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF, UserDidNotFillRequiredGoFs, \
    InvalidStagePermittedGoFs
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserBoardPermissionDenied, UserActionPermissionDenied
from ib_tasks.exceptions.stage_custom_exceptions import \
    InvalidStageIdsListException, StageIdsListEmptyException, \
    DuplicateStageIds, InvalidDbStageIdsListException, \
    StageIdsWithInvalidPermissionForAssignee
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskTemplateDBId, \
    PriorityIsRequired, InvalidTaskJson, InvalidTaskDisplayId
from ib_tasks.interactors.presenter_interfaces.create_sub_task_presenter import \
    CreateSubTaskPresenterInterface
from ib_tasks.presenters.mixins.gofs_fields_validation_presenter_mixin import \
    GoFsFieldsValidationPresenterMixin


class CreateSubTaskPresenterImplementation(
    CreateSubTaskPresenterInterface, HTTPResponseMixin,
    GoFsFieldsValidationPresenterMixin
):

    def raise_invalid_parent_task_id(self, err: InvalidTaskDisplayId):
        from ib_tasks.constants.exception_messages import \
            INVALID_PARENT_TASK_ID
        message = INVALID_PARENT_TASK_ID[0].format(err.task_display_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_PARENT_TASK_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_gof_ids(self, err):
        return self.raise_invalid_gof_ids_exception(err)

    def raise_invalid_field_ids(self, err):
        return self.raise_invalid_field_ids_exception(err)

    def raise_invalid_gofs_given_to_a_task_template(self, err):
        return self.raise_invalid_gofs_given_to_a_task_template_exception(err)

    def raise_duplicate_field_ids_to_a_gof(self, err):
        return self.raise_duplicate_field_ids_to_a_gof_exception(err)

    def raise_invalid_fields_given_to_a_gof(self, err):
        return self.raise_invalid_fields_given_to_a_gof_exception(err)

    def raise_invalid_stage_permitted_gofs(
            self, err: InvalidStagePermittedGoFs):
        return self.raise_invalid_stage_permitted_gofs_exception(err)

    def raise_user_needs_gof_writable_permission(self, err):
        return self.raise_user_needs_gof_writable_permission_exception(err)

    def raise_user_needs_field_writable_permission(self, err):
        return self.raise_user_needs_field_writable_permission_exception(err)

    def raise_empty_value_in_required_field(self, err):
        return self.raise_empty_value_in_required_field_exception(err)

    def raise_invalid_phone_number_value(self, err):
        return self.raise_invalid_phone_number_value_exception(err)

    def raise_invalid_email_address(self, err):
        return self.raise_invalid_email_address_exception(err)

    def raise_invalid_url_address(self, err):
        return self.raise_invalid_url_address_exception(err)

    def raise_weak_password(self, err):
        return self.raise_weak_password_exception(err)

    def raise_invalid_number_value(self, err):
        return self.raise_invalid_number_value_exception(err)

    def raise_invalid_float_value(self, err):
        return self.raise_invalid_float_value_exception(err)

    def raise_invalid_dropdown_value(self, err):
        return self.raise_invalid_dropdown_value_exception(err)

    def raise_invalid_name_in_gof_selector(self, err):
        return self.raise_invalid_name_in_gof_selector_exception(err)

    def raise_invalid_choice_in_radio_group_field(self, err):
        return self.raise_invalid_choice_in_radio_group_field_exception(err)

    def raise_invalid_checkbox_group_options_selected(self, err):
        return self.raise_invalid_checkbox_group_options_exception(err)

    def raise_invalid_multi_select_options_selected(self, err):
        return self.raise_invalid_multi_select_options_selected_exception(err)

    def raise_invalid_multi_select_labels_selected(self, err):
        return self.raise_invalid_multi_select_labels_selected_exception(err)

    def raise_invalid_date_format(self, err: InvalidDateFormat):
        return self.raise_invalid_date_format_exception(err)

    def raise_invalid_time_format(self, err):
        return self.raise_invalid_time_format_exception(err)

    def raise_invalid_image_url(self, err):
        return self.raise_invalid_image_url_exception(err)

    def raise_not_acceptable_image_format(self, err):
        return self.raise_not_acceptable_image_format_exception(err)

    def raise_invalid_file_url(self, err):
        return self.raise_invalid_file_url_exception(err)

    def raise_not_acceptable_file_format(self, err):
        return self.raise_not_acceptable_file_format_exception(err)

    def raise_invalid_project_id(self, err: InvalidProjectId):
        from ib_tasks.constants.exception_messages import INVALID_PROJECT_ID
        message = INVALID_PROJECT_ID[0].format(err.project_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_PROJECT_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_task_json(self, err: InvalidTaskJson):
        from ib_tasks.constants.exception_messages import INVALID_TASK_JSON
        data = {
            "response": INVALID_TASK_JSON[0],
            "http_status_code": 400,
            "res_status": INVALID_TASK_JSON[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_user_did_not_fill_required_fields(
            self, err: UserDidNotFillRequiredFields):
        from ib_tasks.constants.exception_messages import \
            USER_DID_NOT_FILL_REQUIRED_FIELDS
        field_display_names = [
            dto.field_display_name for dto in err.unfilled_field_dtos]
        message = USER_DID_NOT_FILL_REQUIRED_FIELDS[0].format(
            field_display_names)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": USER_DID_NOT_FILL_REQUIRED_FIELDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_user_did_not_fill_required_gofs(
            self, err: UserDidNotFillRequiredGoFs):
        from ib_tasks.constants.exception_messages import \
            USER_DID_NOT_FILL_REQUIRED_GOFS
        message = USER_DID_NOT_FILL_REQUIRED_GOFS[0].format(
            err.gof_display_names)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": USER_DID_NOT_FILL_REQUIRED_GOFS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_priority_is_required(self, err: PriorityIsRequired):
        from ib_tasks.constants.exception_messages import \
            PRIORITY_IS_REQUIRED
        data = {
            "response": PRIORITY_IS_REQUIRED[0],
            "http_status_code": 400,
            "res_status": PRIORITY_IS_REQUIRED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_due_date_time_without_start_datetime(
            self, err: DueDateTimeWithoutStartDateTimeIsNotValid):
        from ib_tasks.constants.exception_messages import \
            DUE_DATE_TIME_WITHOUT_START_DATE_TIME
        message = DUE_DATE_TIME_WITHOUT_START_DATE_TIME[0].format(
            err.due_datetime)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": DUE_DATE_TIME_WITHOUT_START_DATE_TIME[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_start_date_time_is_required(self, err: StartDateTimeIsRequired):
        from ib_tasks.constants.exception_messages import \
            START_DATE_TIME_IS_REQUIRED
        data = {
            "response": START_DATE_TIME_IS_REQUIRED[0],
            "http_status_code": 400,
            "res_status": START_DATE_TIME_IS_REQUIRED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_due_date_time_is_required(self, err: DueDateTimeIsRequired):
        from ib_tasks.constants.exception_messages import \
            DUE_DATE_TIME_IS_REQUIRED
        data = {
            "response": DUE_DATE_TIME_IS_REQUIRED[0],
            "http_status_code": 400,
            "res_status": DUE_DATE_TIME_IS_REQUIRED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_due_date_time_has_expired(self, err: DueDateTimeHasExpired):
        from ib_tasks.constants.exception_messages import \
            DUE_DATE_TIME_HAS_EXPIRED
        message = DUE_DATE_TIME_HAS_EXPIRED[0].format(err.due_datetime)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": DUE_DATE_TIME_HAS_EXPIRED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_stage_ids_list_empty(
            self, err: StageIdsListEmptyException):
        from ib_tasks.constants.exception_messages import \
            EMPTY_STAGE_IDS_ARE_INVALID
        data = {
            "response": EMPTY_STAGE_IDS_ARE_INVALID[0],
            "http_status_code": 400,
            "res_status": EMPTY_STAGE_IDS_ARE_INVALID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_stage_ids_list(self,
                                     err: InvalidStageIdsListException):
        from ib_tasks.constants.exception_messages import INVALID_STAGE_IDS
        message = INVALID_STAGE_IDS[0].format(err.invalid_stage_ids)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_STAGE_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_task_template_of_project(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_PROJECT_TEMPLATE
        message = INVALID_PROJECT_TEMPLATE[0].format(err.template_id,
                                                     err.project_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_PROJECT_TEMPLATE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_present_stage_actions(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_PRESENT_STAGE_ACTION
        message = INVALID_PRESENT_STAGE_ACTION[0].format(err.action_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_PRESENT_STAGE_ACTION[1]
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

    def raise_invalid_key_error(self):
        from ib_tasks.constants.exception_messages import \
            INVALID_KEY_ERROR
        data = {
            "response": INVALID_KEY_ERROR[0],
            "http_status_code": 400,
            "res_status": INVALID_KEY_ERROR[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_custom_logic_function(self):
        from ib_tasks.constants.exception_messages import \
            INVALID_CUSTOM_LOGIC
        data = {
            "response": INVALID_CUSTOM_LOGIC[0],
            "http_status_code": 400,
            "res_status": INVALID_CUSTOM_LOGIC[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_path_not_found(self, err: InvalidModulePathFound):
        from ib_tasks.constants.exception_messages import \
            PATH_NOT_FOUND
        data = {
            "response": PATH_NOT_FOUND[0],
            "http_status_code": 400,
            "res_status": PATH_NOT_FOUND[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_method_not_found(self, err: InvalidMethodFound):
        from ib_tasks.constants.exception_messages import \
            METHOD_NOT_FOUND
        data = {
            "response": METHOD_NOT_FOUND[0],
            "http_status_code": 400,
            "res_status": METHOD_NOT_FOUND[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_duplicate_stage_ids_not_valid(self, err: DuplicateStageIds):
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_STAGE_IDS
        data = {
            "response": DUPLICATE_STAGE_IDS[0].format(err.duplicate_stage_ids),
            "http_status_code": 400,
            "res_status": DUPLICATE_STAGE_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_stage_ids(self, err: InvalidDbStageIdsListException):
        from ib_tasks.constants.exception_messages import \
            INVALID_STAGE_IDS
        data = {
            "response": INVALID_STAGE_IDS[0].format(err.invalid_stage_ids),
            "http_status_code": 400,
            "res_status": INVALID_STAGE_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_stage_assignees(
            self, err: StageIdsWithInvalidPermissionForAssignee
    ):
        from ib_tasks.constants.exception_messages import \
            STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE
        message = STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE[0].format(
            err.invalid_stage_ids)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_duplicate_same_gof_orders_for_a_gof(
            self, err: DuplicateSameGoFOrderForAGoF
    ):
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

    def get_create_sub_task_response(self):
        data = {
            "response": "Sub task created Successfully"
        }
        return self.prepare_201_created_response(response_dict=data)

    def raise_invalid_task_template_id(self, err: InvalidTaskTemplateDBId):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_TEMPLATE_DB_ID
        response_message = INVALID_TASK_TEMPLATE_DB_ID[0].format(
            err.task_template_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_TEMPLATE_DB_ID[1]
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

    def raise_user_action_permission_denied(
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