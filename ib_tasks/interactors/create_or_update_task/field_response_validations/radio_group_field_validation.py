from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import \
    IncorrectRadioGroupChoice
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO


class RadioGroupFieldValidationInteractor(BaseFieldValidation):

    def __init__(
            self, field_id: str, field_response: str,
            valid_radio_group_options: List[str]
    ):
        self.field_id = field_id
        self.field_response = field_response
        self.valid_radio_group_options = valid_radio_group_options

    def validate_field_response(
            self,
            field_id_with_display_name_dtos: List[FieldWithGoFDisplayNameDTO]
    ) -> Optional[IncorrectRadioGroupChoice]:
        invalid_radio_group_choice = \
            self.field_response not in self.valid_radio_group_options
        if invalid_radio_group_choice:
            field_display_name = self.get_field_display_name(
                self.field_id, field_id_with_display_name_dtos)
            raise IncorrectRadioGroupChoice(
                field_display_name, self.field_response,
                self.valid_radio_group_options)
        return
