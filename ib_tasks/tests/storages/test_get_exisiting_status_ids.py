import pytest

from ib_tasks.storages.storage_implementation import StagesStorageImplementation
from ib_tasks.tests.factories.models import TaskTemplateStatusVariableFactory


@pytest.mark.django_db
class TestGetExistingStageIds:

    @pytest.fixture
    def populate_data(self):
        TaskTemplateStatusVariableFactory.reset_sequence()
        TaskTemplateStatusVariableFactory.create_batch(size=2)

    def test_get_existing_stage_ids(self, populate_data):
        # Arrange
        expected = ["variable1", "variable2"]
        status_ids = ["variable1", "variable2"]
        storage = StagesStorageImplementation()

        # Act
        result = storage.get_existing_status_ids(status_ids)

        # Assert
        assert result == expected