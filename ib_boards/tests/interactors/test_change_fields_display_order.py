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
            FieldsDisplayOrderPresenterInterface
        return create_autospec(FieldsDisplayOrderPresenterInterface)

    def test_with_invalid_column_id_return_exception_message(self, storage,
                                                             presenter):
        # Arrange
        expected_response = Mock()
        from ib_boards.interactors.dtos import ChangeFieldsOrderParameter
        from ib_boards.interactors.change_field_order_in_column_list_view import \
            ChangeFieldsDisplayOrder
        interactor = ChangeFieldsDisplayOrder(
            storage=storage
        )
        from ib_boards.exceptions.custom_exceptions import InvalidColumnId
        storage.validate_column_id.side_effect = InvalidColumnId
        presenter.get_response_for_the_invalid_column_id.return_value = expected_response
        field_order_parameter = ChangeFieldsOrderParameter(
            user_id='user_id_1',
            column_id='column_id_1',
            field_id='field_id',
            display_order=1,
            field_ids=['field_id_0', 'field_id_1', 'field_id_3']
        )

        # Act
        actual_response = interactor.change_field_display_order_wrapper(
            field_order_parameter=field_order_parameter,
            presenter=presenter
        )

        # Assert
        storage.validate_column_id.assert_called_once_with(
            column_id=field_order_parameter.column_id
        )
        presenter.get_response_for_the_invalid_column_id.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_invalid_display_order_return_exception_message(self, storage,
                                                                 presenter):
        # Arrange
        expected_response = Mock()
        from ib_boards.interactors.dtos import ChangeFieldsOrderParameter
        from ib_boards.interactors.change_field_order_in_column_list_view import \
            ChangeFieldsDisplayOrder
        interactor = ChangeFieldsDisplayOrder(
            storage=storage
        )
        presenter.get_response_for_the_invalid_display_order.return_value = expected_response
        field_order_parameter = ChangeFieldsOrderParameter(
            user_id='user_id_1',
            column_id='column_id_1',
            field_id='field_id',
            display_order=-1,
            field_ids=['field_id_0', 'field_id_1', 'field_id_3']
        )

        # Act
        actual_response = interactor.change_field_display_order_wrapper(
            field_order_parameter=field_order_parameter,
            presenter=presenter
        )

        # Assert
        presenter.get_response_for_the_invalid_display_order.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_user_not_have_access_to_column_return_exception_message(
            self, storage, presenter, mocker):
        # Arrange
        expected_response = Mock()
        user_role = 'User',
        project_id = "1"
        from ib_boards.interactors.dtos import ChangeFieldsOrderParameter
        from ib_boards.interactors.change_field_order_in_column_list_view import \
            ChangeFieldsDisplayOrder
        interactor = ChangeFieldsDisplayOrder(
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
        field_order_parameter = ChangeFieldsOrderParameter(
            user_id='user_id_1',
            column_id='column_id_1',
            field_id='field_id',
            display_order=1,
            field_ids=['field_id_0', 'field_id_1', 'field_id_3']
        )

        # Act
        actual_response = interactor.change_field_display_order_wrapper(
            field_order_parameter=field_order_parameter,
            presenter=presenter
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=field_order_parameter.user_id, project_id=project_id
        )
        storage.validate_user_role_with_column_roles.assert_called_once_with(
            user_role=user_role, column_id=field_order_parameter.column_id
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
        field_ids = ['field_id_0', 'field_id_1', 'field_id_3']
        valid_field_ids = ['field_id_0', 'field_id_1']
        invalid_field_ids = ['field_id_3']
        from ib_boards.interactors.dtos import ChangeFieldsOrderParameter
        from ib_boards.interactors.change_field_order_in_column_list_view import \
            ChangeFieldsDisplayOrder
        interactor = ChangeFieldsDisplayOrder(
            storage=storage
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )
        storage.get_project_id_for_given_column_id.return_value = project_id
        storage.get_valid_field_ids.return_value = valid_field_ids
        presenter.get_response_for_field_not_belongs_to_column.return_value = expected_response
        field_order_parameter = ChangeFieldsOrderParameter(
            user_id='user_id_1',
            column_id='column_id_1',
            field_id='field_id_0',
            display_order=1,
            field_ids=['field_id_0', 'field_id_1', 'field_id_3']
        )

        # Act
        actual_response = interactor.change_field_display_order_wrapper(
            field_order_parameter=field_order_parameter,
            presenter=presenter
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=field_order_parameter.user_id, project_id=project_id
        )
        storage.get_valid_field_ids.assert_called_once_with(
            column_id=field_order_parameter.column_id,
            field_ids=field_ids,
            user_id=field_order_parameter.user_id
        )
        call_args = presenter.get_response_for_field_not_belongs_to_column.call_args
        assert call_args.kwargs['error'].invalid_field_ids == invalid_field_ids
        assert actual_response == expected_response

    def test_with_valid_data_creates_data(
            self, storage, presenter, mocker):
        # Arrange
        expected_response = Mock()
        user_role = 'User',
        project_id = "1"
        from ib_boards.tests.factories.storage_dtos import \
            FieldDisplayStatusDTOFactory
        from ib_boards.tests.factories.interactor_dtos import \
            FieldNameDTOFactory
        field_display_name_dtos = FieldNameDTOFactory.create_batch(3)
        field_display_status_dtos = FieldDisplayStatusDTOFactory.create_batch(3)
        field_ids = [
            field_display_status_dto.field_id
            for field_display_status_dto in field_display_status_dtos
        ]
        from ib_boards.interactors.dtos import ChangeFieldsOrderParameter
        from ib_boards.interactors.change_field_order_in_column_list_view import \
            ChangeFieldsDisplayOrder
        interactor = ChangeFieldsDisplayOrder(
            storage=storage
        )
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )
        storage.get_valid_field_ids.return_value = field_ids
        storage.get_project_id_for_given_column_id.return_value = project_id
        storage.get_field_display_status_dtos.return_value = field_display_status_dtos
        storage.get_field_ids_list_in_order.return_value = field_ids
        presenter.get_response_for_field_order_in_column.return_value = expected_response
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            field_display_name_mock
        field_name_adapter_mock = field_display_name_mock(
            mocker=mocker, field_display_name_dtos=field_display_name_dtos
        )
        field_order_parameter = ChangeFieldsOrderParameter(
            user_id='user_id_1',
            column_id='column_id_1',
            field_id='field_id_0',
            display_order=1,
            field_ids=field_ids
        )
        from ib_boards.interactors.storage_interfaces.dtos import AllFieldsDTO
        from ib_boards.constants.enum import DisplayStatus
        all_fields = [
            AllFieldsDTO(
                field_id='field_id_0',
                display_name='display_name_0',
                display_order=0,
                display_status=DisplayStatus.SHOW.value
            ),
            AllFieldsDTO(
                field_id='field_id_1',
                display_name='display_name_1',
                display_order=1,
                display_status=DisplayStatus.SHOW.value
            ),
            AllFieldsDTO(
                field_id='field_id_2',
                display_name='display_name_2',
                display_order=2,
                display_status=DisplayStatus.SHOW.value
            )
        ]
        # Act
        actual_response = interactor.change_field_display_order_wrapper(
            field_order_parameter=field_order_parameter,
            presenter=presenter
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=field_order_parameter.user_id, project_id=project_id
        )
        field_name_adapter_mock.assert_called_once_with(
            field_ids=field_ids, user_id=field_order_parameter.user_id,
            project_id=project_id
        )
        storage.get_valid_field_ids.assert_called_once_with(
            field_ids=field_order_parameter.field_ids,
            column_id=field_order_parameter.column_id,
            user_id=field_order_parameter.user_id
        )
        storage.change_display_order_of_field.assert_called_once_with(
            field_order_parameter=field_order_parameter
        )
        presenter.get_response_for_field_order_in_column.assert_called_once_with(
            all_fields=all_fields
        )
        assert actual_response == expected_response
