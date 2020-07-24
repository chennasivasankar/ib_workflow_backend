import pytest

from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
from ib_tasks.storages.tasks_storage_implementation import TasksStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory, StageActionFactory, TaskStageModelFactory, TaskFactory


@pytest.mark.django_db
class TestGetTaskDetails:

    @pytest.fixture()
    def populate_data(self):
        StageModelFactory.reset_sequence()
        stages = StageModelFactory.create_batch(size=10)
        StageActionFactory.reset_sequence()
        StageActionFactory.create_batch(size=3, stage=stages[0])
        TaskFactory.reset_sequence()
        tasks = TaskFactory.create_batch(size=3)
        TaskStageModelFactory.reset_sequence()
        TaskStageModelFactory(stage=stages[0], task=tasks[0])
        TaskStageModelFactory(stage=stages[0], task=tasks[1])
        TaskStageModelFactory(stage=stages[0], task=tasks[2])

    def test_with_valid_details_returns_task_details_dtos(self,
                                                          snapshot,
                                                          populate_data):
        # Arrange
        task_dtos = [GetTaskDetailsDTO(
            task_id=1,
            stage_id="stage_id_1"
        ),
            GetTaskDetailsDTO(
                task_id=2,
                stage_id="stage_id_2"
            )
        ]
        storage = TasksStorageImplementation()

        # Act
        result = storage.get_task_details(task_dtos=task_dtos)

        # Assert
        snapshot.assert_match(result, "result")
