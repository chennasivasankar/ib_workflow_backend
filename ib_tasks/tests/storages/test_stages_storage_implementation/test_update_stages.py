import pytest

from ib_tasks.interactors.stages_dtos import StageDTO
from ib_tasks.models import Stage, StagePermittedRoles
from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.tests.factories.models import (StageModelFactory,
                                             StagePermittedRolesFactory)
from ib_tasks.tests.factories.storage_dtos import StageDTOFactory


@pytest.mark.django_db
class TestUpdateStages:

    @pytest.fixture()
    def stage_dtos(self):
        StageDTOFactory.reset_sequence(50)
        return StageDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def create_stages(self):
        StageModelFactory.reset_sequence(51)
        objs = StageModelFactory.create_batch(size=4)
        StagePermittedRolesFactory.reset_sequence()
        StagePermittedRolesFactory(stage=objs[0])
        StagePermittedRolesFactory(stage=objs[1])
        StagePermittedRolesFactory(stage=objs[2])
        StagePermittedRolesFactory(stage=objs[3])

    def test_update_stages_stage_details(self, snapshot,
                                         stage_dtos, create_stages):
        # Arrange
        stage_dtos = stage_dtos
        stage_ids = ["stage_id_51", "stage_id_52", "stage_id_53"]
        storage = StagesStorageImplementation()

        # Act
        storage.update_stages(stage_dtos)

        # Assert
        stages = Stage.objects.filter(stage_id__in=stage_ids)
        self._validate_stages_details(stages, stage_dtos)
        roles = list(StagePermittedRoles.objects.filter(
            stage__stage_id__in=stage_ids).values('role_id',
                                                  'stage__stage_id'))
        snapshot.assert_match(roles, "roles")

    @staticmethod
    def _validate_stages_details(stages, expected_dtos):
        returned_dtos = [StageDTO(
            stage_id=stage.stage_id,
            task_template_id=stage.task_template_id,
            value=stage.value,
            card_info_kanban=stage.card_info_kanban,
            card_info_list=stage.card_info_list,
            stage_display_name=stage.display_name,
            stage_display_logic=stage.display_logic,
            stage_color=stage.stage_color,
            roles=""
        ) for stage in stages]

        for index, expected_dto in enumerate(expected_dtos):
            assert returned_dtos[index].stage_id == expected_dto.stage_id
            assert returned_dtos[
                       index].task_template_id == expected_dto.task_template_id
            assert returned_dtos[index].value == expected_dto.value
            assert returned_dtos[
                       index].stage_display_logic == \
                   expected_dto.stage_display_logic
            assert returned_dtos[
                       index].stage_display_name == \
                   expected_dto.stage_display_name
            assert returned_dtos[index].card_info_list == \
                   expected_dto.card_info_list
            assert returned_dtos[index].card_info_kanban == \
                   expected_dto.card_info_kanban
            assert returned_dtos[index].stage_color == expected_dto.stage_color
