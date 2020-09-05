import pytest

from ib_tasks.models import StageAction
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.tests.factories.models import StageActionFactory, \
    StageModelFactory
from ib_tasks.tests.factories.storage_dtos import StageActionsDTOFactory


@pytest.mark.django_db
class TestGetStageActions:
    @pytest.fixture()
    def create_stage_actions(self):
        StageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageActionFactory.create_batch(size=3)

    @pytest.fixture()
    def expected_output(self):
        StageActionsDTOFactory.reset_sequence()
        return StageActionsDTOFactory.create_batch(size=3)

    def test_get_stage_actions(self, snapshot,
                               create_stage_actions, expected_output):
        # Arrange
        stage_ids = ["stage_id_3", "stage_id_1", "stage_id_2", "stage_id_0"]
        storage = ActionsStorageImplementation()

        # Act
        result = storage.get_stage_action_names(stage_ids=stage_ids)

        # Assert
        stages = StageAction.objects.filter(stage__stage_id__in=stage_ids)
        snapshot.assert_match(result, "result")
