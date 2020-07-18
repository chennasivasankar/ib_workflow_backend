from unittest.mock import create_autospec, patch
import pytest

from ib_boards.interactors.dtos import ColumnParametersDTO
from ib_boards.interactors.get_column_details_interactor import GetColumnDetailsInteractor
from ib_boards.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import TaskDTO
from ib_boards.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_boards.tests.factories.storage_dtos import (
    ColumnDetailsDTOFactory, TaskActionsDTOFactory, TaskFieldsDTOFactory)


class TestGetColumnDetailsInteractor:

    @pytest.fixture()
    def get_column_details_dto(self):
        return ColumnDetailsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_actions_dtos(self):
        TaskActionsDTOFactory.reset_sequence()

        return TaskActionsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_fields_dtos(self):
        TaskFieldsDTOFactory.reset_sequence()

        return TaskFieldsDTOFactory.create_batch(size=3)

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

    @patch("ib_boards.adapters.service_adapter.ServiceAdapter.user_roles_service")
    def test_validate_user_permissions_given_board_which_donot_have_access_raises_exception(
            self, user_roles_service):
        # Arrange

        board_id = "board_id_1"
        user_id = "user_id_1"
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            offset=2,
            limit=10,
            user_id=user_id
        )

        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_LEVEL1_VERIFIER",
                      "FIN_PAYMENTS_LEVEL2_VERIFIER",
                      "FIN_PAYMENTS_LEVEL3_VERIFIER"]

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        board_permitted_user_roles = ["FIN_PAYMENTS_LEVEL4_VERIFIER",
                                      "FIN_PAYMENTS_LEVEL5_VERIFIER",
                                      "FIN_PAYMENTS_LEVEL6_VERIFIER"]
        user_roles_service.get_user_roles.return_value = user_roles
        storage.get_permitted_user_roles_for_board.return_value = board_permitted_user_roles

        interactor = GetColumnDetailsInteractor(
            storage=storage
        )

        # Act

        interactor.get_column_details_wrapper(
            presenter=presenter,
            columns_parameters=columns_parameters)

        # Assert
        storage.get_permitted_user_roles_for_board.assert_called_once_with(
            board_id=board_id
        )
        presenter.raise_exception_for_user_donot_have_access_for_board.assert_called_once()

    @patch("ib_boards.adapters.service_adapter.ServiceAdapter.user_roles_service")
    def test_get_columns_details_given_valid_board_id_returns_columns_details(
            self, user_roles_service, get_column_details_dto, mocker,
            get_task_actions_dtos, get_task_fields_dtos):
        # Arrange
        board_id = "board_id_1"
        user_id = "user_id_1"
        task_fields_dto = get_task_fields_dtos
        task_actions_dto = get_task_actions_dtos
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            offset=0,
            limit=10,
            user_id=user_id
        )
        column_ids = ["column_id_1", "column_id_2", "column_id_3"]
        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_LEVEL1_VERIFIER",
                      "FIN_PAYMENTS_LEVEL2_VERIFIER",
                      "FIN_PAYMENTS_LEVEL3_VERIFIER"]

        tasks_dtos = [TaskDTO(task_id="task_id_1",
                              column_id="column_id_1",
                              stage_id="stage_id_1")]

        from ib_boards.tests.common_fixtures.adapters.task_service import prepare_task_details_dtos
        task_details_dto = prepare_task_details_dtos(mocker, tasks_dtos, user_id=user_id)
        task_details_dto.return_value = task_fields_dto, task_actions_dto
        user_roles_service.get_user_roles.return_value = user_roles
        board_permitted_user_roles = ["FIN_PAYMENT_POC"]

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        storage.get_column_ids_for_board.return_value = column_ids
        storage.get_permitted_user_roles_for_board.return_value = board_permitted_user_roles
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
