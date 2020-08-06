"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock

import pytest

from ib_boards.interactors.dtos import GetBoardsDTO
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
            user_id=1,
            offset=1,
            limit=1
        )

    @pytest.fixture
    def get_boards_dto_invalid_offset(self):
        return GetBoardsDTO(
            user_id=1,
            offset=-1,
            limit=1
        )

    @pytest.fixture
    def get_boards_dto_invalid_limit(self):
        return GetBoardsDTO(
            user_id=1,
            offset=1,
            limit=-2
        )

    @pytest.fixture
    def get_boards_dto_with_offset_exceeds(self):
        return GetBoardsDTO(
            user_id=1,
            offset=10,
            limit=2
        )

    def test_with_user_id_not_have_permission_for_boards_return_error_message(
            self, storage_mock, presenter_mock, get_boards_dto, mocker):
        # Arrange
        user_role = 'User'
        expected_response = Mock()
        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        from ib_boards.exceptions.custom_exceptions import \
            UserDoNotHaveAccessToBoards
        storage_mock.validate_user_role_with_boards_roles. \
            side_effect = UserDoNotHaveAccessToBoards
        presenter_mock.get_response_for_user_have_no_access_for_boards. \
            return_value = expected_response

        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto,
            presenter=presenter_mock
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=get_boards_dto.user_id
        )
        storage_mock.validate_user_role_with_boards_roles.assert_called_once_with(
            user_role=user_role
        )
        presenter_mock.get_response_for_user_have_no_access_for_boards. \
            assert_called_once_with()
        assert actual_response == expected_response

    def test_with_invalid_offset_value_return_error_message(
            self, storage_mock, presenter_mock, get_boards_dto_invalid_offset, mocker):
        # Arrange
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
        presenter_mock.get_response_for_invalid_offset. \
            return_value = expected_response

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto_invalid_offset,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.get_response_for_invalid_offset.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_invalid_limit_value_return_error_message(
            self, storage_mock, presenter_mock, get_boards_dto_invalid_limit, mocker):
        # Arrange
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
        presenter_mock.get_response_for_invalid_limit. \
            return_value = expected_response

        # Act
        actual_response = interactor.get_boards_wrapper(
            get_boards_dto=get_boards_dto_invalid_limit,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.get_response_for_invalid_limit.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_valid_details_return_board_details(
            self, storage_mock, presenter_mock, get_boards_dto, mocker):
        # Arrange
        total_boards = 3
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        board_ids_need_to_send = ['BOARD_ID_2']
        user_id = "user_id_1"
        board_dtos = BoardDTOFactory.create_batch(3)
        BoardDTOFactory.reset_sequence()

        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        user_role = 'User'
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )
        expected_response = Mock()
        storage_mock.get_board_ids.return_value = board_ids
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
            user_id=user_id
        )
        interactor_mock.assert_called_once_with(
            board_ids=board_ids_need_to_send
        )
        presenter_mock.get_response_for_get_boards.assert_called_once_with(
            board_dtos=board_dtos, total_boards=total_boards
        )
        assert actual_response == expected_response

    def test_with_offset_exceeds_total_count_return_error_message(
            self, storage_mock, presenter_mock,
            get_boards_dto_with_offset_exceeds, mocker):
        # Arrange
        total_boards = 3
        board_ids = ['BOARD_ID_1', 'BOARD_ID_2', 'BOARD_ID_3']
        board_ids_need_to_send = ['BOARD_ID_2']
        user_id="user_id_1"
        board_dtos = BoardDTOFactory.create_batch(3)
        BoardDTOFactory.reset_sequence()

        interactor = GetBoardsInteractor(
            storage=storage_mock
        )
        user_role = 'User'
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )
        expected_response = Mock()
        storage_mock.get_board_ids.return_value = board_ids
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
            user_id=user_id
        )
        presenter_mock.get_response_for_offset_exceeds_total_tasks. \
            assert_called_once_with()
        assert actual_response == expected_response
