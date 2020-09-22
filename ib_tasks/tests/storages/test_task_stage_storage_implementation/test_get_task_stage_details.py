import pytest

from ib_tasks.tests.factories.models import StageModelFactory, CurrentTaskStageModelFactory, TaskFactory


@pytest.mark.django_db
class TestGetTaskStageDTOs:

    @pytest.fixture()
    def setup(self):
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence(1)
        CurrentTaskStageModelFactory.reset_sequence()
        task = TaskFactory()
        stage_1 = StageModelFactory()
        stage_2 = StageModelFactory(value=-1)
        CurrentTaskStageModelFactory(task=task, stage=stage_1)
        CurrentTaskStageModelFactory(task=task, stage=stage_2)

    def test_given_valid_returns_task_stage_dtos(self, setup):
        # Arrange
        from ib_tasks.storages.task_stage_storage_implementation \
            import TaskStageStorageImplementation
        storage = TaskStageStorageImplementation()
        task_ids = [1]
        from ib_tasks.tests.factories.interactor_dtos import TaskStageIdDTOFactory
        TaskStageIdDTOFactory.reset_sequence()
        expected = TaskStageIdDTOFactory.create_batch(2, task_id=1)

        # Act
        response = storage.get_task_stage_details_dtos(task_ids=task_ids)

        # Assert
        assert expected == response
