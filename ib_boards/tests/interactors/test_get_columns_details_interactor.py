from unittest.mock import create_autospec, patch, Mock

import factory
import pytest

from ib_boards.constants.enum import ViewType
from ib_boards.interactors.dtos import ColumnParametersDTO, \
    PaginationParametersDTO, TaskStageIdDTO
from ib_boards.interactors.get_column_details_interactor import \
    GetColumnDetailsInteractor
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_boards.tests.factories.interactor_dtos import \
    ColumnTaskIdsDTOFactory, \
    TaskColumnDTOFactory, ColumnStageIdsDTOFactory, \
    TaskDetailsConfigDTOFactory, \
    GetTaskDetailsDTOFactory, TaskStageIdDTOFactory
from ib_boards.tests.factories.storage_dtos import (
    ColumnDetailsDTOFactory, TaskActionsDTOFactory, TaskFieldsDTOFactory,
    ColumnCompleteDetailsDTOFactory, TaskStageColorDTOFactory)


class TestGetColumnDetailsInteractor:

    @classmethod
    def setup_class(cls):
        ColumnDetailsDTOFactory.reset_sequence()
        TaskStageColorDTOFactory.reset_sequence()
        ColumnTaskIdsDTOFactory.reset_sequence()
        ColumnStageIdsDTOFactory.reset_sequence()
        ColumnCompleteDetailsDTOFactory.reset_sequence()
        TaskStageIdDTOFactory.reset_sequence()


    @classmethod
    def teardown_class(cls):
        pass

    @pytest.fixture()
    def mock_storage(self):
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def mock_presenter(self):
        presenter = create_autospec(PresenterInterface)
        return presenter

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

    @pytest.fixture
    def column_tasks_ids(self):
        TaskStageIdDTOFactory.reset_sequence()
        return ColumnTaskIdsDTOFactory.create_batch(3)

    @pytest.fixture
    def column_tasks_ids_no_duplicates(self):
        task_stage_ids = [TaskStageIdDTOFactory.create_batch(3),
                          TaskStageIdDTOFactory.create_batch(3),
                          TaskStageIdDTOFactory.create_batch(3)]
        return ColumnTaskIdsDTOFactory.create_batch(
            3, task_stage_ids=factory.Iterator(task_stage_ids)
        )

    @pytest.fixture
    def task_stage_color_dtos(self):
        return TaskStageColorDTOFactory.create_batch(size=4)

    @pytest.fixture
    def column_task_stage_ids(self):
        return TaskColumnDTOFactory.create_batch(
            9, column_id=factory.Iterator(
                [
                    'COLUMN_ID_1', 'COLUMN_ID_1', 'COLUMN_ID_1',
                    'COLUMN_ID_2', 'COLUMN_ID_2', 'COLUMN_ID_2',
                    'COLUMN_ID_3', 'COLUMN_ID_3', 'COLUMN_ID_3'
                ]
            ),
            task_id=factory.Iterator(
                ['TASK_ID_1', 'TASK_ID_2', 'TASK_ID_3']
            ),
            stage_id=factory.Iterator(
                ['STAGE_ID_1', 'STAGE_ID_2', 'STAGE_ID_3'],
            )
        )

    @pytest.fixture
    def column_task_stage_ids_no_duplicates(self):
        return TaskColumnDTOFactory.create_batch(
            9, column_id=factory.Iterator(
                [
                    'COLUMN_ID_4', 'COLUMN_ID_4', 'COLUMN_ID_4',
                    'COLUMN_ID_5', 'COLUMN_ID_5', 'COLUMN_ID_5',
                    'COLUMN_ID_6', 'COLUMN_ID_6', 'COLUMN_ID_6'
                ]
            ),
            task_id=factory.Iterator(
                [
                    'TASK_ID_1', 'TASK_ID_2', 'TASK_ID_3',
                    'TASK_ID_4', 'TASK_ID_5', 'TASK_ID_6',
                    'TASK_ID_7', 'TASK_ID_8', 'TASK_ID_9'
                ]
            ),
            stage_id=factory.Iterator(
                [
                    'STAGE_ID_1', 'STAGE_ID_2', 'STAGE_ID_3',
                    'STAGE_ID_4', 'STAGE_ID_5', 'STAGE_ID_6',
                    'STAGE_ID_7', 'STAGE_ID_8', 'STAGE_ID_9'
                ],
            )
        )

    @pytest.fixture
    def column_stage_dtos(self):
        ColumnStageIdsDTOFactory.reset_sequence()
        ColumnStageIdsDTOFactory.stage_ids.reset()
        return ColumnStageIdsDTOFactory.create_batch(3)

    @pytest.fixture
    def column_complete_details(self):
        return ColumnCompleteDetailsDTOFactory.create_batch(
            3, total_tasks=10
        )

    @pytest.fixture
    def task_ids_config(self):
        TaskDetailsConfigDTOFactory.reset_sequence()
        return TaskDetailsConfigDTOFactory.create_batch(3)

    @pytest.fixture
    def task_ids_stage_id(self):
        return GetTaskDetailsDTOFactory.create_batch(
            9,
            task_id=factory.Iterator(
                ['TASK_ID_1', 'TASK_ID_2', 'TASK_ID_3']
            ),
            stage_id=factory.Iterator(
                ['STAGE_ID_1', 'STAGE_ID_2', 'STAGE_ID_3'],
            )
        )

    @pytest.fixture
    def task_ids_stage_id_no_duplicates(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory.create_batch(9)

    def test_with_invalid_board_id_raises_exception(self):
        # Arrange

        board_id = "board_id_1"
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            user_id="user_id_1",
            view_type=ViewType.LIST.value,
            search_query="hello"
        )
        pagination_parameters = PaginationParametersDTO(
            offset=2,
            limit=10
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
            columns_parameters=columns_parameters,
            pagination_parameters=pagination_parameters)

        # Assert
        storage.validate_board_id.assert_called_once_with(board_id=board_id)
        presenter.response_for_invalid_board_id.assert_called_once()

    @patch("ib_boards.adapters.service_adapter.ServiceAdapter.iam_service")
    def test_with_invalid_offset_raises_exception(self, user_roles_service):
        # Arrange

        board_id = "board_id_1"
        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_LEVEL1_VERIFIER",
                      "FIN_PAYMENTS_LEVEL2_VERIFIER",
                      "FIN_PAYMENTS_LEVEL3_VERIFIER"]
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            user_id="user_id_1",
            view_type=ViewType.LIST.value,
            search_query="hello"
        )
        pagination_parameters = PaginationParametersDTO(
            offset=-1,
            limit=10
        )

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetColumnDetailsInteractor(
            storage=storage
        )
        user_roles_service.get_user_roles.return_value = user_roles
        board_permitted_user_roles = ["FIN_PAYMENT_POC"]

        storage.get_permitted_user_roles_for_board.return_value = board_permitted_user_roles

        # Act
        interactor.get_column_details_wrapper(
            presenter=presenter,
            columns_parameters=columns_parameters,
            pagination_parameters=pagination_parameters)

        # Assert
        presenter.response_for_invalid_offset_value.assert_called_once()

    @patch("ib_boards.adapters.service_adapter.ServiceAdapter.iam_service")
    def test_with_invalid_limit_raises_exception(self, user_roles_service):
        # Arrange
        board_id = "board_id_1"
        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_LEVEL1_VERIFIER",
                      "FIN_PAYMENTS_LEVEL2_VERIFIER",
                      "FIN_PAYMENTS_LEVEL3_VERIFIER"]
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            user_id="user_id_1",
            view_type=ViewType.LIST.value,
            search_query="hello"
        )
        pagination_parameters = PaginationParametersDTO(
            offset=2,
            limit=0
        )
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = GetColumnDetailsInteractor(
            storage=storage
        )
        user_roles_service.get_user_roles.return_value = user_roles
        board_permitted_user_roles = ["FIN_PAYMENT_POC"]

        storage.get_permitted_user_roles_for_board.return_value = board_permitted_user_roles

        # Act
        interactor.get_column_details_wrapper(
            presenter=presenter,
            columns_parameters=columns_parameters,
            pagination_parameters=pagination_parameters)

        # Assert
        presenter.response_for_invalid_limit_value.assert_called_once()

    @patch("ib_boards.adapters.service_adapter.ServiceAdapter.iam_service")
    def test_with_board_which_do_not_have_access_raises_exception(
            self, user_roles_service, mock_storage, mock_presenter):
        # Arrange
        storage = mock_storage
        presenter = mock_presenter
        board_id = "board_id_1"
        user_id = "user_id_1"
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            user_id=user_id,
            view_type=ViewType.LIST.value,
            search_query="hello"
        )
        pagination_parameters = PaginationParametersDTO(
            offset=2,
            limit=10
        )
        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_LEVEL1_VERIFIER",
                      "FIN_PAYMENTS_LEVEL2_VERIFIER",
                      "FIN_PAYMENTS_LEVEL3_VERIFIER"]

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
            columns_parameters=columns_parameters,
            pagination_parameters=pagination_parameters)

        # Assert
        storage.get_permitted_user_roles_for_board.assert_called_once_with(
            board_id=board_id
        )
        presenter.response_for_user_donot_have_access_for_board.assert_called_once()

    @patch("ib_boards.adapters.service_adapter.ServiceAdapter.iam_service")
    def test_with_valid_board_id_returns_columns_details_return_column_details_with_duplicate(
            self, user_roles_service, get_column_details_dto, mocker,
            get_task_actions_dtos, get_task_fields_dtos, mock_storage,
            mock_presenter, column_tasks_ids, column_task_stage_ids,
            column_stage_dtos, column_complete_details, task_ids_config,
            task_ids_stage_id, task_stage_color_dtos):
        # Arrange
        storage = mock_storage
        presenter = mock_presenter
        board_id = "board_id_1"
        user_id = "user_id_1"
        expected_response = Mock()
        task_fields_dto = get_task_fields_dtos
        task_actions_dto = get_task_actions_dtos
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            user_id=user_id,
            view_type=ViewType.LIST.value,
            search_query="hello"
        )
        pagination_parameters = PaginationParametersDTO(
            offset=0,
            limit=10
        )
        column_ids = ["COLUMN_ID_1", "COLUMN_ID_2", "COLUMN_ID_3"]
        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_LEVEL1_VERIFIER",
                      "FIN_PAYMENTS_LEVEL2_VERIFIER",
                      "FIN_PAYMENTS_LEVEL3_VERIFIER"]

        tasks_dtos = [TaskStageIdDTO(task_id="task_id_1",
                                     stage_id="stage_id_1")]

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            prepare_task_details_dtos
        task_details_dto = prepare_task_details_dtos(mocker, tasks_dtos,
                                                     user_id=user_id,
                                                     view_type=ViewType.LIST.value)
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_task_ids_mock

        task_ids_mock = get_task_ids_mock(mocker, column_tasks_ids)
        task_details_dto.return_value = task_fields_dto, task_actions_dto, task_stage_color_dtos
        user_roles_service.get_user_roles.return_value = user_roles
        board_permitted_user_roles = ["FIN_PAYMENT_POC"]

        storage.get_column_ids_for_board.return_value = column_ids
        storage.get_permitted_user_roles_for_board.return_value = board_permitted_user_roles
        storage.get_columns_details.return_value = get_column_details_dto
        storage.get_columns_stage_ids.return_value = column_stage_dtos
        presenter.get_response_for_column_details.return_value = expected_response
        interactor = GetColumnDetailsInteractor(
            storage=storage
        )

        # Act
        actual_response = interactor.get_column_details_wrapper(
            presenter=presenter,
            columns_parameters=columns_parameters,
            pagination_parameters=pagination_parameters)

        # Assert
        storage.get_columns_details.assert_called_once_with(
            column_ids=column_ids)
        storage.get_columns_stage_ids.assert_called_once_with(
            column_ids=column_ids
        )
        task_ids_mock.assert_called_once_with(
            task_config_dtos=task_ids_config
        )
        task_details_dto.assert_called_once_with(
            task_ids_stage_id, user_id=user_id, view_type=ViewType.LIST.value
        )
        presenter.get_response_for_column_details.assert_called_once_with(
            column_tasks=column_task_stage_ids,
            task_actions_dtos=task_actions_dto,
            task_fields_dtos=task_fields_dto,
            column_details=column_complete_details,
            task_stage_color_dtos=task_stage_color_dtos
        )
        assert actual_response == expected_response

    @patch("ib_boards.adapters.service_adapter.ServiceAdapter.iam_service")
    def test_with_valid_board_id_returns_columns_details_return_column_details(
            self, user_roles_service, get_column_details_dto, mocker,
            get_task_actions_dtos, get_task_fields_dtos, mock_storage,
            mock_presenter, column_tasks_ids_no_duplicates,
            column_task_stage_ids_no_duplicates,
            column_stage_dtos, column_complete_details, task_ids_config,
            task_ids_stage_id_no_duplicates, task_stage_color_dtos):
        # Arrange
        storage = mock_storage
        presenter = mock_presenter
        board_id = "board_id_1"
        user_id = "user_id_1"
        expected_response = Mock()
        task_fields_dto = get_task_fields_dtos
        task_actions_dto = get_task_actions_dtos
        columns_parameters = ColumnParametersDTO(
            board_id=board_id,
            user_id=user_id,
            view_type=ViewType.LIST.value,
            search_query="hello"
        )
        pagination_parameters = PaginationParametersDTO(
            offset=0,
            limit=10
        )
        column_ids = ["COLUMN_ID_4", "COLUMN_ID_5", "COLUMN_ID_6"]
        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_LEVEL1_VERIFIER",
                      "FIN_PAYMENTS_LEVEL2_VERIFIER",
                      "FIN_PAYMENTS_LEVEL3_VERIFIER"]

        tasks_dtos = [TaskStageIdDTO(task_id="task_id_1",
                                     stage_id="stage_id_1")]

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            prepare_task_details_dtos
        task_details_dto = prepare_task_details_dtos(mocker, tasks_dtos,
                                                     user_id=user_id,
                                                     view_type=ViewType.LIST.value)
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_task_ids_mock

        task_ids_mock = get_task_ids_mock(mocker, column_tasks_ids_no_duplicates)
        task_details_dto.return_value = task_fields_dto, task_actions_dto, task_stage_color_dtos
        user_roles_service.get_user_roles.return_value = user_roles
        board_permitted_user_roles = ["FIN_PAYMENT_POC"]

        storage.get_column_ids_for_board.return_value = column_ids
        storage.get_permitted_user_roles_for_board.return_value = board_permitted_user_roles
        storage.get_columns_details.return_value = get_column_details_dto
        storage.get_columns_stage_ids.return_value = column_stage_dtos
        presenter.get_response_for_column_details.return_value = expected_response
        interactor = GetColumnDetailsInteractor(
            storage=storage
        )

        # Act
        actual_response = interactor.get_column_details_wrapper(
            presenter=presenter,
            columns_parameters=columns_parameters,
            pagination_parameters=pagination_parameters)

        # Assert
        storage.get_columns_details.assert_called_once_with(
            column_ids=column_ids)
        task_ids_mock.assert_called_once_with(
            task_config_dtos=task_ids_config
        )
        task_details_dto.assert_called_once_with(
            task_ids_stage_id_no_duplicates, user_id=user_id,
            view_type=ViewType.LIST.value
        )
        presenter.get_response_for_column_details.assert_called_once_with(
            column_tasks=column_task_stage_ids_no_duplicates,
            task_actions_dtos=task_actions_dto,
            task_fields_dtos=task_fields_dto,
            column_details=column_complete_details,
            task_stage_color_dtos=task_stage_color_dtos
        )
        assert actual_response == expected_response
