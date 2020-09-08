import pytest

from ib_tasks.tests.factories.models import StageActionFactory


@pytest.mark.django_db
class TestValidateAction:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageActionFactory.reset_sequence()

    def test_given_valid_action_id_returns_true(self, storage):
        # Arrange
        action_id = 1
        StageActionFactory()

        # Act
        is_action_id_exists = storage.validate_action(action_id)

        # Assert
        assert is_action_id_exists is True

    def test_given_invalid_action_id_returns_false(self, storage):
        # Arrange
        action_id = 2
        StageActionFactory()

        # Act
        is_action_id_exists = storage.validate_action(action_id)

        # Assert
        assert is_action_id_exists is False
