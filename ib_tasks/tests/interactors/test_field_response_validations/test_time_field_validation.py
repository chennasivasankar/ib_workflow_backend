import pytest

from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    TimeFieldValidationInteractor
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


class TestTimeFieldValidationInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldWithGoFDisplayNameDTOFactory.reset_sequence()

    def test_given_invalid_time_format_in_field_response_raise_exception(self):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidTimeFormat
        from ib_tasks.constants.config import TIME_FORMAT
        expected_format = TIME_FORMAT
        field_id = "FIN_VENDOR_APPROVAL_DUE_TIME"
        field_response = "6/7:8"
        interactor = TimeFieldValidationInteractor(
            field_id=field_id, field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        with pytest.raises(InvalidTimeFormat) as err:
            interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
        assert exception_object.field_value == field_response
        assert exception_object.expected_format == expected_format

    def test_given_invalid_time_format_when_time_is_not_zero_padded_in_field_response_raise_exception(
            self):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidTimeFormat
        from ib_tasks.constants.config import TIME_FORMAT
        expected_format = TIME_FORMAT
        field_id = "FIN_VENDOR_APPROVAL_DUE_TIME"
        field_response = "6:7:8"
        interactor = TimeFieldValidationInteractor(
            field_id=field_id, field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        with pytest.raises(InvalidTimeFormat) as err:
            interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
        exception_object = err.value
        assert exception_object.field_display_name == expected_field_display_name
        assert exception_object.field_value == field_response
        assert exception_object.expected_format == expected_format

    def test_given_valid_time_format_in_field_response(self):
        # Arrange
        field_id = "FIN_VENDOR_APPROVAL_DUE_TIME"
        field_response = "06:07:08"
        interactor = TimeFieldValidationInteractor(
            field_id=field_id, field_response=field_response)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)

        # Act
        interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
