import abc

from ib_tasks.exceptions.custom_exceptions import InvalidProjectId, \
    InvalidModulePathFound, InvalidMethodFound
from ib_tasks.exceptions.datetime_custom_exceptions import \
    DueDateTimeHasExpired, DueDateTimeWithoutStartDateTimeIsNotValid, \
    StartDateTimeIsRequired, DueDateTimeIsRequired
from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidDateFormat
from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.gofs_custom_exceptions import \
    UserDidNotFillRequiredGoFs, InvalidStagePermittedGoFs
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsListEmptyException, InvalidStageIdsListException, \
    DuplicateStageIds, InvalidDbStageIdsListException, \
    StageIdsWithInvalidPermissionForAssignee
from ib_tasks.exceptions.task_custom_exceptions import PriorityIsRequired, \
    InvalidTaskJson, InvalidTaskDisplayId
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO


class CreateSubTaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_create_sub_task_response(self):
        pass

    @abc.abstractmethod
    def raise_invalid_task_template_id(self, err):
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
    def raise_empty_value_in_required_field(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_phone_number_value(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_email_address(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_url_address(self, err):
        pass

    @abc.abstractmethod
    def raise_weak_password(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_number_value(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_float_value(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_dropdown_value(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_name_in_gof_selector(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_choice_in_radio_group_field(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_checkbox_group_options_selected(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_multi_select_options_selected(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_multi_select_labels_selected(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_date_format(self, err: InvalidDateFormat):
        pass

    @abc.abstractmethod
    def raise_invalid_time_format(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_image_url(self, err):
        pass

    @abc.abstractmethod
    def raise_not_acceptable_image_format(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_file_url(self, err):
        pass

    @abc.abstractmethod
    def raise_not_acceptable_file_format(self, err):
        pass

    @abc.abstractmethod
    def raise_user_action_permission_denied(self, error_obj):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_board_permission_denied(self, error_obj):
        pass

    @abc.abstractmethod
    def raise_duplicate_same_gof_orders_for_a_gof(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_key_error(self):
        pass

    @abc.abstractmethod
    def raise_invalid_custom_logic_function(self):
        pass

    @abc.abstractmethod
    def raise_invalid_path_not_found(self, err: InvalidModulePathFound):
        pass

    @abc.abstractmethod
    def raise_invalid_method_not_found(self, err: InvalidMethodFound):
        pass

    @abc.abstractmethod
    def raise_duplicate_stage_ids_not_valid(self, err: DuplicateStageIds):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_ids(self, err: InvalidDbStageIdsListException):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_assignees(
            self, err: StageIdsWithInvalidPermissionForAssignee):
        pass

    @abc.abstractmethod
    def raise_start_date_is_ahead_of_due_date(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_present_stage_actions(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_task_template_of_project(self, err):
        pass

    @abc.abstractmethod
    def raise_stage_ids_list_empty(
            self, err: StageIdsListEmptyException):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_ids_list(
            self, err: InvalidStageIdsListException):
        pass

    @abc.abstractmethod
    def raise_due_date_time_without_start_datetime(
            self, err: DueDateTimeWithoutStartDateTimeIsNotValid):
        pass

    @abc.abstractmethod
    def raise_start_date_time_is_required(self, err: StartDateTimeIsRequired):
        pass

    @abc.abstractmethod
    def raise_due_date_time_is_required(self, err: DueDateTimeIsRequired):
        pass

    @abc.abstractmethod
    def raise_due_date_time_has_expired(self, err: DueDateTimeHasExpired):
        pass

    @abc.abstractmethod
    def raise_priority_is_required(self, err: PriorityIsRequired):
        pass

    @abc.abstractmethod
    def raise_user_did_not_fill_required_gofs(
            self, err: UserDidNotFillRequiredGoFs):
        pass

    @abc.abstractmethod
    def raise_user_did_not_fill_required_fields(
            self, err: UserDidNotFillRequiredFields):
        pass

    @abc.abstractmethod
    def raise_invalid_task_json(self, err: InvalidTaskJson):
        pass

    @abc.abstractmethod
    def raise_invalid_project_id(self, err: InvalidProjectId):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_permitted_gofs(self,
                                           err: InvalidStagePermittedGoFs):
        pass

    @abc.abstractmethod
    def raise_invalid_parent_task_id(self, err: InvalidTaskDisplayId):
        pass