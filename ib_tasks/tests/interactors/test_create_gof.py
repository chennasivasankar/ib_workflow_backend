from unittest.mock import patch

import pytest

from ib_tasks.adapters.roles_service import RolesService
from ib_tasks.interactors.create_gofs import CreateGoFsInteractor
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory


class TestCreateGOF:

    @pytest.fixture
    def storage_mock(self):
        from mock import create_autospec
        storage_mock = create_autospec(StorageInterface)
        return storage_mock

    def test_create_gofs_with_valid_details(self, mocker, storage_mock):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_all_valid_read_permission_roles, get_all_valid_write_permission_roles
        get_valid_read_permissions_mock_method = get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = get_all_valid_write_permission_roles(mocker)

        gof_dtos = [
            GoFDTOFactory(),
            GoFDTOFactory()
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        get_valid_write_permissions_mock_method.assert_called_once()
        storage_mock.create_gofs.assert_called_once_with(gof_dtos=gof_dtos)

    @pytest.mark.parametrize("gof_id", [None, ""])
    def test_create_gofs_with_invalid_gof_id_field_raise_exception(self, storage_mock, gof_id):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFIdCantBeEmpty
        gof_dtos = [
            GoFDTOFactory(gof_id=gof_id)
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFIdCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    @pytest.mark.parametrize("gof_display_name", [None, ""])
    def test_create_gofs_with_invalid_gof_display_name_field_raise_exception(
            self, gof_display_name, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFDisplayNameCantBeEmpty
        gof_dtos = [
            GoFDTOFactory(gof_display_name=gof_display_name)
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFDisplayNameCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    @pytest.mark.parametrize("read_permission_roles", [None, []])
    def test_create_gofs_with_empty_gof_read_permission_roles_raise_exception(
            self, storage_mock, read_permission_roles
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFReadPermissionsCantBeEmpty
        gof_dtos = [
            GoFDTOFactory(read_permission_roles=None)
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFReadPermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    @pytest.mark.parametrize("write_permission_roles", [None, []])
    def test_create_gofs_with_empty_write_permission_roles_raise_exception(
            self, storage_mock, write_permission_roles
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFWritePermissionsCantBeEmpty
        gof_dtos = [
            GoFDTOFactory(write_permission_roles=write_permission_roles)
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFWritePermissionsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    @pytest.mark.parametrize("field_ids", [None, []])
    def test_create_gofs_with_empty_field_ids_raise_exception(self, field_ids, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFFieldIdsCantBeEmpty
        gof_dtos = [
            GoFDTOFactory(field_ids=field_ids)
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFFieldIdsCantBeEmpty) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_duplicate_field_ids_raises_exception(self, storage_mock):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import DuplicatedFieldIds
        gof_dtos = [
            GoFDTOFactory(field_ids=["FIN_PAYMENT_REQUESTOR", "FIN_PAYMENT_REQUESTOR"])
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(DuplicatedFieldIds) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_invalid_read_permission_roles_raises_exception(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import InvalidReadPermissionRoles
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_all_valid_read_permission_roles, get_all_valid_write_permission_roles
        get_valid_read_permissions_mock_method = get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = get_all_valid_write_permission_roles(mocker)
        gof_dtos = [
            GoFDTOFactory(read_permission_roles=["payment requester"])
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidReadPermissionRoles) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_invalid_write_permission_roles_raises_exception(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import InvalidWritePermissionRoles
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_all_valid_read_permission_roles, get_all_valid_write_permission_roles
        get_valid_read_permissions_mock_method = get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = get_all_valid_write_permission_roles(mocker)
        gof_dtos = [
            GoFDTOFactory(write_permission_roles=["payment requester"])
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidWritePermissionRoles) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        get_valid_write_permissions_mock_method.assert_called_once()
        storage_mock.create_gofs.assert_not_called()

    def test_create_gofs_with_different_display_names_for_same_gof_id_raises_exception(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import DifferentDisplayNamesForSameGOF
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_all_valid_read_permission_roles, get_all_valid_write_permission_roles
        get_valid_read_permissions_mock_method = get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = get_all_valid_write_permission_roles(mocker)
        gof_dtos = [
            GoFDTOFactory(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Details"
            ),
            GoFDTOFactory(field_ids=["FIN_SALUATION"]),
            GoFDTOFactory(
                gof_id="FIN_REQUEST_DETAILS",
                gof_display_name="Request Data"
            )
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(DifferentDisplayNamesForSameGOF) as err:
            interactor.create_gofs(gof_dtos=gof_dtos)

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        get_valid_write_permissions_mock_method.assert_called_once()
        storage_mock.create_gofs.assert_not_called()