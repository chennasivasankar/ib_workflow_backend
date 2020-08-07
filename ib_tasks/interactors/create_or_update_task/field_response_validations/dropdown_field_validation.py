from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidValueForDropdownField
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class DropDownFieldValidationInteractor(BaseFieldValidation):

    def __init__(
            self, field_id: str, field_response: str,
            valid_dropdown_values: List[str]
    ):
        self.field_id = field_id
        self.field_response = field_response
        self.valid_dropdown_values = valid_dropdown_values

    def validate_field_response(
            self
    ) -> Optional[InvalidValueForDropdownField]:
        invalid_dropdown_value = \
            self.field_response not in self.valid_dropdown_values
        if invalid_dropdown_value:
            raise InvalidValueForDropdownField(
                self.field_id, self.field_response, self.valid_dropdown_values
            )
        return
