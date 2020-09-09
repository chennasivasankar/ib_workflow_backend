import datetime
from typing import Optional

from ib_tasks.constants.config import TIME_FORMAT
from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidTimeFormat
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class TimeFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(self) -> Optional[InvalidTimeFormat]:
        try:
            self._validate_time_string(self.field_response)
        except ValueError:
            raise InvalidTimeFormat(
                self.field_id, self.field_response, TIME_FORMAT
            )
        return

    @staticmethod
    def _validate_time_string(field_response):
        datetime.datetime.strptime(field_response, TIME_FORMAT).time()
        split_field_response = field_response.split(':')
        hours_does_not_have_zeroes_padded = False
        minutes_does_not_have_zeroes_padded = False
        seconds_does_not_have_zeroes_padded = False
        if len(split_field_response[0]) != 2:
            hours_does_not_have_zeroes_padded = True
        if len(split_field_response[1]) != 2:
            minutes_does_not_have_zeroes_padded = True
        if len(split_field_response[2]) != 2:
            seconds_does_not_have_zeroes_padded = True
        if hours_does_not_have_zeroes_padded or \
                minutes_does_not_have_zeroes_padded or \
                seconds_does_not_have_zeroes_padded:
            raise ValueError
