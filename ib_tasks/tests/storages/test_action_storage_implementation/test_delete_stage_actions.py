import pytest

from ib_tasks.models import StageAction
from ib_tasks.tests.factories.models import StageActionFactory
from ib_tasks.tests.factories.storage_dtos import StageActionsDTOFactory


@pytest.mark.django_db
class TestDeleteStageActions:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageActionsDTOFactory.reset_sequence(4)
        StageActionFactory.reset_sequence()

    @pytest.fixture()
    def stage_actions_dtos(self):
        return StageActionsDTOFactory.create_batch(size=4)

    @pytest.fixture()
    def create_stage_actions(self):
        StageActionFactory.create_batch(size=4)

    def test_with_action_details_deletes_action(
            self, storage, stage_actions_dtos, create_stage_actions):
        # Arrange
        action_ids = [8, 5, 6, 7]
        empty_list = []

        # Act
        storage.delete_stage_actions(stage_actions_dtos)

        # Assert
        result = list(StageAction.objects.filter(id__in=action_ids))
        assert result == empty_list
