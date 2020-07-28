import pytest


@pytest.mark.django_db
class TestGetAllowedStageIdsOfUser:
    @pytest.fixture()
    def create_stages(self):
        from ib_tasks.tests.factories.models import StageModelFactory
        StageModelFactory.create_batch(size=3)

    def test_get_stage_actions(self, create_stages):
        # Arrange
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()

        # Act
        result = storage.get_allowed_stage_ids_of_user()

        # Assert
        assert result == stage_ids
