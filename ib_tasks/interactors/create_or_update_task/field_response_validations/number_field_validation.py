from typing import Optional

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidNumberValue
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class NumberFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(self) -> Optional[InvalidNumberValue]:
        invalid_number_value = not self.field_response.isdigit()
        if invalid_number_value:
            raise InvalidNumberValue(self.field_id, self.field_response)
        return
