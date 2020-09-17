import pytest

from ib_tasks.tests.factories.models import StageModelFactory, \
    StageFlowFactory, StageActionFactory


@pytest.mark.django_db
class TestGetAllowedStageIdsOfUser:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageModelFactory.reset_sequence(1)
        StageFlowFactory.reset_sequence()
        StageActionFactory.reset_sequence(1)

    @pytest.fixture()
    def storage(self):
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        return storage

    def expected_response(self):
        from ib_tasks.tests.factories.storage_dtos import StageFlowDTOFactory
        StageFlowDTOFactory.reset_sequence(1)

        return StageFlowDTOFactory.create_batch(2)

    def setup_storage(self):
        stages = StageModelFactory.create_batch(3)
        action_1 = StageActionFactory(stage=stages[0])
        action_2 = StageActionFactory(stage=stages[1])
        StageFlowFactory(previous_stage=stages[0], action=action_1, next_stage=stages[1])
        StageFlowFactory(previous_stage=stages[1], action=action_2, next_stage=stages[2])

    def test_get_stage_flows_to_user(self, storage):

        # Arrange
        stage_ids = [1, 2, 3]
        action_ids = [1, 2, 3]
        self.setup_storage()
        expected = self.expected_response()

        # Act
        result = storage.get_stage_flows_to_user(
            stage_ids=stage_ids, action_ids=action_ids
        )

        # Assert
        assert result == expected

    def test_returns_empty_stage_roles(self, storage):
        # Arrange
        stage_ids = []
        action_ids = []
        expected = []

        # Act
        result = storage.get_stage_flows_to_user(
            stage_ids=stage_ids, action_ids=action_ids
        )

        # Assert
        assert result == expected
