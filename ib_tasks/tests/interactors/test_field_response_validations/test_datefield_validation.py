import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    DateFieldValidationInteractor


class TestDateFieldValidationInteractor:

    def test_given_invalid_date_format_in_field_response_raise_exception(self):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidDateFormat
        from ib_tasks.constants.config import DATE_FORMAT
        expected_format = DATE_FORMAT
        field_id = "FIN_VENDOR_APPROVAL_DUE_DATE"
        field_response = "2303/05/4"
        interactor = DateFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response
        )

        # Act
        with pytest.raises(InvalidDateFormat) as err:
            interactor.validate_field_response()

        # Assert
        exception_object = err.value
        assert exception_object.field_id == field_id
        assert exception_object.field_value == field_response
        assert exception_object.expected_format == expected_format

    def test_given_valid_date_format_in_field_response(self):
        # Arrange
        field_id = "FIN_VENDOR_APPROVAL_DUE_DATE"
        field_response = "2303-05-04"
        interactor = DateFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response
        )

        # Act
        interactor.validate_field_response()

        # Assert
