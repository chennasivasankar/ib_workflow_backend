import pytest
import factory

from ib_tasks.tests.factories.storage_dtos import (
    CompleteGoFDetailsDTOFactory, GoFDTOFactory, GoFRolesDTOFactory
)
from ib_tasks.tests.factories.models import GoFFactory, GoFRoleFactory


@pytest.mark.django_db
class TestPopulateGoFs:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        CompleteGoFDetailsDTOFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        GoFRolesDTOFactory.reset_sequence(1)
        GoFFactory.reset_sequence(1)
        GoFRoleFactory.reset_sequence(1)

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
    def test_populate_gofs_with_empty_gof_ids(
            self, interactor, gof_id, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.gofs_custom_exceptions import GOFIdCantBeEmpty
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
    def test_populate_gofs_with_empty_gof_display_names(
            self, interactor, gof_display_name, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.gofs_custom_exceptions import GOFDisplayNameCantBeEmpty
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

    @pytest.mark.parametrize("max_columns", [0, -1])
    def test_populate_gofs_with_invalid_max_columns_value(
            self, interactor, max_columns, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.columns_custom_exceptions import MaxColumnsMustBeAPositiveInteger
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

    @pytest.mark.parametrize("read_permissions", [None, []])
    def test_populate_gofs_with_empty_read_permissions(
            self, interactor, read_permissions, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.gofs_custom_exceptions import GOFReadPermissionsCantBeEmpty
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
    def test_populate_gofs_with_empty_write_permissions(
            self, interactor, write_permissions, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.gofs_custom_exceptions import GOFWritePermissionsCantBeEmpty
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

    def test_populate_gofs_with_invalid_read_permission_roles(
            self, interactor, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.roles_custom_exceptions import InvalidReadPermissionRoles
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

    def test_populate_gofs_with_invalid_write_permission_roles(
            self, interactor, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.roles_custom_exceptions import InvalidWritePermissionRoles
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

    def test_populate_gofs_with_valid_details(
            self, interactor, snapshot
    ):
        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.models.gof_role import GoFRole
        from ib_tasks.constants.enum import PermissionTypes
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=3
        )
        gof_dtos = [
            complete_gof_details_dto.gof_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        gof_roles_dtos = [
            complete_gof_details_dto.gof_roles_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]

        # Act
        interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        gof_counter = 1
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            snapshot.assert_match(
                name="gof_id {}".format(gof_counter),
                value=gof.gof_id
            )
            snapshot.assert_match(
                name="gof_display_name {}".format(gof_counter),
                value=gof.display_name
            )
            snapshot.assert_match(
                name="gof_max_columns {}".format(gof_counter),
                value=gof.max_columns
            )
            gof_counter += 1

        read_permission_role_counter, write_permission_role_counter = 1, 1
        for gof_roles_dto in gof_roles_dtos:
            for gof_read_permission_role in gof_roles_dto.read_permission_roles:
                gof_role_object = GoFRole.objects.get(
                    gof_id=gof_roles_dto.gof_id, role=gof_read_permission_role,
                    permission_type=PermissionTypes.READ.value
                )
                snapshot.assert_match(
                    name="gof_id_in_gof_role {}".format(
                        read_permission_role_counter),
                    value=gof_role_object.gof_id
                )
                snapshot.assert_match(
                    name="gof_read_permission_role {}".format(read_permission_role_counter),
                    value=gof_role_object.role
                )
                snapshot.assert_match(
                    name="read_role_permission_type {}".format(
                        read_permission_role_counter),
                    value=gof_role_object.permission_type
                )
                read_permission_role_counter += 1
            for gof_write_permission_role in gof_roles_dto.read_permission_roles:
                gof_role_object = GoFRole.objects.get(
                    gof_id=gof_roles_dto.gof_id,
                    role=gof_write_permission_role,
                    permission_type=PermissionTypes.WRITE.value
                )
                snapshot.assert_match(
                    name="gof_id_in_gof_role {}".format(
                        write_permission_role_counter),
                    value=gof_role_object.gof_id
                )
                snapshot.assert_match(
                    name="gof_write_permission_role {}".format(write_permission_role_counter),
                    value=gof_role_object.role
                )
                snapshot.assert_match(
                    name="write_role_permission_type {}".format(
                        write_permission_role_counter),
                    value=gof_role_object.permission_type
                )
                write_permission_role_counter += 1

    def test_populate_gofs_with_already_existing_gofs_updates_gofs(
            self, interactor, snapshot
    ):
        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.constants.enum import PermissionTypes
        from ib_tasks.models.gof_role import GoFRole
        gofs = GoFFactory.create_batch(size=2)
        gof_ids = [gof.gof_id for gof in gofs]
        gof_dtos = GoFDTOFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_ids)
        )
        complete_gof_details_dtos = CompleteGoFDetailsDTOFactory.create_batch(
            size=2, gof_dto=factory.Iterator(gof_dtos)
        )
        complete_gof_details_dtos += CompleteGoFDetailsDTOFactory.create_batch(
            size=2
        )
        gof_dtos = [
            complete_gof_details_dto.gof_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        gof_roles_dtos = [
            complete_gof_details_dto.gof_roles_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]

        # Act
        interactor.create_or_update_gofs(complete_gof_details_dtos)

        # Assert
        gof_counter = 1
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            snapshot.assert_match(
                name="gof_id {}".format(gof_counter),
                value=gof.gof_id
            )
            snapshot.assert_match(
                name="gof_display_name {}".format(gof_counter),
                value=gof.display_name
            )
            snapshot.assert_match(
                name="gof_max_columns {}".format(gof_counter),
                value=gof.max_columns
            )
            gof_counter += 1

        read_permission_role_counter, write_permission_role_counter = 1, 1
        for gof_roles_dto in gof_roles_dtos:
            for gof_read_permission_role in gof_roles_dto.read_permission_roles:
                gof_role_object = GoFRole.objects.get(
                    gof_id=gof_roles_dto.gof_id, role=gof_read_permission_role,
                    permission_type=PermissionTypes.READ.value
                )
                snapshot.assert_match(
                    name="gof_id_in_gof_role {}".format(
                        read_permission_role_counter),
                    value=gof_role_object.gof_id
                )
                snapshot.assert_match(
                    name="gof_read_permission_role {}".format(read_permission_role_counter),
                    value=gof_role_object.role
                )
                snapshot.assert_match(
                    name="read_role_permission_type {}".format(
                        read_permission_role_counter),
                    value=gof_role_object.permission_type
                )
                read_permission_role_counter += 1
            for gof_write_permission_role in gof_roles_dto.read_permission_roles:
                gof_role_object = GoFRole.objects.get(
                    gof_id=gof_roles_dto.gof_id,
                    role=gof_write_permission_role,
                    permission_type=PermissionTypes.WRITE.value
                )
                snapshot.assert_match(
                    name="gof_id_in_gof_role {}".format(
                        write_permission_role_counter),
                    value=gof_role_object.gof_id
                )
                snapshot.assert_match(
                    name="gof_write_permission_role {}".format(write_permission_role_counter),
                    value=gof_role_object.role
                )
                snapshot.assert_match(
                    name="write_role_permission_type {}".format(
                        write_permission_role_counter),
                    value=gof_role_object.permission_type
                )
                write_permission_role_counter += 1
