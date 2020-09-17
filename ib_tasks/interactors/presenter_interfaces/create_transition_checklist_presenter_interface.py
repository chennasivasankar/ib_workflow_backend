import abc

from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.gofs_custom_exceptions import \
    UserDidNotFillRequiredGoFs


class CreateOrUpdateTransitionChecklistPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_create_transition_checklist_response(self):
        pass

    @abc.abstractmethod
    def raise_invalid_task_id(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_transition_checklist_template_id(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_action(self, err):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_id(self, err):
        pass

    @abc.abstractmethod
    def raise_same_gof_order_for_a_gof(self, err):
        pass

    @abc.abstractmethod
    def raise_transition_template_is_not_linked_to_action(self,
                                                          err):
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
    def raise_invalid_date_format(self, err):
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
    def raise_invalid_task_display_id(self, err):
        pass

    @abc.abstractmethod
    def raise_user_did_not_fill_required_gofs(self,
                                              err: UserDidNotFillRequiredGoFs):
        pass

    @abc.abstractmethod
    def raise_user_did_not_fill_required_fields(
            self, err: UserDidNotFillRequiredFields):
        pass
