"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock

import pytest

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

    def test_with_invalid_column_id_return_error_message(
            self, presenter_mock, storage_mock):
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
            column_id=column_id,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.validate_column_id.assert_called_once_with(
            column_id=column_id
        )
        presenter_mock.get_response_for_the_invalid_column_id.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_valid_details_return_task_details(
            self, storage_mock, presenter_mock):
        pass


