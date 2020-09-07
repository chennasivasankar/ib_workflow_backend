import pytest

from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageValueDTO
from ib_tasks.tests.factories.models import TaskFactory, \
    CurrentTaskStageModelFactory, StageModelFactory


@pytest.mark.django_db
class TestGetUserTaskAndMaxStageValueDTOBasedOnGivenStageIds:

    @pytest.fixture()
    def create_tasks(self):
        TaskFactory.reset_sequence()
        task_objects = TaskFactory.create_batch(size=3)
        return task_objects

    @pytest.fixture()
    def create_task_stages_setup(self, create_tasks):
        task_objects = create_tasks
        CurrentTaskStageModelFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        CurrentTaskStageModelFactory.create_batch(size=3, task=task_objects[0])
        stage = StageModelFactory(value=2)
        CurrentTaskStageModelFactory(task=task_objects[1], stage=stage)

    @pytest.fixture()
    def get_task_id_with_max_stage_value_dtos(self, create_tasks):
        task_objects = create_tasks
        task_id_with_max_stage_value_dtos = [
            TaskIdWithStageValueDTO(task_id=task_objects[0].id, stage_value=1),
            TaskIdWithStageValueDTO(task_id=task_objects[1].id, stage_value=2)
        ]
        return task_id_with_max_stage_value_dtos

    def test_validate_tasks_with_stages_of_max_values(
            self, create_tasks, create_task_stages_setup, storage,
            get_task_id_with_max_stage_value_dtos):
        # Arrange
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_3"]

        # Act
        result = storage. \
            get_user_task_and_max_stage_value_dto_based_on_given_stage_ids(
            offset=0, limit=2,
            user_id="123e4567-e89b-12d3-a456-426614174000",
            stage_ids=stage_ids)

        # Assert
        assert result == get_task_id_with_max_stage_value_dtos
