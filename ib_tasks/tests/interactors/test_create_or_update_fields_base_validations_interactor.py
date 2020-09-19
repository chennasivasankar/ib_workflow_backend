import pytest

from ib_tasks.interactors.create_or_update_fields \
    .create_or_update_fields_base_validations_interactor \
    import CreateOrUpdateFieldsBaseValidationInteractor
from ib_tasks.tests.factories.storage_dtos import FieldDTOFactory


class TestCreateOrUpdateFieldsBaseValidationInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import \
            GoFStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(GoFStorageInterface)
        return storage

    def test_given_field_ids_empty_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_FIELD_ID

        field_dtos = [FieldDTOFactory(), FieldDTOFactory(field_id=" ")]
        from ib_tasks.exceptions.fields_custom_exceptions \
            import FieldIdEmptyValueException
        interactor = CreateOrUpdateFieldsBaseValidationInteractor(
            gof_storage=storage_mock
        )

        # Act
        with pytest.raises(FieldIdEmptyValueException) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Arrange
        assert str(err.value) == EMPTY_VALUE_FOR_FIELD_ID

    def test_given_duplication_of_filed_ids_raise_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import DUPLICATION_OF_FIELD_IDS
        from ib_tasks.exceptions.fields_custom_exceptions \
            import DuplicationOfFieldIdsExist

        field_dtos = [
            FieldDTOFactory(), FieldDTOFactory(),
            FieldDTOFactory(field_id="FIN_SALUATION"),
            FieldDTOFactory(field_id="FIN_SALUATION")
        ]
        duplication_of_field_ids = ["FIN_SALUATION"]
        exception_message = DUPLICATION_OF_FIELD_IDS.format(
            duplication_of_field_ids
        )
        interactor = CreateOrUpdateFieldsBaseValidationInteractor(
            gof_storage=storage_mock
        )

        # Act
        with pytest.raises(DuplicationOfFieldIdsExist) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Assert
        assert str(err.value) == exception_message

    def test_given_field_display_name_as_empty_raise_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import INVALID_FIELDS_DISPLAY_NAMES
        from ib_tasks.exceptions.fields_custom_exceptions \
            import InvalidValueForFieldDisplayName

        field_dtos = [
            FieldDTOFactory(field_id="field1"),
            FieldDTOFactory(field_id="field2", field_display_name=""),
            FieldDTOFactory(field_id="field3", field_display_name=" "),
            FieldDTOFactory(field_id="field4")
        ]
        field_ids = ["field2", "field3"]
        exception_message = INVALID_FIELDS_DISPLAY_NAMES.format(field_ids)
        interactor = CreateOrUpdateFieldsBaseValidationInteractor(
            gof_storage=storage_mock
        )

        # Act
        with pytest.raises(InvalidValueForFieldDisplayName) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Assert

        assert str(err.value) == exception_message

    def test_given_invalid_field_type_raise_ecxception(self, storage_mock):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import INVALID_VALUES_FOR_FIELD_TYPES
        from ib_tasks.exceptions.fields_custom_exceptions \
            import InvalidValueForFieldType
        from ib_tasks.constants.constants import FIELD_TYPES_LIST
        from ib_tasks.constants.enum import FieldTypes

        field_dtos = [
            FieldDTOFactory(field_id="field1", field_type=""),
            FieldDTOFactory(field_id="field2", field_type="Hello"),
            FieldDTOFactory(
                field_id="field3",
                field_type=FieldTypes.PLAIN_TEXT.value
            )
        ]
        field_ids = ["field1", "field2"]

        interactor = CreateOrUpdateFieldsBaseValidationInteractor(
            gof_storage=storage_mock
        )
        error_message = INVALID_VALUES_FOR_FIELD_TYPES.format(
            FIELD_TYPES_LIST, field_ids
        )

        # Act
        with pytest.raises(InvalidValueForFieldType) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Arrange
        assert str(err.value) == error_message

    def test_given_gof_ids_not_in_database_raise_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import INVALID_GOF_IDS_EXCEPTION_MESSAGE
        from ib_tasks.exceptions.fields_custom_exceptions import InvalidGOFIds
        field_dtos = [
            FieldDTOFactory(),
            FieldDTOFactory(gof_id="Hello"),
            FieldDTOFactory(gof_id="")
        ]
        interactor = CreateOrUpdateFieldsBaseValidationInteractor(
            gof_storage=storage_mock
        )
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS"]
        invalid_gof_ids = ["Hello", ""]
        error_message = INVALID_GOF_IDS_EXCEPTION_MESSAGE.format(
            invalid_gof_ids
        )
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids

        # Act
        with pytest.raises(InvalidGOFIds) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Arrange
        assert str(err.value) == error_message

    def test_given_negative_order_for_fields_raises_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import ORDER_FOR_FIELD_SHOULD_NOT_BE_NEGATIVE
        from ib_tasks.exceptions.fields_custom_exceptions \
            import OrderForFieldShouldNotBeNegativeException

        field_dtos = [
            FieldDTOFactory(field_id="FIN_SALUTATION", order=-1),
            FieldDTOFactory(field_id="FIN_PR", order=-2)
        ]
        negative_ordered_fields = ["FIN_SALUTATION", "FIN_PR"]
        expected_exception_message = \
            ORDER_FOR_FIELD_SHOULD_NOT_BE_NEGATIVE.format(
                negative_ordered_fields)

        interactor = CreateOrUpdateFieldsBaseValidationInteractor(
            gof_storage=storage_mock
        )

        # Act
        with pytest.raises(OrderForFieldShouldNotBeNegativeException) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Assert
        assert str(err.value) == expected_exception_message

    def test_given_duplicate_order_for_fields_of_same_gof_raises_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import DUPLICATE_ORDER_FOR_FIELDS_OF_SAME_GOF
        from ib_tasks.exceptions.fields_custom_exceptions \
            import DuplicateOrdersForFieldsOfGoFException

        field_dtos = [
            FieldDTOFactory(gof_id="gof_1", order=1),
            FieldDTOFactory(gof_id="gof_1", order=1)
        ]
        duplicate_orders = [1]
        duplicate_ordered_fields_gof = "gof_1"
        expected_exception_message = \
            DUPLICATE_ORDER_FOR_FIELDS_OF_SAME_GOF.format(
                duplicate_orders, duplicate_ordered_fields_gof)

        interactor = CreateOrUpdateFieldsBaseValidationInteractor(
            gof_storage=storage_mock
        )

        # Act
        with pytest.raises(DuplicateOrdersForFieldsOfGoFException) as err:
            interactor.fields_base_validations(field_dtos=field_dtos)

        # Assert
        assert str(err.value) == expected_exception_message
