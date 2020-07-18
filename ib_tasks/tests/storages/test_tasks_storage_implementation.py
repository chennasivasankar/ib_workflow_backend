import factory
import pytest

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.tests.factories.models import GoFFactory, TaskTemplateFactory, \
    GoFRoleFactory, FieldFactory
from ib_tasks.tests.factories.storage_dtos import GoFRoleDTOFactory, \
    GoFRoleWithIdDTOFactory, GoFDTOFactory, GoFRolesDTOFactory, \
    CompleteGoFDetailsDTOFactory


@pytest.mark.django_db
class TestTasksStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        return TasksStorageImplementation()

    @pytest.fixture
    def reset_sequence(self):
        GoFFactory.reset_sequence(1)
        TaskTemplateFactory.reset_sequence(1)
        FieldFactory.reset_sequence(1)
        GoFRoleFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        GoFRolesDTOFactory.reset_sequence(1)
        CompleteGoFDetailsDTOFactory.reset_sequence(1)
        GoFRoleDTOFactory.reset_sequence(1)
        GoFRoleWithIdDTOFactory.reset_sequence(1)

    def test_get_existing_gof_ids_in_given_gof_ids(
            self, storage, reset_sequence
    ):
        # Arrange
        GoFFactory.create_batch(size=2)
        gof_ids = ["GOF_ID-1", "GOF_ID-2", "GOF_ID-3"]
        expected_existing_gof_ids = ["GOF_ID-1", "GOF_ID-2"]

        # Act
        actual_existing_gof_ids = \
            storage.get_existing_gof_ids_in_given_gof_ids(
                gof_ids=gof_ids
            )

        # Assert
        assert expected_existing_gof_ids == actual_existing_gof_ids

    def test_create_gofs(self, storage, reset_sequence):
        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory
        gof_dtos = [GoFDTOFactory(), GoFDTOFactory()]

        # Act
        storage.create_gofs(gof_dtos=gof_dtos)

        # Assert
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            assert gof.display_name == gof_dto.gof_display_name
            assert gof.max_columns == gof_dto.max_columns

    def test_create_gof_roles(self, storage, reset_sequence):

        # Arrange
        gof_role_dtos = [
            GoFRoleDTOFactory(), GoFRoleDTOFactory()
        ]
        gof_ids = [
            gof_role_dto.gof_id
            for gof_role_dto in gof_role_dtos
        ]
        GoFFactory.create_batch(size=2, gof_id=factory.Iterator(gof_ids))

        # Act
        storage.create_gof_roles(gof_role_dtos=gof_role_dtos)

        # Assert
        for gof_role_dto in gof_role_dtos:
            gof_role = GoFRole.objects.get(
                gof_id=gof_role_dto.gof_id, role=gof_role_dto.role
            )
            assert gof_role_dto.permission_type == gof_role.permission_type

    def test_update_gofs(self, storage, reset_sequence):

        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory
        from ib_tasks.tests.factories.models import GoFFactory
        gofs = [
            GoFFactory(
                display_name="Request Details",
                max_columns=3
            ),
            GoFFactory(
                display_name="Vendor Type",
                max_columns=4
            )
        ]

        gof_dtos = [
            GoFDTOFactory(
                gof_id=gofs[0].gof_id,
                gof_display_name="details of request",
                max_columns=12
            ),
            GoFDTOFactory(
                gof_id=gofs[1].gof_id,
                gof_display_name="details of vendor",
                max_columns=12
            )
        ]

        # Act
        storage.update_gofs(gof_dtos=gof_dtos)

        # Assert
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            assert gof.display_name == gof_dto.gof_display_name
            assert gof.max_columns == gof_dto.max_columns

    def test_update_gof_roles(self, storage, reset_sequence):

        # Arrange
        gof_roles = GoFRoleFactory.create_batch(size=2)
        gof_role_with_id_dtos = [
            GoFRoleWithIdDTOFactory(
                id=gof_role.id,
                gof_id=gof_role.gof_id,
                role=gof_role.role,
                permission_type=PermissionTypes.WRITE.value
            )
            for gof_role in gof_roles
        ]

        # Act
        storage.update_gof_roles(gof_role_with_id_dtos=gof_role_with_id_dtos)

        # Assert
        for gof_role_with_id_dto in gof_role_with_id_dtos:
            gof_role = GoFRole.objects.get(
                gof_id=gof_role_with_id_dto.gof_id,
                role=gof_role_with_id_dto.role
            )
            assert gof_role_with_id_dto.permission_type == \
                   gof_role.permission_type

    def test_get_roles_for_given_gof_ids(self, storage, reset_sequence):

        # Arrange
        gof_roles = GoFRoleFactory.create_batch(size=2)
        gof_ids = [gof_role.gof_id for gof_role in gof_roles]

        # Act
        actual_gof_role_with_id_dtos = \
            storage.get_roles_for_given_gof_ids(gof_ids=gof_ids)

        # Assert
        for gof_role_with_id_dto in actual_gof_role_with_id_dtos:
            for gof_role in gof_roles:
                if gof_role.id == gof_role_with_id_dto.id:
                    assert gof_role.gof_id == gof_role_with_id_dto.gof_id
                    assert gof_role.role == gof_role_with_id_dto.role
                    assert gof_role.permission_type == \
                           gof_role_with_id_dto.permission_type

    def test_get_gof_dtos_for_given_gof_ids(self, storage, reset_sequence):

        # Arrange
        from ib_tasks.tests.factories.models import GoFFactory
        gofs = GoFFactory.create_batch(size=2)
        gof_ids = [gof.gof_id for gof in gofs]

        # Act
        actual_gof_dtos = storage.get_gof_dtos_for_given_gof_ids(gof_ids)

        # Assert
        for gof_dto in actual_gof_dtos:
            for gof in gofs:
                if gof.gof_id == gof_dto.gof_id:
                    assert gof.display_name == gof_dto.gof_display_name
                    assert gof.max_columns == gof_dto.max_columns
