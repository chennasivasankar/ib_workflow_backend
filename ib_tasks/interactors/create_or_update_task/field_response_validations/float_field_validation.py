from typing import Optional

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidFloatValue
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class FloatFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(self) -> Optional[InvalidFloatValue]:
        invalid_float_value = not self.field_response.replace('.', '',
                                                              1).isdigit()
        if invalid_float_value:
            raise InvalidFloatValue(self.field_id, self.field_response)
        return
