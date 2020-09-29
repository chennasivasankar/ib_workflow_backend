from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidPhoneNumberValue
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO


class PhoneNumberFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(
            self,
            field_id_with_display_name_dtos: List[FieldWithGoFDisplayNameDTO]
    ) -> Optional[InvalidPhoneNumberValue]:
        phone_number_has_non_digit_chars = not self.field_response.isdigit()
        field_display_name = self.get_field_display_name(
            self.field_id, field_id_with_display_name_dtos)
        if phone_number_has_non_digit_chars:
            raise InvalidPhoneNumberValue(
                field_display_name, self.field_response)
        phone_number_does_not_contain_10_digits = \
            len(self.field_response) != 10
        if phone_number_does_not_contain_10_digits:
            raise InvalidPhoneNumberValue(
                field_display_name, self.field_response)
        return
