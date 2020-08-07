"""
Created on: 05/08/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock, create_autospec

import pytest

from ib_tasks.exceptions.filter_exceptions import UserNotHaveAccessToFields, \
    InvalidFilterId, UserNotHaveAccessToFilter
from ib_tasks.interactors.filter_interactor import FilterInteractor


class TestFiltersInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.filter_storage_interface import \
            FilterStorageInterface
        storage = create_autospec(FilterStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface import \
            FilterPresenterInterface
        presenter = create_autospec(FilterPresenterInterface)
        return presenter

    @pytest.fixture
    def filter_dto(self):
        from ib_tasks.tests.factories.filter_dtos import CreateFilterDTOFactory
        CreateFilterDTOFactory.reset_sequence()
        return CreateFilterDTOFactory()

    @pytest.fixture
    def update_filter_dto(self):
        from ib_tasks.tests.factories.filter_dtos import UpdateFilterDTOFactory
        UpdateFilterDTOFactory.reset_sequence()
        return UpdateFilterDTOFactory()

    @pytest.fixture
    def condition_dtos(self):
        from ib_tasks.tests.factories.filter_dtos import \
            CreateConditionDTOFactory
        CreateConditionDTOFactory.reset_sequence()
        return CreateConditionDTOFactory.create_batch(3)

    @pytest.fixture
    def new_filter_dto(self):
        from ib_tasks.tests.factories.filter_dtos import FilterDTOFactory
        FilterDTOFactory.reset_sequence()
        return FilterDTOFactory()

    @pytest.fixture
    def new_condition_dtos(self):
        from ib_tasks.tests.factories.filter_dtos import \
            ConditionDTOFactory
        ConditionDTOFactory.reset_sequence()
        return ConditionDTOFactory.create_batch(3)

    def test_with_invalid_template_return_error_message(
            self, storage_mock, presenter_mock, filter_dto, condition_dtos):
        # Arrange
        template_id = filter_dto.template_id
        expected_response = Mock()
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )

        from ib_tasks.exceptions.filter_exceptions import InvalidTemplateID
        storage_mock.validate_template_id.side_effect = InvalidTemplateID
        presenter_mock.get_response_for_invalid_task_template_id.return_value = \
            expected_response

        # Act

        actual_response = interactor.create_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        storage_mock.validate_template_id.assert_called_once_with(
            template_id=template_id
        )
        presenter_mock.get_response_for_invalid_task_template_id. \
            assert_called_once_with()
        assert actual_response == expected_response

    def test_with_fields_not_belongs_to_template_id_return_error_message(
            self, storage_mock, presenter_mock, filter_dto, condition_dtos):
        # Arrange
        valid_field_ids = ['field_id_0']
        invalid_field_ids = ['field_id_1', 'field_id_2']
        template_id = filter_dto.template_id
        field_ids = [condition_dto.field_id for condition_dto in condition_dtos]
        expected_response = Mock()
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )
        storage_mock.get_field_ids_for_task_template. \
            return_value = valid_field_ids
        presenter_mock.get_response_for_invalid_field_ids. \
            return_value = expected_response

        # Act
        actual_response = interactor.create_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        storage_mock.get_field_ids_for_task_template.assert_called_once_with(
            template_id=template_id, field_ids=field_ids
        )
        calls = presenter_mock.get_response_for_invalid_field_ids.call_args
        # assert calls['error'].field_ids == invalid_field_ids
        assert actual_response == expected_response

    def test_with_fields_not_have_access_to_user_return_error_message(
            self, storage_mock, presenter_mock, filter_dto, condition_dtos,
            mocker):
        # Arrange
        user_roles = ['ALL_ROLES', 'FIN_PAYMENT_REQUESTER',
                         'FIN_PAYMENT_POC',
                         'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                         'FIN_COMPLIANCE_APPROVER',
                         'FIN_PAYMENTS_LEVEL1_VERIFIER',
                         'FIN_PAYMENTS_LEVEL2_VERIFIER',
                         'FIN_PAYMENTS_LEVEL3_VERIFIER',
                         'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                         'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                         'FIN_ACCOUNTS_LEVEL2_VERIFIER']
        field_ids = [condition_dto.field_id for condition_dto in condition_dtos]
        expected_response = Mock()
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )

        storage_mock.get_field_ids_for_task_template. \
            return_value = field_ids
        storage_mock.validate_user_roles_with_field_ids_roles. \
            side_effect = UserNotHaveAccessToFields
        presenter_mock.get_response_for_user_not_have_access_to_fields. \
            return_value = expected_response
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        # Act
        actual_response = interactor.create_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        storage_mock.validate_user_roles_with_field_ids_roles. \
            assert_called_once_with(
                user_roles=user_roles, field_ids=field_ids
            )
        presenter_mock.get_response_for_user_not_have_access_to_fields. \
            assert_called_once_with()
        assert actual_response == expected_response

    def test_create_filter_with_valid_details_create_filter(
            self, storage_mock, presenter_mock, filter_dto, condition_dtos,
            mocker, new_filter_dto, new_condition_dtos):
        # Arrange
        user_roles = [
            "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
        ]
        field_ids = [condition_dto.field_id for condition_dto in condition_dtos]
        expected_response = Mock()
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )

        storage_mock.get_field_ids_for_task_template. \
            return_value = field_ids
        storage_mock.create_filter.return_value = new_filter_dto, new_condition_dtos
        presenter_mock.get_response_for_create_filter. \
            return_value = expected_response
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        # Act
        actual_response = interactor.create_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        storage_mock.create_filter. \
            assert_called_once_with(
                filter_dto=filter_dto, condition_dtos=condition_dtos
            )
        presenter_mock.get_response_for_create_filter. \
            assert_called_once_with(
                filter_dto=new_filter_dto, condition_dtos=new_condition_dtos
            )
        assert actual_response == expected_response

    def test_update_filter_with_valid_details_create_filter(
            self, storage_mock, presenter_mock, update_filter_dto, condition_dtos,
            mocker, new_filter_dto, new_condition_dtos):
        # Arrange
        filter_dto = update_filter_dto
        user_roles = [
            "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
        ]
        field_ids = [condition_dto.field_id for condition_dto in condition_dtos]
        expected_response = Mock()
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )

        storage_mock.get_field_ids_for_task_template. \
            return_value = field_ids
        storage_mock.update_filter.return_value = new_filter_dto, new_condition_dtos
        presenter_mock.get_response_for_update_filter. \
            return_value = expected_response
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        # Act
        actual_response = interactor.update_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        storage_mock.update_filter. \
            assert_called_once_with(
                filter_dto=filter_dto, condition_dtos=condition_dtos
            )
        presenter_mock.get_response_for_update_filter. \
            assert_called_once_with(
                filter_dto=new_filter_dto, condition_dtos=new_condition_dtos
            )
        assert actual_response == expected_response

    def test_with_invalid_filter_id_return_error_message(
            self, storage_mock, presenter_mock, update_filter_dto, condition_dtos,
            mocker, new_filter_dto, new_condition_dtos):
        # Arrange
        filter_dto = update_filter_dto
        filter_id = filter_dto.filter_id
        expected_response = Mock()
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )

        storage_mock.validate_filter_id.side_effect = InvalidFilterId
        presenter_mock.get_response_for_invalid_filter_id. \
            return_value = expected_response

        # Act
        actual_response = interactor.update_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        storage_mock.validate_filter_id. \
            assert_called_once_with(
                filter_id=filter_id
            )
        presenter_mock.get_response_for_invalid_filter_id. \
            assert_called_once_with()
        assert actual_response == expected_response

    def test_with_invalid_user_id_filter_in_update_return_error_message(
            self, storage_mock, presenter_mock, update_filter_dto, condition_dtos,
            mocker, new_filter_dto, new_condition_dtos):
        # Arrange
        filter_dto = update_filter_dto
        filter_id = filter_dto.filter_id
        user_id = filter_dto.user_id
        expected_response = Mock()
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )

        storage_mock.validate_user_with_filter_id.side_effect = UserNotHaveAccessToFilter
        presenter_mock.get_response_for_user_not_have_access_to_update_filter. \
            return_value = expected_response

        # Act
        actual_response = interactor.update_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        storage_mock.validate_user_with_filter_id. \
            assert_called_once_with(
                filter_id=filter_id,
                user_id=user_id
            )
        presenter_mock.get_response_for_user_not_have_access_to_update_filter. \
            assert_called_once_with()
        assert actual_response == expected_response

    def test_with_invalid_user_id_filter_in_delete_return_error_message(
            self, storage_mock, presenter_mock):
        # Arrange

        filter_id = 1
        user_id = 'user_id_0'
        expected_response = Mock()
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )

        storage_mock.validate_user_with_filter_id.side_effect = UserNotHaveAccessToFilter
        presenter_mock.get_response_for_user_not_have_access_to_delete_filter. \
            return_value = expected_response

        # Act
        actual_response = interactor.delete_filter_wrapper(
            filter_id=filter_id, user_id=user_id
        )

        # Assert
        storage_mock.validate_user_with_filter_id. \
            assert_called_once_with(
                filter_id=filter_id,
                user_id=user_id
            )
        presenter_mock.get_response_for_user_not_have_access_to_delete_filter. \
            assert_called_once_with()
        assert actual_response == expected_response

    def test_delete_filter_with_details_delete_filter(
            self, storage_mock, presenter_mock):
        # Arrange

        filter_id = 1
        user_id = 'user_id_0'
        expected_response = Mock()
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )

        # Act
        actual_response = interactor.delete_filter_wrapper(
            filter_id=filter_id, user_id=user_id
        )

        # Assert
        storage_mock.delete_filter.assert_called_once_with(
            filter_id=filter_id,
            user_id=user_id
        )


