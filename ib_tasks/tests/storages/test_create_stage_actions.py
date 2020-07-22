import pytest

from ib_tasks.models import StageAction, ActionPermittedRoles
from ib_tasks.storages.action_storage_implementation import ActionsStorageImplementation
from ib_tasks.tests.factories.interactor_dtos import ActionDTOFactory
from ib_tasks.tests.factories.models import StageModelFactory


@pytest.mark.django_db
class TestCreateStageActions:
    @pytest.fixture()
    def stage_actions_dtos(self):
        ActionDTOFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=4)
        return ActionDTOFactory.create_batch(size=4)


    def test_with_action_details_creates_action(self, stage_actions_dtos, snapshot):
        # Arrange
        action_ids = [1, 2, 3, 4]
        storage = ActionsStorageImplementation()

        # Act
        storage.create_stage_actions(stage_actions_dtos)

        # Assert
        actions = StageAction.objects.filter(id__in=action_ids).values()
        roles = ActionPermittedRoles.objects.filter(action_id__in=action_ids).values()
        snapshot.assert_match(roles, "roles")
        snapshot.assert_match(actions, "stage_actions")
