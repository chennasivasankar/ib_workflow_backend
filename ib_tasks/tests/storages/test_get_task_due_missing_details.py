import pytest

from ib_tasks.storages.storage_implementation import StorageImplementation
from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestGetTaskDueMissingDetails:

    @pytest.fixture()
    def populate_data(self):
        TaskFactory.reset_sequence()
        TaskFactory.create_batch(size=3)

    def test_validate_task_id_given_valid_task_id(self, populate_data):
        # Arrange
        task_id = 1
        expected_response = True
        storage = StorageImplementation()

        # Act
        response = storage.validate_task_id(task_id)

        # Assert
        assert response == expected_response

    def test_validate_task_id_given_invalid_task_id(self):
        # Arrange
        task_id = 1
        expected_response = False
        storage = StorageImplementation()

        # Act
        response = storage.validate_task_id(task_id)

        # Assert
        assert response == expected_response

    def test_validate_if_task_is_assigned_to_user_when_user_is_assigend(
            self, populate_data):
        # Arrange
        task_id = 1
        user_id = "user_id_1"
        storage = StorageImplementation()
        expected_response = True

        # Act
        response = storage.validate_if_task_is_assigned_to_user(task_id, user_id)

        # Assert
        assert response == expected_response
