import pytest
import factory

from ib_tasks.tests.factories.storage_dtos import (
    CompleteGoFDetailsDTOFactory, GoFDTOFactory, GoFRolesDTOFactory
)


class TestCreateOrUpdateGoFsInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        CompleteGoFDetailsDTOFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        GoFRolesDTOFactory.reset_sequence(1)

    @pytest.fixture
    def interactor(self):
        from ib_tasks.interactors.create_or_update_gofs import \
            CreateOrUpdateGoFsInteractor
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        storage = TasksStorageImplementation()
        interactor = CreateOrUpdateGoFsInteractor(storage)
        return interactor

    @pytest.mark.parametrize("gof_id", [None, "", "  "])
    def test_create_or_update_gofs_interactor_with_empty_gof_ids(
            self, interactor, gof_id, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import GOFIdCantBeEmpty
        gof_dtos = GoFDTOFactory.create_batch(size=2, gof_id=gof_id)
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_dto=factory.Iterator(gof_dtos)
        )

        # Act
        with pytest.raises(GOFIdCantBeEmpty) as err:
            interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        snapshot.assert_match(
            name="empty_gof_id_message", value=str(err.value)
        )

    @pytest.mark.parametrize("gof_display_name", [None, "", "  "])
    def test_create_or_update_gofs_interactor_with_empty_gof_display_names(
            self, interactor, gof_display_name, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            GOFDisplayNameCantBeEmpty
        gof_dtos = GoFDTOFactory.create_batch(
            size=2, gof_display_name=gof_display_name
        )
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_dto=factory.Iterator(gof_dtos)
        )

        # Act
        with pytest.raises(GOFDisplayNameCantBeEmpty) as err:
            interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        snapshot.assert_match(
            name="empty_gof_display_name_message", value=str(err.value)
        )

    @pytest.mark.parametrize("max_columns", [None, "", "  "])
    def test_create_or_update_gofs_interactor_with_empty_gof_max_columns(
            self, interactor, max_columns, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            MaxColumnsCantBeEmpty
        gof_dtos = GoFDTOFactory.create_batch(
            size=2, max_columns=max_columns
        )
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_dto=factory.Iterator(gof_dtos)
        )

        # Act
        with pytest.raises(MaxColumnsCantBeEmpty) as err:
            interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        snapshot.assert_match(
            name="empty_gof_max_columns_message", value=str(err.value)
        )

    @pytest.mark.parametrize("max_columns", [0, -1])
    def test_create_or_update_gofs_interactor_with_invalid_max_columns_value(
            self, interactor, max_columns, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            MaxColumnsMustBeAPositiveInteger
        gof_dtos = GoFDTOFactory.create_batch(
            size=2, max_columns=max_columns
        )
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_dto=factory.Iterator(gof_dtos)
        )

        # Act
        with pytest.raises(MaxColumnsMustBeAPositiveInteger) as err:
            interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        snapshot.assert_match(
            name="invalid_max_columns_message", value=str(err.value)
        )

    def test_create_or_update_gofs_interactor_with_a_string_as_max_columns_value(
            self, interactor, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            MaxColumnsMustBeANumber
        gof_dtos = GoFDTOFactory.create_batch(
            size=2, max_columns="two"
        )
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_dto=factory.Iterator(gof_dtos)
        )

        # Act
        with pytest.raises(MaxColumnsMustBeANumber) as err:
            interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        snapshot.assert_match(
            name="max_columns_as_string_error_message", value=str(err.value)
        )

    @pytest.mark.parametrize("read_permissions", [None, []])
    def test_create_or_update_gofs_interactor_with_empty_read_permissions(
            self, interactor, read_permissions, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            GOFReadPermissionsCantBeEmpty
        gof_roles_dtos = GoFRolesDTOFactory.create_batch(
            size=2, read_permission_roles=read_permissions
        )
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_roles_dto=factory.Iterator(gof_roles_dtos)
        )

        # Act
        with pytest.raises(GOFReadPermissionsCantBeEmpty) as err:
            interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        snapshot.assert_match(
            name="empty_gof_read_permission_roles_message",
            value=str(err.value)
        )

    @pytest.mark.parametrize("write_permissions", [None, []])
    def test_create_or_update_gofs_interactor_with_empty_write_permissions(
            self, interactor, write_permissions, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            GOFWritePermissionsCantBeEmpty
        gof_roles_dtos = GoFRolesDTOFactory.create_batch(
            size=2, write_permission_roles=write_permissions
        )
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_roles_dto=factory.Iterator(gof_roles_dtos)
        )

        # Act
        with pytest.raises(GOFWritePermissionsCantBeEmpty) as err:
            interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        snapshot.assert_match(
            name="empty_gof_write_permission_roles_message",
            value=str(err.value)
        )

    def test_create_or_update_gofs_interactor_with_invalid_read_permission_roles(
            self, interactor, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidReadPermissionRoles
        gof_roles_dtos = GoFRolesDTOFactory.create_batch(
            size=2, read_permission_roles=["Payment Requestor"]
        )
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_roles_dto=factory.Iterator(gof_roles_dtos)
        )

        # Act
        with pytest.raises(InvalidReadPermissionRoles) as err:
            interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        snapshot.assert_match(
            name="invalid_gof_read_permission_roles_message",
            value=str(err.value)
        )

    def test_create_or_update_gofs_interactor_with_invalid_write_permission_roles(
            self, interactor, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidWritePermissionRoles
        gof_roles_dtos = GoFRolesDTOFactory.create_batch(
            size=2, write_permission_roles=["Payment Requestor"]
        )
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_roles_dto=factory.Iterator(gof_roles_dtos)
        )

        # Act
        with pytest.raises(InvalidWritePermissionRoles) as err:
            interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        snapshot.assert_match(
            name="invalid_gof_write_permission_roles_message",
            value=str(err.value)
        )
