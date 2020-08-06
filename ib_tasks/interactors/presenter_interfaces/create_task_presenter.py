import abc


class CreateTaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_create_task_response(self):
        pass

    @abc.abstractmethod
    def raise_invalid_task_template_ids(self, err):
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