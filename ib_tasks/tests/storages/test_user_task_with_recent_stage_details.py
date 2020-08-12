import pytest

from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageValueDTO, StageValueWithTaskIdsDTO, \
    TaskIdWithStageDetailsDTO
from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation
from ib_tasks.tests.factories.models import TaskStageFactory, TaskFactory, \
    StageModelFactory


@pytest.mark.django_db
class TestUserTaskWithRecentStageDetails:
    @pytest.fixture()
    def create_tasks(self):
        TaskFactory.reset_sequence()
        task_objs = TaskFactory.create_batch(size=3)
        return task_objs

    @pytest.fixture()
    def create_task_stages_setup(self, create_tasks):
        task_objs = create_tasks
        TaskStageFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskStageFactory.create_batch(size=3, task=task_objs[0])
        stage = StageModelFactory(value=2)
        TaskStageFactory(task=task_objs[1], stage=stage)

    @pytest.fixture()
    def get_task_id_with_max_stage_value_dtos(self, create_tasks):
        task_objs = create_tasks
        task_id_with_max_stage_value_dtos = [
            TaskIdWithStageValueDTO(task_id=task_objs[0].id, stage_value=1),
            TaskIdWithStageValueDTO(task_id=task_objs[1].id, stage_value=2)
        ]
        return task_id_with_max_stage_value_dtos

    @pytest.fixture()
    def get_task_id_with_stage_details_dtos(self, create_tasks):
        task_objs = create_tasks
        task_id_with_stage_details_dtos = [
            TaskIdWithStageDetailsDTO(task_id=task_objs[0].id,
                                      stage_id="stage_id_2",
                                      db_stage_id=3,
                                      stage_color="blue",
                                      stage_display_name="name_2"),
            TaskIdWithStageDetailsDTO(task_id=task_objs[1].id,
                                      stage_id="stage_id_3",
                                      db_stage_id=4,
                                      stage_color="blue",
                                      stage_display_name="name_3")
        ]
        return task_id_with_stage_details_dtos

    def test_validate_tasks_with_stages_of_max_values(
            self, create_tasks, create_task_stages_setup,
            get_task_id_with_max_stage_value_dtos):
        # Arrange
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_3"]
        storage = TasksStorageImplementation()

        # Act
        result = storage. \
            get_user_task_and_max_stage_value_dto_based_on_given_stage_ids(
            offset=0, limit=2,
            user_id="123e4567-e89b-12d3-a456-426614174000",
            stage_ids=stage_ids)

        # Assert
        assert result == get_task_id_with_max_stage_value_dtos

    def test_get_task_id_with_stage_details_based_on_stage_value(
            self, create_tasks, create_task_stages_setup,
            get_task_id_with_stage_details_dtos):
        # Arrange
        task_objs = create_tasks
        expected_output = get_task_id_with_stage_details_dtos
        stage_values = [2]
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        task_ids_group_by_stage_value_dtos = [
            StageValueWithTaskIdsDTO(
                task_ids=[task_objs[0].id, task_objs[1].id], stage_value=2)
        ]
        storage = StagesStorageImplementation()

        # Act
        result = storage. \
            get_task_id_with_stage_details_dtos_based_on_stage_value(
                stage_values=stage_values,
                user_id=user_id,
                task_ids_group_by_stage_value_dtos=
                task_ids_group_by_stage_value_dtos)
        assert result == expected_output
