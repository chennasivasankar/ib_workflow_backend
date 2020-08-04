from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import \
    IncorrectNameInGoFSelectorField
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class GoFSelectorFieldValidationInteractor(BaseFieldValidation):

    def __init__(
            self, field_id: str, field_response: str,
            valid_gof_selector_names: List[str]
    ):
        self.field_id = field_id
        self.field_response = field_response
        self.valid_gof_selector_names = valid_gof_selector_names

    def validate_field_response(
            self) -> Optional[IncorrectNameInGoFSelectorField]:
        invalid_gof_option = \
            self.field_response not in self.valid_gof_selector_names
        if invalid_gof_option:
            raise IncorrectNameInGoFSelectorField(
                self.field_id, self.field_response,
                self.valid_gof_selector_names
            )
        return
