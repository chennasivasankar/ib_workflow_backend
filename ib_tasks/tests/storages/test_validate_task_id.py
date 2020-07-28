import pytest


@pytest.mark.django_db
class TestValidateTaskId:

    def test_giuevn_valid_task_returns_true(self):
        # Arrange
        task_id = 1
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation

        from ib_tasks.tests.factories.models import TaskModelFactory
        TaskModelFactory.reset_sequence(0)
        storage = StorageImplementation()
        TaskModelFactory()
        expected = True

        # Act
        response = storage.validate_task_id(task_id=task_id)

        # Assert
        assert response == expected

    def test_given_invalid_task_returns_false(self):
        # Arrange
        task_id = 2
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation
        from ib_tasks.tests.factories.models import TaskModelFactory
        TaskModelFactory.reset_sequence(0)
        storage = StorageImplementation()
        TaskModelFactory()
        expected = False

        # Act
        response = storage.validate_task_id(task_id=task_id)

        # Assert
        assert response == expected
