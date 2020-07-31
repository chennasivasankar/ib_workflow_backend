import pytest

from ib_tasks.storages.fields_storage_implementation import FieldsStorageImplementation
from ib_tasks.tests.factories.models import TaskStageModelFactory, TaskFactory, StageModelFactory


@pytest.mark.django_db
class TestGetStagesDetails:

    @pytest.fixture()
    def create_task_stages(self):
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskStageModelFactory.reset_sequence()
        TaskStageModelFactory.create_batch(size=10, task_id=1)

    def test_get_stage_ids_details(self,
                                   snapshot,
                                   create_task_stages):
        # Arrange
        stage_ids = [
            'stage_id_0',
            'stage_id_1',
            'stage_id_2',
            'stage_id_3',
            'stage_id_4',
            'stage_id_5',
            'stage_id_6',
            'stage_id_7',
            'stage_id_8',
            'stage_id_9'
        ]
        storage = FieldsStorageImplementation()

        # Act
        stage_details_dtos = storage.get_stage_complete_details(stage_ids)

        # Assert
        snapshot.assert_match(stage_details_dtos, "stage_details_dtos")
