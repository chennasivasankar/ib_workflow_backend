from typing import Optional

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidTimeFormat
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class TimeFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(self) -> Optional[InvalidTimeFormat]:
        import datetime
        from ib_tasks.constants.config import TIME_FORMAT
        try:
            datetime.datetime.strptime(self.field_response, TIME_FORMAT).time()
        except ValueError:
            raise InvalidTimeFormat(
                self.field_id, self.field_response, TIME_FORMAT
            )
        return
