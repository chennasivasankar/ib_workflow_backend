import pytest


@pytest.mark.django_db
class TestValidateAction:

    @pytest.fixture
    def action_storage(self):
        from ib_tasks.storages.action_storage_implementation import \
            ActionsStorageImplementation
        action_storage = ActionsStorageImplementation()
        return action_storage

    def test_given_valid_action_id_returns_true(self, action_storage):
        # Arrange
        action_id = 1
        from ib_tasks.tests.factories.models import StageActionFactory
        StageActionFactory()

        # Act
        is_action_id_exists = action_storage.validate_action(action_id)

        # Assert
        assert is_action_id_exists == True

    def test_given_invalid_action_id_returns_false(self, action_storage):
        # Arrange
        action_id = 2
        from ib_tasks.tests.factories.models import StageActionFactory
        StageActionFactory()

        # Act
        is_action_id_exists = action_storage.validate_action(action_id)

        # Assert
        assert is_action_id_exists == False