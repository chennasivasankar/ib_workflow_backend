"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock

import pytest

from ib_boards.interactors.dtos import ColumnTasksParametersDTO, TaskIdStageDTO
from ib_boards.interactors.get_column_tasks_interactor import \
    GetColumnTasksInteractor
from ib_boards.tests.factories.interactor_dtos import ActionDTOFactory, \
    TaskDTOFactory, TaskStatusDTOFactory


class TestGetColumnTasksInteractor:

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
            GetColumnTasksPresenterInterface
        presenter = mock.create_autospec(GetColumnTasksPresenterInterface)
        return presenter

    @pytest.fixture
    def get_column_tasks_dto(self):
        return ColumnTasksParametersDTO(
            column_id='COLUMN_ID_1',
            offset=0,
            limit=5
        )

    @pytest.fixture
    def get_column_tasks_dto_with_invalid_offset(self):
        return ColumnTasksParametersDTO(
            column_id='COLUMN_ID_1',
            offset=-1,
            limit=1
        )

    @pytest.fixture
    def get_column_tasks_dto_with_invalid_limit(self):
        return ColumnTasksParametersDTO(
            column_id='COLUMN_ID_1',
            offset=1,
            limit=-1
        )

    @pytest.fixture
    def task_complete_details_dto(self, task_dtos, action_dtos):
        from ib_boards.interactors.presenter_interfaces.presenter_interface import \
            TaskCompleteDetailsDTO
        return TaskCompleteDetailsDTO(
            total_tasks=3,
            task_dtos=task_dtos,
            action_dtos=action_dtos
        )

    @pytest.fixture
    def task_stage_dtos(self):
        return [
            TaskIdStageDTO(
                task_id="TASK_ID_1",
                stage_id="STAGE_ID_1"
            ),
            TaskIdStageDTO(
                task_id="TASK_ID_2",
                stage_id="STAGE_ID_2"
            )
        ]

    @pytest.fixture
    def task_dtos(self):
        return TaskDTOFactory.create_batch(5)

    @pytest.fixture
    def action_dtos(self):
        return ActionDTOFactory.create_batch(9)

    @pytest.fixture
    def task_status_dtos(self):
        return TaskStatusDTOFactory.create_batch(2)

    def test_with_invalid_column_id_return_error_message(
            self, presenter_mock, storage_mock, get_column_tasks_dto):
        # Arrange
        expected_response = Mock()
        column_id = 'COLUMN_ID_1'
        from ib_boards.exceptions.custom_exceptions import InvalidColumnId
        storage_mock.validate_column_id.side_effect = InvalidColumnId
        presenter_mock.get_response_for_the_invalid_column_id.\
            return_value = expected_response

        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )
        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.validate_column_id.assert_called_once_with(
            column_id=column_id
        )
        presenter_mock.get_response_for_the_invalid_column_id.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_invalid_offset_value_return_error_message(
            self, storage_mock, presenter_mock,
            get_column_tasks_dto_with_invalid_offset):
        # Arrange
        expected_response = Mock()
        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )
        presenter_mock.get_response_for_invalid_offset.\
            return_value = expected_response

        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto_with_invalid_offset,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.get_response_for_invalid_offset.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_invalid_limit_value_return_error_message(
            self, storage_mock, presenter_mock,
            get_column_tasks_dto_with_invalid_limit):
        # Arrange
        expected_response = Mock()
        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )
        presenter_mock.get_response_for_invalid_limit.\
            return_value = expected_response

        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto_with_invalid_limit,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.get_response_for_invalid_limit.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_valid_details_return_task_details(
            self, storage_mock, presenter_mock, get_column_tasks_dto, mocker,
            task_complete_details_dto, task_status_dtos, task_dtos, action_dtos,
            task_stage_dtos):

        # Arrange
        stage_ids = ['STAGE_ID_1', 'STAGE_ID_1']
        task_ids = ['TASK_ID_1', 'TASK_ID_2', 'TASK_ID_3']

        expected_response = Mock()
        storage_mock.get_column_display_stage_ids.return_value = stage_ids
        presenter_mock.get_response_column_tasks.\
            return_value = expected_response
        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )
        from ib_boards.tests.common_fixtures.interactors import \
            get_stage_display_logic_mock, get_task_details_mock

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_task_ids_mock, validate_stage_ids_mock

        validate_stage_ids_mock(
            mocker=mocker, stage_ids=stage_ids
        )
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_stage_display_logics_mock

        stage_display_logic_mock = get_stage_display_logics_mock(
            mocker=mocker
        )
        task_ids_mock = get_task_ids_mock(
            mocker=mocker,
            task_stage_dtos=task_stage_dtos
        )
        task_details_mock = get_task_details_mock(
            mocker=mocker, task_dtos=task_dtos, action_dtos=action_dtos
        )
        stage_display_logic_interactor_mock = get_stage_display_logic_mock(
            mocker=mocker, task_status_dtos=task_status_dtos
        )

        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto,
            presenter=presenter_mock
        )

        # Assert
        assert actual_response == expected_response
        task_details_mock.assert_called_once_with(
            tasks_parameters=task_stage_dtos,
            column_id=get_column_tasks_dto.column_id
        )
        task_ids_mock.assert_called_once_with(
            task_status_dtos=task_status_dtos
        )
        stage_display_logic_interactor_mock.assert_called_once_with(
            stage_ids=stage_ids
        )
        presenter_mock.get_response_column_tasks.assert_called_once_with(
            task_complete_details_dto=task_complete_details_dto
        )
        stage_display_logic_mock.assert_called_once_with(
            stage_ids=stage_ids
        )

    def test_with_user_id_not_have_permission_for_boards_return_error_message(
            self, storage_mock, presenter_mock, get_column_tasks_dto, mocker):
        # Arrange
        user_role = 'User'
        expected_response = Mock()
        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )
        from ib_boards.exceptions.custom_exceptions import \
            UserDoNotHaveAccessToColumn
        storage_mock.validate_user_role_with_column_roles.\
            side_effect = UserDoNotHaveAccessToColumn
        presenter_mock.get_response_for_user_have_no_access_for_boards.\
            return_value = expected_response

        from ib_boards.tests.common_fixtures.adapters.user_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )

        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto,
            presenter=presenter_mock
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=get_column_tasks_dto.user_id
        )
        storage_mock.validate_user_role_with_column_roles.assert_called_once_with(
            user_role=user_role
        )
        presenter_mock.get_response_for_user_have_no_access_for_boards.\
            assert_called_once_with()
        assert actual_response == expected_response




