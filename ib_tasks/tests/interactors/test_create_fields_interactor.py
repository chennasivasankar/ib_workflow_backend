from unittest.mock import create_autospec, Mock

import pytest

from ib_tasks.tests.factories.interactor_dtos import FieldDTOFactory

from ib_tasks.interactors.create_fields_ineractor import CreateFieldsInteractor


class TestCreateFieldsInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.create_fields_storage_interface \
            import CreateFieldsStorageInterface
        storage = create_autospec(CreateFieldsStorageInterface)
        return storage

    def test_given_field_id_is_empty_raise_exception(self, storage_mock):
        # Arrange
        field_dtos = [FieldDTOFactory(), FieldDTOFactory(field_id="")]
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


    def test_given_field_display_name_as_empty_rise_exception(
            self, storage_mock
    ):
        # Arrange
        field_dtos = [
            FieldDTOFactory(),
            FieldDTOFactory(),
            FieldDTOFactory(field_display_name=""),
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
            self, storage_mock
    ):
        # Arrange
        avaliable_roles = ["FIN_PAYMENTS_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER"]
        FieldDTOFactory.reset_sequence(1)
        field_dtos = [
            FieldDTOFactory(
                # field_id="field1",
                read_permissions_to_roles=[
                    "FIN_PAYMENTS_RP", "User", "Vendor", "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ]
            ),
            FieldDTOFactory(
                # field_id="filed2",
                read_permissions_to_roles=[
                    "FIN_PAYMENTS_LEVEL1_VERIFIER",
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
        from ib_tasks.exceptions.custom_exceptions import InvalidRolesException
        storage_mock.get_available_roles.return_value = avaliable_roles
        interactor = CreateFieldsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidRolesException) as err:
            interactor.create_fields(field_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.roles == fields_invalid_roles_for_read_permission


    def test_given_invalid_roles_for_write_permissions_raise_exception(
            self, storage_mock
    ):
        # Arrange
        avaliable_roles = ["FIN_PAYMENTS_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER"]
        FieldDTOFactory.reset_sequence(1)
        field_dtos = [
            FieldDTOFactory(
                read_permissions_to_roles=[
                    "FIN_PAYMENTS_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ],
                write_permissions_to_roles=[
                    "FIN_PAYMENTS_RP", "User", "Vendor", "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ]
            ),
            FieldDTOFactory(
                read_permissions_to_roles=[
                    "FIN_PAYMENTS_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ],
                write_permissions_to_roles=[
                    "FIN_PAYMENTS_LEVEL1_VERIFIER",
                    "admin",
                ]
            )
        ]
        fields_invalid_roles_for_write_permission = [
            {
                "field_id": "field1",
                "invalid_roles": ["User", "Vendor"],
                "permissions": "write_permissions",
            },
            {
                "field_id": "field2",
                "permissions": "write_permissions",
                "invalid_roles": ["admin"]
            }
        ]
        from ib_tasks.exceptions.custom_exceptions import InvalidRolesException
        storage_mock.get_available_roles.return_value = avaliable_roles
        interactor = CreateFieldsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidRolesException) as err:
            interactor.create_fields(field_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.roles == fields_invalid_roles_for_write_permission

    def test_given_empty_values_for_read_permissions_raise_exception(
            self, storage_mock
    ):
        # Arrange
        exception_message = "Premissions to roles shouldn't be empty"
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
        exception_message = "Premissions to roles shouldn't be empty"
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

    def test_with_valid_data_populate_fields(
            self, storage_mock
    ):
        # Arrange
        avaliable_roles = ["FIN_PAYMENTS_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER"]
        FieldDTOFactory.reset_sequence(1)
        field_dtos = [
            FieldDTOFactory(),
            FieldDTOFactory(),
            FieldDTOFactory()
        ]
        interactor = CreateFieldsInteractor(storage=storage_mock)
        storage_mock.get_available_roles.return_value = avaliable_roles

        # Act
        interactor.create_fields(field_dtos)

        # Assert
        storage_mock.create_fields.assert_called_once_with(field_dtos)
