from typing import List, Union

from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidUrlForImage, InvalidImageFormat
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO


class ImageUploaderFieldValidationInteractor(BaseFieldValidation):

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
    ) -> Union[None, InvalidUrlForImage, InvalidImageFormat]:
        from ib_tasks.constants.config import VALID_URL_REGEX_PATTERN
        invalid_url_path = \
            not VALID_URL_REGEX_PATTERN.search(self.field_response)
        try:
            image_file = self.field_response[
                         self.field_response.rindex("/") + 1:]
        except ValueError:
            raise InvalidUrlForImage(self.field_id, self.field_response)
        image_file_is_empty = not image_file
        field_display_name = self.get_field_display_name(
            self.field_id, field_id_with_display_name_dtos)
        if invalid_url_path or image_file_is_empty:
            raise InvalidUrlForImage(field_display_name, self.field_response)
        given_image_format = '.' + image_file.split('.')[-1]
        given_image_format_not_in_allowed_formats = \
            given_image_format not in self.allowed_formats
        if given_image_format_not_in_allowed_formats:
            raise InvalidImageFormat(
                field_display_name, given_image_format, self.allowed_formats)
        return
