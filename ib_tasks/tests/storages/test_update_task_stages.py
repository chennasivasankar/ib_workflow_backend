
import pytest


@pytest.mark.django_db
class TestUpdateTaskStages:

    def test_update_task_stages(self):
        # Arrange
        task_id = 1
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation
        from ib_tasks.tests.factories.models \
            import CurrentTaskStageModelFactory, TaskFactory, StageModelFactory
        TaskFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        task = TaskFactory()
        CurrentTaskStageModelFactory.create_batch(size=2, task=task)

        storage = StorageImplementation()


        # Act
        storage.update_task_stages(task_id=task_id, stage_ids=['stage_id_0'])

        # Assert
        from ib_tasks.models import CurrentTaskStage
        task_stage_obj = CurrentTaskStage.objects.get(id=3)
        assert CurrentTaskStage.objects.filter(id__in=[1, 2]).exists() == False
        assert task_stage_obj.task_display_id == 1
        assert task_stage_obj.stage_id == 1