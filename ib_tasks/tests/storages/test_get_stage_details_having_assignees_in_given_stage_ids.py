import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation
from ib_tasks.tests.factories.models import TaskFactory, TaskStageFactory, \
    StageModelFactory
from ib_tasks.tests.factories.storage_dtos import \
    TaskStageHavingAssigneeIdDTOFactory


@pytest.mark.django_db
class TestUserTaskWithRecentStageDetails:
    @pytest.fixture()
    def create_task(self):
        TaskFactory.reset_sequence()
        task_obj = TaskFactory()
        return task_obj

    @pytest.fixture()
    def create_task_stages_setup(self, create_task):
        task_obj = create_task

        TaskStageFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskStageFactory.create_batch(size=3, task=task_obj)

    @pytest.fixture()
    def stages_having_assignees_dtos(self):
        stages_having_assignees_dtos = TaskStageHavingAssigneeIdDTOFactory.create_batch(
            2)
        return stages_having_assignees_dtos

    def test_get_stage_details_having_assignees_in_given_stage_ids(self,
                                                                   create_task,
                                                                   create_task_stages_setup,
                                                                   stages_having_assignees_dtos):
        # Arrange
        task_obj = create_task
        stage_ids = [1, 2]
        storage = StagesStorageImplementation()

        # Act
        result = storage. \
            get_stage_details_having_assignees_in_given_stage_ids(
            task_id=task_obj, db_stage_ids=stage_ids)

        # Assert
        assert result == stages_having_assignees_dtos
