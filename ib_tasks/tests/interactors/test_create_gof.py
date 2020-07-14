import pytest

from ib_tasks.interactors.create_gofs import CreateGOF
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.tests.factories.storage_dtos import GOFDTOFactory


class TestCreateGOF:

    @pytest.fixture
    def storage_mock(self):
        from mock import create_autospec
        storage_mock = create_autospec(StorageInterface)
        return storage_mock

    def test_create_gofs(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTOFactory()
        ]
        storage_mock.get_valid_read_permission_roles.return_value = [
            "ALL_ROLES"
        ]
        storage_mock.get_valid_write_permission_roles.return_value = [
            "ALL_ROLES"
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_called_once_with(gof_dtos=gof_dtos)

    def test_create_gofs_without_gof_id_field_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFIdCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(gof_id=None)
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFIdCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_gof_id_field_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFIdCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(gof_id="")
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFIdCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_without_gof_display_name_field_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFDisplayNameCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(gof_display_name=None)
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFDisplayNameCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_gof_display_name_field_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFDisplayNameCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(gof_display_name="")
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFDisplayNameCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_without_gof_read_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFReadPermissionsCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(read_permission_roles=None)
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFReadPermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_read_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFReadPermissionsCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(read_permission_roles="")
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFReadPermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_list_of_read_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFReadPermissionsCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(read_permission_roles=[])
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFReadPermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_without_write_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFWritePermissionsCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(write_permission_roles=None)
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFWritePermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_write_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFWritePermissionsCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(write_permission_roles="")
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFWritePermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_list_of_write_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFWritePermissionsCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(write_permission_roles=[])
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFWritePermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_without_field_ids_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFFieldIdsCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(field_ids=None)
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFFieldIdsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_list_of_field_ids_raise_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFFieldIdsCantBeEmpty
        gof_dtos = [
            GOFDTOFactory(field_ids=[])
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFFieldIdsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_duplicate_field_ids_raises_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import DuplicatedFieldIds
        gof_dtos = [
            GOFDTOFactory(field_ids=["FIN_PAYMENT_REQUESTOR", "FIN_PAYMENT_REQUESTOR"])
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(DuplicatedFieldIds) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_invalid_read_permission_roles_raises_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import InvalidReadPermissionRoles
        gof_dtos = [
            GOFDTOFactory(read_permission_roles="all roles")
        ]
        storage_mock.get_valid_read_permission_roles.return_value = [
            "ALL_ROLES"
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(InvalidReadPermissionRoles) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.get_valid_read_permission_roles.assert_called_once()
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_invalid_list_of_read_permission_roles_raises_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import InvalidReadPermissionRoles
        gof_dtos = [
            GOFDTOFactory(read_permission_roles=["payment requestor"])
        ]
        storage_mock.get_valid_read_permission_roles.return_value = [
            "ALL_ROLES"
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(InvalidReadPermissionRoles) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.get_valid_read_permission_roles.assert_called_once()
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_invalid_write_permission_roles_raises_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import InvalidWritePermissionRoles
        gof_dtos = [
            GOFDTOFactory(write_permission_roles="all roles")
        ]
        storage_mock.get_valid_read_permission_roles.return_value = [
            "ALL_ROLES"
        ]
        storage_mock.get_valid_write_permission_roles.return_value = [
            "ALL_ROLES"
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(InvalidWritePermissionRoles) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.get_valid_write_permission_roles.assert_called_once()
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_invalid_list_of_write_permission_roles_raises_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import InvalidWritePermissionRoles
        gof_dtos = [
            GOFDTOFactory(write_permission_roles=["payment requester"])
        ]
        storage_mock.get_valid_read_permission_roles.return_value = [
            "ALL_ROLES"
        ]
        storage_mock.get_valid_write_permission_roles.return_value = [
            "ALL_ROLES"
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(InvalidWritePermissionRoles) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.get_valid_read_permission_roles.assert_called_once()
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_different_display_names_for_same_gof_id_raises_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import DifferentDisplayNamesForSameGOF
        gof_dtos = [
            GOFDTOFactory(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details"
            ),
            GOFDTOFactory(field_ids=["FIN_SALUATION"]),
            GOFDTOFactory(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Data"
            )
        ]
        storage_mock.get_valid_read_permission_roles.return_value = [
            "ALL_ROLES"
        ]
        storage_mock.get_valid_write_permission_roles.return_value = [
            "ALL_ROLES"
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(DifferentDisplayNamesForSameGOF) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()