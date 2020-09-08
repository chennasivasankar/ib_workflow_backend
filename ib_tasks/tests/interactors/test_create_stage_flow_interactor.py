import pytest

from ib_tasks.tests.factories.interactor_dtos import StageFlowWithActionIdDTOFactory
from ib_tasks.tests.factories.storage_dtos import StageIdActionNameDTOFactory, StageActionIdDTOFactory


class TestCreateStageFlowInteractor:

    @pytest.fixture
    def action_storage(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces \
            .action_storage_interface import \
            ActionStorageInterface
        return create_autospec(ActionStorageInterface)

    @staticmethod
    @pytest.fixture()
    def stage_storage():
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces \
            .stages_storage_interface import StageStorageInterface
        storage = create_autospec(StageStorageInterface)
        return storage

    def test_given_valid_details_creates_stage_flow(
            self, action_storage, stage_storage):

        # Arrange
        from ib_tasks.tests.factories.interactor_dtos \
            import CreateStageFlowDTOFactory
        CreateStageFlowDTOFactory.reset_sequence()
        stage_flow_dtos = CreateStageFlowDTOFactory.create_batch(2)
        StageFlowWithActionIdDTOFactory.reset_sequence()
        create_stage_flows = StageFlowWithActionIdDTOFactory.create_batch(2)
        from ib_tasks.interactors.create_stage_flow_interactor import CreateStageFlowInteractor
        interactor = CreateStageFlowInteractor(
            action_storage=action_storage, stage_storage=stage_storage
        )
        stage_ids = ["stage_0", "stage_1", "stage_2"]
        stage_storage.get_valid_stage_ids_in_given_stage_ids.return_value = stage_ids
        StageIdActionNameDTOFactory.reset_sequence()
        StageActionIdDTOFactory.reset_sequence()
        input_dtos = StageIdActionNameDTOFactory.create_batch(2)
        output_dtos = StageActionIdDTOFactory.create_batch(2)
        action_storage.get_stage_action_name_dtos.return_value = output_dtos

        # Act
        interactor.create_stage_flows(stage_flow_dtos=stage_flow_dtos)

        # Assert
        action_storage.get_stage_action_name_dtos.assert_called_once_with(
            stage_id_action_dtos=input_dtos
        )
        stage_storage.create_stage_flows.assert_called_once_with(
            stage_flow_dtos=create_stage_flows
        )