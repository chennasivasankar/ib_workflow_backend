from unittest.mock import create_autospec
import pytest

from ib_boards.interactors.dtos import ColumnParametersDTO
from ib_boards.interactors.get_column_details_interactor import GetColumnDetailsInteractor
from ib_boards.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_boards.tests.factories.storage_dtos import ColumnDetailsDTOFactory


class TestGetColumnDetailsInteractor:

    @pytest.fixture()
    def get_column_details_dto(self):
        return ColumnDetailsDTOFactory.create_batch(size=3)

    def test_validate_board_id_given_invalid_board_id_raises_exception(self):
        # Arrange
        board_id = "board_id_1"
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            offset=0,
            limit=10,
            user_id="user_id_1"
        )

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.validate_board_id.return_value = False
        interactor = GetColumnDetailsInteractor(
            storage=storage
        )

        # Act
        interactor.get_column_details_wrapper(
            presenter=presenter,
            columns_parameters=columns_parameters)

        # Assert
        storage.validate_board_id.assert_called_once_with(board_id=board_id)
        presenter.raise_exception_for_invalid_board_id.assert_called_once()

    def test_validate_offset_given_invalid_offset_raises_exception(self):
        # Arrange
        board_id = "board_id_1"
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            offset=-1,
            limit=10,
            user_id="user_id_1"
        )

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetColumnDetailsInteractor(
            storage=storage
        )

        # Act
        interactor.get_column_details_wrapper(
            presenter=presenter,
            columns_parameters=columns_parameters)

        # Assert
        presenter.raise_exception_for_invalid_offset_value.assert_called_once()

    def test_validate_limit_given_invalid_limit_raises_exception(self):
        # Arrange
        board_id = "board_id_1"
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            offset=2,
            limit=0,
            user_id="user_id_1"
        )

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetColumnDetailsInteractor(
            storage=storage
        )

        # Act
        interactor.get_column_details_wrapper(
            presenter=presenter,
            columns_parameters=columns_parameters)

        # Assert
        presenter.raise_exception_for_invalid_limit_value.assert_called_once()

    def test_validate_user_permissions_given_board_which_donot_have_access_raises_exception(
            self):
        # Arrange
        board_id = "board_id_1"
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            offset=2,
            limit=10,
            user_id="user_id_1"
        )

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.check_if_user_has_permissions_for_board_id.return_value = False
        interactor = GetColumnDetailsInteractor(
            storage=storage
        )

        # Act
        interactor.get_column_details_wrapper(
            presenter=presenter,
            columns_parameters=columns_parameters)

        # Assert
        presenter.raise_exception_for_user_donot_have_access_for_board.assert_called_once()

    def test_get_columns_details_given_valid_board_id_returns_columns_details(
            self, get_column_details_dto):
        # Arrange
        board_id = "board_id_1"
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            offset=0,
            limit=10,
            user_id="user_id_1"
        )
        column_ids = ["column_id_1", "column_id_2", "column_id_3"]
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.get_column_ids_for_board.return_value = column_ids
        storage.check_if_user_has_permissions_for_board_id.return_value = True
        storage.get_columns_details.return_value = get_column_details_dto
        interactor = GetColumnDetailsInteractor(
            storage=storage
        )

        # Act
        interactor.get_column_details_wrapper(
            presenter=presenter,
            columns_parameters=columns_parameters)

        # Assert
        storage.get_columns_details.assert_called_once_with(column_ids=column_ids)
