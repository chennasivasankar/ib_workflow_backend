import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.tests.factories.interactor_dtos import GetTaskDetailsDTOFactory
from ib_tasks.tests.factories.models import StageModelFactory, TaskFactory, \
    TaskTemplateFactory, CurrentTaskStageModelFactory, \
    GoFFactory


@pytest.mark.django_db
class TestGetStageDetails:

    @pytest.fixture()
    def get_task_stage_dtos(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_stage_dtos_for_three_stages(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory.create_batch(size=3, task_id=1)

    @pytest.fixture()
    def populate_data(self):
        GoFFactory.reset_sequence(-1)
        GoFFactory.create_batch(size=4)
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=4)
        TaskFactory.reset_sequence()
        TaskFactory.create_batch(size=3)
        TaskTemplateFactory.reset_sequence()
        TaskTemplateFactory.create_batch(size=3)
        CurrentTaskStageModelFactory.reset_sequence()
        CurrentTaskStageModelFactory.create_batch(size=4)

    def test_get_stage_details(self, get_task_stage_dtos,
                               populate_data,
                               snapshot):
        # Arrange
        storage = StagesStorageImplementation()

        # Act
        response = storage.get_stage_details(get_task_stage_dtos)

        # Assert
        snapshot.assert_match(response, "response")

    def test_get_stage_details_when_a_task_is_in_three_stages(
            self, get_task_stage_dtos_for_three_stages,
            populate_data,
            snapshot):
        # Arrange
        storage = StagesStorageImplementation()

        # Act
        response = storage.get_stage_details(
            get_task_stage_dtos_for_three_stages)

        # Assert
        snapshot.assert_match(response, "response")
