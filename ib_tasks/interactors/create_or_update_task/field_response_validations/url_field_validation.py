from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import InvalidURLValue
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO


class URLFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(
            self,
            field_id_with_display_name_dtos: List[FieldWithGoFDisplayNameDTO]
    ) -> Optional[InvalidURLValue]:
        from ib_tasks.constants.config import VALID_URL_REGEX_PATTERN
        url_is_invalid = not VALID_URL_REGEX_PATTERN.search(
            self.field_response)
        if url_is_invalid:
            field_display_name = self.get_field_display_name(
                self.field_id, field_id_with_display_name_dtos)
            raise InvalidURLValue(field_display_name, self.field_response)
        return
