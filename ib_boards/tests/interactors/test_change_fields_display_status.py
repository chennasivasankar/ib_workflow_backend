"""
Created on: 04/09/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock, create_autospec

import pytest


class TestChangeFieldsDisplayOrder:

    @pytest.fixture
    def storage(self):
        from ib_boards.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        return create_autospec(StorageInterface)

    @pytest.fixture
    def presenter(self):
        from ib_boards.interactors.presenter_interfaces.presenter_interface import \
            FieldsDisplayStatusPresenterInterface
        return create_autospec(FieldsDisplayStatusPresenterInterface)

    def test_with_invalid_column_id_return_exception_message(self, storage, presenter):
        # Arrange
        expected_response = Mock()
        from ib_boards.interactors.change_field_display_status_in_columns_list_view import \
            ChangeFieldsDisplayStatus
        from ib_boards.interactors.dtos import ChangeFieldsStatusParameter
        interactor = ChangeFieldsDisplayStatus(
            storage=storage
        )
        from ib_boards.exceptions.custom_exceptions import InvalidColumnId
        storage.validate_column_id.side_effect = InvalidColumnId
        presenter.get_response_for_the_invalid_column_id.return_value = expected_response
        from ib_boards.constants.enum import DisplayStatus
        field_display_status_parameter = ChangeFieldsStatusParameter(
            user_id='user_id_1',
            column_id='column_id_1',
            field_id='field_id',
            display_status=DisplayStatus.HIDE.value
        )

        # Act
        actual_response = interactor.change_field_display_status_wrapper(
            field_display_status_parameter=field_display_status_parameter,
            presenter=presenter
        )

        # Assert
        storage.validate_column_id.assert_called_once_with(
            column_id=field_display_status_parameter.column_id
        )
        presenter.get_response_for_the_invalid_column_id.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_user_not_have_access_to_column_return_exception_message(
            self, storage, presenter, mocker):
        # Arrange
        expected_response = Mock()
        user_role = 'User',
        project_id = "1"
        from ib_boards.interactors.change_field_display_status_in_columns_list_view import \
            ChangeFieldsDisplayStatus
        from ib_boards.interactors.dtos import ChangeFieldsStatusParameter
        interactor = ChangeFieldsDisplayStatus(
            storage=storage
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )
        from ib_boards.exceptions.custom_exceptions import \
            UserDoNotHaveAccessToColumn
        storage.validate_user_role_with_column_roles. \
            side_effect = UserDoNotHaveAccessToColumn
        storage.get_project_id_for_given_column_id.return_value = project_id
        presenter.get_response_for_user_have_no_access_for_column.return_value = expected_response
        from ib_boards.constants.enum import DisplayStatus
        field_display_status_parameter = ChangeFieldsStatusParameter(
            user_id='user_id_1',
            column_id='column_id_1',
            field_id='field_id',
            display_status=DisplayStatus.HIDE.value
        )

        # Act
        actual_response = interactor.change_field_display_status_wrapper(
            field_display_status_parameter=field_display_status_parameter,
            presenter=presenter
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=field_display_status_parameter.user_id, project_id=project_id
        )
        storage.validate_user_role_with_column_roles.assert_called_once_with(
            user_role=user_role, column_id=field_display_status_parameter.column_id
        )
        presenter.get_response_for_user_have_no_access_for_column. \
            assert_called_once_with()
        assert actual_response == expected_response

    def test_with_field_not_belongs_to_column_return_exception_message(
            self, storage, presenter, mocker):
        # Arrange
        expected_response = Mock()
        user_role = 'User',
        project_id = "1"
        from ib_boards.interactors.change_field_display_status_in_columns_list_view import \
            ChangeFieldsDisplayStatus
        from ib_boards.interactors.dtos import ChangeFieldsStatusParameter
        interactor = ChangeFieldsDisplayStatus(
            storage=storage
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )
        storage.get_project_id_for_given_column_id.return_value = project_id
        from ib_boards.exceptions.custom_exceptions import \
            FieldNotBelongsToColumn
        storage.validate_field_id_with_column_id.side_effect = FieldNotBelongsToColumn
        presenter.get_response_for_field_not_belongs_to_column.return_value = expected_response
        from ib_boards.constants.enum import DisplayStatus
        field_display_status_parameter = ChangeFieldsStatusParameter(
            user_id='user_id_1',
            column_id='column_id_1',
            field_id='field_id',
            display_status=DisplayStatus.HIDE.value
        )

        # Act
        actual_response = interactor.change_field_display_status_wrapper(
            field_display_status_parameter=field_display_status_parameter,
            presenter=presenter
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=field_display_status_parameter.user_id, project_id=project_id
        )
        storage.validate_field_id_with_column_id.assert_called_once_with(
            field_id=field_display_status_parameter.field_id,
            column_id=field_display_status_parameter.column_id,
            user_id=field_display_status_parameter.user_id
        )
        presenter.get_response_for_field_not_belongs_to_column. \
            assert_called_once_with()
        assert actual_response == expected_response

    def test_with_valid_data_creates_data(
            self, storage, presenter, mocker):
        # Arrange
        expected_response = Mock()
        user_role = 'User',
        project_id = "1"
        from ib_boards.interactors.change_field_display_status_in_columns_list_view import \
            ChangeFieldsDisplayStatus
        from ib_boards.interactors.dtos import ChangeFieldsStatusParameter
        interactor = ChangeFieldsDisplayStatus(
            storage=storage
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )
        storage.get_project_id_for_given_column_id.return_value = project_id
        from ib_boards.constants.enum import DisplayStatus
        field_display_status_parameter = ChangeFieldsStatusParameter(
            user_id='user_id_1',
            column_id='column_id_1',
            field_id='field_id',
            display_status=DisplayStatus.HIDE.value
        )

        # Act
        interactor.change_field_display_status_wrapper(
            field_display_status_parameter=field_display_status_parameter,
            presenter=presenter
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=field_display_status_parameter.user_id, project_id=project_id
        )
        storage.validate_field_id_with_column_id.assert_called_once_with(
            field_id=field_display_status_parameter.field_id,
            column_id=field_display_status_parameter.column_id,
            user_id=field_display_status_parameter.user_id
        )
        storage.change_display_status_of_field.assert_called_once_with(
            field_display_status_parameter=field_display_status_parameter
        )