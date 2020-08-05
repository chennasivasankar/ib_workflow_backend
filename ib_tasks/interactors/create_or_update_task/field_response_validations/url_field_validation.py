from typing import Optional

from ib_tasks.exceptions.field_values_custom_exceptions import InvalidURLValue
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class URLFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(self) -> Optional[InvalidURLValue]:
        from ib_tasks.constants.config import VALID_URL_REGEX_PATTERN
        url_is_invalid = not VALID_URL_REGEX_PATTERN.search(
            self.field_response)
        if url_is_invalid:
            raise InvalidURLValue(self.field_id, self.field_response)
        return
