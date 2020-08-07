from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import \
    IncorrectMultiSelectOptionsSelected
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class MultiSelectFieldValidationInteractor(BaseFieldValidation):

    def __init__(
            self, field_id: str, field_response: str,
            valid_multi_select_options: List[str]
    ):
        self.field_id = field_id
        self.field_response = field_response
        self.valid_multi_select_options = valid_multi_select_options

    def validate_field_response(
            self) -> Optional[IncorrectMultiSelectOptionsSelected]:
        import json
        selected_multi_select_options = json.loads(self.field_response)
        invalid_multi_select_options = list(
            set(selected_multi_select_options) - set(
                self.valid_multi_select_options)
        )
        if invalid_multi_select_options:
            raise IncorrectMultiSelectOptionsSelected(
                self.field_id, invalid_multi_select_options,
                self.valid_multi_select_options
            )
        return
