import pytest

from ib_tasks.exceptions.field_values_custom_exceptions import \
    IncorrectRadioGroupChoice
from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    RadioGroupFieldValidationInteractor


class TestRadioGroupFieldValidationInteractor:

    @pytest.fixture
    def valid_radio_group_options(self):
        valid_radio_group_options = [
            "Registered",
            "Not Registered"
        ]
        return valid_radio_group_options

    def test_given_invalid_radio_group_option_in_field_response_raise_exception(
            self, valid_radio_group_options
    ):
        # Arrange
        field_id = "FIN_GOF_VENDOR_TYPE"
        field_response = "hello"
        interactor = RadioGroupFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            valid_radio_group_options=valid_radio_group_options
        )

        # Act
        with pytest.raises(IncorrectRadioGroupChoice) as err:
            interactor.validate_field_response()

        # Assert
        exception_obj = err.value
        assert exception_obj.field_id == field_id
        assert exception_obj.field_value == field_response
        assert exception_obj.valid_radio_group_options == \
               valid_radio_group_options

    def test_given_valid_radio_group_option_in_field_response(
            self, valid_radio_group_options
    ):
        # Arrange
        field_id = "FIN_GOF_VENDOR_TYPE"
        field_response = "Registered"
        interactor = RadioGroupFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            valid_radio_group_options=valid_radio_group_options
        )

        # Act
        interactor.validate_field_response()

        # Assert
