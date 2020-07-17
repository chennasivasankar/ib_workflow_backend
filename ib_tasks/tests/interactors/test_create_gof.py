
import pytest

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.create_gofs import CreateGoFsInteractor
from ib_tasks.interactors.storage_interfaces.dtos import GoFRoleDTO, \
    GoFFieldDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.tests.factories.storage_dtos import (
    CompleteGoFDetailsDTOFactory, GoFDTOFactory, GoFRolesDTOFactory,
    GoFFieldsDTOFactory
)


class TestCreateGOF:

    @pytest.fixture
    def storage_mock(self):
        from mock import create_autospec
        storage_mock = create_autospec(TaskStorageInterface)
        return storage_mock

    def test_create_gofs_with_valid_details(self, mocker, storage_mock):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_all_valid_read_permission_roles,
            get_all_valid_write_permission_roles
        )
        get_valid_read_permissions_mock_method = \
            get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = \
            get_all_valid_write_permission_roles(mocker)

        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(),
            CompleteGoFDetailsDTOFactory()
        ]
        valid_field_ids = []
        for complete_gof_details_dto in complete_gof_details_dtos:
            valid_field_ids += \
                complete_gof_details_dto.gof_fields_dto.field_ids
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        storage_mock.get_valid_field_ids_in_given_field_ids.return_value = \
            valid_field_ids
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        interactor.create_gofs(
            complete_gof_details_dtos=complete_gof_details_dtos
        )

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        get_valid_write_permissions_mock_method.assert_called_once()
        gof_dtos = [
            complete_gof_details_dto.gof_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        gof_roles_dtos = [
            complete_gof_details_dto.gof_roles_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        gof_role_dtos = []
        for gof_roles_dto in gof_roles_dtos:
            gof_role_dtos += [
                GoFRoleDTO(
                    gof_id=gof_roles_dto.gof_id,
                    role=read_permission_role,
                    permission_type=PermissionTypes.READ
                )
                for read_permission_role in gof_roles_dto.read_permission_roles
            ]
        for gof_roles_dto in gof_roles_dtos:
            gof_role_dtos += [
                GoFRoleDTO(
                    gof_id=gof_roles_dto.gof_id,
                    role=write_permission_role,
                    permission_type=PermissionTypes.WRITE
                )
                for write_permission_role in (
                    gof_roles_dto.write_permission_roles
                )
            ]
        gof_fields_dtos = [
            complete_gof_details_dto.gof_fields_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        gof_field_dtos = []
        for gof_fields_dto in gof_fields_dtos:
            for gof_field_id in gof_fields_dto.field_ids:
                gof_field_dtos.append(
                    GoFFieldDTO(
                        gof_id=gof_fields_dto.gof_id,
                        field_id=gof_field_id
                    )
                )
        storage_mock.create_gofs.assert_called_once_with(gof_dtos=gof_dtos)
        storage_mock.create_gof_roles.assert_called_once_with(
            gof_role_dtos=gof_role_dtos
        )
        storage_mock.create_gof_fields.assert_called_once_with(
            gof_field_dtos=gof_field_dtos
        )

    @pytest.mark.parametrize("gof_id", [None, ""])
    def test_create_gofs_with_invalid_gof_id_field_raise_exception(
            self, storage_mock, gof_id
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFIdCantBeEmpty
        gof_dto = GoFDTOFactory(gof_id=gof_id)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_dto=gof_dto)
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFIdCantBeEmpty) as err:
            interactor.create_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.create_gof_fields.assert_not_called()

    @pytest.mark.parametrize("gof_display_name", [None, ""])
    def test_create_gofs_with_invalid_gof_display_name_field_raise_exception(
            self, gof_display_name, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            GOFDisplayNameCantBeEmpty
        gof_dto = GoFDTOFactory(gof_display_name=gof_display_name)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_dto=gof_dto)
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFDisplayNameCantBeEmpty) as err:
            interactor.create_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.create_gof_fields.assert_not_called()

    @pytest.mark.parametrize("read_permission_roles", [None, []])
    def test_create_gofs_with_empty_gof_read_permission_roles_raise_exception(
            self, storage_mock, read_permission_roles
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            GOFReadPermissionsCantBeEmpty
        gof_roles_dto = GoFRolesDTOFactory(
            read_permission_roles=read_permission_roles
        )
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_roles_dto=gof_roles_dto)
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFReadPermissionsCantBeEmpty) as err:
            interactor.create_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.create_gof_fields.assert_not_called()

    @pytest.mark.parametrize("write_permission_roles", [None, []])
    def test_create_gofs_with_empty_write_permission_roles_raise_exception(
            self, storage_mock, write_permission_roles
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            GOFWritePermissionsCantBeEmpty
        gof_roles_dto = GoFRolesDTOFactory(
            write_permission_roles=write_permission_roles)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_roles_dto=gof_roles_dto)
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFWritePermissionsCantBeEmpty) as err:
            interactor.create_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.create_gof_fields.assert_not_called()

    @pytest.mark.parametrize("field_ids", [None, []])
    def test_create_gofs_with_empty_field_ids_raise_exception(
            self, field_ids, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            GOFFieldIdsCantBeEmpty
        gof_fields_dto = GoFFieldsDTOFactory(field_ids=field_ids)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_fields_dto=gof_fields_dto)
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFFieldIdsCantBeEmpty) as err:
            interactor.create_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.create_gof_fields.assert_not_called()

    def test_create_gofs_with_already_existing_gof_ids_raises_exception(
            self, storage_mock
    ):

        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GoFIDsAlreadyExists
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(),
            CompleteGoFDetailsDTOFactory()
        ]
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = \
            [complete_gof_details_dtos[0].gof_dto.gof_id]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GoFIDsAlreadyExists) as err:
            interactor.create_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.create_gof_fields.assert_not_called()

    def test_create_gofs_with_duplicate_field_ids_raises_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import DuplicatedFieldIds
        gof_fields_dto = GoFFieldsDTOFactory(
            field_ids=["FIN_PAYMENT_REQUESTOR", "FIN_PAYMENT_REQUESTOR"]
        )
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_fields_dto=gof_fields_dto)
        ]
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(DuplicatedFieldIds) as err:
            interactor.create_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.create_gof_fields.assert_not_called()

    def test_create_gofs_with_invalid_field_ids(self, storage_mock):

        # Arrange
        from ib_tasks.exceptions.custom_exceptions import InvalidFieldIds
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(), CompleteGoFDetailsDTOFactory()
        ]
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        storage_mock.get_valid_field_ids_in_given_field_ids.return_value = [
            complete_gof_details_dtos[0].gof_fields_dto.field_ids[0]
        ]
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidFieldIds) as err:
            interactor.create_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.create_gof_fields.assert_not_called()

    def test_create_gofs_with_invalid_read_permission_roles_raises_exception(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidReadPermissionRoles
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_all_valid_read_permission_roles
        )
        get_valid_read_permissions_mock_method = \
            get_all_valid_read_permission_roles(mocker)
        gof_roles_dto = GoFRolesDTOFactory(
            read_permission_roles=["payment requester"]
        )
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_roles_dto=gof_roles_dto)
        ]
        valid_field_ids = []
        for complete_gof_details_dto in complete_gof_details_dtos:
            valid_field_ids += \
                complete_gof_details_dto.gof_fields_dto.field_ids
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        storage_mock.get_valid_field_ids_in_given_field_ids.return_value = \
            valid_field_ids
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidReadPermissionRoles) as err:
            interactor.create_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.create_gof_fields.assert_not_called()

    def test_create_gofs_with_invalid_write_permission_roles_raises_exception(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidWritePermissionRoles
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_all_valid_read_permission_roles,
            get_all_valid_write_permission_roles
        )
        get_valid_read_permissions_mock_method = \
            get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = \
            get_all_valid_write_permission_roles(mocker)
        gof_roles_dto = GoFRolesDTOFactory(
            write_permission_roles=["payment requester"])
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_roles_dto=gof_roles_dto)
        ]
        valid_field_ids = []
        for complete_gof_details_dto in complete_gof_details_dtos:
            valid_field_ids += \
                complete_gof_details_dto.gof_fields_dto.field_ids
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        storage_mock.get_valid_field_ids_in_given_field_ids.return_value = \
            valid_field_ids
        interactor = CreateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidWritePermissionRoles) as err:
            interactor.create_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        get_valid_write_permissions_mock_method.assert_called_once()
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.create_gof_fields.assert_not_called()
