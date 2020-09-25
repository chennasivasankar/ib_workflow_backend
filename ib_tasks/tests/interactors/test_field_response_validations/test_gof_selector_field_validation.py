import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    GoFSelectorFieldValidationInteractor
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


class TestGoFSelectorFieldValidationInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldWithGoFDisplayNameDTOFactory.reset_sequence()

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

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        with pytest.raises(IncorrectNameInGoFSelectorField) as err:
            interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
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

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)

        # Act
        interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
