from unittest.mock import create_autospec, patch

import pytest

from ib_boards.exceptions.custom_exceptions import InvalidBoardId, InvalidStageIds, UserDonotHaveAccess
from ib_boards.interactors.get_board_complete_details_interactor import GetBoardDetailsInteractor
from ib_boards.interactors.storage_interfaces.dtos import TaskBoardsDetailsDTO, BoardDTO, ColumnStageDTO, \
    ColumnBoardDTO, ColumnFieldDTO
from ib_boards.interactors.storage_interfaces.storage_interface import StorageInterface


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
                display_name="display_name"
            ),
            column_stage_dtos=[ColumnStageDTO(
                column_id="column_id_1",
                stage_id="stage_id_2"
            )],
            columns_dtos=[ColumnBoardDTO(
                board_id="board_id_1",
                name="display_name",
                column_id="column_id_1"
            )],
            columns_fields_dtos=[ColumnFieldDTO(
                column_id="column_id_1",
                field_ids=["field_id_1", "field_id_2"]
            )])
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

    @patch("ib_boards.adapters.service_adapter.ServiceAdapter.iam_service")
    def test_with_board_which_donot_have_access_raises_exception(
            self, user_roles_service, storage):
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

        user_roles_service.get_user_roles.return_value = user_roles
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

    @patch("ib_boards.adapters.service_adapter.ServiceAdapter.iam_service")
    def test_get_columns_details_given_valid_board_id(self,
                                                      user_roles_service,
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
        user_roles_service.get_user_roles.return_value = user_roles
        storage.validate_board_id.return_value = True
        storage.get_permitted_user_roles_for_board. \
            return_value = ["FIN_PAYMENT_REQUESTER"]

        # Act
        board_details = interactor.get_board_details(board_id, stages, user_id)

        # Assert
        assert board_details == response
