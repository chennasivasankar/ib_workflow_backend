import pytest

from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory, \
    StageActionFactory, ActionPermittedRolesFactory, \
    StageActionWithTransitionFactory, TaskTemplateFactory, TaskFactory, \
    TaskStageModelFactory


@pytest.mark.django_db
class TestGetPermittedActionIdsInGivenStageIds:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        TaskStageModelFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()

    @pytest.fixture()
    def populate_data(self):
        stages = StageModelFactory.create_batch(size=3)
        tasks = TaskFactory.create_batch(size=10, project_id="project_id_1")
        TaskStageModelFactory(task=tasks[0], stage=stages[0])
        TaskStageModelFactory(task=tasks[1], stage=stages[1])
        TaskStageModelFactory(task=tasks[1])
        actions = StageActionWithTransitionFactory.create_batch(
            size=3, stage=stages[0])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])
        actions = StageActionWithTransitionFactory.create_batch(
            size=3, stage=stages[1])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])
        actions = StageActionWithTransitionFactory.create_batch(
            size=3, stage=stages[2])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])

    def test_get_permitted_action_ids_given_stage_ids(
            self, populate_data, snapshot):
        # Arrange
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]
        user_roles = ["role_1", "role_2", "role_3", "role_4"]
        storage = ActionsStorageImplementation()

        # Act
        response = storage.get_permitted_action_ids_given_stage_ids(
            stage_ids=stage_ids, user_roles=user_roles)

        # Assert
        snapshot.assert_match(response, "response")
