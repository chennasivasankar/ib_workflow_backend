import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    ImageUploaderFieldValidationInteractor
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


class TestImageUploaderFieldValidationInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldWithGoFDisplayNameDTOFactory.reset_sequence()

    @pytest.fixture
    def allowed_formats(self):
        allowed_formats = [
            ".pdf",
            ".jpg",
            ".png"
        ]
        return allowed_formats

    @pytest.mark.parametrize(
        "field_response",
        ["hps://www.google.com/search?q=images&client=ubuntu&hs=f83&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjm_L6voJLrAhVYyDgGHccbCaYQ_AUoAXoECA0QAw&biw=1848&bih=913#imgrc=a9B7raWE3PxoBM",
         ""])
    def test_given_invalid_image_uploader_value_in_field_response_raise_exception(
            self, allowed_formats, field_response
    ):

        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForImage
        field_id = "FIN_VENDOR_COMPANY_DETAILS"
        field_response = "hps://www.google.com/search?q=images&client=ubuntu&hs=f83&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjm_L6voJLrAhVYyDgGHccbCaYQ_AUoAXoECA0QAw&biw=1848&bih=913#imgrc=a9B7raWE3PxoBM"
        interactor = ImageUploaderFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            allowed_formats=allowed_formats)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act

        with pytest.raises(InvalidUrlForImage) as err:
            interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
        assert exception_object.image_url == field_response

    def test_invalid_image_format_in_field_response_raise_exception(self, allowed_formats):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidImageFormat
        field_id = "FIN_VENDOR_COMPANY_DETAILS"
        field_response = "https://www.google.com/bright-spring-view-cameo-island-260nw-1048185397.jqa"
        given_image_format = ".jqa"
        interactor = ImageUploaderFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            allowed_formats=allowed_formats)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        with pytest.raises(InvalidImageFormat) as err:
            interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
        assert exception_object.given_format == given_image_format
        assert exception_object.allowed_formats == allowed_formats

    def test_given_valid_url_and_format_in_field_response(
            self, allowed_formats
    ):
        # Arrange
        field_id = "FIN_VENDOR_COMPANY_DETAILS"
        field_response = "https://www.google.com/bright-spring-view-cameo-island-260nw-1048185397.jpg"
        interactor = ImageUploaderFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            allowed_formats=allowed_formats)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)

        # Act
        interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert

