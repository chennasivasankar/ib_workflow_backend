import pytest
from freezegun import freeze_time


@pytest.mark.django_db
class TestGetDueMissedCount:

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

    def test_get_task_due_missed_count(self, populate_data):
        # Arrange
        expected_output = 4
        task_id = 1
        stage_id = "stage_id_0"
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        from ib_tasks.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        # Act
        result = storage.get_due_missed_count(task_id=task_id,
                                              stage_id=stage_id,
                                              user_id=user_id)

        # Assert
        assert result == expected_output