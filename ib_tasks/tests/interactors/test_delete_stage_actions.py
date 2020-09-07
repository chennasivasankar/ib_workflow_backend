
from unittest.mock import create_autospec
from ib_tasks.interactors.storage_interfaces.action_storage_interface \
    import ActionStorageInterface
from ib_tasks.tests.factories.interactor_dtos \
    import StageActionDTOFactory, StageActionNamesDTOFactory


class TestDeleteStageActionsInteractor:

    @staticmethod
    def test_given_delete_stage_actions_deletes_actions():

        StageActionDTOFactory.reset_sequence(0)
        StageActionNamesDTOFactory.reset_sequence(0)
        stage_action_name_dtos = StageActionNamesDTOFactory.create_batch(2)
        action_dtos = StageActionDTOFactory.create_batch(size=1)
        delete_stage_actions_dto = [stage_action_name_dtos[1]]
        storage = create_autospec(ActionStorageInterface)
        from ib_tasks.interactors.delete_stage_actions_interactor \
            import DeleteStageActionsInteractor
        interactor = DeleteStageActionsInteractor(
            storage=storage
        )

        # Act
        interactor.delete_stage_actions_wrapper(
            db_stage_action_name_dtos=stage_action_name_dtos,
            action_dtos=action_dtos
        )

        # Assert
        storage.delete_stage_actions \
            .assert_called_once_with(stage_actions=delete_stage_actions_dto)