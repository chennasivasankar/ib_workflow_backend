import pytest
from freezegun import freeze_time

from ib_tasks.models import TaskStageHistory


@pytest.mark.django_db
class TestUpdateTaskStagesWithLeftAtStatus:

    @pytest.fixture()

    def populate_task_stage_histories(self):
        from ib_tasks.tests.factories.models import \
            TaskStageHistoryModelFactory, TaskFactory
        TaskFactory.reset_sequence()
        task = TaskFactory()
        stage_histories_1 = TaskStageHistoryModelFactory.create_batch(
            2, task=task, left_at=None)
        stage_histories_2 = TaskStageHistoryModelFactory.create_batch(2, task=task)
        return

    @freeze_time("2020-08-10 12:30:00")
    def test_update_task_stages_other_than_matched_stages_with_left_at_status(
            self, populate_task_stage_histories, snapshot):
        # Arrange
        task_id = 1
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()

        # Act
        storage. \
            update_task_stages_other_than_matched_stages_with_left_at_status(
            task_id=task_id, db_stage_ids=[3, 4])

        # Assert
        task_stage_objs = list(TaskStageHistory.objects.filter(
            task_id=task_id).values('task_id', 'stage_id', 'assignee_id','left_at'))


        snapshot.assert_match(task_stage_objs, "task_stage_objs")
