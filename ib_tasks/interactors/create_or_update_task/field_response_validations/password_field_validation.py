from typing import Optional

from ib_tasks.exceptions.field_values_custom_exceptions import \
    NotAStrongPassword
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class PasswordFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(self) -> Optional[NotAStrongPassword]:
        import re
        from ib_tasks.constants.config import STRONG_PASSWORD_REGEX
        password_is_not_strong_enough = not re.search(
            STRONG_PASSWORD_REGEX, self.field_response
        )
        if password_is_not_strong_enough:
            raise NotAStrongPassword(self.field_id, self.field_response)
        return
