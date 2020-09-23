from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidEmailFieldValue
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO


class EmailFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(
            self,
            field_id_with_display_name_dtos: List[FieldWithGoFDisplayNameDTO]
    ) -> Optional[InvalidEmailFieldValue]:
        import re
        from ib_tasks.constants.config import VALID_EMAIL_REGEX
        email_address_is_invalid = not re.search(VALID_EMAIL_REGEX,
                                                 self.field_response)
        if email_address_is_invalid:
            field_display_name = self.get_field_display_name(
                self.field_id, field_id_with_display_name_dtos)
            raise InvalidEmailFieldValue(
                field_display_name, self.field_response)
        return
