import pytest

from ib_tasks.tests.factories.storage_dtos import \
    FieldDTOFactory
from ib_tasks.constants.enum import FieldTypes
from ib_tasks.interactors.image_or_file_uploader_validations_interactor \
    import ImageOrFileUploaderValidationsInteractor


class TestImageOrFileUploaderValidationsInteractor:

    @pytest.mark.parametrize("field_type", [FieldTypes.IMAGE_UPLOADER, FieldTypes.FILE_UPLOADER.value])
    def test_given_empty_values_for_allowed_format_raise_exception(self, field_type):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions \
            import AllowedFormatsEmptyValueException
        from ib_tasks.constants.exception_messages \
            import ALLOWED_FORMAT_EMPTY_VALUES_EXCEPTION

        field_dto = FieldDTOFactory(field_id="field1", field_type=field_type, allowed_formats=[])
        field_id = "field1"
        exception_mesaage = ALLOWED_FORMAT_EMPTY_VALUES_EXCEPTION.format(field_id)
        interactor = ImageOrFileUploaderValidationsInteractor()

        # Act
        with pytest.raises(AllowedFormatsEmptyValueException) as err:
            interactor.image_or_file_uploader_validations(field_dto)

        # Assert
        assert str(err.value) == exception_mesaage

    def test_given_duplication_of_allowed_formats_for_field_type_image_uploder_raise_exception(self):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions \
            import FieldsDuplicationOfAllowedFormatsValues
        from ib_tasks.constants.exception_messages \
            import FIELD_DUPLICATION_OF_ALLOWED_FORMATS

        field_dto = FieldDTOFactory(
            field_id="field1",
            field_type=FieldTypes.IMAGE_UPLOADER.value,
            allowed_formats=[".jpg", ".jpg", ".mpeg"]
        )
        duplication_of_values = [".jpg"]
        duplication_of_values_dict = {
            "field_id": "field1",
            "field_type": FieldTypes.IMAGE_UPLOADER.value,
            "duplication_of_values": duplication_of_values
        }
        exception_message = FIELD_DUPLICATION_OF_ALLOWED_FORMATS.format(duplication_of_values_dict)
        interactor = ImageOrFileUploaderValidationsInteractor()

        # Act
        with pytest.raises(FieldsDuplicationOfAllowedFormatsValues) as err:
            interactor.image_or_file_uploader_validations(field_dto)

        # Assert
        assert str(err.value) == exception_message

    def test_given_duplication_of_allowed_formats_for_field_type_file_uploader_raise_exception(self):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions \
            import FieldsDuplicationOfAllowedFormatsValues
        from ib_tasks.constants.exception_messages \
            import FIELD_DUPLICATION_OF_ALLOWED_FORMATS

        field_dto = FieldDTOFactory(
            field_id="field1",
            field_type=FieldTypes.FILE_UPLOADER.value,
            allowed_formats=[".pdf", ".pdf"]
        )
        duplication_of_values = [".pdf"]
        duplication_of_values_dict = {
            "field_id": "field1",
            "field_type": FieldTypes.FILE_UPLOADER.value,
            "duplication_of_values": duplication_of_values
        }
        exception_message = FIELD_DUPLICATION_OF_ALLOWED_FORMATS.format(duplication_of_values_dict)
        interactor = ImageOrFileUploaderValidationsInteractor()

        # Act
        with pytest.raises(FieldsDuplicationOfAllowedFormatsValues) as err:
            interactor.image_or_file_uploader_validations(field_dto)

        # Assert
        assert str(err.value) == exception_message

    @pytest.mark.parametrize("field_type", [FieldTypes.IMAGE_UPLOADER, FieldTypes.FILE_UPLOADER.value])
    def test_given_empty_values_for_allowed_formats_raise_exception(self, field_type):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions \
            import EmptyValuesForAllowedFormats
        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUES_FOR_ALLOWED_FORMATS

        field_dto = FieldDTOFactory(
            field_id="field1",
            field_type=field_type,
            allowed_formats=[".pdf", "  "]
        )
        field_id = "field1"
        exception_message = EMPTY_VALUES_FOR_ALLOWED_FORMATS.format(field_id)
        interactor = ImageOrFileUploaderValidationsInteractor()

        # Act
        with pytest.raises(EmptyValuesForAllowedFormats) as err:
            interactor.image_or_file_uploader_validations(field_dto)

        # Assert
        assert str(err.value) == exception_message




