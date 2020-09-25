from typing import Optional, List

from ib_tasks.exceptions.field_values_custom_exceptions import \
    NotAStrongPassword
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO


class PasswordFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(
            self,
            field_id_with_display_name_dtos: List[FieldWithGoFDisplayNameDTO]
    ) -> Optional[NotAStrongPassword]:
        import re
        from ib_tasks.constants.config import STRONG_PASSWORD_REGEX
        password_is_not_strong_enough = not re.search(
            STRONG_PASSWORD_REGEX, self.field_response)
        if password_is_not_strong_enough:
            field_display_name = self.get_field_display_name(
                self.field_id, field_id_with_display_name_dtos)
            raise NotAStrongPassword(field_display_name, self.field_response)
        return
