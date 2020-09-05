import pytest

from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory, \
    StageActionFactory, ActionPermittedRolesFactory, \
    StageActionWithTransitionFactory, TaskTemplateFactory, TaskFactory, \
    TaskStageModelFactory


@pytest.mark.django_db
class TestGetActionDetails:

    @pytest.fixture()
    def populate_data(self):
        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskFactory.reset_sequence()
        stages = StageModelFactory.create_batch(size=3)
        tasks = TaskFactory.create_batch(size=10, project_id="project_id_1")
        ActionPermittedRolesFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        TaskStageModelFactory.reset_sequence()
        TaskStageModelFactory(task=tasks[0], stage=stages[0])
        TaskStageModelFactory(task=tasks[1], stage=stages[1])
        TaskStageModelFactory(task=tasks[1])
        actions = StageActionWithTransitionFactory.create_batch(
            size=3, stage=stages[0])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])
        actions = StageActionWithTransitionFactory.create_batch(
            size=3, stage=stages[1])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])
        actions = StageActionWithTransitionFactory.create_batch(
            size=3, stage=stages[2])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])

    def test_get_action_details(self, populate_data, snapshot):
        # Arrange
        action_ids = [1, 2, 3, 4]
        storage = ActionsStorageImplementation()

        # Act
        response = storage.get_actions_details(action_ids=action_ids)

        # Assert
        snapshot.assert_match(response, "response")

    def test_get_action_details_when_no_actions(self, populate_data, snapshot):
        # Arrange
        action_ids = []
        storage = ActionsStorageImplementation()

        # Act
        response = storage.get_actions_details(action_ids=action_ids)

        # Assert
        snapshot.assert_match(response, "response")
