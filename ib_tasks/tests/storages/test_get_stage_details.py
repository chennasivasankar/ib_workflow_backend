import pytest

from ib_tasks.storages.fields_storage_implementation import FieldsStorageImplementation
from ib_tasks.tests.factories.interactor_dtos import GetTaskDetailsDTOFactory
from ib_tasks.tests.factories.models import StageModelFactory, TaskFactory, TaskTemplateFactory, TaskStageModelFactory


@pytest.mark.django_db
class TestGetStageDetails:

    @pytest.fixture()
    def get_task_stage_dtos(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def populate_data(self):
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=4)
        TaskFactory.reset_sequence()
        TaskFactory.create_batch(size=3)
        TaskTemplateFactory.reset_sequence()
        TaskTemplateFactory.create_batch(size=3)
        TaskStageModelFactory.reset_sequence()
        TaskStageModelFactory.create_batch(size=4)

    def test_get_stage_details(self, get_task_stage_dtos,
                               populate_data,
                               snapshot):
        # Arrange
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_stage_details(get_task_stage_dtos)

        # Assert
        snapshot.assert_match(response, "response")
