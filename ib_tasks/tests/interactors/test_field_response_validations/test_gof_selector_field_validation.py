import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    GoFSelectorFieldValidationInteractor


class TestGoFSelectorFieldValidationInteractor:

    @pytest.fixture
    def valid_gof_selector_names(self):
        valid_gof_selector_names = [
            "Vendor Type",
            "Vendor Basic Details",
            "Type of GST Registration",
        ]
        return valid_gof_selector_names

    def test_given_invalid_gof_selector_name_in_filed_response_raise_exception(
            self, valid_gof_selector_names
    ):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectNameInGoFSelectorField
        field_id = "FIN_TAX_PAYER_TYPE"
        field_response = "Vendor GST Details Verification Checklist"
        interactor = GoFSelectorFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            valid_gof_selector_names=valid_gof_selector_names
        )

        # Act
        with pytest.raises(IncorrectNameInGoFSelectorField) as err:
            interactor.validate_field_response()

        # Assert
        exception_object = err.value
        assert exception_object.field_id == field_id
        assert exception_object.field_value == field_response
        assert exception_object.valid_gof_selector_names == \
               valid_gof_selector_names

    def test_given_valid_gof_selector_name_in_filed_response(
            self, valid_gof_selector_names
    ):
        # Arrange
        field_id = "FIN_TAX_PAYER_TYPE"
        field_response = "Vendor Basic Details"
        interactor = GoFSelectorFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            valid_gof_selector_names=valid_gof_selector_names
        )
        # Act
        interactor.validate_field_response()

        # Assert
