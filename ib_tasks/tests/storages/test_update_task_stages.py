
import pytest


@pytest.mark.django_db
class TestUpdateTaskStages:

    def test_update_task_stages(self):
        # Arrange
        task_id = 1
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation
        from ib_tasks.tests.factories.models \
            import TaskStageModelFactory, TaskFactory, StageModelFactory
        TaskFactory.reset_sequence()
        TaskStageModelFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        task = TaskFactory()
        TaskStageModelFactory.create_batch(size=2, task=task)

        storage = StorageImplementation()


        # Act
        storage.update_task_stages(task_id=task_id, stage_ids=['stage_id_0'])

        # Assert
        from ib_tasks.models import TaskStage
        task_stage_obj = TaskStage.objects.get(id=3)
        assert TaskStage.objects.filter(id__in=[1, 2]).exists() == False
        assert task_stage_obj.task_id == 1
        assert task_stage_obj.stage_id == 1