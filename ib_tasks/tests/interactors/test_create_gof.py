import pytest

from ib_tasks.exceptions.custom_exceptions import GOFIdCantBeEmpty, GOFDisplayNameCantBeEmpty, \
    GOFReadPermissionsCantBeEmpty, GOFWritePermissionsCantBeEmpty, GOFFieldIdsCantBeEmpty, DuplicatedFieldIds
from ib_tasks.interactors.create_gofs import CreateGOF
from ib_tasks.interactors.storage_interfaces.dtos import GOFDTO
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface


class TestCreateGOF:

    @pytest.fixture
    def storage_mock(self):
        from mock import create_autospec
        storage_mock = create_autospec(StorageInterface)
        return storage_mock

    def test_create_gofs(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details",
                read_permission_roles="ALL_ROLES",
                write_permission_roles="ALL_ROLES",
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_called_once_with(gof_dtos=gof_dtos)

    def test_create_gofs_without_gof_id_field_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id=None,
                gof_display_name="Request Details",
                read_permission_roles="ALL_ROLES",
                write_permission_roles="ALL_ROLES",
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFIdCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_gof_id_field_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="",
                gof_display_name="Request Details",
                read_permission_roles="ALL_ROLES",
                write_permission_roles="ALL_ROLES",
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFIdCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_without_gof_display_name_field_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name=None,
                read_permission_roles="ALL_ROLES",
                write_permission_roles="ALL_ROLES",
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFDisplayNameCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_gof_display_name_field_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="",
                read_permission_roles="ALL_ROLES",
                write_permission_roles="ALL_ROLES",
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFDisplayNameCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_without_gof_read_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details",
                read_permission_roles=None,
                write_permission_roles="ALL_ROLES",
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFReadPermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_read_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details",
                read_permission_roles="",
                write_permission_roles="ALL_ROLES",
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFReadPermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_list_of_read_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details",
                read_permission_roles=[],
                write_permission_roles="ALL_ROLES",
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFReadPermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_without_write_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details",
                read_permission_roles="ALL_ROLES",
                write_permission_roles=None,
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFWritePermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_write_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details",
                read_permission_roles="ALL_ROLES",
                write_permission_roles="",
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFWritePermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_list_of_write_permission_roles_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details",
                read_permission_roles="ALL_ROLES",
                write_permission_roles=[],
                field_ids=["FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFWritePermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_without_field_ids_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details",
                read_permission_roles="ALL_ROLES",
                write_permission_roles="ALL_ROLES",
                field_ids=None
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFFieldIdsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_empty_list_of_field_ids_raise_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details",
                read_permission_roles="ALL_ROLES",
                write_permission_roles="ALL_ROLES",
                field_ids=[]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(GOFFieldIdsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_duplicate_field_ids_raises_exception(self, storage_mock):
        # Arrange
        gof_dtos = [
            GOFDTO(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details",
                read_permission_roles="ALL_ROLES",
                write_permission_roles="ALL_ROLES",
                field_ids=["FIN_PAYMENT_REQUESTOR", "FIN_PAYMENT_REQUESTOR"]
            )
        ]
        interactor = CreateGOF(storage=storage_mock)

        # Act
        with pytest.raises(DuplicatedFieldIds) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()