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

    @freeze_time("2020-08-10 12:30:56")
    def test_get_due_details_of_task_given_task_id(self, populate_data,
                                                   snapshot):
        # Arrange
        task_id = 1
        stage_id = 1
        storage = StorageImplementation()

        # Act
        response = storage.get_task_due_details(task_id, stage_id)

        # Assert
        snapshot.assert_match(response, "due_details")

    @freeze_time("2020-08-10 12:30:56")
    def test_get_due_details_of_task_when_task_has_no_delays(self, snapshot):
        # Arrange
        TaskFactory.reset_sequence()
        tasks = TaskFactory.create_batch(size=3)
        stage_id = 1
        TaskStageHistoryModelFactory.reset_sequence()
        TaskStageHistoryModelFactory(task=tasks[0])
        task_id = 1
        storage = StorageImplementation()

        # Act
        response = storage.get_task_due_details(task_id, stage_id)

        # Assert
        snapshot.assert_match(response, "due_details")
