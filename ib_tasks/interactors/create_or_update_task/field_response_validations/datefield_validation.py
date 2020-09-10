import datetime
from typing import Optional

from ib_tasks.constants.config import DATE_FORMAT
from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidDateFormat
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation


class DateFieldValidationInteractor(BaseFieldValidation):

    def __init__(self, field_id: str, field_response: str):
        self.field_id = field_id
        self.field_response = field_response

    def validate_field_response(self) -> Optional[InvalidDateFormat]:
        try:
            self._validate_date_string(self.field_response)
        except ValueError:
            raise InvalidDateFormat(
                self.field_id, self.field_response, DATE_FORMAT
            )
        return

    @staticmethod
    def _validate_date_string(field_response):
        datetime.datetime.strptime(field_response, DATE_FORMAT).date()
        split_field_response = field_response.split('-')
        year_does_not_have_zeroes_padded = False
        month_does_not_have_zeroes_padded = False
        date_does_not_have_zeroes_padded = False
        if len(split_field_response[0]) != 4:
            year_does_not_have_zeroes_padded = True
        if len(split_field_response[1]) != 2:
            month_does_not_have_zeroes_padded = True
        if len(split_field_response[2]) != 2:
            date_does_not_have_zeroes_padded = True

        if year_does_not_have_zeroes_padded or \
                month_does_not_have_zeroes_padded or \
                date_does_not_have_zeroes_padded:
            raise ValueError
