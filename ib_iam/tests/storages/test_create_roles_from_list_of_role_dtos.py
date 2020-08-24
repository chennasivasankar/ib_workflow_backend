import pytest

from ib_iam.models.project_role import ProjectRole
from ib_iam.storages.roles_storage_implementation import RolesStorageImplementation


class TestCreateRoles:
    @pytest.mark.django_db
    def test_create_roles_given_role_dtos_then_store_roles_in_db(self):
        # Arrange
        storage = RolesStorageImplementation()
        previous_storage_len = ProjectRole.objects.count()
        objects_count = 3
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_for_role_dto_factory
        reset_sequence_for_role_dto_factory()
        role_dtos = RoleDTOFactory.create_batch(objects_count)

        # Act
        storage.create_roles(role_dtos=role_dtos)

        # Assert
        current_storage_len = ProjectRole.objects.count()
        no_of_objects_created = current_storage_len - previous_storage_len
        expeected_role_objs = ProjectRole.objects.all()
        assert no_of_objects_created == objects_count
        for role_dto, role_obj in zip(role_dtos, expeected_role_objs):
            self._compare_role_ids(role_dto.role_id, role_obj.role_id)

    @staticmethod
    def _compare_role_ids(role_id1, role_id2):
        assert role_id1 == role_id2
