from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import \
    IncorrectNameInGoFSelectorField
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO


class GoFSelectorFieldValidationInteractor(BaseFieldValidation):

    def __init__(
            self, field_id: str, field_response: str,
            valid_gof_selector_names: List[str]):
        self.field_id = field_id
        self.field_response = field_response
        self.valid_gof_selector_names = valid_gof_selector_names

    def validate_field_response(
            self,
            field_id_with_display_name_dtos: List[FieldWithGoFDisplayNameDTO]
    ) -> Optional[IncorrectNameInGoFSelectorField]:
        invalid_gof_option = \
            self.field_response not in self.valid_gof_selector_names
        if invalid_gof_option:
            field_display_name = self.get_field_display_name(
                self.field_id, field_id_with_display_name_dtos)
            raise IncorrectNameInGoFSelectorField(
                field_display_name, self.field_response,
                self.valid_gof_selector_names)
        return
