
from unittest.mock import create_autospec
from ib_tasks.interactors.storage_interfaces.action_storage_interface \
    import ActionStorageInterface
from ib_tasks.tests.factories.interactor_dtos \
    import StageActionDTOFactory, StageActionNamesDTOFactory


class TestCreateUpdateStageActionsInteractor:

    @staticmethod
    def test_given_create_stage_actions_creates_actions():

        StageActionDTOFactory.reset_sequence(0)
        StageActionNamesDTOFactory.reset_sequence(0)
        stage_action_name_dtos = StageActionNamesDTOFactory.create_batch(1)
        action_dtos = StageActionDTOFactory.create_batch(size=2)
        create_stage_actions_dto = [action_dtos[1]]
        storage = create_autospec(ActionStorageInterface)
        from ib_tasks.interactors.create_or_update_stage_actions_interactor \
            import CreateOrUpdateStageActions
        interactor = CreateOrUpdateStageActions(
            storage=storage
        )

        # Act
        interactor.create_or_update_stage_actions(
            db_stage_action_name_dtos=stage_action_name_dtos,
            action_dtos=action_dtos
        )

        # Assert
        storage.create_stage_actions \
            .assert_called_once_with(stage_actions=create_stage_actions_dto)

    @staticmethod
    def test_given_update_stage_actions_updates_actions():
        StageActionDTOFactory.reset_sequence(0)
        StageActionNamesDTOFactory.reset_sequence(0)
        stage_action_name_dtos = StageActionNamesDTOFactory.create_batch(2)
        action_dtos = StageActionDTOFactory.create_batch(size=2)
        update_stage_actions_dto = action_dtos
        storage = create_autospec(ActionStorageInterface)
        from ib_tasks.interactors.create_or_update_stage_actions_interactor \
            import CreateOrUpdateStageActions
        interactor = CreateOrUpdateStageActions(
            storage=storage
        )

        # Act
        interactor.create_or_update_stage_actions(
            db_stage_action_name_dtos=stage_action_name_dtos,
            action_dtos=action_dtos
        )

        # Assert
        storage.update_stage_actions \
            .assert_called_once_with(stage_actions=update_stage_actions_dto)

    @staticmethod
    def test_given_stage_actions_creates_actions():
        StageActionDTOFactory.reset_sequence(0)
        StageActionNamesDTOFactory.reset_sequence(0)
        stage_action_name_dtos = StageActionNamesDTOFactory.create_batch(2)
        action_dtos = StageActionDTOFactory.create_batch(size=3)
        update_stage_actions_dto = action_dtos[:-1]
        create_stage_actions_dto = [action_dtos[-1]]
        storage = create_autospec(ActionStorageInterface)
        from ib_tasks.interactors.create_or_update_stage_actions_interactor \
            import CreateOrUpdateStageActions
        interactor = CreateOrUpdateStageActions(
            storage=storage
        )

        # Act
        interactor.create_or_update_stage_actions(
            db_stage_action_name_dtos=stage_action_name_dtos,
            action_dtos=action_dtos
        )

        # Assert
        storage.create_stage_actions \
            .assert_called_once_with(stage_actions=create_stage_actions_dto)
        storage.update_stage_actions \
            .assert_called_once_with(stage_actions=update_stage_actions_dto)