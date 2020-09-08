"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock

import pytest

from ib_boards.adapters.iam_service import UserIsNotInProjectException
from ib_boards.interactors.dtos import GetBoardsDTO, StarredAndOtherBoardsDTO
from ib_boards.interactors.get_boards_interactor import GetBoardsInteractor
from ib_boards.tests.factories.storage_dtos import BoardDTOFactory


class TestGetBoardsInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_boards.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        from unittest import mock
        storage = mock.create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_boards.interactors.presenter_interfaces.presenter_interface import \
            GetBoardsPresenterInterface
        presenter = mock.create_autospec(GetBoardsPresenterInterface)
        return presenter

    @pytest.fixture
    def get_boards_dto(self):
        return GetBoardsDTO(
            project_id="project_id_1",
            user_id="user_id_1",
            offset=0,
            limit=100
        )

    @pytest.fixture
    def get_boards_dto_invalid_offset(self):
        return GetBoardsDTO(
            project_id="project_id_1",
            user_id="user_id_1",
            offset=-1,
            limit=1
        )

    @pytest.fixture
    def get_boards_dto_invalid_limit(self):
        return GetBoardsDTO(
            project_id="project_id_1",
            user_id="user_id_1",
            offset=1,
            limit=-2
        )

    @pytest.fixture
    def get_boards_dto_with_offset_exceeds(self):
        return GetBoardsDTO(
            project_id="project_id_1",
            user_id="user_id_1",
            offset=10,
            limit=2
        )

    def test_with_invalid_offset_value_return_error_message(
            self, storage_mock, presenter_mock, get_boards_dto_invalid_offset, mocker):
        # Arrange
        project_id = get_boards_dto_invalid_offset.project_id
        project_ids = [project_id]
        user_id = get_boards_dto_invalid_offset.user_id
        expected_response = Mock()
        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        user_role = 'User'
        roles = ["role_1"]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_get_user_roles
        adapter_mock = mock_get_user_roles(
                mocker=mocker, roles=roles
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_for_validate_if_user_is_in_project
        user_in_project_mock = mock_for_validate_if_user_is_in_project(mocker)
        user_in_project_mock.return_value = True
        presenter_mock.get_response_for_invalid_offset. \
            return_value = expected_response

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto_invalid_offset,
            presenter=presenter_mock
        )

        # Assert
        user_in_project_mock.assert_called_once_with(
            project_id=project_id, user_id=user_id)
        project_adapter_mock.assert_called_once_with(
            project_ids
        )
        adapter_mock.assert_called_once_with(user_id=user_id)
        presenter_mock.get_response_for_invalid_offset.assert_called_once()
        assert actual_response == expected_response

    def test_with_invalid_project_id_return_error_message(
            self, storage_mock, presenter_mock, get_boards_dto_invalid_offset, mocker):
        # Arrange
        project_id = get_boards_dto_invalid_offset.project_id
        project_ids = [project_id]
        user_id = get_boards_dto_invalid_offset.user_id
        expected_response = Mock()
        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        user_role = 'User'
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, [])
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_for_validate_if_user_is_in_project
        user_in_project_mock = mock_for_validate_if_user_is_in_project(mocker)
        user_in_project_mock.return_value = True
        presenter_mock.get_response_for_invalid_project_id. \
            return_value = expected_response

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto_invalid_offset,
            presenter=presenter_mock
        )

        # Assert
        project_adapter_mock.assert_called_once_with(
            project_ids
        )
        dict_obj = presenter_mock.get_response_for_invalid_project_id.call_args.kwargs
        expected_project_ids = dict_obj['error'].invalid_project_ids
        assert project_ids == expected_project_ids
        assert actual_response == expected_response

    def test_when_user_not_in_project_return_error_message(
            self, storage_mock, presenter_mock, get_boards_dto_invalid_offset, mocker):
        # Arrange
        project_id = get_boards_dto_invalid_offset.project_id
        project_ids = [project_id]
        user_id = get_boards_dto_invalid_offset.user_id
        expected_response = Mock()
        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        user_role = 'User'
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_for_validate_if_user_is_in_project
        user_in_project_mock = mock_for_validate_if_user_is_in_project(mocker)
        user_in_project_mock.side_effect = UserIsNotInProjectException
        presenter_mock.get_response_for_user_is_not_in_project. \
            return_value = expected_response

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto_invalid_offset,
            presenter=presenter_mock
        )

        # Assert
        project_adapter_mock.assert_called_once_with(
            project_ids
        )
        user_in_project_mock.assert_called_once_with(
            project_id=project_id, user_id=user_id)
        presenter_mock.get_response_for_user_is_not_in_project.assert_called_once()
        assert actual_response == expected_response

    def test_with_invalid_limit_value_return_error_message(
            self, storage_mock, presenter_mock, get_boards_dto_invalid_limit, mocker):
        # Arrange
        project_id = get_boards_dto_invalid_limit.project_id
        user_id = get_boards_dto_invalid_limit.user_id
        project_ids = [project_id]
        expected_response = Mock()
        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        user_role = 'User'
        roles = ["role_1"]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_get_user_roles
        adapter_mock = mock_get_user_roles(
                mocker=mocker, roles=roles
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_for_validate_if_user_is_in_project
        user_in_project_mock = mock_for_validate_if_user_is_in_project(mocker)
        user_in_project_mock.return_value = True
        presenter_mock.get_response_for_invalid_limit. \
            return_value = expected_response

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto_invalid_limit,
            presenter=presenter_mock
        )

        # Assert
        user_in_project_mock.assert_called_once_with(
            project_id=project_id, user_id=user_id)
        project_adapter_mock.assert_called_once_with(
            project_ids
        )
        adapter_mock.assert_called_once_with(user_id=user_id)
        presenter_mock.get_response_for_invalid_limit.assert_called_once()
        assert actual_response == expected_response

    def test_with_offset_exceeds_total_count_return_error_message(
            self, storage_mock, presenter_mock,
            get_boards_dto_with_offset_exceeds, mocker):
        # Arrange
        project_id = get_boards_dto_with_offset_exceeds.project_id
        user_id = get_boards_dto_with_offset_exceeds.user_id
        project_ids = [project_id]
        total_boards = 3
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        board_dtos = BoardDTOFactory.create_batch(3)
        starred_boards = []
        BoardDTOFactory.reset_sequence()

        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        roles = ["role_1"]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_get_user_roles
        adapter_mock = mock_get_user_roles(
                mocker=mocker, roles=roles
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_for_validate_if_user_is_in_project
        user_in_project_mock = mock_for_validate_if_user_is_in_project(mocker)
        user_in_project_mock.return_value = True
        expected_response = Mock()
        storage_mock.get_board_ids.return_value = board_ids, starred_boards
        presenter_mock.get_response_for_offset_exceeds_total_tasks. \
            return_value = expected_response
        from ib_boards.tests.common_fixtures.interactors import \
            get_board_details_mock
        interactor_mock = get_board_details_mock(mocker)

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto_with_offset_exceeds,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_board_ids.assert_called_once_with(
            user_id=user_id, project_id=project_id
        )
        user_in_project_mock.assert_called_once_with(
            project_id=project_id, user_id=user_id)
        project_adapter_mock.assert_called_once_with(
            project_ids
        )
        adapter_mock.assert_called_once_with(user_id=user_id)
        presenter_mock.get_response_for_offset_exceeds_total_tasks. \
            assert_called_once()
        assert actual_response == expected_response

    def test_with_user_id_not_have_permission_for_boards_return_error_message(
            self, storage_mock, presenter_mock, get_boards_dto, mocker):
        # Arrange
        project_id = get_boards_dto.project_id
        user_id = get_boards_dto.user_id
        project_ids = [project_id]
        user_role = 'User'
        expected_response = Mock()
        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        from ib_boards.exceptions.custom_exceptions import \
            UserDoNotHaveAccessToBoards
        storage_mock.validate_user_role_with_boards_roles. \
            side_effect = UserDoNotHaveAccessToBoards
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_for_validate_if_user_is_in_project
        user_in_project_mock = mock_for_validate_if_user_is_in_project(mocker)
        user_in_project_mock.return_value = True

        presenter_mock.get_response_for_user_have_no_access_for_boards. \
            return_value = expected_response

        roles = ["role_1"]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_get_user_roles
        adapter_mock = mock_get_user_roles(
                mocker=mocker, roles=roles
        )

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto,
            presenter=presenter_mock
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=user_id
        )
        storage_mock.validate_user_role_with_boards_roles.assert_called_once_with(
            user_role=user_role
        )
        user_in_project_mock.assert_called_once_with(
            project_id=project_id, user_id=user_id)
        project_adapter_mock.assert_called_once_with(
            project_ids
        )
        presenter_mock.get_response_for_user_have_no_access_for_boards. \
            assert_called_once()
        assert actual_response == expected_response

    def test_with_valid_details_return_board_details(
            self, storage_mock, presenter_mock, get_boards_dto, mocker):
        # Arrange
        total_boards = 3
        all_board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2']
        starred_boards = ['BOARD_ID_3']
        project_id = get_boards_dto.project_id
        project_ids = [project_id]

        BoardDTOFactory.reset_sequence()
        board_dtos = BoardDTOFactory.create_batch(2)
        starred_boards_dtos = BoardDTOFactory()
        BoardDTOFactory.reset_sequence()
        all_board_dtos = StarredAndOtherBoardsDTO(
            starred_boards_dtos=[starred_boards_dtos],
            other_boards_dtos=board_dtos
        )

        roles = ["role_1"]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_get_user_roles
        adapter_mock = mock_get_user_roles(
                mocker=mocker, roles=roles
        )
        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        user_role = "User"
        user_id = get_boards_dto.user_id
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_for_validate_if_user_is_in_project
        user_in_project_mock = mock_for_validate_if_user_is_in_project(mocker)
        user_in_project_mock.return_value = True
        expected_response = Mock()
        storage_mock.get_board_ids.return_value = board_ids, starred_boards
        presenter_mock.get_response_for_get_boards. \
            return_value = expected_response
        from ib_boards.tests.common_fixtures.interactors import \
            get_board_details_mock
        interactor_mock = get_board_details_mock(mocker)

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_board_ids.assert_called_once_with(
            user_id=user_id, project_id=project_id
        )
        interactor_mock.assert_called_once_with(
            board_ids=all_board_ids
        )
        user_in_project_mock.assert_called_once_with(
            project_id=project_id, user_id=user_id)
        project_adapter_mock.assert_called_once_with(
            project_ids
        )
        adapter_mock.assert_called_once_with(user_id=user_id)
        presenter_mock.get_response_for_get_boards.assert_called_once_with(
            starred_and_other_boards_dto=all_board_dtos, total_boards=total_boards
        )
        assert actual_response == expected_response

    def test_given_valid_details_but_user_has_no_starred_boards_return_empty_starred_boards(
            self, storage_mock, presenter_mock, get_boards_dto, mocker):
        # Arrange
        total_boards = 3
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        starred_board_ids = []
        project_id = get_boards_dto.project_id
        project_ids = [project_id]
        user_id = get_boards_dto.user_id
        BoardDTOFactory.reset_sequence()
        board_dtos = BoardDTOFactory.create_batch(3)
        all_board_dtos = StarredAndOtherBoardsDTO(
            starred_boards_dtos=[],
            other_boards_dtos=board_dtos
        )
        BoardDTOFactory.reset_sequence()
        roles = ["role_1"]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_get_user_roles
        adapter_mock = mock_get_user_roles(
                mocker=mocker, roles=roles
        )
        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_for_validate_if_user_is_in_project
        user_in_project_mock = mock_for_validate_if_user_is_in_project(mocker)
        user_in_project_mock.return_value = True
        expected_response = Mock()
        storage_mock.get_board_ids.return_value = board_ids, starred_board_ids
        presenter_mock.get_response_for_get_boards. \
            return_value = expected_response
        from ib_boards.tests.common_fixtures.interactors import \
            get_board_details_mock
        interactor_mock = get_board_details_mock(mocker)

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_board_ids.assert_called_once_with(
            user_id=user_id, project_id=project_id
        )
        interactor_mock.assert_called_once_with(
            board_ids=board_ids
        )
        user_in_project_mock.assert_called_once_with(
            project_id=project_id, user_id=user_id)
        project_adapter_mock.assert_called_once_with(
            project_ids
        )
        adapter_mock.assert_called_once_with(user_id=user_id)
        presenter_mock.get_response_for_get_boards.assert_called_once_with(
            starred_and_other_boards_dto=all_board_dtos, total_boards=total_boards
        )
        assert actual_response == expected_response

    def test_with_given_valid_project_details_return_board_details(
            self, storage_mock, presenter_mock, get_boards_dto, mocker):
        # Arrange
        total_boards = 3
        all_board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2']
        starred_boards = ['BOARD_ID_3']
        project_id = get_boards_dto.project_id
        project_ids = [project_id]
        user_id = get_boards_dto.user_id

        BoardDTOFactory.reset_sequence()
        board_dtos = BoardDTOFactory.create_batch(2)
        starred_boards_dtos = BoardDTOFactory()
        BoardDTOFactory.reset_sequence()
        all_board_dtos = StarredAndOtherBoardsDTO(
            starred_boards_dtos=[starred_boards_dtos],
            other_boards_dtos=board_dtos
        )

        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        user_role = "User"
        roles = ["role_1"]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_get_user_roles
        adapter_mock = mock_get_user_roles(
            mocker=mocker, roles=roles
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_for_validate_if_user_is_in_project
        user_in_project_mock = mock_for_validate_if_user_is_in_project(mocker)
        user_in_project_mock.return_value = True
        expected_response = Mock()
        storage_mock.get_board_ids.return_value = board_ids, starred_boards
        presenter_mock.get_response_for_get_boards. \
            return_value = expected_response
        from ib_boards.tests.common_fixtures.interactors import \
            get_board_details_mock
        interactor_mock = get_board_details_mock(mocker)

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_board_ids.assert_called_once_with(
            user_id=user_id, project_id=project_id
        )
        interactor_mock.assert_called_once_with(
            board_ids=all_board_ids
        )
        user_in_project_mock.assert_called_once_with(
            project_id=project_id, user_id=user_id)
        project_adapter_mock.assert_called_once_with(
            project_ids
        )
        adapter_mock.assert_called_once_with(user_id=user_id)
        presenter_mock.get_response_for_get_boards.assert_called_once_with(
            starred_and_other_boards_dto=all_board_dtos, total_boards=total_boards
        )
        assert actual_response == expected_response
