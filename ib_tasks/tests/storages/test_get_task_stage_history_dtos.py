import pytest

from ib_tasks.storages.task_stage_storage_implementation import TaskStageStorageImplementation


@pytest.mark.django_db
class TestGetTaskStageDTOs:

    @pytest.fixture()
    def populate_data(self):
        pass

    def test_with_valid_details_returns_task_details_dtos(self,
                                                          snapshot,
                                                          populate_data):
        # Arrange
        storage = TaskStageStorageImplementation()
        task_id = 1

        # Act
        result = storage.get_task_stage_dtos(task_id=task_id)

        # Assert
        snapshot.assert_match(result, "result")
