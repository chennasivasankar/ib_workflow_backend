
class TestGetUserPermittedStageActions:

    @staticmethod
    def test_given_valid_details_returns_actions_dto(mocker):
        # Arrange
        from unittest.mock import create_autospec
        from ib_tasks.interactors.get_user_permitted_stage_actions \
            import GetUserPermittedStageActions
        from ib_tasks.interactors.storage_interfaces.storage_interface \
            import StorageInterface

        from ib_tasks.tests.factories.storage_dtos import ActionDTOFactory
        user_id = "user_1"
        user_roles = ["ROLE_2", "ROLE_3"]
        stage_ids = ["stage_1", "stage_2"]
        ActionDTOFactory.reset_sequence()
        actions_dto = ActionDTOFactory.create_batch(size=2)
        from ib_tasks.interactors.storage_interfaces.dtos \
            import ActionRolesDTO

        action_roles = [
            ActionRolesDTO(action_id="action_1", roles=["ROLE_1", "ROLE_2"]),
            ActionRolesDTO(action_id="action_2", roles=["ROLE_3", "ROLE_4"]),
        ]
        action_ids = ["action_1", "action_2"]
        storage = create_autospec(StorageInterface)
        interactor = GetUserPermittedStageActions(
            user_id=user_id, stage_ids=stage_ids, storage=storage
        )
        storage.get_action_roles_to_stages.return_value = action_roles
        mock_obj = mocker.patch('ib_tasks.adapters.roles_service.RolesService.get_user_roles')
        mock_obj.return_value = user_roles
        storage.get_actions_dto.return_value = actions_dto

        # Act
        response = interactor.get_user_permitted_stage_actions()

        # Assert
        assert response == actions_dto
        mock_obj.called_once()
        storage.get_action_roles_to_stages\
            .assert_called_once_with(stage_ids=stage_ids)
        storage.get_actions_dto\
            .assert_called_once_with(action_ids=action_ids)