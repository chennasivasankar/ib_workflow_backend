import abc

from ib_tasks.exceptions.datetime_custom_exceptions import DueDateHasExpired
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsWithInvalidPermissionForAssignee, InvalidStageId
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO


class SaveAndActOnATaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_save_and_act_on_task_response(self,
                                          task_current_stage_details_dto:
                                          TaskCurrentStageDetailsDTO):
        pass

    @abc.abstractmethod
    def raise_invalid_task_id(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_action_id(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_gof_ids(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_field_ids(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_gofs_given_to_a_task_template(self, err):
        pass

    @abc.abstractmethod
    def raise_duplicate_field_ids_to_a_gof(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_fields_given_to_a_gof(self, err):
        pass

    @abc.abstractmethod
    def raise_user_needs_gof_writable_permission(self, err):
        pass

    @abc.abstractmethod
    def raise_user_needs_field_writable_permission(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_empty_value_in_required_field(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_phone_number_value(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_email_address(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_url_address(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_weak_password(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_number_value(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_float_value(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_dropdown_value(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_name_in_gof_selector_field_value(self,
                                                                     err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_choice_in_radio_group_field(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_checkbox_group_options_selected(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_multi_select_options_selected(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_multi_select_labels_selected(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_date_format(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_time_format(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_image_url(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_not_acceptable_image_format(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_file_url(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_not_acceptable_file_format(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_action_permission_denied(self, error_obj):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_board_permission_denied(self, error_obj):
        pass

    @abc.abstractmethod
    def raise_stage_ids_with_invalid_permission_for_assignee_exception(
            self, err: StageIdsWithInvalidPermissionForAssignee
    ):
        pass

    @abc.abstractmethod
    def raise_invalid_due_time_format(self, err):
        pass

    @abc.abstractmethod
    def raise_start_date_is_ahead_of_due_date(self, err):
        pass

    @abc.abstractmethod
    def raise_due_date_is_behind_start_date(self, err):
        pass

    @abc.abstractmethod
    def raise_due_time_has_expired_for_today(self, err):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_present_actions(self, error_obj):
        pass

    @abc.abstractmethod
    def raise_invalid_key_error(self):
        pass

    @abc.abstractmethod
    def raise_invalid_custom_logic_function_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_path_not_found_exception(self, path_name):
        pass

    @abc.abstractmethod
    def raise_invalid_method_not_found_exception(self, method_name):
        pass

    @abc.abstractmethod
    def raise_duplicate_stage_ids_not_valid(self, duplicate_stage_ids):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_ids_exception(self, invalid_stage_ids):
        pass

    @abc.abstractmethod
    def raise_invalid_task_display_id(self, err):
        pass

    @abc.abstractmethod
    def raise_due_date_has_expired(self, err: DueDateHasExpired):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_id(self, err: InvalidStageId):
        pass
