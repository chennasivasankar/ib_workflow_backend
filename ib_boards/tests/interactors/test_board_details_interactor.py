from unittest.mock import create_autospec

import pytest

from ib_boards.exceptions.custom_exceptions import InvalidBoardId, \
    UserDonotHaveAccess
from ib_boards.interactors.get_board_complete_details_interactor import \
    GetBoardDetailsInteractor
from ib_boards.interactors.storage_interfaces.dtos import TaskBoardsDetailsDTO, \
    BoardDTO, ColumnStageDTO, \
    ColumnBoardDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class TestBoardDetailsInteractor:

    @pytest.fixture()
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def response(self):
        task_details = TaskBoardsDetailsDTO(
            board_dto=BoardDTO(
                board_id="board_id_1",
                name="name"
            ),
            column_stage_dtos=[ColumnStageDTO(
                column_id="column_id_1",
                stage_id="stage_id_2"
            )],
            columns_dtos=[ColumnBoardDTO(
                board_id="board_id_1",
                name="name",
                column_id="column_id_1"
            )])
        return task_details

    @pytest.fixture()
    def response_with_no_columns_and_stages(self):
        task_details = TaskBoardsDetailsDTO(
            board_dto=BoardDTO(
                board_id="board_id_1",
                name="name"
            ),
            column_stage_dtos=[],
            columns_dtos=[])
        return task_details

    def test_validate_board_id_given_invalid_raises_exception(self, storage):
        # Arrange
        user_id = "user_id_1"
        board_id = "board_id"
        stages = ["stage_id_1", "stage_id_2", "stage_id_3"]

        interactor = GetBoardDetailsInteractor(storage=storage)

        storage.validate_board_id.return_value = False

        # Act
        with pytest.raises(InvalidBoardId):
            interactor.get_board_details(board_id=board_id, stage_ids=stages,
                                         user_id=user_id)

        # Assert
        storage.validate_board_id.assert_called_once_with(board_id)

    def test_with_board_which_donot_have_access_raises_exception(
            self, mocker, storage):
        # Arrange
        storage = storage
        user_id = "user_id_1"
        board_id = "board_id"
        stages = ["stage_id_1", "stage_id_2", "stage_id_3"]

        interactor = GetBoardDetailsInteractor(storage=storage)

        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_LEVEL1_VERIFIER",
                      "FIN_PAYMENTS_LEVEL2_VERIFIER",
                      "FIN_PAYMENTS_LEVEL3_VERIFIER"]

        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_get_user_roles

        user_roles_mock = mock_get_user_roles(mocker, user_roles)

        storage.validate_board_id.return_value = True
        storage.get_permitted_user_roles_for_board. \
            return_value = ["FIN_PAYMENTS_LEVEL4_VERIFIER",
                            "FIN_PAYMENTS_LEVEL5_VERIFIER",
                            "FIN_PAYMENTS_LEVEL6_VERIFIER"]

        # Act
        with pytest.raises(UserDonotHaveAccess):
            interactor.get_board_details(board_id=board_id, stage_ids=stages,
                                         user_id=user_id)

        # Assert
        storage.validate_board_id.assert_called_once_with(board_id)
        user_roles_mock.assert_called_once_with(user_id)

    def test_get_columns_details_given_valid_board_id(self,
                                                      mocker,
                                                      storage,
                                                      response):
        # Arrange
        storage = storage
        user_id = "user_id_1"
        board_id = "board_id"
        stages = ["stage_id_1", "stage_id_2", "stage_id_3"]

        interactor = GetBoardDetailsInteractor(storage=storage)

        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER"]

        storage.get_board_complete_details.return_value = response
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_get_user_roles

        user_roles_mock = mock_get_user_roles(mocker, user_roles)

        storage.validate_board_id.return_value = True
        storage.get_permitted_user_roles_for_board. \
            return_value = ["FIN_PAYMENT_REQUESTER"]

        # Act
        board_details = interactor.get_board_details(board_id, stages, user_id)

        # Assert
        assert board_details == response
        user_roles_mock.assert_called_once_with(user_id)


    def test_get_columns_details_given_valid_board_id_but_board_has_no_columns(
            self, mocker, storage, response_with_no_columns_and_stages):
        # Arrange
        storage = storage
        user_id = "user_id_1"
        board_id = "board_id"
        stages = []

        interactor = GetBoardDetailsInteractor(storage=storage)

        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER"]

        storage.get_board_complete_details.return_value = \
            response_with_no_columns_and_stages
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_get_user_roles

        user_roles_mock = mock_get_user_roles(mocker, user_roles)

        storage.validate_board_id.return_value = True
        storage.get_permitted_user_roles_for_board. \
            return_value = ["FIN_PAYMENT_REQUESTER"]

        # Act
        board_details = interactor.get_board_details(board_id, stages, user_id)

        # Assert
        assert board_details == response_with_no_columns_and_stages
        user_roles_mock.assert_called_once_with(user_id)
