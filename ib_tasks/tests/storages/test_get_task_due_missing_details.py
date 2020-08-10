import pytest

from ib_tasks.storages.storage_implementation import StorageImplementation
from ib_tasks.tests.factories.models import TaskFactory, TaskStageModelFactory, TaskDueDetailsFactory


@pytest.mark.django_db
class TestGetTaskDueMissingDetails:

    @pytest.fixture()
    def populate_data(self):
        TaskFactory.reset_sequence()
        tasks = TaskFactory.create_batch(size=3)
        TaskStageModelFactory.reset_sequence()
        TaskStageModelFactory(task=tasks[0])
        TaskDueDetailsFactory.reset_sequence()
        TaskDueDetailsFactory.create_batch(task=tasks[0], size=2, count=1)
        TaskDueDetailsFactory.create_batch(task=tasks[0], size=2, reason_id=-1, count=1)

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

    def test_validate_if_task_is_assigned_to_user_when_user_is_assigend_to_task(
            self, populate_data):
        # Arrange
        task_id = 1
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        storage = StorageImplementation()
        expected_response = True

        # Act
        response = storage.validate_if_task_is_assigned_to_user(task_id, user_id)

        # Assert
        assert response == expected_response

    def test_validate_if_task_is_assigned_to_user_when_user_is_not_assigend_to_task(
            self, populate_data):
        # Arrange
        task_id = 1
        user_id = "user_id_1"
        storage = StorageImplementation()
        expected_response = False

        # Act
        response = storage.validate_if_task_is_assigned_to_user(task_id, user_id)

        # Assert
        assert response == expected_response

    def test_get_due_details_of_task_given_task_id(self, populate_data, snapshot):
        # Arrange
        task_id = 1
        storage = StorageImplementation()

        # Act
        response = storage.get_task_due_details(task_id)

        # Assert
        snapshot.assert_match(response, "due_details")

    def test_get_due_details_of_task_when_task_has_no_delays(self, snapshot):
        # Arrange
        TaskFactory.reset_sequence()
        tasks = TaskFactory.create_batch(size=3)
        TaskStageModelFactory.reset_sequence()
        TaskStageModelFactory(task=tasks[0])
        task_id = 1
        storage = StorageImplementation()

        # Act
        response = storage.get_task_due_details(task_id)

        # Assert
        snapshot.assert_match(response, "due_details")
