import datetime

import pytest
from freezegun import freeze_time


@pytest.mark.django_db
class TestGetUserMissedTaskDueTime:

    @pytest.fixture
    @freeze_time("2020-10-12 4:40")
    def populate_data(self):
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.reset_sequence()
        task = TaskFactory()
        from ib_tasks.tests.factories.models import StageModelFactory
        StageModelFactory.reset_sequence()
        stage = StageModelFactory()
        from ib_tasks.tests.factories.models import TaskStageHistoryFactory
        TaskStageHistoryFactory.reset_sequence()
        TaskStageHistoryFactory(stage=stage, task=task)
        from ib_tasks.tests.factories.models import TaskDueDetailsFactory
        TaskDueDetailsFactory.reset_sequence()
        TaskDueDetailsFactory.create_batch(size=4, stage=stage, task=task,
                                           user_id="123e4567-e89b-12d3-a456-426614174000")
        from ib_tasks.tests.factories.models import UserRpInTaskStageFactory
        UserRpInTaskStageFactory.reset_sequence()
        UserRpInTaskStageFactory.create_batch(size=4, task=task, stage=stage)

    @freeze_time("2020-10-12 4:40")
    def test_get_task_due_date(self, populate_data):
        # Arrange
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        task_id = 1
        expected_output = datetime.datetime(2020, 10, 22, 4, 40)
        stage_id = 1

        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        storage = TasksStorageImplementation()

        # Act
        result = storage.get_user_missed_the_task_due_time(task_id, user_id,
                                                           stage_id)

        # Assert
        assert result == expected_output
