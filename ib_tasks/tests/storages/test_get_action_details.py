import pytest

from ib_tasks.storages.fields_storage_implementation import FieldsStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory, StageActionFactory, ActionPermittedRolesFactory


@pytest.mark.django_db
class TestGetActionDetails:

    @pytest.fixture()
    def populate_data(self):
        StageModelFactory.reset_sequence()
        stages = StageModelFactory.create_batch(size=3)
        ActionPermittedRolesFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        actions = StageActionFactory.create_batch(size=3, stage=stages[0])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])
        actions = StageActionFactory.create_batch(size=3, stage=stages[1])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])
        actions = StageActionFactory.create_batch(size=3, stage=stages[2])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])

    @pytest.fixture()
    def populate_data_with_all_roles(self):
        StageModelFactory.reset_sequence()
        stages = StageModelFactory.create_batch(size=3)
        ActionPermittedRolesFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        actions = StageActionFactory.create_batch(size=3, stage=stages[0])
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[0])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[1])
        ActionPermittedRolesFactory.reset_sequence()
        ActionPermittedRolesFactory.create_batch(size=4, action=actions[2])
        actions = StageActionFactory.create_batch(size=3, stage=stages[1])
        ActionPermittedRolesFactory(action=actions[0], role_id="ALL_ROLES")
        ActionPermittedRolesFactory(action=actions[1], role_id="ALL_ROLES")
        ActionPermittedRolesFactory(action=actions[2], role_id="ALL_ROLES")
        actions = StageActionFactory.create_batch(size=3, stage=stages[2])
        ActionPermittedRolesFactory(action=actions[0], role_id="ALL_ROLES")
        ActionPermittedRolesFactory(action=actions[1], role_id="ALL_ROLES")
        ActionPermittedRolesFactory(action=actions[2], role_id="ALL_ROLES")

    def test_get_action_details(self,
                                populate_data,
                                snapshot):
        # Arrange
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]
        user_roles = ["role_1", "role_2", "role_3", "role_4"]
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_actions_details(stage_ids=stage_ids,
                                               user_roles=user_roles)

        # Assert
        snapshot.assert_match(response, "response")

    def test_given_stage_ids_has_no_permitted_actions(self,
                                                      populate_data,
                                                      snapshot):
        # Arrange
        stage_ids = ["stage_id_1", "stage_id_2", "stage_id_3"]
        user_roles = ["role_10", "role_12", "role_13", "role_14"]
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_actions_details(stage_ids=stage_ids,
                                               user_roles=user_roles)

        # Assert
        snapshot.assert_match(response, "response")

    def test_get_action_details_when_action_has_all_roles_permission(
            self, snapshot,
            populate_data_with_all_roles):
        # Arrange
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]
        user_roles = ["role_1", "role_2", "role_3", "role_4"]
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_actions_details(stage_ids=stage_ids,
                                               user_roles=user_roles)

        # Assert
        snapshot.assert_match(response, "response")
