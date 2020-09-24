import factory
import pytest


@pytest.mark.django_db
class TestGetCompletedSubTaskIds:

    @pytest.fixture
    def populate_data(self):
        task_template_id = "Adhoc template"
        sub_task_ids = [0, 1, 2, 3, 4, 5]
        stage_values = [6, 8, 3, 8, 3, 8]
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.create_batch(size=6, id=factory.Iterator(sub_task_ids))
        from ib_tasks.tests.factories.models import \
            CurrentTaskStageModelFactory

        from ib_tasks.tests.factories.models import StageModelFactory
        StageModelFactory.reset_sequence()
        stage_objs = StageModelFactory.create_batch(
            size=6, task_template_id=task_template_id,
            value=factory.Iterator(stage_values)
        )
        CurrentTaskStageModelFactory.create_batch(
            size=6,
            task_id=factory.Iterator(sub_task_ids),
            stage=factory.Iterator(stage_objs)
        )

    def test_given_sub_task_ids_returns_completed_sub_task_ids(
            self, populate_data
    ):
        # Arrange
        max_stage_value = 8
        sub_task_ids = [0, 1, 2, 3, 4, 5]
        from ib_tasks.storages.task_stage_storage_implementation import \
            TaskStageStorageImplementation
        storage = TaskStageStorageImplementation()

        expected_completed_sub_tasks_ids = [1, 3, 5]

        # Act
        actual_completed_sub_tasks_ids = \
            storage.get_completed_sub_task_ids(
                sub_task_ids, max_stage_value
            )

        # Assert
        assert expected_completed_sub_tasks_ids == \
               actual_completed_sub_tasks_ids
