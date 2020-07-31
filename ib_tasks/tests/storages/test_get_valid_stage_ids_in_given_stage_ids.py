import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory


@pytest.mark.django_db
class TestValidateStageIds:

    @pytest.fixture()
    def create_stages(self):
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=3)

    def test_list_of_stage_ids_in_given_stage_ids(self, create_stages):
        # Arrange
        storage = StagesStorageImplementation()
        given_stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2",
                           "stage_id_3"]
        expected_result = ["stage_id_0", "stage_id_1", "stage_id_2"]

        # Act
        valid_stage_ids = storage.get_valid_stage_ids_in_given_stage_ids(
            given_stage_ids)

        # Assert
        assert valid_stage_ids == expected_result
