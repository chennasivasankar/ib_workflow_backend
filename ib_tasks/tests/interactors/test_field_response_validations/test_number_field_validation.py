import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    NumberFieldValidationInteractor
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


class TestNumberFieldValidationInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldWithGoFDisplayNameDTOFactory.reset_sequence()

    def test_given_invalid_number_value_in_field_response_raise_exception(
            self):
        # Arrange
        field_id = "FIN_PAN_DETAILS"
        field_response = "123we"
        interactor = NumberFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidNumberValue
        with pytest.raises(InvalidNumberValue) as err:
            interactor.validate_field_response(
                [field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
        assert exception_object.field_value == field_response

    def test_given_valid_number_value_in_field_response(self):
        # Arrange
        field_id = "FIN_PAN_DETAILS"
        field_response = "12356789"
        interactor = NumberFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)

        # Act
        interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
