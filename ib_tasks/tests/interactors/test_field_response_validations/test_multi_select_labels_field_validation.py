import json

import pytest

from ib_tasks.exceptions.field_values_custom_exceptions import \
    IncorrectMultiSelectLabelsSelected
from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import \
    MultiSelectLabelFieldValidationInteractor
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


class TestMultiSelectLabelFieldValidationInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldWithGoFDisplayNameDTOFactory.reset_sequence()

    @pytest.fixture
    def valid_multi_select_labels(self):
        valid_multi_select_labels = [
            "multi_select_label1",
            "multi_select_label2",
            "multi_select_label3",
            "multi_select_label4"
        ]
        return valid_multi_select_labels

    def test_given_invalid_multi_select_labels_in_field_response_raise_exception(
            self, valid_multi_select_labels
    ):
        # Arrange
        import json
        field_id = "FIN_GOF_VENDOR_TYPE"
        field_response = [
            "multi_select_label1",
            "multi_select_label2",
            "multi_select_label5",
            "multi_select_label6"

        ]
        field_response = json.dumps(field_response)
        invalid_multi_select_labels = [
            "multi_select_label5",
            "multi_select_label6"
        ]
        interactor = MultiSelectLabelFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            valid_multi_select_labels=valid_multi_select_labels)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)
        expected_field_display_name = field_with_gof_display_name_dto.field_display_name

        # Act
        with pytest.raises(IncorrectMultiSelectLabelsSelected) as err:
            interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
        exception_obj = err.value
        assert exception_obj.field_display_name == expected_field_display_name
        assert exception_obj.invalid_multi_select_labels == \
               invalid_multi_select_labels
        assert exception_obj.valid_multi_select_labels == \
               valid_multi_select_labels

    def test_given_valid_multi_select_labels_in_field_response(
            self, valid_multi_select_labels
    ):
        # Arrange
        field_id = "FIN_GOF_VENDOR_TYPE"
        field_response = [
            "multi_select_label1",
            "multi_select_label2",
            "multi_select_label3",
            "multi_select_label4"

        ]
        field_response = json.dumps(field_response)
        interactor = MultiSelectLabelFieldValidationInteractor(
            field_id=field_id,
            field_response=field_response,
            valid_multi_select_labels=valid_multi_select_labels)

        field_with_gof_display_name_dto = FieldWithGoFDisplayNameDTOFactory(
            field_id=field_id)

        # Act
        interactor.validate_field_response([field_with_gof_display_name_dto])

        # Assert
