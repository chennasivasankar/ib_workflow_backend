import pytest
from freezegun import freeze_time
from ib_tasks.storages.task_stage_storage_implementation import TaskStageStorageImplementation
from ib_tasks.tests.factories.models import TaskStageHistoryModelFactory, TaskFactory
from ib_tasks.tests.factories.storage_dtos import TaskStageHistoryDTOFactory


@pytest.mark.django_db
class TestGetTaskStageDTOs:

    @pytest.fixture()
    def populate_data(self):
        pass

    @freeze_time('2012-10-10')
    def test_with_valid_details_returns_task_details_dtos(self,
                                                          snapshot,
                                                          populate_data):
        # Arrange
        TaskFactory.reset_sequence(1)
        task = TaskFactory()
        storage = TaskStageStorageImplementation()
        task_id = 1
        TaskStageHistoryDTOFactory.reset_sequence(1)
        TaskStageHistoryModelFactory.reset_sequence(1)
        TaskStageHistoryModelFactory(task=task)
        TaskStageHistoryModelFactory(left_at=None, task=task)
        task_stages = [
            TaskStageHistoryDTOFactory(assignee_id='123e4567-e89b-12d3-a456-426614174001'),
            TaskStageHistoryDTOFactory(
                task_id=task_id, left_at=None,
                assignee_id='123e4567-e89b-12d3-a456-426614174002'
            )
        ]

        # Act
        result = storage.get_task_stage_dtos(task_id=task_id)

        # Assert
        assert task_stages == result
