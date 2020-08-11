import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    MultiSelectFieldValidationInteractor


class TestMultiSelectFieldValidationInteractor:

    @pytest.fixture
    def valid_multi_select_options(self):
        valid_multi_select_options = [
            "194 IA",
            "194C CD",
            "194C NCD",
            "194H CD",
            "194H NCD",
            "194I CD",
            "194I CD - Equipment"
        ]
        return valid_multi_select_options

    def test_given_invalid_multi_select_options_in_field_response_raise_exception(
            self, valid_multi_select_options
    ):
        # Arrange
        import json
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectOptionsSelected
        field_id = "FIN_GOF_VENDOR_TYPE"
        field_response = [
            "194H",
            "194I CD - Equipment",
            "1954",
            "Hello"
        ]
        field_response = json.dumps(field_response)
        invalid_multi_select_options = [
            "194H",
            "1954",
            "Hello"
        ]
        interactor = MultiSelectFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            valid_multi_select_options=valid_multi_select_options
        )

        # Act
        with pytest.raises(IncorrectMultiSelectOptionsSelected) as err:
            interactor.validate_field_response()

        # Assert
        exception_obj = err.value
        assert exception_obj.field_id == field_id
        assert exception_obj.invalid_multi_select_options == \
               invalid_multi_select_options
        assert exception_obj.valid_multi_select_options == \
               valid_multi_select_options

    def test_given_valid_multi_select_options_in_field_response(
            self, valid_multi_select_options
    ):
        # Arrange
        import json
        field_id = "FIN_GOF_VENDOR_TYPE"
        field_response = [
            "194C CD",
            "194C NCD",
            "194H CD",
            "194H NCD",
            "194I CD",
        ]
        field_response = json.dumps(field_response)
        interactor = MultiSelectFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            valid_multi_select_options=valid_multi_select_options
        )

        # Act
        interactor.validate_field_response()

