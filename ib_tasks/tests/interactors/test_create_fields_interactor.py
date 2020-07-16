from unittest.mock import create_autospec, Mock

import pytest

from ib_tasks.tests.factories.interactor_dtos import FieldDTOFactory

from ib_tasks.interactors.create_fields_ineractor import CreateFieldsInteractor


class TestCreateFieldsInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.tasks_storage_interface \
            import TaskStorageInterface
        storage = create_autospec(TaskStorageInterface)
        return storage

    def test_given_gof_id_is_empty_raise_exception(self, storage_mock):
        # Arrange
        field_dtos = [FieldDTOFactory(), FieldDTOFactory(gof_id=" ")]
        from ib_tasks.exceptions.custom_exceptions import InvalidGOFId
        interactor = CreateFieldsInteractor(storage=storage_mock)
        error_message = "GOF Id shouldn't be empty"

        # Act
        with pytest.raises(InvalidGOFId) as err:
            interactor.create_fields(field_dtos)

        # Arrange
        assert str(err.value) == error_message


    def test_given_field_id_is_empty_raise_exception(self, storage_mock):
        # Arrange
        field_dtos = [FieldDTOFactory(), FieldDTOFactory(field_id=" ")]
        from ib_tasks.exceptions.custom_exceptions import InvalidFieldIdException
        interactor = CreateFieldsInteractor(storage=storage_mock)
        error_message = "Field Id shouldn't be empty"

        # Act
        with pytest.raises(InvalidFieldIdException) as err:
            interactor.create_fields(field_dtos)

        # Arrange
        assert str(err.value) == error_message


    def test_given_duplication_of_filed_ids_raise_exception(self, storage_mock):
        # Arrange
        field_dtos = [
            FieldDTOFactory(), FieldDTOFactory(),
            FieldDTOFactory(field_id="FIN_SALUATION"),
            FieldDTOFactory(field_id="FIN_SALUATION")
        ]
        duplication_of_field_ids = ["FIN_SALUATION"]
        from ib_tasks.exceptions.custom_exceptions import DuplicationOfFieldIdsExist
        interactor = CreateFieldsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(DuplicationOfFieldIdsExist) as err:
            interactor.create_fields(field_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.field_ids == duplication_of_field_ids

    def test_given_invalid_field_type_raise_ecxception(self, storage_mock):
        # Arrange
        field_dtos = [FieldDTOFactory(field_type=""), FieldDTOFactory(field_type="Hello")]
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForFieldType
        from ib_tasks.constants.constants import FIELD_TYPES_LIST
        interactor = CreateFieldsInteractor(storage=storage_mock)
        error_message = "Field_Type should be one of these {}".format(FIELD_TYPES_LIST)

        # Act
        with pytest.raises(InvalidValueForFieldType) as err:
            interactor.create_fields(field_dtos)

        # Arrange
        assert str(err.value) == error_message

    def test_given_field_display_name_as_empty_rise_exception(
            self, storage_mock
    ):
        # Arrange
        field_dtos = [
            FieldDTOFactory(),
            FieldDTOFactory(),
            FieldDTOFactory(field_display_name=" "),
            FieldDTOFactory()
        ]
        exception_message = "Field display name shouldn't be empty"
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForFieldDisplayName
        interactor = CreateFieldsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidValueForFieldDisplayName) as err:
            interactor.create_fields(field_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.message == exception_message



    def test_given_field_type_is_dropdown_if_filed_values_are_duplicate_raise_exception(
            self, storage_mock
    ):
        # Arrange
        FieldDTOFactory.reset_sequence(1)
        field_dtos = [
            FieldDTOFactory(),
            FieldDTOFactory(field_values=["Mr", "Mrs", "Ms", "Mr", "Mrs"]),
            FieldDTOFactory(field_values=["admin", "User", "admin", "User"])
        ]
        from ib_tasks.constants.enum import FieldTypes
        fieds_with_dropdown_duplicate_values = [
            {
                "field_id": "field2",
                "field_type": FieldTypes.DROPDOWN.value,
                "duplicate_values": ["Mr", "Mrs"]
            },
            {
                "field_id": "field3",
                "field_type": FieldTypes.DROPDOWN.value,
                "duplicate_values": ["admin", "User"]
            }
        ]
        from ib_tasks.exceptions.custom_exceptions import FieldsDuplicationOfDropDownValues
        interactor = CreateFieldsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(FieldsDuplicationOfDropDownValues) as err:
            interactor.create_fields(field_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.fieds_with_dropdown_duplicate_values == \
               fieds_with_dropdown_duplicate_values

    def test_given_invalid_roles_for_read_permissions_raise_exception(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_all_valid_read_permission_roles
        get_valid_read_permissions_mock_method = \
            get_all_valid_read_permission_roles(mocker)
        from ib_tasks.exceptions.custom_exceptions import InvalidRolesException
        FieldDTOFactory.reset_sequence(1)
        field_dtos = [
            FieldDTOFactory(
                # field_id="field1",
                read_permissions_to_roles=[
                    "FIN_PAYMENT_POC", "User", "Vendor", "FIN_PAYMENT_REQUESTER"
                ]
            ),
            FieldDTOFactory(
                # field_id="filed2",
                read_permissions_to_roles=[
                    "FIN_PAYMENT_REQUESTER",
                    "admin",
                ]
            )
        ]
        fields_invalid_roles_for_read_permission = [
            {
                "field_id": "field1",
                "invalid_roles": ["User", "Vendor"],
                "permissions": "read_permissions",
            },
            {
                "field_id": "field2",
                "permissions": "read_permissions",
                "invalid_roles": ["admin"]
            }
        ]

        interactor = CreateFieldsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidRolesException) as err:
            interactor.create_fields(field_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.roles == fields_invalid_roles_for_read_permission
        get_valid_read_permissions_mock_method.assert_called_once()
        storage_mock.create_fields.assert_not_called()
        storage_mock.update_fields.assert_not_called()


    def test_given_invalid_roles_for_write_permissions_raise_exception(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_all_valid_read_permission_roles,
            get_all_valid_write_permission_roles
        )
        get_valid_read_permissions_mock_method = \
            get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = \
            get_all_valid_write_permission_roles(mocker)

        from ib_tasks.exceptions.custom_exceptions import InvalidRolesException

        FieldDTOFactory.reset_sequence(1)
        field_dtos = [
            FieldDTOFactory(
                read_permissions_to_roles=[
                    "FIN_PAYMENT_POC", "FIN_PAYMENT_REQUESTER"
                ],
                write_permissions_to_roles=[
                    "FIN_PAYMENT_POC", "User", "Vendor", "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ]
            ),
            FieldDTOFactory(
                read_permissions_to_roles=[
                    "FIN_PAYMENT_POC"
                ],
                write_permissions_to_roles=[
                    "FIN_PAYMENT_POC",
                    "admin",
                ]
            )
        ]
        fields_invalid_roles_for_write_permission = [
            {
                "field_id": "field1",
                "invalid_roles": ["User", "Vendor", "FIN_PAYMENTS_LEVEL1_VERIFIER"],
                "permissions": "write_permissions",
            },
            {
                "field_id": "field2",
                "permissions": "write_permissions",
                "invalid_roles": ["admin"]
            }
        ]
        interactor = CreateFieldsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidRolesException) as err:
            interactor.create_fields(field_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.roles == fields_invalid_roles_for_write_permission
        get_valid_write_permissions_mock_method.assert_called_once()
        get_valid_read_permissions_mock_method.assert_called_once()

    def test_given_empty_values_for_read_permissions_raise_exception(
            self, storage_mock
    ):
        # Arrange
        exception_message = "Permissions to roles shouldn't be empty"
        field_dtos = [
            FieldDTOFactory(
                read_permissions_to_roles=[],
                write_permissions_to_roles=[
                    "FIN_PAYMENTS_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ]
            ),
            FieldDTOFactory(
                read_permissions_to_roles=[
                    "FIN_PAYMENTS_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ],
                write_permissions_to_roles=[
                    "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ]
            )
        ]
        from ib_tasks.exceptions.custom_exceptions import EmptyValueForPermissions
        interactor = CreateFieldsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(EmptyValueForPermissions) as err:
            interactor.create_fields(field_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.message == exception_message

    def test_given_empty_values_for_write_permissions_raise_exception(
            self, storage_mock
    ):
        # Arrange
        exception_message = "Permissions to roles shouldn't be empty"
        field_dtos = [
            FieldDTOFactory(
                read_permissions_to_roles=["FIN_PAYMENTS_RP"],
                write_permissions_to_roles=[
                    "FIN_PAYMENTS_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ]
            ),
            FieldDTOFactory(
                read_permissions_to_roles=[
                    "FIN_PAYMENTS_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ],
                write_permissions_to_roles=[]
            )
        ]
        from ib_tasks.exceptions.custom_exceptions import EmptyValueForPermissions
        interactor = CreateFieldsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(EmptyValueForPermissions) as err:
            interactor.create_fields(field_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.message == exception_message

    def test_given_new_field_ids_populate_fields(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_all_valid_read_permission_roles,
            get_all_valid_write_permission_roles
        )
        get_valid_read_permissions_mock_method = \
            get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = \
            get_all_valid_write_permission_roles(mocker)

        FieldDTOFactory.reset_sequence(1)
        field_dtos = [
            FieldDTOFactory(),
            FieldDTOFactory(),
            FieldDTOFactory()
        ]
        existing_field_ids = []
        interactor = CreateFieldsInteractor(storage=storage_mock)
        storage_mock.get_existing_field_ids.return_value = existing_field_ids

        # Act
        interactor.create_fields(field_dtos)

        # Assert
        storage_mock.create_fields.assert_called_once_with(field_dtos)
        get_valid_write_permissions_mock_method.assert_called_once()
        get_valid_read_permissions_mock_method.assert_called_once()

    def test_given_field_ids_already_exist_in_database_then_update_fields(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_all_valid_read_permission_roles,
            get_all_valid_write_permission_roles
        )
        get_valid_read_permissions_mock_method = \
            get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = \
            get_all_valid_write_permission_roles(mocker)

        field_dtos = [
            FieldDTOFactory(field_id="FIN_TYPE_OF_VENDOR"),
            FieldDTOFactory(field_id="FIN_SALUATION"),
            FieldDTOFactory(field_id="FIN_FIRST NAME"),
            FieldDTOFactory(field_id="FIN_DISPLAY NAME")
        ]
        existing_field_ids = ["FIN_FIRST NAME", "FIN_TYPE_OF_VENDOR"]
        interactor = CreateFieldsInteractor(storage=storage_mock)
        storage_mock.get_existing_field_ids.return_value = existing_field_ids

        # Act
        interactor.create_fields(field_dtos)

        # Assert
        storage_mock.update_fields.assert_called_once_with(field_dtos)
        get_valid_write_permissions_mock_method.assert_called_once()
        get_valid_read_permissions_mock_method.assert_called_once()