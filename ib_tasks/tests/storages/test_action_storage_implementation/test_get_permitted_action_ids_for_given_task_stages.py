import pytest

from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskProjectRolesDTO
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

    def test_get_permitted_action_ids_for_given_task_stages(
            self, populate_data, snapshot):
        # Arrange
        user_roles = [
            TaskProjectRolesDTO(
                task_id=1,
                project_id="project_id_1",
                roles=["role_1", "role_2", "role_3", "role_4"]),
            TaskProjectRolesDTO(
                task_id=2,
                project_id="project_id_1",
                roles=["role_1", "role_2", "role_3", "role_4"])
        ]
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]
        storage = ActionsStorageImplementation()

        # Act
        response = storage.get_permitted_action_ids_for_given_task_stages(
            stage_ids=stage_ids, user_project_roles=user_roles)

        # Assert
        snapshot.assert_match(response, "response")
