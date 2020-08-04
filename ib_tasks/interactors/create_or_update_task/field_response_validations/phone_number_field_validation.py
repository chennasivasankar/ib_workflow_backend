from typing import Optional

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidPhoneNumberValue
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class PhoneNumberFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(self) -> Optional[InvalidPhoneNumberValue]:
        phone_number_has_non_digit_chars = not self.field_response.isdigit()
        if phone_number_has_non_digit_chars:
            raise InvalidPhoneNumberValue(
                self.field_id, self.field_response)
        phone_number_does_not_contain_10_digits = \
            len(self.field_response) != 10
        if phone_number_does_not_contain_10_digits:
            raise InvalidPhoneNumberValue(
                self.field_id, self.field_response)
        return
