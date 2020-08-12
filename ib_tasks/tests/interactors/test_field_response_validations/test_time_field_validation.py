import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    TimeFieldValidationInteractor


class TestTimeFieldValidationInteractor:

    def test_given_invalid_time_format_in_field_response_raise_exception(self):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidTimeFormat
        from ib_tasks.constants.config import TIME_FORMAT
        expected_format = TIME_FORMAT
        field_id = "FIN_VENDOR_APPROVAL_DUE_TIME"
        field_response = "6/7:8"
        interactor = TimeFieldValidationInteractor(
            field_id=field_id, field_response=field_response
        )
        # Act

        with pytest.raises(InvalidTimeFormat) as err:
            interactor.validate_field_response()

        # Assert
        exception_object = err.value
        assert exception_object.field_id == field_id
        assert exception_object.field_value == field_response
        assert exception_object.expected_format == expected_format

    def test_given_valid_time_format_in_field_response(self):
        # Arrange
        field_id = "FIN_VENDOR_APPROVAL_DUE_TIME"
        field_response = "6:7:8"
        interactor = TimeFieldValidationInteractor(
            field_id=field_id, field_response=field_response
        )

        # Act
        interactor.validate_field_response()
        # Assert
