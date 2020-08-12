import pytest

from ib_tasks.tests.factories.models import StageModelFactory


@pytest.mark.django_db
class TestGetAllowedStageIdsOfUser:

    @pytest.fixture()
    def create_stages(self):
        from ib_tasks.tests.factories.models import StagePermittedRolesFactory
        StageModelFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence(1)
        StagePermittedRolesFactory.create_batch(size=3, role_id='ROLE_1')

    def test_get_stage_actions(self, create_stages):
        # Arrange
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        user_roles = ["ROLE_1", "ROLE_2", "ROLE_3"]
        # Act
        result = storage.get_permitted_stage_ids(user_roles)

        # Assert
        assert result == ['stage_id_0', 'stage_id_1', 'stage_id_2']

    def test_returns_empty_stage_roles(self):
        # Arrange
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        user_roles = ["ROLE_1", "ROLE_2", "ROLE_3"]
        expected = []
        # Act
        result = storage.get_permitted_stage_ids(user_roles)

        # Assert
        assert result == expected
