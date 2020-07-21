from unittest.mock import create_autospec

from ib_tasks.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_tasks.interactors.user_action_on_task_interactor import UserActionOnTaskInteractor
from ib_tasks.tests.common_fixtures.interactors import prepare_gof_and_status_variables_dto, \
    prepare_stage_ids_call_action_logic_update_stages


class TestUserActionOnTaskInteractor:

    def test_invalid_task_raises_exception(self):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_id = "task_1"
        action_id = "action_1"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
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

    def test_invalid_board_raises_exception(self, mocker):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_id = "task_1"
        action_id = "action_1"
        mock_obj = mocker.patch('ib_tasks.adapters.service_adapter.get_service_adapter')
        mock_obj.boards_service.validate_board_id.return_value = False
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
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

    def test_invalid_action_raises_exception(self, mocker):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_id = "task_1"
        action_id = "action_1"
        mock_obj = mocker.patch('ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = True
        storage = create_autospec(StorageInterface)
        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, task_id=task_id,
            action_id=action_id, storage=storage
        )
        storage.validate_action.return_value = False
        presenter = create_autospec(PresenterInterface)

        # Act
        interactor.user_action_on_task(presenter=presenter)

        # Assert
        mock_obj.called_once()
        storage.validate_action.assert_called_once_with(action_id=action_id)
        dict_obj = \
            presenter.raise_exception_for_invalid_action.call_args.kwargs
        expected_action_id = dict_obj['error_obj'].action_id
        assert action_id == expected_action_id

    def test_given_user_permission_denied_raises_exception(self, mocker):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_id = "task_1"
        action_id = "action_1"
        mock_obj = mocker.patch('ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = True
        user_roles_mock = mocker.patch('ib_tasks.adapters.roles_service.RolesService.get_user_roles')
        user_roles_mock.return_value = ["ROLE_1", "ROLE_3"]
        storage = create_autospec(StorageInterface)
        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, task_id=task_id,
            action_id=action_id, storage=storage
        )
        storage.validate_action.return_value = True
        storage.get_action_roles.return_value = ["ROLE_2", "ROLE_4"]
        presenter = create_autospec(PresenterInterface)

        # Act
        interactor.user_action_on_task(presenter=presenter)

        # Assert
        mock_obj.called_once()
        user_roles_mock.called_once()
        dict_obj = presenter.raise_exception_for_user_action_permission_denied\
            .call_args.kwargs
        expected_action_id = dict_obj['error_obj'].action_id
        assert action_id == expected_action_id

    def test_given_valid_details_returns_task_complete_details(self, mocker):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_id = "task_1"
        action_id = "action_1"
        mock_obj = mocker.patch('ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = True
        user_roles_mock = mocker.patch('ib_tasks.adapters.roles_service.RolesService.get_user_roles')
        user_roles_mock.return_value = ["ROLE_1", "ROLE_2"]
        storage = create_autospec(StorageInterface)
        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, task_id=task_id,
            action_id=action_id, storage=storage
        )
        gof_mock_obj = prepare_gof_and_status_variables_dto(mocker)
        update_stage_mock = \
            prepare_stage_ids_call_action_logic_update_stages(mocker)

        storage.validate_action.return_value = True
        storage.get_action_roles.return_value = ["ROLE_2", "ROLE_4"]
        presenter = create_autospec(PresenterInterface)

        # Act
        response = interactor.user_action_on_task(presenter=presenter)

        # Assert
        gof_mock_obj.called_once()
        update_stage_mock.called_once()


