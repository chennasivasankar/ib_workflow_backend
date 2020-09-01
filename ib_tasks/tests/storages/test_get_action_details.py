import pytest

from ib_tasks.adapters.dtos import ProjectRolesDTO
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory, \
    StageActionFactory, ActionPermittedRolesFactory, \
    StageActionWithTransitionFactory, TaskTemplateFactory, TaskFactory


@pytest.mark.django_db
class TestGetActionDetails:

    @pytest.fixture()
    def populate_data(self):
        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        stages = StageModelFactory.create_batch(size=3)
        TaskFactory.create_batch(size=10, project_id="project_id_1")
        ActionPermittedRolesFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        actions = StageActionWithTransitionFactory.create_batch(size=3, stage=stages[0])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])
        actions = StageActionWithTransitionFactory.create_batch(size=3, stage=stages[1])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])
        actions = StageActionWithTransitionFactory.create_batch(size=3, stage=stages[2])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])

    @pytest.fixture()
    def populate_data_with_all_roles(self):
        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        stages = StageModelFactory.create_batch(size=3)
        ActionPermittedRolesFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        actions = StageActionWithTransitionFactory.create_batch(size=3, stage=stages[0])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])
        actions = StageActionWithTransitionFactory.create_batch(size=3, stage=stages[1])
        ActionPermittedRolesFactory(action=actions[0], role_id="ALL_ROLES")
        ActionPermittedRolesFactory(action=actions[1], role_id="ALL_ROLES")
        ActionPermittedRolesFactory(action=actions[2], role_id="ALL_ROLES")
        actions = StageActionWithTransitionFactory.create_batch(size=3, stage=stages[2])
        ActionPermittedRolesFactory(action=actions[0], role_id="ALL_ROLES")
        ActionPermittedRolesFactory(action=actions[1], role_id="ALL_ROLES")
        ActionPermittedRolesFactory(action=actions[2], role_id="ALL_ROLES")

    def test_get_action_details(self,
                                populate_data,
                                snapshot):
        # Arrange
        action_ids = [1, 2, 3, 4]
        storage = ActionsStorageImplementation()

        # Act
        response = storage.get_actions_details(action_ids=action_ids)

        # Assert
        snapshot.assert_match(response, "response")

    def test_get_action_details_when_no_actions(self,
                                                populate_data,
                                                snapshot):
        # Arrange
        action_ids = []
        storage = ActionsStorageImplementation()

        # Act
        response = storage.get_actions_details(action_ids=action_ids)

        # Assert
        snapshot.assert_match(response, "response")

    def test_get_permitted_action_ids_given_stage_ids(self,
                                                      populate_data,
                                                      snapshot):
        # Arrange
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]
        user_roles = ["role_1", "role_2", "role_3", "role_4"]
        storage = ActionsStorageImplementation()

        # Act
        response = storage.get_permitted_action_ids_given_stage_ids(
            stage_ids=stage_ids, user_roles=user_roles)

        # Assert
        snapshot.assert_match(response, "response")

    def test_get_permitted_action_ids_for_given_task_stages(self,
                                                            populate_data,
                                                            snapshot):
        # Arrange
        user_roles = [
            ProjectRolesDTO(
                project_id="project_id_1",
                roles=["role_1", "role_2", "role_3", "role_4"]),
            ProjectRolesDTO(
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
