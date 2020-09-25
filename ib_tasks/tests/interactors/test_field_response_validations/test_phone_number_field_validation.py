import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    PhoneNumberFieldValidationInteractor
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


class TestPhoneNumberFieldValidationInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldWithGoFDisplayNameDTOFactory.reset_sequence()

    def test_given_phone_number_has_non_digit_chars_raise_exception(self):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidPhoneNumberValue
        field_id = "FIN_PHONE"
        field_response = "12344fshfg454"
        interactor = PhoneNumberFieldValidationInteractor(
            field_id=field_id, field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        with pytest.raises(InvalidPhoneNumberValue) as err:
            interactor.validate_field_response(
                [field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
        assert exception_object.field_value == field_response

    @pytest.mark.parametrize("field_response", ["12345689", "123456897685"])
    def test_given_phone_number_contains_does_not_contain_10_digits(
            self, field_response
    ):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidPhoneNumberValue
        field_id = "FIN_PHONE"
        field_response = "12345689"
        interactor = PhoneNumberFieldValidationInteractor(
            field_id=field_id, field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        with pytest.raises(InvalidPhoneNumberValue) as err:
            interactor.validate_field_response(
                [field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
        assert exception_object.field_value == field_response

    def test_given_valid_phone_number_in_field_response(self):
        # Arrange
        field_id = "FIN_PHONE"
        field_response = "1234568912"
        interactor = PhoneNumberFieldValidationInteractor(
            field_id=field_id, field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)

        # Act
        interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
