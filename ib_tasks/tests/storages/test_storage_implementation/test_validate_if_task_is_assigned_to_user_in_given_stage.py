import pytest
from freezegun import freeze_time

from ib_tasks.storages.storage_implementation import StorageImplementation
from ib_tasks.tests.factories.models import TaskFactory, \
    TaskDueDetailsFactory, \
    TaskStageHistoryModelFactory, StageModelFactory, TaskStageModelFactory


@pytest.mark.django_db
class TestGetTaskDueMissingDetails:

    @pytest.fixture()
    @freeze_time("2020-08-10 12:30:56")
    def populate_data(self):
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        stage = StageModelFactory()
        tasks = TaskFactory.create_batch(size=3)
        TaskStageModelFactory.reset_sequence()
        TaskStageModelFactory(task=tasks[0])
        TaskDueDetailsFactory.reset_sequence()
        TaskStageHistoryModelFactory.reset_sequence()
        TaskStageHistoryModelFactory.create_batch(size=5, task=tasks[0],
                                                  stage=stage)
        TaskDueDetailsFactory.create_batch(task=tasks[0], size=2, count=1,
                                           stage=stage)
        TaskDueDetailsFactory.create_batch(task=tasks[0], size=2, reason_id=-1,
                                           count=1)

    def test_validate_if_task_is_assigned_to_user_when_user_is_assigned_to_task(
            self, populate_data):
        # Arrange
        task_id = 1
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        stage_id = 1
        storage = StorageImplementation()
        expected_response = True

        # Act
        response = storage.validate_if_task_is_assigned_to_user_in_given_stage(
            task_id, user_id, stage_id)

        # Assert
        assert response == expected_response

    def test_validate_if_task_is_assigned_to_user_when_user_is_not_assigned_to_task(
            self, populate_data):
        # Arrange
        task_id = 1
        user_id = "user_id_1"
        stage_id = 1
        storage = StorageImplementation()
        expected_response = False

        # Act
        response = storage.validate_if_task_is_assigned_to_user_in_given_stage(
            task_id, user_id, stage_id)

        # Assert
        assert response == expected_response
