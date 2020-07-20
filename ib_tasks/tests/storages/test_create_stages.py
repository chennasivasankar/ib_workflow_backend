import pytest

from ib_tasks.interactors.storage_interfaces.dtos import StageDTO
from ib_tasks.models import Stage
from ib_tasks.storages.storage_implementation import StorageImplementation
from ib_tasks.tests.factories.storage_dtos import StageDTOFactory


@pytest.mark.django_db
class TestCreateStages:

    @pytest.fixture()
    def stage_dtos(self):
        StageDTOFactory.reset_sequence()
        return StageDTOFactory.create_batch(size=4)

    def _validate_stages_details(self, stages, expected_dtos):
        returned_dtos = [StageDTO(
            stage_id=stage.stage_id,
            task_template_id=stage.task_template_id,
            value=stage.value,
            id=None,
            stage_display_name=stage.display_name,
            stage_display_logic=stage.display_logic
        ) for stage in stages]

        for dto_value in range(len(expected_dtos)):
            assert returned_dtos[dto_value].stage_id == expected_dtos[dto_value].stage_id
            assert returned_dtos[dto_value].task_template_id == expected_dtos[dto_value].task_template_id
            assert returned_dtos[dto_value].value == expected_dtos[dto_value].value
            assert returned_dtos[dto_value].stage_display_logic == expected_dtos[dto_value].stage_display_logic
            assert returned_dtos[dto_value].stage_display_name == expected_dtos[dto_value].stage_display_name

    def test_create_stages_create_stage_details(self, stage_dtos):
        # Arrange
        stage_dtos = stage_dtos
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2", "stage_id_3"]
        storage = StorageImplementation()

        # Act
        storage.create_stages(stage_dtos)

        # Assert
        stages = Stage.objects.filter(stage_id__in=stage_ids)
        self._validate_stages_details(stages, stage_dtos)
