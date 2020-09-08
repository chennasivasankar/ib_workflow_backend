import pytest


@pytest.mark.django_db
class TestGetUserTeamId:
    @pytest.fixture
    def populate_data_for_user_team(self):
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.reset_sequence()
        from ib_tasks.tests.factories.models import TaskStageHistoryFactory
        TaskStageHistoryFactory.reset_sequence()
        TaskStageHistoryFactory()

    def test_get_user_team_id(self, populate_data_for_user_team):
        # Arrange
        stage_id = 1
        task_id = 1
        expected_output = "TEAM_ID_0"

        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        storage = TasksStorageImplementation()

        # Act
        result = storage.get_team_id(stage_id, task_id)

        # Assert
        assert result == expected_output
