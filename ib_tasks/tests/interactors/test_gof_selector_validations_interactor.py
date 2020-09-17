import json

import pytest

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.interactors.create_or_update_fields \
    .gof_selector_validations_interactor \
    import GoFSelectorValidationsInteractor
from ib_tasks.tests.factories.storage_dtos import FieldDTOFactory


class TestGoFSelectorValidationsInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import \
            GoFStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(GoFStorageInterface)
        return storage

    @pytest.fixture
    def reset_field_dto(self):
        FieldDTOFactory.reset_sequence(1)

    def test_given_field_type_gof_selector_and_field_values_as_invalid_json_raise_exception(
            self, storage_mock, reset_field_dto
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import InvalidJsonForFieldValue
        from ib_tasks.constants.exception_messages import INVALID_JSON
        field_values = [
            {
                "name": "Individual",
                "gof_ids": ['GST_DETAILS', "CUSTOMER_DETAILS"]
            },
            {
                "name": "Company",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            }
        ]
        field_dto = FieldDTOFactory(
            field_id="field1",
            field_type=FieldTypes.GOF_SELECTOR.value,
            field_values=str(field_values)
        )
        field_id = "field1"
        error_message = INVALID_JSON.format(field_id)
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS"]
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids
        interactor = GoFSelectorValidationsInteractor(gof_storage=storage_mock)

        # Act
        with pytest.raises(InvalidJsonForFieldValue) as err:
            interactor.gof_selector_validations(field_dto)

        # Assert
        assert str(err.value) == error_message

    def test_given_gof_names_as_empty_for_field_values_raise_exception(
            self, storage_mock, reset_field_dto
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import EmptyValuesForGoFNames
        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_GOF_NAMES
        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            },
            {
                "name": " ",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            }
        ]
        field_values = json.dumps(field_values)
        field_dto = FieldDTOFactory(
            field_id="field1",
            field_type=FieldTypes.GOF_SELECTOR.value,
            field_values=field_values
        )
        field_id = "field1"
        error_message = EMPTY_VALUE_FOR_GOF_NAMES.format(field_id)
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS"]
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids
        interactor = GoFSelectorValidationsInteractor(gof_storage=storage_mock)

        # Act
        with pytest.raises(EmptyValuesForGoFNames) as err:
            interactor.gof_selector_validations(field_dto)

        # Assert
        assert str(err.value) == error_message

    def test_given_duplication_of_gof_names_for_field_values_raise_exception(
            self, storage_mock, reset_field_dto
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import DuplicationOfGoFNamesForFieldValues
        from ib_tasks.constants.exception_messages \
            import DUPLICATED_OF_GOF_NAMES_FOR_FIELD_VALUES
        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            },
            {
                "name": "Company",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            },
            {
                "name": "Individual",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            }
        ]
        field_values = json.dumps(field_values)
        field_dto = FieldDTOFactory(
            field_id="field1",
            field_type=FieldTypes.GOF_SELECTOR.value,
            field_values=field_values
        )
        exception_message = {
            "field_id": "field1",
            "duplication_of_gof_names": ["Individual"]
        }
        error_message = DUPLICATED_OF_GOF_NAMES_FOR_FIELD_VALUES.format(exception_message)
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS"]
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids
        interactor = GoFSelectorValidationsInteractor(gof_storage=storage_mock)

        # Act
        with pytest.raises(DuplicationOfGoFNamesForFieldValues) as err:
            interactor.gof_selector_validations(field_dto)

        # Assert
        print("str(err.value) = ", str(err.value))
        print("error_message = ", error_message)
        assert str(err.value) == error_message

    def test_given_invalid_gof_ids_for_field_values_raise_exception(
            self, storage_mock, reset_field_dto
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import InvalidGOFIds
        from ib_tasks.constants.exception_messages \
            import INVALID_GOF_IDS_EXCEPTION_MESSAGE
        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            },
            {
                "name": "Company",
                "gof_ids": ["GST_DETAILS", "FIN_VENDOR_BASIC_DETAILS"]
            }
        ]
        field_values = json.dumps(field_values)
        field_dto = FieldDTOFactory(
            field_id="field1",
            field_type=FieldTypes.GOF_SELECTOR.value,
            field_values=field_values
        )
        invalid_gof_ids = ["CUSTOMER_DETAILS", "GST_DETAILS"]
        exception_message = {
            "field_id": "field1",
            "invalid_gof_ids": invalid_gof_ids
        }
        error_message = INVALID_GOF_IDS_EXCEPTION_MESSAGE.format(exception_message)
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS"]
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids
        interactor = GoFSelectorValidationsInteractor(gof_storage=storage_mock)

        # Act
        with pytest.raises(InvalidGOFIds) as err:
            interactor.gof_selector_validations(field_dto)

        # Assert
        assert str(err.value) == error_message

    def test_eliminate_duplication_of_gof_ids(self, storage_mock):
        # Arrange
        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS", "CUSTOMER_DETAILS"]
            },
            {
                "name": "Company",
                "gof_ids": ["GST_DETAILS", "FIN_VENDOR_BASIC_DETAILS", "GST_DETAILS"]
            }
        ]
        field_values = json.dumps(field_values)
        field_dto = FieldDTOFactory(
            field_id="field1",
            field_type=FieldTypes.GOF_SELECTOR.value,
            field_values=field_values
        )
        expected_field_values = [
            {
                "name": "Individual",
                "gof_ids": ["CUSTOMER_DETAILS", "GST_DETAILS"]
            },
            {
                "name": "Company",
                "gof_ids": ["FIN_VENDOR_BASIC_DETAILS", "GST_DETAILS"]
            }
        ]
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS", "CUSTOMER_DETAILS", "GST_DETAILS"]
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids

        expected_field_values = json.dumps(expected_field_values)
        interactor = GoFSelectorValidationsInteractor(gof_storage=storage_mock)

        # Act
        interactor.gof_selector_validations(field_dto)

        # Assert

        assert field_dto.field_values == expected_field_values
