import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    URLFieldValidationInteractor


class TestURLFieldValidationInteractor:

    def test_given_invalid_url_in_field_response_raise_exception(self):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue
        field_id = "FIN_WEBSITE"
        field_response = "hs://editor.swagger.io/"
        interactor = URLFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response
        )

        # Act
        with pytest.raises(InvalidURLValue) as err:
            interactor.validate_field_response()

        # Assert
        exception_object = err.value
        assert exception_object.field_id == field_id
        assert exception_object.field_value == field_response

    def test_given_valid_url_in_field_response(self):
        # Arrange
        field_id = "FIN_WEBSITE"
        field_response = "https://editor.swagger.io/"
        interactor = URLFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response
        )

        # Act
        interactor.validate_field_response()

        # Assert