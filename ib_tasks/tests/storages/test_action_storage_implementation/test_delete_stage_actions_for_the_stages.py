import pytest

from ib_tasks.models import StageAction, ActionPermittedRoles
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory, \
    StageActionFactory
from ib_tasks.tests.factories.storage_dtos import StageActionsDTOFactory


@pytest.mark.django_db
class TestDeleteStageActions:
    @pytest.fixture()
    def stage_actions_dtos(self):
        StageActionsDTOFactory.reset_sequence(4)
        return StageActionsDTOFactory.create_batch(size=4)

    @pytest.fixture()
    def create_stage_actions(self):
        StageActionFactory.reset_sequence()
        StageActionFactory.create_batch(size=4)

    def test_with_action_details_deletes_action(
            self, stage_actions_dtos, create_stage_actions):
        # Arrange
        action_ids = [8, 5, 6, 7]
        storage = ActionsStorageImplementation()
        empty_list = []

        # Act
        storage.delete_stage_actions(stage_actions_dtos)

        # Assert
        result = list(StageAction.objects.filter(id__in=action_ids))
        assert result == empty_list
