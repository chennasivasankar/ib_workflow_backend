from typing import List, Optional, Dict

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.exceptions.datetime_custom_exceptions import \
    StartDateIsAheadOfDueDate, \
    DueDateTimeHasExpired, DueDateTimeIsRequired, \
    StartDateTimeIsRequired, DueDateTimeWithoutStartDateTimeIsNotValid
from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidDateFormat
from ib_tasks.exceptions.gofs_custom_exceptions import \
    InvalidStagePermittedGoFs
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsWithInvalidPermissionForAssignee, InvalidStageId, \
    InvalidStageIdsListException, StageIdsListEmptyException
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskTemplateIds, \
    InvalidTaskDisplayId, \
    TaskDelayReasonIsNotUpdated, PriorityIsRequired
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.presenter_interfaces.update_task_presenter import \
    UpdateTaskPresenterInterface
from ib_tasks.interactors.stage_dtos import TaskStageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO
from ib_tasks.presenters.mixins.gofs_fields_validation_presenter_mixin import \
    GoFsFieldsValidationPresenterMixin


class UpdateTaskPresenterImplementation(
    UpdateTaskPresenterInterface, HTTPResponseMixin,
    GoFsFieldsValidationPresenterMixin
):
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

    def raise_task_delay_reason_not_updated(self,
                                            err: TaskDelayReasonIsNotUpdated):
        from ib_tasks.constants.exception_messages import \
            TASK_DELAY_REASON_NOT_UPDATED
        message = TASK_DELAY_REASON_NOT_UPDATED[0].format(
            err.due_date, err.task_display_id, err.stage_display_name)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": TASK_DELAY_REASON_NOT_UPDATED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_stage_ids_list_empty_exception(self,
                                             err: StageIdsListEmptyException):
        from ib_tasks.constants.exception_messages import \
            EMPTY_STAGE_IDS_ARE_INVALID
        data = {
            "response": EMPTY_STAGE_IDS_ARE_INVALID[0],
            "http_status_code": 400,
            "res_status": EMPTY_STAGE_IDS_ARE_INVALID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_stage_ids_list_exception(self,
                                               err:
                                               InvalidStageIdsListException):
        from ib_tasks.constants.exception_messages import INVALID_STAGE_IDS
        message = INVALID_STAGE_IDS[0].format(err.invalid_stage_ids)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_STAGE_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

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

    def raise_invalid_task_display_id(self, err: InvalidTaskDisplayId):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_DISPLAY_ID
        message = INVALID_TASK_DISPLAY_ID[0].format(err.task_display_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_DISPLAY_ID[1]
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

    def raise_invalid_stage_assignees(
            self, err: StageIdsWithInvalidPermissionForAssignee):
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

    def get_update_task_response(
            self, all_tasks_overview_details_dto: AllTasksOverviewDetailsDTO):
        task_overview_details_dict = \
            self._prepare_task_overview_details_dict(
                all_tasks_overview_details_dto)
        data = {
            "task_details": task_overview_details_dict
        }
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
                task_overview_fields_details = \
                    self._get_task_overview_fields_details(
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
