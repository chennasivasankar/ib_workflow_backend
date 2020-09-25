import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    DropDownFieldValidationInteractor
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


class TestDropDownFieldValidationInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldWithGoFDisplayNameDTOFactory.reset_sequence()

    @pytest.fixture
    def valid_dropdown_values(self):
        valid_dropdown_values = [
            "Mr.",
            "Ms.",
            "Mrs."
        ]
        return valid_dropdown_values

    def test_given_invalid_dropdown_value_in_field_response(self, valid_dropdown_values):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidValueForDropdownField
        field_id = "FIN_GOF_VENDOR_TYPE"
        field_response = "Hello"
        interactor = DropDownFieldValidationInteractor(
            field_id=field_id, field_response=field_response,
            valid_dropdown_values=valid_dropdown_values)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        with pytest.raises(InvalidValueForDropdownField) as err:
            interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
        assert exception_object.field_value == field_response
        assert exception_object.valid_values == valid_dropdown_values

    def test_given_valid_dropdown_values_in_field_response(
            self, valid_dropdown_values
    ):
        # Arrange
        field_id = "FIN_GOF_VENDOR_TYPE"
        field_response = "Mr."
        interactor = DropDownFieldValidationInteractor(
            field_id=field_id, field_response=field_response,
            valid_dropdown_values=valid_dropdown_values)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)

        # Act
        interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert

