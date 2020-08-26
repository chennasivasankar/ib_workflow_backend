import pytest


@pytest.mark.django_db
class TestGetTaskDueMissingCount:
    @pytest.fixture
    def populate_data(self):
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.reset_sequence()
        task = TaskFactory()
        from ib_tasks.tests.factories.models import StageModelFactory
        StageModelFactory.reset_sequence()
        stage = StageModelFactory()
        from ib_tasks.tests.factories.models import TaskDueDetailsFactory
        TaskDueDetailsFactory.reset_sequence()
        TaskDueDetailsFactory.create_batch(size=4, stage=stage, task=task,
                                           user_id="123e4567-e89b-12d3-a456-426614174000")

    def test_get_task_due_missed_count(self, populate_data):
        # Arrange
        expected_output = 4
        task_id = 1
        stage_id = "stage_id_0"
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        from ib_tasks.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()

        # Act
        result = storage.get_due_missed_count(task_id=task_id,
                                              stage_id=stage_id, user_id=user_id)

        # Assert
        assert result == expected_output


@pytest.mark.django_db
class TestGetUserTeamId:
    @pytest.fixture
    def populate_data(self):
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.reset_sequence()
        from ib_tasks.tests.factories.models import TaskStageHistoryFactory
        TaskStageHistoryFactory.reset_sequence()
        TaskStageHistoryFactory()

    def test_get_user_team_id(self, populate_data):
        # Arrange
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        task_id = 1
        expected_output = "TEAM_ID_0"

        from ib_tasks.storages.tasks_storage_implementation import TasksStorageImplementation
        storage = TasksStorageImplementation()

        # Act
        result = storage.get_user_team_id(user_id, task_id)

        # Assert
        assert result == expected_output
