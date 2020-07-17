import pytest

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.create_or_update_gofs import CreateOrUpdateGoFsInteractor
from ib_tasks.interactors.storage_interfaces.dtos import GoFRoleDTO, \
    GoFRoleWithIdDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.tests.factories.storage_dtos import (
    CompleteGoFDetailsDTOFactory, GoFDTOFactory, GoFRolesDTOFactory,
    GoFRoleWithIdDTOFactory
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
            get_all_valid_read_permission_roles,
            get_all_valid_write_permission_roles
        )
        get_valid_read_permissions_mock_method = \
            get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = \
            get_all_valid_write_permission_roles(mocker)

        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory()
        ]
        gof_dtos = [
            complete_gof_details_dto.gof_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        template_ids = [gof_dto.task_template_id for gof_dto in gof_dtos]
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        storage_mock.get_valid_template_ids_in_given_template_ids.return_value = template_ids
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        interactor.create_or_update_gofs(
            complete_gof_details_dtos=complete_gof_details_dtos
        )

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        get_valid_write_permissions_mock_method.assert_called_once()
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
        from ib_tasks.exceptions.custom_exceptions import GOFIdCantBeEmpty
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
        storage_mock.update_gof_roles.assert_not_called()

    @pytest.mark.parametrize("gof_display_name", [None, "", "   "])
    def test_create_or_update_gofs_with_invalid_gof_display_name_field_raise_exception(
            self, gof_display_name, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            GOFDisplayNameCantBeEmpty
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
        storage_mock.update_gof_roles.assert_not_called()

    @pytest.mark.parametrize("read_permission_roles", [None, []])
    def test_create_or_update_gofs_with_empty_gof_read_permission_roles_raise_exception(
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
        storage_mock.update_gof_roles.assert_not_called()

    def test_create_or_update_gofs_with_invalid_gof_order_values_raises_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidOrderValues
        gof_dto = GoFDTOFactory(order=-2)
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(gof_dto=gof_dto)
        ]
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidOrderValues) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()
        storage_mock.update_gof_roles.assert_not_called()

    @pytest.mark.parametrize("write_permission_roles", [None, []])
    def test_create_or_update_gofs_with_empty_write_permission_roles_raise_exception(
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
        storage_mock.update_gof_roles.assert_not_called()

    def test_create_or_update_gofs_with_invalid_read_permission_roles_raises_exception(
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
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidReadPermissionRoles) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()
        storage_mock.update_gof_roles.assert_not_called()

    def test_create_or_update_gofs_with_invalid_write_permission_roles_raises_exception(
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
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidWritePermissionRoles) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        get_valid_write_permissions_mock_method.assert_called_once()
        storage_mock.create_gofs.assert_not_called()
        storage_mock.create_gof_roles.assert_not_called()
        storage_mock.update_gofs.assert_not_called()
        storage_mock.update_gof_roles.assert_not_called()

    def test_create_or_upate_gofs_with_invalid_task_template_id_raises_exception(
            self, storage_mock, mocker
    ):

        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service import (
            get_all_valid_read_permission_roles,
            get_all_valid_write_permission_roles
        )
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidTaskTemplateIds
        get_valid_read_permissions_mock_method = \
            get_all_valid_read_permission_roles(mocker)
        get_valid_write_permissions_mock_method = \
            get_all_valid_write_permission_roles(mocker)

        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory()
        ]
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = []
        storage_mock.get_valid_template_ids_in_given_template_ids.return_value = []
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidTaskTemplateIds) as err:
            interactor.create_or_update_gofs(
                complete_gof_details_dtos=complete_gof_details_dtos
            )

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        get_valid_write_permissions_mock_method.assert_called_once()
        storage_mock.update_gofs.assert_not_called()
        storage_mock.update_gof_roles.assert_not_called()

    def test_create_or_update_gofs_with_already_existing_gof_ids_and_new_gof_ids_crates_and_updates_gofs(
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

        request_details_dto = GoFDTOFactory()
        request_details_roles_dto = GoFRolesDTOFactory()
        vendor_details_dto = GoFDTOFactory()
        vendor_details_roles_dto = GoFRolesDTOFactory()

        complete_gof_details_dtos = [
            CompleteGoFDetailsDTOFactory(
                gof_dto=request_details_dto,
                gof_roles_dto=request_details_roles_dto
            ),
            CompleteGoFDetailsDTOFactory(
                gof_dto=vendor_details_dto,
                gof_roles_dto=vendor_details_roles_dto
            )
        ]
        gof_dtos = [
            complete_gof_details_dto.gof_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        template_ids = [gof_dto.task_template_id for gof_dto in gof_dtos]
        storage_mock.get_existing_gof_ids_in_given_gof_ids.return_value = [
            request_details_dto.gof_id
        ]
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
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
        gof_role_with_id_dtos = [
            GoFRoleWithIdDTOFactory(
                gof_id=gof_role_dto.gof_id,
                role=gof_role_dto.role
            )
            for gof_role_dto in gof_role_dtos
        ]
        storage_mock.get_roles_for_given_gof_ids.return_value = gof_role_with_id_dtos
        storage_mock.get_valid_template_ids_in_given_template_ids.return_value = template_ids
        interactor = CreateOrUpdateGoFsInteractor(storage=storage_mock)

        # Act
        interactor.create_or_update_gofs(
            complete_gof_details_dtos=complete_gof_details_dtos
        )

        # Assert
        get_valid_read_permissions_mock_method.assert_called_once()
        get_valid_write_permissions_mock_method.assert_called_once()

        gof_dtos_for_creation = [vendor_details_dto]
        gof_dtos_for_updation = [request_details_dto]
        gof_role_dtos_for_creation = [
            gof_role_dto
            for gof_role_dto in gof_role_dtos
            if gof_role_dto.gof_id == vendor_details_roles_dto.gof_id
        ]
        gof_role_dtos_for_updation = [
            gof_role_dto
            for gof_role_dto in gof_role_dtos
            if gof_role_dto.gof_id == request_details_dto.gof_id
        ]
        storage_mock.create_gofs.assert_called_once_with(
            gof_dtos=gof_dtos_for_creation
        )
        storage_mock.create_gof_roles.assert_called_once_with(
            gof_role_dtos=gof_role_dtos_for_creation
        )
        storage_mock.update_gofs.assert_called_once_with(
            gof_dtos=gof_dtos_for_updation
        )
        storage_mock.update_gof_roles.assert_called_once_with(
            gof_role_with_id_dtos=gof_role_with_id_dtos
        )
