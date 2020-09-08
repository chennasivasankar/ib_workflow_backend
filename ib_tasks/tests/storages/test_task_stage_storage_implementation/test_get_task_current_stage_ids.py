import pytest

from ib_tasks.tests.factories.models import TaskFactory, \
    CurrentTaskStageModelFactory


@pytest.mark.django_db
class TestGetTaskCurrentStageIds:

    def test_task_id_returns_current_stage_ids_of_task(self, task_storage):
        # Arrange
        task_obj = TaskFactory(task_display_id="IBWF-1")
        task_id = task_obj.id
        task_stage_objects = CurrentTaskStageModelFactory.create_batch(
            size=5, task=task_obj
        )
        expected_stage_ids = [
            task_stage_obj.stage_id
            for task_stage_obj in task_stage_objects
        ]

        # Act
        actual_stage_ids = task_storage.get_task_current_stage_ids(task_id)

        # Assert
        assert expected_stage_ids == actual_stage_ids
