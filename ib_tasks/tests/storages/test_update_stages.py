import pytest

from ib_tasks.interactors.stages_dtos import StageDTO
from ib_tasks.models import Stage
from ib_tasks.storages.storage_implementation import StagesStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory
from ib_tasks.tests.factories.storage_dtos import StageDTOFactory


@pytest.mark.django_db
class TestUpdateStages:

    @pytest.fixture()
    def stage_dtos(self):
        StageDTOFactory.reset_sequence(50)
        return StageDTOFactory.create_batch(size=3, id_value=True)

    @pytest.fixture()
    def create_stages(self):
        StageModelFactory.reset_sequence(50)
        StageModelFactory.create_batch(size=3)

    def _validate_stages_details(self, stages, expected_dtos):
        returned_dtos = [StageDTO(
            stage_id=stage.stage_id,
            task_template_id=stage.task_template_id,
            value=stage.value,
            id=stage.id,
            stage_display_name=stage.display_name,
            stage_display_logic=stage.display_logic
        ) for stage in stages]

        for dto_value in range(len(expected_dtos)-1):
            assert returned_dtos[dto_value].stage_id == expected_dtos[dto_value].stage_id
            assert returned_dtos[dto_value].task_template_id == expected_dtos[dto_value].task_template_id
            assert returned_dtos[dto_value].value == expected_dtos[dto_value].value
            assert returned_dtos[dto_value].stage_display_logic == expected_dtos[dto_value].stage_display_logic
            assert returned_dtos[dto_value].stage_display_name == expected_dtos[dto_value].stage_display_name

    def test_update_stages_stage_details(self, stage_dtos, create_stages):
        # Arrange
        stage_dtos = stage_dtos
        stage_ids = ["stage_id_50", "stage_id_51", "stage_id_52", "stage_id_53"]
        storage = StagesStorageImplementation()

        # Act
        storage.update_stages(stage_dtos)

        # Assert
        stages = Stage.objects.filter(stage_id__in=stage_ids)
        self._validate_stages_details(stages, stage_dtos)
