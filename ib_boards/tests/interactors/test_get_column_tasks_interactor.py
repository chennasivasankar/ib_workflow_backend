"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock

import pytest

from ib_boards.interactors.dtos import GetColumnTasksDTO
from ib_boards.interactors.get_column_tasks_interactor import \
    GetColumnTasksInteractor


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
        return GetColumnTasksDTO(
            column_id='COLUMN_ID_1',
            offset=1,
            limit=1
        )

    @pytest.fixture
    def get_column_tasks_dto_with_invalid_offset(self):
        return GetColumnTasksDTO(
            column_id='COLUMN_ID_1',
            offset=-1,
            limit=1
        )

    @pytest.fixture
    def get_column_tasks_dto_with_invalid_limit(self):
        return GetColumnTasksDTO(
            column_id='COLUMN_ID_1',
            offset=1,
            limit=-1
        )

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
            get_column_tasks_dto=get_column_tasks_dto,
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
            get_column_tasks_dto=get_column_tasks_dto_with_invalid_offset,
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
            get_column_tasks_dto=get_column_tasks_dto_with_invalid_limit,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.get_response_for_invalid_limit.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_valid_details_return_task_details(
            self, storage_mock, presenter_mock):
        pass


