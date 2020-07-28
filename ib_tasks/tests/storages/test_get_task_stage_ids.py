import pytest

from ib_tasks.storages.fields_storage_implementation import FieldsStorageImplementation
from ib_tasks.tests.factories.models import TaskStageModelFactory


@pytest.mark.django_db
class TestGetTaskStages:

    @pytest.fixture()
    def create_task_stages(self):
        TaskStageModelFactory.reset_sequence()
        TaskStageModelFactory.create_batch(size=10, task_id=1)

    def test_get_task_stage_ids(self,
                                snapshot,
                                create_task_stages):
        # Arrange
        task_id = 1
        storage = FieldsStorageImplementation()

        # Act
        stage_ids = storage.get_task_stages(task_id)

        # Assert
        snapshot.assert_match(stage_ids, "task_stage_ids")
