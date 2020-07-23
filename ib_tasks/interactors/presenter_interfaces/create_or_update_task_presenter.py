import abc

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidPhoneNumberValue, EmptyValueForPlainTextField, \
    InvalidEmailFieldValue, InvalidURLValue, NotAStrongPassword, \
    InvalidNumberValue, InvalidFloatValue, InvalidValueForDropdownField, \
    InvalidGoFIDsInGoFSelectorField
from ib_tasks.exceptions.fields_custom_exceptions import \
    DuplicationOfFieldIdsExist, InvalidFieldIds
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds


class CreateOrUpdateTaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_duplicate_field_ids(self, err: DuplicationOfFieldIdsExist):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_task_template_id(
            self, err: InvalidTaskTemplateIds
    ):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_gof_ids(
        self, err: InvalidGoFIds
    ):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_field_ids(
            self, err: InvalidFieldIds
    ):
        pass

    @abc.abstractmethod
    def get_response_for_create_or_update_task(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_gof_ids_in_gof_selector_field_value(
            self, err: InvalidGoFIDsInGoFSelectorField
    ):
        pass

    @abc.abstractmethod
    def raise_exception_for_empty_value_in_plain_text_field(
            self, err: EmptyValueForPlainTextField
    ):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_phone_number_value(self, err: InvalidPhoneNumberValue):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_email_address(self, err: InvalidEmailFieldValue):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_url_address(self, err: InvalidURLValue):
        pass

    @abc.abstractmethod
    def raise_exception_for_weak_password(self, err: NotAStrongPassword):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_number_value(self, err: InvalidNumberValue):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_float_value(self, err: InvalidFloatValue):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_dropdown_value(
            self, err: InvalidValueForDropdownField
    ):
        pass
