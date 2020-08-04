import abc


class FieldResponseValidationsPresenter(abc.ABC):

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
