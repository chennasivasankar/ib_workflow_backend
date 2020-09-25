from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import \
    IncorrectMultiSelectLabelsSelected
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO


class MultiSelectLabelFieldValidationInteractor(BaseFieldValidation):

    def __init__(
            self, field_id: str, field_response: str,
            valid_multi_select_labels: List[str]
    ):
        self.field_id = field_id
        self.field_response = field_response
        self.valid_multi_select_labels = valid_multi_select_labels

    def validate_field_response(
            self,
            field_id_with_display_name_dtos: List[FieldWithGoFDisplayNameDTO]
    ) -> Optional[IncorrectMultiSelectLabelsSelected]:
        import json
        selected_multi_select_labels = json.loads(self.field_response)
        invalid_multi_select_labels = sorted(list(
            set(selected_multi_select_labels) - set(
                self.valid_multi_select_labels)
        ))
        if invalid_multi_select_labels:
            field_display_name = self.get_field_display_name(
                self.field_id, field_id_with_display_name_dtos)
            raise IncorrectMultiSelectLabelsSelected(
                field_display_name, invalid_multi_select_labels,
                self.valid_multi_select_labels)
        return
