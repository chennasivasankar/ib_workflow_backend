import pytest

from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation
from ib_tasks.tests.factories.interactor_dtos import TaskStageIdDTOFactory
from ib_tasks.tests.factories.models import CurrentTaskStageModelFactory


@pytest.mark.django_db
class TestValidateTaskStageIds:

    @pytest.fixture()
    def get_task_stage_dtos(self):
        TaskStageIdDTOFactory.reset_sequence()
        return TaskStageIdDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def populate_data(self):
        CurrentTaskStageModelFactory.reset_sequence()
        CurrentTaskStageModelFactory.create_batch(size=4)

    def test_validate_stage_task_details(self, get_task_stage_dtos,
                                         populate_data,
                                         snapshot):
        # Arrange
        storage = TasksStorageImplementation()

        # Act
        response = storage.validate_task_related_stage_ids(get_task_stage_dtos)

        # Assert
        snapshot.assert_match(response, "response")
