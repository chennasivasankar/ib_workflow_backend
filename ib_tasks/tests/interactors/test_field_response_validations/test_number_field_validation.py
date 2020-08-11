import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    NumberFieldValidationInteractor


class TestNumberFieldValidationInteractor:

    def test_given_invalid_number_value_in_field_response_raise_exception(self):
        # Arrange
        field_id = "FIN_PAN_DETAILS"
        field_response = "123we"
        interactor = NumberFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response
        )

        # Act
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidNumberValue
        with pytest.raises(InvalidNumberValue) as err:
            interactor.validate_field_response()

        # Assert
        exception_object = err.value
        assert exception_object.field_id == field_id
        assert exception_object.field_value == field_response

    def test_given_valid_number_value_in_field_response(self):
        # Arrange
        field_id = "FIN_PAN_DETAILS"
        field_response = "12356789"
        interactor = NumberFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response
        )
        # Act
        interactor.validate_field_response()

        # Assert
