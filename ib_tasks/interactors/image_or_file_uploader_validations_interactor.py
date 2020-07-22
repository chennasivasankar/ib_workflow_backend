import collections
import json

from ib_tasks.interactors.storage_interfaces.dtos \
    import FieldDTO


class ImageOrFileUploaderValidationsInteractor:

    def image_or_file_uploader_validations(self, field_dto: FieldDTO):
        self._check_allowed_formats_is_empty_value_for_field_dto(
            field_dto
        )
        self._check_for_empty_values_in_allowed_formats_for_field_dto(field_dto)
        self._check_for_duplication_of_allowed_formats_for_field_dto(field_dto)
        allowed_formats = field_dto.allowed_formats
        field_dto.allowed_formats = json.dumps(allowed_formats)

    @staticmethod
    def _check_allowed_formats_is_empty_value_for_field_dto(
             field_dto: FieldDTO
    ):
        from ib_tasks.exceptions.fields_custom_exceptions \
            import AllowedFormatsEmptyValueException
        from ib_tasks.constants.exception_messages \
            import ALLOWED_FORMAT_EMPTY_VALUES_EXCEPTION
        is_allowed_formats_empty = not field_dto.allowed_formats
        if is_allowed_formats_empty:
            raise AllowedFormatsEmptyValueException(
                ALLOWED_FORMAT_EMPTY_VALUES_EXCEPTION.format(field_dto.field_id)
            )
        return

    @staticmethod
    def _check_for_duplication_of_allowed_formats_for_field_dto(field_dto):
        from ib_tasks.exceptions.fields_custom_exceptions \
            import FieldsDuplicationOfAllowedFormatsValues
        from ib_tasks.constants.exception_messages \
            import FIELD_DUPLICATION_OF_ALLOWED_FORMATS

        allowed_formats_values = field_dto.allowed_formats
        duplication_of_values = [
            allowed_formats_value
            for allowed_formats_value, count in collections.Counter(allowed_formats_values).items()
            if count > 1
        ]
        if duplication_of_values:
            exception_message = {
                "field_id": field_dto.field_id,
                "field_type": field_dto.field_type,
                "duplication_of_values": duplication_of_values
            }
            raise FieldsDuplicationOfAllowedFormatsValues(
                FIELD_DUPLICATION_OF_ALLOWED_FORMATS.format(exception_message)
            )
        return

    @staticmethod
    def _check_for_empty_values_in_allowed_formats_for_field_dto(field_dto):
        from ib_tasks.exceptions.fields_custom_exceptions import EmptyValuesForAllowedFormats
        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUES_FOR_ALLOWED_FORMATS

        allowed_formats_values = field_dto.allowed_formats
        for allowed_formats_value in allowed_formats_values:
            is_allowed_formats_value_empty = not allowed_formats_value.strip()
            if is_allowed_formats_value_empty:
                raise EmptyValuesForAllowedFormats(
                    EMPTY_VALUES_FOR_ALLOWED_FORMATS.format(field_dto.field_id)
                )
        return
