"""
Created on: 13/07/20
Author: Pavankumar Pamuru

"""

import pytest

from ib_boards.interactors.create_boards_and_columns_interactor import \
    CreateBoardsAndColumnsInteractor
from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory, \
    ColumnDTOFactory, TaskTemplateStagesDTOFactory, TaskSummaryFieldsDTOFactory


class TestCreateBoardsAndColumnsInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_boards.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        from unittest import mock
        storage = mock.create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def sequence_reset(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        TaskSummaryFieldsDTOFactory.reset_sequence()
        BoardDTOFactory.reset_sequence()
        ColumnDTOFactory.reset_sequence()

    @pytest.fixture
    def board_dtos_with_no_display_name(self):
        return [
            BoardDTOFactory(name=''),
            BoardDTOFactory()
        ]

    @pytest.fixture
    def board_dtos(self):
        return BoardDTOFactory.create_batch(3)

    @pytest.fixture
    def column_dtos(self):
        return ColumnDTOFactory.create_batch(3)

    @pytest.fixture
    def column_dtos_with_invalid_task_template_id(self):
        return ColumnDTOFactory.create_batch(1)

    @pytest.fixture
    def mock_valid_task_and_template_ids(self, mocker):
        task_template_ids = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_valid_task_template_ids_mock
        get_valid_task_template_ids_mock(
            mocker=mocker,
            task_template_ids=task_template_ids
        )

    def test_with_invalid_board_display_name_raise_exception(
            self, storage_mock, sequence_reset,
            board_dtos_with_no_display_name, column_dtos):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidBoardDisplayName
        with pytest.raises(InvalidBoardDisplayName) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos_with_no_display_name,
                column_dtos=column_dtos
            )

    def test_with_invalid_user_role_ids_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_invalid_task_template_id,
            mocker, mock_valid_task_and_template_ids):
        # Arrange
        valid_user_roles = ['ALL_ROLES', 'MEMBER']
        user_roles = ['ALL_ROLES']
        invalid_user_roles = ['USER']
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock

        adapter_mock = adapter_mock(mocker=mocker,
                                    user_roles=invalid_user_roles)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidUserRoles
        with pytest.raises(InvalidUserRoles) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_id
            )
        # Assert
        adapter_mock.assert_called_once_with(
            user_roles=user_roles
        )
        assert error.value.user_role_ids == user_roles

    def test_with_valid_data_creates_data(
            self, storage_mock, sequence_reset, board_dtos, column_dtos,
            mock_valid_task_and_template_ids, mocker):
        # Arrange
        user_roles = ['ALL_ROLES', 'MEMBER', 'USER']
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock
        adapter_mock = adapter_mock(mocker=mocker,
                                    user_roles=user_roles)
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )
        board_dtos.append(
            BoardDTOFactory(board_id='BOARD_ID_0')
        )
        storage_mock.get_existing_board_ids.return_value = []
        # Act
        interactor.create_boards_and_columns(
            board_dtos=board_dtos,
            column_dtos=column_dtos
        )

        # Assert
        storage_mock.create_boards_and_columns.assert_called_once_with(
            board_dtos=board_dtos,
            column_dtos=column_dtos
        )
