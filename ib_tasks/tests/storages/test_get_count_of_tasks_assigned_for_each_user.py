import factory
import pytest


@pytest.mark.django_db
class TestGetCountOfTasksAssignedForEachUser:

    def test_given_db_stage_ids_and_task_ids_returns_assignee_current_tasks_count_dtos(
            self, snapshot
    ):
        # Arrange
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.reset_sequence()
        task_objs = TaskFactory.create_batch(size=3)
        from ib_tasks.tests.factories.models import StageModelFactory
        StageModelFactory.reset_sequence()
        stage_objs = StageModelFactory.create_batch(size=10)
        db_stage_ids = [
            stage_obj.id
            for stage_obj in stage_objs
        ]
        task_ids = [
            task_obj.id
            for task_obj in task_objs
        ]
        assignee_ids = [
            "123e4567-e89b-12d3-a456-426614174000",
            "123e4567-e89b-12d3-a456-426614174001",
            "123e4567-e89b-12d3-a456-426614174002",
            "123e4567-e89b-12d3-a456-426614174003"
        ]
        from ib_tasks.tests.factories.models import \
            TaskStageHistoryModelFactory
        TaskStageHistoryModelFactory.reset_sequence()
        TaskStageHistoryModelFactory.create_batch(
            size=10,
            assignee_id=factory.Iterator(assignee_ids),
            stage=factory.Iterator(stage_objs),
            task=factory.Iterator(task_objs),
            left_at=None
        )
        from ib_tasks.storages.task_stage_storage_implementation import \
            TaskStageStorageImplementation
        task_storage = TaskStageStorageImplementation()

        # Act
        assignee_with_current_tasks_count_dtos = task_storage.get_count_of_tasks_assigned_for_each_user(
            db_stage_ids=db_stage_ids, task_ids=task_ids
        )

        # Assert
        snapshot.assert_match(
            name="assignee_with_current_tasks_count_dtos",
            value=assignee_with_current_tasks_count_dtos
        )