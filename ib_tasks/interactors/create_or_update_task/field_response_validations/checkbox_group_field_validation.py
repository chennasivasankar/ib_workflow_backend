from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import \
    IncorrectCheckBoxOptionsSelected
from ib_tasks.interactors.create_or_update_task.field_response_validations.\
    base_field_validation import BaseFieldValidation


class CheckBoxGroupFieldValidationInteractor(BaseFieldValidation):

    def __init__(
            self, field_id: str, field_response: str,
            valid_check_box_options: List[str]
    ):
        self.field_id = field_id
        self.field_response = field_response
        self.valid_check_box_options = valid_check_box_options

    def validate_field_response(
            self) -> Optional[IncorrectCheckBoxOptionsSelected]:
        import json
        selected_check_box_options = json.loads(self.field_response)
        invalid_checkbox_options = sorted(list(
            set(selected_check_box_options) - set(self.valid_check_box_options)
        ))
        if invalid_checkbox_options:
            raise IncorrectCheckBoxOptionsSelected(
                self.field_id, invalid_checkbox_options,
                self.valid_check_box_options
            )
        return
