import pytest
from ib_tasks.tests.factories.storage_dtos import FieldDTOFactory
from ib_tasks.interactors.create_update_fields_base_validations_interactor \
    import CreateUpdateFieldsBaseVaidationInteractor


class TestCreateUpdateFieldsBaseVaidationInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(TaskStorageInterface)
        return storage

    def test_given_field_ids_empty_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_FIELD_ID

        field_dtos = [FieldDTOFactory(), FieldDTOFactory(field_id=" ")]
        from ib_tasks.exceptions.custom_exceptions import FieldIdEmptyValueException
        interactor = CreateUpdateFieldsBaseVaidationInteractor(storage=storage_mock)

        # Act
        with pytest.raises(FieldIdEmptyValueException) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Arrange
        assert str(err.value) == EMPTY_VALUE_FOR_FIELD_ID

    def test_given_duplication_of_filed_ids_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import DUPLICATION_OF_FIELD_IDS
        from ib_tasks.exceptions.custom_exceptions import DuplicationOfFieldIdsExist

        field_dtos = [
            FieldDTOFactory(), FieldDTOFactory(),
            FieldDTOFactory(field_id="FIN_SALUATION"),
            FieldDTOFactory(field_id="FIN_SALUATION")
        ]
        duplication_of_field_ids = ["FIN_SALUATION"]
        exception_message = DUPLICATION_OF_FIELD_IDS.format(duplication_of_field_ids)
        interactor = CreateUpdateFieldsBaseVaidationInteractor(storage=storage_mock)

        # Act
        with pytest.raises(DuplicationOfFieldIdsExist) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Assert
        assert str(err.value) == exception_message


    def test_given_field_display_name_as_empty_rise_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import INVALID_FIELDS_DISPLAY_NAMES
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidValueForFieldDisplayName

        field_dtos = [
            FieldDTOFactory(field_id="field1"),
            FieldDTOFactory(field_id="field2", field_display_name=""),
            FieldDTOFactory(field_id="field3", field_display_name=" "),
            FieldDTOFactory(field_id="field4")
        ]
        invalid_fields_display_names = [
            {
                "field_id": "field2",
                "display_name": ""
            },
            {
                "field_id": "field3",
                "display_name": " "
            }
        ]
        exception_message = INVALID_FIELDS_DISPLAY_NAMES.format(invalid_fields_display_names)
        interactor = CreateUpdateFieldsBaseVaidationInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidValueForFieldDisplayName) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Assert

        assert str(err.value) == exception_message

    def test_given_invalid_field_type_raise_ecxception(self, storage_mock):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import INVALID_VALUES_FOR_FIELD_TYPES
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForFieldType
        from ib_tasks.constants.constants import FIELD_TYPES_LIST
        from ib_tasks.constants.enum import FieldTypes

        field_dtos = [
            FieldDTOFactory(field_id="field1", field_type=""),
            FieldDTOFactory(field_id="field2", field_type="Hello"),
            FieldDTOFactory(field_id="field3", field_type=FieldTypes.PLAIN_TEXT.value)
        ]
        field_ids = ["field1", "field2"]

        interactor = CreateUpdateFieldsBaseVaidationInteractor(storage=storage_mock)
        error_message = INVALID_VALUES_FOR_FIELD_TYPES.format(FIELD_TYPES_LIST, field_ids)
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS"]
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids

        # Act
        with pytest.raises(InvalidValueForFieldType) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Arrange
        assert str(err.value) == error_message

    def test_given_gof_ids_not_in_database_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.constants.exception_messages import INVALID_GOF_IDS_EXCEPTION_MESSAGE
        from ib_tasks.exceptions.custom_exceptions import InvalidGOFIds
        field_dtos = [FieldDTOFactory(), FieldDTOFactory(gof_id="Hello"), FieldDTOFactory(gof_id="")]
        interactor = CreateUpdateFieldsBaseVaidationInteractor(storage=storage_mock)
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS"]
        invalid_gof_ids = ["Hello", ""]
        error_message = INVALID_GOF_IDS_EXCEPTION_MESSAGE.format(invalid_gof_ids)
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids

        # Act
        with pytest.raises(InvalidGOFIds) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Arrange
        assert str(err.value) == error_message
