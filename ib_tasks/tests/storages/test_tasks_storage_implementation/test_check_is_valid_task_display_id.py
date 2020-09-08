import pytest


@pytest.mark.django_db
class TestCheckIsValidTaskDisplayId:

    def test_check_is_valid_task_display_id_with_invalid_task_display_id_returns_false(
            self, storage):
        # Arrange
        task_display_id = "iB_001"

        # Act
        result = storage.check_is_valid_task_display_id(
            task_display_id=task_display_id)

        # Assert
        assert result is False

    def test_check_is_valid_task_display_id_with_valid_task_display_id_returns_true(
            self, storage):
        # Arrange
        task_display_id = "iB_001"
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.create(task_display_id=task_display_id)

        # Act
        result = storage.check_is_valid_task_display_id(
            task_display_id=task_display_id)

        # Assert
        assert result is True

    def test_get_task_id_for_task_display_id_returns_task_id(self, storage):
        # Arrange
        expected_task_id = 1
        task_display_id = "iB_001"
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.create(task_display_id=task_display_id)

        # Act
        result = storage.check_is_valid_task_display_id(
            task_display_id=task_display_id)

        # Assert
        assert result == expected_task_id
