import pytest
from ib_tasks.interactors.user_action_on_task_interactor import UserActionOnTaskInteractor


class TestUserActionOnTaskInteractor:

    @staticmethod
    @pytest.fixture()
    def storage():
        from unittest.mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def presenter():
        from unittest.mock import create_autospec
        from ib_tasks.interactors.presenter_interfaces.presenter_interface \
            import PresenterInterface
        presenter = create_autospec(PresenterInterface)
        return presenter

    @staticmethod
    def gof_and_status_mock(mocker, task_dto):
        path = 'ib_tasks.interactors.get_gofs_and_status_variables_to_task' \
               '.GetGroupOfFieldsAndStatusVariablesToTaskInteractor' \
               '.get_gofs_and_status_variables_to_task'
        mock_obj = mocker.patch(path)
        mock_obj.return_value = task_dto
        return mock_obj

    @staticmethod
    def task_boards_mock(mocker, task_board_details):

        path = 'ib_tasks.adapters.boards_service.BoardsService.get_display_boards_and_column_details'

        mock_obj = mocker.patch(path)
        mock_obj.return_value = task_board_details
        return mock_obj

    @staticmethod
    def actions_dto_mock(mocker, actions_dto):

        path = 'ib_tasks.interactors.get_user_permitted_stage_actions'\
               '.GetUserPermittedStageActions' \
               '.get_user_permitted_stage_actions'
        mock_obj = mocker.patch(path)
        mock_obj.return_value = actions_dto
        return mock_obj

    @staticmethod
    def fields_mock(mocker, fields_dto):

        path = 'ib_tasks.interactors.get_field_details.GetFieldsDetails.get_fields_details'
        mock_obj = mocker.patch(path)
        mock_obj.return_value = fields_dto
        return mock_obj

    @staticmethod
    def prepare_task_complete_details(board_id,
                                      task_boards_details,
                                      actions_dto, field_dtos):
        from ib_tasks.interactors.presenter_interfaces.dtos \
            import TaskCompleteDetailsDTO
        return TaskCompleteDetailsDTO(
            board_id=board_id,
            task_boards_details=task_boards_details,
            actions_dto=actions_dto,
            field_dtos=field_dtos
        )

    def test_invalid_task_raises_exception(self, storage, presenter):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_id = "task_1"
        action_id = "action_1"

        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, task_id=task_id,
            action_id=action_id, storage=storage
        )
        storage.validate_task_id.return_value = False

        # Act
        interactor.user_action_on_task(presenter=presenter)

        # Assert
        dict_obj = presenter.raise_exception_for_invalid_task.call_args.kwargs
        expected_task_id = dict_obj['error_obj'].task_id
        assert expected_task_id == task_id

    def test_invalid_board_raises_exception(self, mocker, storage, presenter):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_id = "task_1"
        action_id = "action_1"
        mock_obj = mocker.patch(
            'ib_tasks.adapters.service_adapter.get_service_adapter')
        mock_obj.boards_service.validate_board_id.return_value = False
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, task_id=task_id,
            action_id=action_id, storage=storage
        )
        storage.validate_task_id.return_value = True

        # Act
        interactor.user_action_on_task(presenter=presenter)

        # Assert
        mock_obj.called_once()
        dict_obj = presenter.raise_exception_for_invalid_board.call_args.kwargs
        expected_board_id = dict_obj['error_obj'].board_id
        assert board_id == expected_board_id

    def test_invalid_action_raises_exception(self, mocker, storage, presenter):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_id = "task_1"
        action_id = "action_1"
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = True

        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, task_id=task_id,
            action_id=action_id, storage=storage
        )
        storage.validate_action.return_value = False

        # Act
        interactor.user_action_on_task(presenter=presenter)

        # Assert
        mock_obj.called_once()
        storage.validate_action.assert_called_once_with(action_id=action_id)
        dict_obj = \
            presenter.raise_exception_for_invalid_action.call_args.kwargs
        expected_action_id = dict_obj['error_obj'].action_id
        assert action_id == expected_action_id

    def test_given_user_permission_denied_raises_exception(
            self, mocker, storage, presenter):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_id = "task_1"
        action_id = "action_1"
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = True
        user_roles_mock = mocker.patch(
            'ib_tasks.adapters.roles_service.RolesService.get_user_roles')
        user_roles_mock.return_value = ["ROLE_1", "ROLE_3"]
        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, task_id=task_id,
            action_id=action_id, storage=storage
        )
        storage.validate_action.return_value = True
        storage.get_action_roles.return_value = ["ROLE_2", "ROLE_4"]

        # Act
        interactor.user_action_on_task(presenter=presenter)

        # Assert
        mock_obj.called_once()
        user_roles_mock.called_once()
        dict_obj = presenter.raise_exception_for_user_action_permission_denied\
            .call_args.kwargs
        expected_action_id = dict_obj['error_obj'].action_id
        assert action_id == expected_action_id

    def test_given_valid_details_returns_task_complete_details(
            self, mocker, storage, presenter):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_id = "task_1"
        action_id = "action_1"
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = True
        user_roles_mock = mocker.patch(
            'ib_tasks.adapters.roles_service.RolesService.get_user_roles')
        user_roles_mock.return_value = ["ROLE_1", "ROLE_2"]
        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, task_id=task_id,
            action_id=action_id, storage=storage
        )
        from ib_tasks.tests.common_fixtures.interactors import (
            prepare_gof_and_status_variables_dto,
            prepare_stage_ids_call_action_logic_update_stages,
            prepare_task_boards_details, prepare_user_permitted_actions,
            prepare_fields_dto
        )
        task_dto = prepare_gof_and_status_variables_dto()
        gof_mock_obj = self.gof_and_status_mock(mocker, task_dto)
        update_stage_mock = \
            prepare_stage_ids_call_action_logic_update_stages(mocker)
        task_boards_details = prepare_task_boards_details()
        task_boards_mock = self.task_boards_mock(mocker, task_boards_details)
        actions_dto = prepare_user_permitted_actions()
        actions_mock = self.actions_dto_mock(mocker, actions_dto)
        field_dtos = prepare_fields_dto()
        field_mock = self.fields_mock(mocker, field_dtos)
        storage.validate_action.return_value = True
        storage.get_action_roles.return_value = ["ROLE_2", "ROLE_4"]
        task_complete_details = self.prepare_task_complete_details(
            board_id, task_boards_details,
            actions_dto, field_dtos
        )

        # Act
        response = interactor.user_action_on_task(presenter=presenter)

        # Assert
        gof_mock_obj.called_once()
        update_stage_mock.called_once()
        task_boards_mock.called_once()
        actions_mock.called_once()
        field_mock.called_once()
        presenter.get_response_for_user_action_on_task.assert_called_once_with(
            task_complete_details_dto=task_complete_details
        )



