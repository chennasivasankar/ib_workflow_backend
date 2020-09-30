import pytest

from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageValueWithTaskIdsDTO, TaskIdWithStageDetailsDTO, \
    TaskIdWithStageValueDTO
from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.tests.factories.models import CurrentTaskStageModelFactory, \
    StageModelFactory, TaskFactory


@pytest.mark.django_db
class TestGetTaskIdWithStageDetailsDTOSBasedOnStageValue:
    @pytest.fixture()
    def create_tasks(self):
        TaskFactory.reset_sequence()
        task_objects = TaskFactory.create_batch(size=3)
        return task_objects

    @pytest.fixture()
    def create_task_stages_setup(self, create_tasks):
        from ib_tasks.tests.factories.storage_dtos import StageDTOFactory

        task_objects = create_tasks
        CurrentTaskStageModelFactory.reset_sequence()
        StageDTOFactory.reset_sequence()
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

    @pytest.fixture()
    def get_task_id_with_stage_details_dtos(self, create_tasks):
        task_objects = create_tasks
        task_id_with_stage_details_dtos = [
            TaskIdWithStageDetailsDTO(task_id=task_objects[0].id,
                                      task_display_id=task_objects[
                                          0].task_display_id,
                                      stage_id="stage_id_2",
                                      stage_display_name="name_2",
                                      db_stage_id=3, stage_color="orange")
        ]
        return task_id_with_stage_details_dtos

    def test_get_task_id_with_stage_details_based_on_stage_value(
            self, create_tasks, create_task_stages_setup,
            get_task_id_with_stage_details_dtos):
        # Arrange
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]
        task_objects = create_tasks
        expected_output = get_task_id_with_stage_details_dtos
        stage_values = [2]
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        task_ids_group_by_stage_value_dtos = [
            StageValueWithTaskIdsDTO(
                task_ids=[task_objects[0].id, task_objects[1].id],
                stage_value=2)
        ]
        storage = StagesStorageImplementation()

        # Act
        result = storage. \
            get_task_id_with_stage_details_dtos_based_on_stage_value(
                stage_values=stage_values,
                task_ids_group_by_stage_value_dtos=
                task_ids_group_by_stage_value_dtos, stage_ids=stage_ids)

        # Assert
        assert result == expected_output
