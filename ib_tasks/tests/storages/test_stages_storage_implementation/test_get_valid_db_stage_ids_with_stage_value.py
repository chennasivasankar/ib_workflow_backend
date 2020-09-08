import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.tests.factories.interactor_dtos import StageIdWithValueDTOFactory
from ib_tasks.tests.factories.models import StageModelFactory


@pytest.mark.django_db
class TestValidStageIdsWithStageValue:

    @pytest.fixture()
    def create_stages(self):
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=3)

    def test_get_valid_db_stage_ids_with_stage_value(self, create_stages):
        # Arrange
        storage = StagesStorageImplementation()
        given_stage_ids = [1, 2, 3, 4]
        expected_result = StageIdWithValueDTOFactory.create_batch(3)

        # Act
        result = storage.get_valid_db_stage_ids_with_stage_value(
            given_stage_ids)

        # Assert
        assert result == expected_result
