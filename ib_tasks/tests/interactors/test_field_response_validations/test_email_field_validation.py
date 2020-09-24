import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    EmailFieldValidationInteractor
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


class TestEmailFieldValidationInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldWithGoFDisplayNameDTOFactory.reset_sequence()

    def test_given_invalid_email_in_field_response(self):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidEmailFieldValue
        field_id = "FIN_PAN_NUMBER"
        field_response = "hubs_gmail.com"
        interactor = EmailFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        with pytest.raises(InvalidEmailFieldValue) as err:
            interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
        assert exception_object.field_value == field_response

    def test_given_valid_gmail_in_field_response(self):
        # Arrange
        field_id = "FIN_PAN_NUMBER"
        field_response = "hubs_@gmail.com"
        interactor = EmailFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)

        # Act
        interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
