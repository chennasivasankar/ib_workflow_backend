import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    EmailFieldValidationInteractor


class TestEmailFieldValidationInteractor:

    def test_given_invalid_email_in_field_response(self):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidEmailFieldValue
        field_id = "FIN_PAN_NUMBER"
        field_response = "hubs_gmail.com"
        interactor = EmailFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response
        )

        # Act
        with pytest.raises(InvalidEmailFieldValue) as err:
            interactor.validate_field_response()

        # Assert
        exception_object = err.value
        assert exception_object.field_id == field_id
        assert exception_object.field_value == field_response

    def test_given_valid_gmail_in_field_response(self):
        # Arrange
        field_id = "FIN_PAN_NUMBER"
        field_response = "hubs_@gmail.com"
        interactor = EmailFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response
        )

        # Act
        interactor.validate_field_response()

        # Assert
