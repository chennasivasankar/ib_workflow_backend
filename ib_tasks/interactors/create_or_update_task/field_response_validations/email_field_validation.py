from typing import Optional

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidEmailFieldValue
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class EmailFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(self) -> Optional[InvalidEmailFieldValue]:
        import re
        from ib_tasks.constants.config import VALID_EMAIL_REGEX
        email_address_is_invalid = not re.search(VALID_EMAIL_REGEX,
                                                 self.field_response)
        if email_address_is_invalid:
            raise InvalidEmailFieldValue(self.field_id, self.field_response)
        return
