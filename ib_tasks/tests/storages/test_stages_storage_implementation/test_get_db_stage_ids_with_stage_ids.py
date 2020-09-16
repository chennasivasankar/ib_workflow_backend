import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation


@pytest.mark.django_db
class TestGetDBStageIdsWithStageIds:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import StageFactory
        StageFactory.reset_sequence()

    def test_when_stage_ids_exists_returns_dtos(self, snapshot):
        # Arrange
        from ib_tasks.tests.factories.models import StageFactory
        stages = StageFactory.create_batch(size=2)

        stage_ids = [stage.stage_id for stage in stages]
        storage = StagesStorageImplementation()

        # Act
        response = storage.get_db_stage_ids_with_stage_ids_dtos(
            stage_ids=stage_ids)

        # Assert
        snapshot.assert_match(response, "db_stage_ids_with_stage_ids_dtos")

    def test_when_stage_ids_not_exists_returns_empty_dtos(self, snapshot):
        # Arrange
        stage_ids = ["stage_4"]
        storage = StagesStorageImplementation()

        # Act
        response = storage.get_db_stage_ids_with_stage_ids_dtos(
            stage_ids=stage_ids)

        # Assert
        snapshot.assert_match(response, "db_stage_ids_with_stage_ids_dtos")
