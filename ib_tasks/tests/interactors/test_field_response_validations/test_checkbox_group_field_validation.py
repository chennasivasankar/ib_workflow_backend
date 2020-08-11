import json

import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    CheckBoxGroupFieldValidationInteractor


class TestCheckBoxGroupFieldValidationInteractor:
    @pytest.fixture
    def valid_check_box_options(self):
        valid_check_box_options = [
            "Verified the Bank Details",
            "Verified the GST Certificate",
            "Verified the Address Details",
        ]
        return valid_check_box_options

    def test_given_invalid_checkbox_options_in_field_response_raise_exception(
            self, valid_check_box_options
    ):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectCheckBoxOptionsSelected

        field_id = "FIN_GOF_VENDOR_TYPE"
        field_response = [
            "Verified the Bank Details",
            "Verified the GST Certificate",
            "Verified the Address Details",
            "Verified the office Details"
        ]
        invalid_checkbox_options = ["Verified the office Details"]
        field_response = json.dumps(field_response)
        interactor = CheckBoxGroupFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            valid_check_box_options=valid_check_box_options
        )

        # Act
        with pytest.raises(IncorrectCheckBoxOptionsSelected) as err:
            interactor.validate_field_response()

        # Assert
        exception_obj = err.value
        assert exception_obj.field_id == field_id
        assert exception_obj.invalid_checkbox_options == \
               invalid_checkbox_options
        assert exception_obj.valid_check_box_options == valid_check_box_options

    def test_given_valid_checkbox_options_in_field_response(
            self, valid_check_box_options
    ):
        # Arrange
        field_id = "FIN_GOF_VENDOR_TYPE"
        field_response = [
            "Verified the Bank Details",
            "Verified the GST Certificate",
            "Verified the Address Details",
        ]

        field_response = json.dumps(field_response)
        interactor = CheckBoxGroupFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            valid_check_box_options=valid_check_box_options
        )

        # Act
        interactor.validate_field_response()

        # Assert


