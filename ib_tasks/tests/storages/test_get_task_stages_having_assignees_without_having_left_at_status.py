import pytest

from ib_tasks.tests.factories.interactor_dtos import StageAssigneeDTOFactory
from ib_tasks.tests.factories.models import TaskStageHistoryModelFactory


@pytest.mark.django_db
class TestGetTaskStageAssugneesWithoutHavingLeftAtStatus:
    def test_get_task_stages_having_assignees_without_having_left_at_status(
            self):
        # Arrange
        TaskStageHistoryModelFactory.reset_sequence()
        StageAssigneeDTOFactory.reset_sequence(1)
        TaskStageHistoryModelFactory()
        TaskStageHistoryModelFactory.create_batch(2, task_id=1, left_at=None)
        expected_result = StageAssigneeDTOFactory.create_batch(2)
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        # Act
        actual_result = storage. \
            get_task_stages_assignees_without_having_left_at_status(
            db_stage_ids=[1, 2, 3],
            task_id=1)
        # Assert
        assert actual_result == expected_result
