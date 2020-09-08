import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory
from ib_tasks.tests.factories.storage_dtos import TaskStageDTOFactory


@pytest.mark.django_db
class TestStageTemplateId:
    @pytest.fixture()
    def create_stages(self):
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=3)
        StageModelFactory(stage_id="stage_id_3",
                          task_template_id="task_template_100")

    @pytest.fixture()
    def get_stage_task_dto(self):
        TaskStageDTOFactory.reset_sequence()
        return TaskStageDTOFactory.create_batch(size=4)

    def test_validate_stage_related_task_template_ids(self, create_stages,
                                                      get_stage_task_dto):
        # Arrange
        invalid_stage_ids = ["stage_id_3"]
        storage = StagesStorageImplementation()

        # Act
        returned_ids = storage.validate_stages_related_task_template_ids(
            get_stage_task_dto)

        # Assert
        assert invalid_stage_ids == returned_ids
