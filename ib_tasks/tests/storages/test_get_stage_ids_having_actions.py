import pytest

from ib_tasks.tests.factories.models import StagePermittedRolesFactory, ActionPermittedRolesFactory, StageModelFactory, \
    StageActionFactory


@pytest.mark.django_db
class TestGetStageIdsHavingActions:

    @pytest.fixture()
    def setup(self):
        StagePermittedRolesFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        stages = StageModelFactory.create_batch(2)
        actions = StageActionFactory.create_batch(2, stage=stages[0])
        actions += StageActionFactory.create_batch(2, stage=stages[1])
        StagePermittedRolesFactory(stage=stages[0])
        StagePermittedRolesFactory(stage=stages[1])
        roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"]
        ActionPermittedRolesFactory(action=actions[0], role_id='FIN_PAYMENT_REQUESTER')
        ActionPermittedRolesFactory(action=actions[1], role_id='FIN_PAYMENT_APPROVER')
        ActionPermittedRolesFactory(action=actions[2], role_id='FIN_PAYMENT_REQUESTER')
        ActionPermittedRolesFactory(action=actions[3], role_id='FIN_PAYMENT_APPROVER')


    def test_given_some_roles_returns_stage_ids(self, setup):
        # Arrange

        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        user_roles = ['FIN_PAYMENT_REQUESTER']
        expected_stage_ids = ['stage_id_0']

        # Act
        stage_ids = storage.get_stage_ids_having_actions(user_roles=user_roles)

        # Assert
        assert expected_stage_ids == stage_ids

    def test_given_user_all_roles_returns_stage_ids(self, setup):
        # Arrange

        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        user_roles = ['FIN_PAYMENT_APPROVER']
        expected_stage_ids = ['stage_id_1']

        # Act
        stage_ids = storage.get_stage_ids_having_actions(user_roles=user_roles)

        # Assert
        assert expected_stage_ids == stage_ids

    def test_given_user_some_roles_returns_all_stage_ids(self, setup):
        # Arrange

        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        from ib_tasks.models import StagePermittedRoles
        stage_role = StagePermittedRoles.objects.get(id=1)
        from ib_tasks.constants.constants import ALL_ROLES_ID
        stage_role.role_id = ALL_ROLES_ID
        stage_role.save()
        user_roles = ['FIN_PAYMENT_APPROVER']
        expected_stage_ids = ['stage_id_0', 'stage_id_1']

        # Act
        stage_ids = storage.get_stage_ids_having_actions(user_roles=user_roles)

        # Assert
        assert expected_stage_ids == stage_ids