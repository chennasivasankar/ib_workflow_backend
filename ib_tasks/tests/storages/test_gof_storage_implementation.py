import factory
import pytest

from ib_tasks.models import GoFRole
from ib_tasks.tests.factories.models import GoFFactory, TaskTemplateWithTransitionFactory, \
    GoFRoleFactory, FieldFactory, TaskTemplateWith2GoFsFactory
from ib_tasks.tests.factories.storage_dtos import (
    GoFDTOFactory,
    GoFRolesDTOFactory,
    CompleteGoFDetailsDTOFactory,
    FieldCompleteDetailsDTOFactory
)
from ib_tasks.tests.factories.storage_dtos \
    import GoFRoleDTOFactory


@pytest.mark.django_db
class TestGoFStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.gof_storage_implementation import \
            GoFStorageImplementation
        return GoFStorageImplementation()

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        GoFFactory.reset_sequence(1)
        TaskTemplateWithTransitionFactory.reset_sequence(1)
        FieldFactory.reset_sequence(1)
        GoFRoleFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        GoFRolesDTOFactory.reset_sequence(1)
        CompleteGoFDetailsDTOFactory.reset_sequence(1)
        GoFRoleDTOFactory.reset_sequence(1)
        FieldCompleteDetailsDTOFactory.reset_sequence(1)

    def test_get_gof_ids_with_read_permission_for_user(self, storage, reset_sequence):
        # Arrange
        from ib_tasks.tests.factories.models import GoFRoleFactory
        expected_output = ['gof_2', 'gof_3']
        expected_roles = ['FIN_MAN']
        GoFRoleFactory.create_batch(size=2, role="ALL_ROLES")

        # Act
        result = storage.get_gof_ids_with_read_permission_for_user(
            roles=expected_roles
        )

        # Assert
        assert result == expected_output

    def test_get_valid_gof_ids_in_given_gof_ids(self, storage):
        # Arrange
        template_id = "FIN_VENDOR"
        gof_ids = ['gof_1', 'gof_3']
        expected_gof_ids = ['gof_1']
        TaskTemplateWith2GoFsFactory(template_id=template_id)

        # Act
        valid_gof_ids = \
            storage.get_valid_gof_ids_in_given_gof_ids(gof_ids=gof_ids)

        # Assert
        assert valid_gof_ids == expected_gof_ids

    def test_get_existing_gof_ids_in_given_gof_ids(
            self, storage
    ):
        # Arrange
        gofs = GoFFactory.create_batch(size=2)
        gof_ids = ["gof_1", "gof_2", "gof_3"]
        expected_existing_gof_ids = [gof.gof_id for gof in gofs]

        # Act
        actual_existing_gof_ids = \
            storage.get_existing_gof_ids_in_given_gof_ids(
                gof_ids=gof_ids
            )

        # Assert
        assert expected_existing_gof_ids == actual_existing_gof_ids

    def test_create_gofs(self, storage):
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

    def test_create_gof_roles(self, storage):

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

    def test_update_gofs(self, storage):

        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory
        from ib_tasks.tests.factories.models import GoFFactory
        gofs = GoFFactory.create_batch(size=2)

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

    def test_delete_gof_roles(self, storage):

        # Arrange
        gof_roles = GoFRoleFactory.create_batch(size=2)
        gof_ids = [gof_role.gof_id for gof_role in gof_roles]

        # Act
        storage.delete_gof_roles(gof_ids=gof_ids)

        # Assert
        gof_roles = list(GoFRole.objects.filter(gof_id__in=gof_ids))
        assert gof_roles == []

    def test_get_gof_dtos_for_given_gof_ids(self, storage):

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
