import datetime

import pytest
from freezegun import freeze_time

from ib_tasks.models import TaskStageRp


@pytest.mark.django_db
class TestGetTaskRPs:

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
        from ib_tasks.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()

        # Act
        result = storage.get_due_missed_count(task_id=task_id,
                                              stage_id=stage_id, user_id=user_id)

        # Assert
        assert result == expected_output

    @pytest.fixture
    def populate_data_for_user_team(self):
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.reset_sequence()
        from ib_tasks.tests.factories.models import TaskStageHistoryFactory
        TaskStageHistoryFactory.reset_sequence()
        TaskStageHistoryFactory()

    def test_get_user_team_id(self, populate_data_for_user_team):
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

    @freeze_time("2020-10-12 4:40")
    def test_get_task_due_date(self, populate_data):
        # Arrange
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        task_id = 1
        expected_output = datetime.datetime(2020, 10, 22, 4, 40)
        stage_id = 1

        from ib_tasks.storages.tasks_storage_implementation import TasksStorageImplementation
        storage = TasksStorageImplementation()

        # Act
        result = storage.get_user_missed_the_task_due_time(task_id, user_id, stage_id)

        # Assert
        assert result == expected_output

    def test_get_rp_id_if_exists(self, populate_data):
        # Arrange
        expected_output = '123e4567-e89b-12d3-a456-426614174053'
        task_id = 1
        stage_id = 1
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        from ib_tasks.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()

        # Act
        result = storage.get_latest_rp_id_if_exists(task_id=task_id,
                                                    stage_id=stage_id)

        # Assert
        assert result == expected_output

    def test_get_rp_ids(self, populate_data):
        # Arrange
        expected_output = ['123e4567-e89b-12d3-a456-426614174050',
                           '123e4567-e89b-12d3-a456-426614174051',
                           '123e4567-e89b-12d3-a456-426614174052',
                           '123e4567-e89b-12d3-a456-426614174053']
        task_id = 1
        stage_id = 1
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        from ib_tasks.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()

        # Act
        result = storage.get_rp_ids(task_id=task_id,
                                    stage_id=stage_id)

        # Assert
        assert result == expected_output

    def test_add_superior_to_db(self, populate_data):
        # Arrange
        expected_output = True
        task_id = 1
        stage_id = 1
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        superior_id = '123e4567-e89b-12d3-a456-426614174104'
        from ib_tasks.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()

        # Act
        result = storage.add_superior_to_db(task_id=task_id, superior_id=superior_id,
                                            stage_id=stage_id)

        # Assert
        does_exist = TaskStageRp.objects.filter(
            task_id=task_id, stage_id=stage_id,
            rp_id=superior_id
        ).exists()
        assert does_exist == expected_output

    def test_get_latest_rp_added_datetime(self, populate_data):
        # Arrange
        expected_output = datetime.datetime(2020, 10, 12, 4, 40)
        task_id = 1
        stage_id = 1
        from ib_tasks.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()

        # Act
        result = storage.get_latest_rp_added_datetime(task_id=task_id,
                                            stage_id=stage_id)

        # Assert
        assert result == expected_output

