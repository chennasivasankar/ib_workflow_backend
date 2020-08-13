import pytest

from ib_tasks.tests.factories.models import CurrentTaskStageModelFactory, TaskFactory


class TestGetTaskStageIds:
    @pytest.fixture()
    def task_stage_objs(self):
        CurrentTaskStageModelFactory.reset_sequence()
        TaskFactory.reset_sequence()
        task_obj = TaskFactory()
        task_stage_objs = CurrentTaskStageModelFactory.create_batch(4, task=task_obj)
        return task_stage_objs

    @pytest.mark.django_db
    def test_get_task_stage_ids_in_given_stage_ids(self, task_stage_objs):
        # Arrange
        expected_result = [1, 3]
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        # Act
        actual_result = storage.get_task_stage_ids_in_given_stage_ids(
            stage_ids=[1, 3, 5],
            task_id=task_stage_objs[0].task_display_id)
        # Assert
        assert actual_result == expected_result
