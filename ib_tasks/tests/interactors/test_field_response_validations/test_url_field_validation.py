import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    URLFieldValidationInteractor
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


class TestURLFieldValidationInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldWithGoFDisplayNameDTOFactory.reset_sequence()

    def test_given_invalid_url_in_field_response_raise_exception(self):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue
        field_id = "FIN_WEBSITE"
        field_response = "hs://editor.swagger.io/"
        interactor = URLFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        with pytest.raises(InvalidURLValue) as err:
            interactor.validate_field_response(
                [field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
        assert exception_object.field_value == field_response

    def test_given_valid_url_in_field_response(self):
        # Arrange
        field_id = "FIN_WEBSITE"
        field_response = "https://editor.swagger.io/"
        interactor = URLFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
