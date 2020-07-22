import pytest
import factory

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.create_or_update_gofs import \
    CreateOrUpdateGoFsInteractor
from ib_tasks.interactors.storage_interfaces.dtos import GoFRoleDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.tests.factories.storage_dtos import (
    CompleteGoFDetailsDTOFactory, GoFDTOFactory, GoFRolesDTOFactory
)


class TestCreateOrUpdateGOFs:

    @pytest.fixture
    def storage_mock(self):
        from mock import create_autospec
        storage_mock = create_autospec(TaskStorageInterface)
        return storage_mock

    def test_create_or_update_gofs_with_valid_details(self, mocker,
                                                      storage_mock):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_valid_role_ids_in_given_role_ids
        )
        get_valid_role_ids_in_given_role_ids_mock_method = \
            get_valid_role_ids_in_given_role_ids(mocker)

        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory()
        ]
        gof_dtos = [
            complete_gof_details_dto.gof_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        interactor.create_or_update_gofs(
            complete_gof_details_dtos=complete_gof_details_dtos
        )

        # Assert
        get_valid_role_ids_in_given_role_ids_mock_method.assert_called_once()
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
                    permission_type=PermissionTypes.READ.value
                )
                for read_permission_role in gof_roles_dto.read_permission_roles
            ]
        for gof_roles_dto in gof_roles_dtos:
            gof_role_dtos += [
                GoFRoleDTO(
                    gof_id=gof_roles_dto.gof_id,
                    role=write_permission_role,
                    permission_type=PermissionTypes.WRITE.value
                )
                for write_permission_role in (
                    gof_roles_dto.write_permission_roles
                )
            ]
        storage_mock.create_gofs.assert_called_once_with(gof_dtos=gof_dtos)
        storage_mock.create_gof_roles.assert_called_once_with(
            gof_role_dtos=gof_role_dtos
        )
        storage_mock.update_gofs.assert_not_called()

    @pytest.mark.parametrize("gof_id", [None, "", "  "])
    def test_create_or_update_gofs_with_invalid_gof_id_field_raise_exception(
            self, storage_mock, gof_id
    ):
        # Arrange
        from ib_tasks.exceptions.gofs_custom_exceptions import GOFIdCantBeEmpty
        gof_dto = GoFDTOFactory(gof_id=gof_id)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_dto=gof_dto)
        ]
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFIdCantBeEmpty) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()

    @pytest.mark.parametrize("gof_display_name", [None, "", "   "])
    def test_create_or_update_gofs_with_invalid_gof_display_name_field_raise_exception(
            self, gof_display_name, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.gofs_custom_exceptions import GOFDisplayNameCantBeEmpty
        gof_dto = GoFDTOFactory(gof_display_name=gof_display_name)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_dto=gof_dto)
        ]
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFDisplayNameCantBeEmpty) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()

    @pytest.mark.parametrize("max_columns", [0, -1])
    def test_create_or_update_gofs_with_invalid_gof_max_coloumns_value_raise_exception(
            self, max_columns, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.columns_custom_exceptions import MaxColumnsMustBeAPositiveInteger
        gof_dto = GoFDTOFactory(max_columns=max_columns)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_dto=gof_dto)
        ]
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(MaxColumnsMustBeAPositiveInteger) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()

    @pytest.mark.parametrize("read_permission_roles", [None, []])
    def test_create_or_update_gofs_with_empty_gof_read_permission_roles_raise_exception(
            self, storage_mock, read_permission_roles
    ):
        # Arrange
        from ib_tasks.exceptions.gofs_custom_exceptions import GOFReadPermissionsCantBeEmpty
        gof_roles_dto = GoFRolesDTOFactory(
            read_permission_roles=read_permission_roles
        )
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_roles_dto=gof_roles_dto)
        ]
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFReadPermissionsCantBeEmpty) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()

    @pytest.mark.parametrize("write_permission_roles", [None, []])
    def test_create_or_update_gofs_with_empty_write_permission_roles_raise_exception(
            self, storage_mock, write_permission_roles
    ):
        # Arrange
        from ib_tasks.exceptions.gofs_custom_exceptions import GOFWritePermissionsCantBeEmpty
        gof_roles_dto = GoFRolesDTOFactory(
            write_permission_roles=write_permission_roles)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_roles_dto=gof_roles_dto)
        ]
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(GOFWritePermissionsCantBeEmpty) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()

    def test_create_or_update_gofs_with_duplicate_write_permission_roles_raise_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            DuplicateWritePermissionRolesForAGoF
        write_permission_roles = ["ALL_ROLES", "ALL_ROLES"]
        gof_roles_dto = GoFRolesDTOFactory(
            write_permission_roles=write_permission_roles)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_roles_dto=gof_roles_dto)
        ]
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(DuplicateWritePermissionRolesForAGoF) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()

    def test_create_or_update_gofs_with_duplicate_read_permission_roles_raise_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            DuplicateReadPermissionRolesForAGoF
        read_permission_roles = ["ALL_ROLES", "ALL_ROLES"]
        gof_roles_dto = GoFRolesDTOFactory(
            read_permission_roles=read_permission_roles)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_roles_dto=gof_roles_dto)
        ]
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(DuplicateReadPermissionRolesForAGoF) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()


    def test_create_or_update_gofs_with_invalid_read_permission_roles_raises_exception(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.exceptions.roles_custom_exceptions import InvalidReadPermissionRoles
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_valid_role_ids_in_given_role_ids
        )
        get_valid_role_ids_in_given_role_ids_mock_method = \
            get_valid_role_ids_in_given_role_ids(mocker)
        gof_roles_dto = GoFRolesDTOFactory(
            read_permission_roles=["payment requester"]
        )
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_roles_dto=gof_roles_dto)
        ]
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidReadPermissionRoles) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        get_valid_role_ids_in_given_role_ids_mock_method.assert_called_once()
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()

    def test_create_or_update_gofs_with_invalid_write_permission_roles_raises_exception(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.exceptions.roles_custom_exceptions import InvalidWritePermissionRoles
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_valid_role_ids_in_given_role_ids
        )
        get_valid_role_ids_in_given_role_ids_mock_method = \
            get_valid_role_ids_in_given_role_ids(mocker)
        gof_roles_dto = GoFRolesDTOFactory(
            write_permission_roles=["payment requester"])
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_roles_dto=gof_roles_dto)
        ]
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidWritePermissionRoles) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        get_valid_role_ids_in_given_role_ids_mock_method.assert_called_once()
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()

    def test_create_or_update_gofs_with_already_existing_gof_ids_updates_gofs(
            self, storage_mock, mocker
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_valid_role_ids_in_given_role_ids
        )
        get_valid_role_ids_in_given_role_ids_mock_method = \
            get_valid_role_ids_in_given_role_ids(mocker)

        gof_dtos = GoFDTOFactory.create_batch(size=2)
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
        gof_roles_dtos = GoFRolesDTOFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_ids)
        )

        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_dto=factory.Iterator(gof_dtos),
            gof_roles_dto=factory.Iterator(gof_roles_dtos)
        )
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = gof_ids
        gof_role_dtos = []
        for gof_roles_dto in gof_roles_dtos:
            gof_role_dtos += [
                GoFRoleDTO(
                    gof_id=gof_roles_dto.gof_id,
                    role=read_permission_role,
                    permission_type=PermissionTypes.READ.value
                )
                for read_permission_role in gof_roles_dto.read_permission_roles
            ]
        for gof_roles_dto in gof_roles_dtos:
            gof_role_dtos += [
                GoFRoleDTO(
                    gof_id=gof_roles_dto.gof_id,
                    role=write_permission_role,
                    permission_type=PermissionTypes.WRITE.value
                )
                for write_permission_role in (
                    gof_roles_dto.write_permission_roles
                )
            ]
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        interactor.create_or_update_gofs(
            complete_gof_details_dtos=complete_gof_details_dtos
        )

        # Assert
        get_valid_role_ids_in_given_role_ids_mock_method.assert_called_once()
        storage_mock.update_gofs.assert_called_once_with(
            gof_dtos=gof_dtos
        )
        storage_mock.create_gof_roles.assert_called_once_with(
            gof_role_dtos=gof_role_dtos
        )
