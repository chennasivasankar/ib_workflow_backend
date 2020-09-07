import pytest


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