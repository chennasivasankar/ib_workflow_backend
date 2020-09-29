from typing import List, Union

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidUrlForFile, InvalidFileFormat
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO


class FileUploaderFieldValidationInteractor(BaseFieldValidation):

    def __init__(
            self, field_id: str, field_response: str,
            allowed_formats: List[str]
    ):
        self.field_id = field_id
        self.field_response = field_response
        self.allowed_formats = allowed_formats

    def validate_field_response(
            self,
            field_id_with_display_name_dtos: List[FieldWithGoFDisplayNameDTO]
    ) -> Union[None, InvalidUrlForFile, InvalidFileFormat]:
        from ib_tasks.constants.config import VALID_URL_REGEX_PATTERN
        invalid_url_path = \
            not VALID_URL_REGEX_PATTERN.search(self.field_response)
        field_display_name = self.get_field_display_name(
            self.field_id, field_id_with_display_name_dtos)
        try:
            file = self.field_response[self.field_response.rindex("/") + 1:]
        except ValueError:
            raise InvalidUrlForFile(field_display_name, self.field_response)
        file_is_empty = not file
        if invalid_url_path or file_is_empty:
            raise InvalidUrlForFile(field_display_name, self.field_response)
        given_file_format = '.' + file.split('.')[-1]
        invalid_file_format = given_file_format not in self.allowed_formats
        if invalid_file_format:
            raise InvalidFileFormat(
                field_display_name, given_file_format, self.allowed_formats)
        return
