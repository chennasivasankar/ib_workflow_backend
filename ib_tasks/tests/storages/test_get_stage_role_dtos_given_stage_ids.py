import pytest

from ib_tasks.tests.factories.models import StageRoleFactory
from ib_tasks.tests.factories.storage_dtos import StageRoleDTOFactory


@pytest.mark.django_db
class TestGetStageRoles:
    @pytest.fixture()
    def stage_role_objs(self):
        StageRoleFactory.reset_sequence()
        stage_role_objs = StageRoleFactory.create_batch(2)
        return stage_role_objs

    @pytest.fixture()
    def stage_role_dtos(self):
        StageRoleDTOFactory.reset_sequence()
        stage_role_dtos = StageRoleDTOFactory.create_batch(2)
        return stage_role_dtos

    def test_get_stage_role_dtos_given_stage_ids(self, stage_role_objs,
                                                 stage_role_dtos):
        # Arrange

        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        # Act
        expected_result = storage.get_stage_role_dtos_given_stage_ids(
            stage_ids=[stage_role_objs[0].stage__stage_id,
                       stage_role_objs[1].stage__stage_id])
        assert stage_role_dtos == expected_result
