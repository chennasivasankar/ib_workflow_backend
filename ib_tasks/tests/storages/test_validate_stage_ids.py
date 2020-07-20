import pytest

from ib_tasks.storages.storage_implementation import StorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory
from ib_tasks.tests.factories.storage_dtos import ValidStageDTOFactory


@pytest.mark.django_db
class TestValidateStageIds:

    @pytest.fixture()
    def create_stages(self):
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=3)

    @pytest.fixture()
    def valid_stages_dto(self):
        ValidStageDTOFactory.reset_sequence()
        return ValidStageDTOFactory.create_batch(size=3)

    def test_validate_stage_ids(self, create_stages, valid_stages_dto):
        # Arrange
        storage = StorageImplementation()
        expected_stage_dtos = valid_stages_dto
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2", "stage_id_3"]

        # Act
        valid_stage_dtos = storage.get_valid_stage_ids(stage_ids)

        # Assert
        assert valid_stage_dtos == expected_stage_dtos
