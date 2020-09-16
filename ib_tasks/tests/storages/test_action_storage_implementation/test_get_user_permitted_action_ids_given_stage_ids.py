import pytest
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory, \
    StageActionFactory, ActionPermittedRolesFactory


@pytest.mark.django_db
class TestGetActionDetails:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence(1)

    @pytest.fixture
    def populate_data(self, reset_sequence):
        stages = StageModelFactory.create_batch(size=3)
        action_1 = StageActionFactory(stage=stages[0])
        action_2 = StageActionFactory(stage=stages[1])
        action_3 = StageActionFactory(stage=stages[2])
        ActionPermittedRolesFactory(action=action_1)
        ActionPermittedRolesFactory(action=action_2)
        ActionPermittedRolesFactory(action=action_3)

    def test_get_permitted_action_ids_for_given_stage_ids(
            self, populate_data):
        # Arrange
        user_roles = [
            "role_1", "role_2"
        ]
        expected_action_ids = [1, 2]
        stage_ids = [1, 2, 3]
        storage = ActionsStorageImplementation()

        # Act
        response = storage.get_user_permitted_action_ids_given_stage_ids(
            stage_ids=stage_ids, user_roles=user_roles)

        # Assert
        assert response == expected_action_ids

    def test_get_empty_action_ids_for_given_stage_ids(
            self, populate_data):
        # Arrange
        user_roles = [
            "role_9", "role_8"
        ]
        expected_action_ids = []
        stage_ids = [1, 2, 3]
        storage = ActionsStorageImplementation()

        # Act
        response = storage.get_user_permitted_action_ids_given_stage_ids(
            stage_ids=stage_ids, user_roles=user_roles)

        # Assert
        assert response == expected_action_ids

    def test_get_action_ids_for_given_stage_ids(
            self, populate_data):
        # Arrange
        expected_action_ids = [1, 2, 3]
        stage_ids = [1, 2, 3]
        storage = ActionsStorageImplementation()

        # Act
        response = storage.get_action_ids_given_stage_ids(
            stage_ids=stage_ids)

        # Assert
        assert response == expected_action_ids