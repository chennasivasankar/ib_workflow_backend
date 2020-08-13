import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    PasswordFieldValidationInteractor


class TestPasswordFieldValidationInteractor:

    @pytest.mark.parametrize(
        "field_response",
        ["password", "hello123", "hello@123", "hii"])
    def test_given_invalid_password_in_field_response(self, field_response):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            NotAStrongPassword
        field_id = "FIN_TAX_PAYER_TYPE",
        interactor = PasswordFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response
        )

        # Act
        with pytest.raises(NotAStrongPassword) as err:
            interactor.validate_field_response()

        # Assert
        exception_object = err.value
        assert exception_object.field_id == field_id
        assert exception_object.field_value == field_response

    @pytest.mark.parametrize(
        "field_response",
        ["passwOrd@123", "Hello%123", "hellO@123"])
    def test_given_valid_password_in_field_response(self, field_response):
        # Arrange
        field_id = "FIN_TAX_PAYER_TYPE",
        interactor = PasswordFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response
        )

        # Act
        interactor.validate_field_response()

        # Assert
