import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation


@pytest.mark.django_db
class TestGetTaskCurrentStages:

    @pytest.fixture()
    def populate_task_with_stages(self):
        from ib_tasks.tests.factories.models import \
            CurrentTaskStageModelFactory, TaskFactory
        TaskFactory.reset_sequence()
        task = TaskFactory()
        CurrentTaskStageModelFactory.reset_sequence()
        current_task_stages = CurrentTaskStageModelFactory.create_batch(
            2, task=task)
        return current_task_stages

    def test_get_current_stage_db_ids_of_task(self,
                                              populate_task_with_stages,
                                              snapshot):
        # Arrange
        storage = StagesStorageImplementation()

        # Act
        response = storage.get_current_stage_db_ids_of_task(task_id=1)

        # Assert
        snapshot.assert_match(response, "response")
