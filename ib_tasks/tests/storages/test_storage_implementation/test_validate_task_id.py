import pytest
from freezegun import freeze_time

from ib_tasks.storages.storage_implementation import StorageImplementation
from ib_tasks.tests.factories.models import TaskFactory, \
    TaskDueDetailsFactory, \
    TaskStageHistoryModelFactory, StageModelFactory, TaskStageModelFactory


@pytest.mark.django_db
class TestValidateTaskId:

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
