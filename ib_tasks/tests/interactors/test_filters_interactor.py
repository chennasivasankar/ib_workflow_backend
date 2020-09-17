"""
Created on: 05/08/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock, create_autospec

import pytest

from ib_tasks.exceptions.filter_exceptions import InvalidFilterId, \
    UserNotHaveAccessToFilter, UserNotHaveAccessToFields
from ib_tasks.interactors.filters.create_or_update_or_delete_filters import \
    CreateOrUpdateOrDeleteFiltersInteractor
from ib_tasks.tests.common_fixtures.interactors import \
    prepare_get_field_ids__user


class TestFiltersInteractor:

    @pytest.fixture
    def field_storage(self):
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
            FieldsStorageInterface
        return create_autospec(FieldsStorageInterface)

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
    def condition_dtos_with_invalid_operation(self):
        from ib_tasks.tests.factories.filter_dtos import \
            CreateConditionDTOFactory
        CreateConditionDTOFactory.reset_sequence()
        from ib_tasks.constants.enum import Operators
        return CreateConditionDTOFactory.create_batch(
            3, operator=Operators.LTE.value
        )

    @pytest.fixture
    def condition_dtos_with_invalid_operation_for_integer(self):
        from ib_tasks.tests.factories.filter_dtos import \
            CreateConditionDTOFactory
        CreateConditionDTOFactory.reset_sequence()
        from ib_tasks.constants.enum import Operators
        return CreateConditionDTOFactory.create_batch(
            3, operator=Operators.CONTAINS.value
        )

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

    @pytest.fixture
    def field_type_dtos(self):
        from ib_tasks.tests.factories.filter_dtos import FieldTypeDTOFactory
        FieldTypeDTOFactory.reset_sequence()
        return FieldTypeDTOFactory.create_batch(5)

    @pytest.fixture
    def field_type_dtos_with_type_number(self):
        from ib_tasks.tests.factories.filter_dtos import FieldTypeDTOFactory
        FieldTypeDTOFactory.reset_sequence()
        from ib_tasks.constants.enum import FieldTypes
        return FieldTypeDTOFactory.create_batch(
            5, field_type=FieldTypes.NUMBER.value
        )

    def test_with_invalid_template_id_return_error_message(
            self, storage_mock, presenter_mock, filter_dto, condition_dtos,
            field_storage, mocker):
        # Arrange
        template_id = filter_dto.template_id
        expected_response = Mock()
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[filter_dto.project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
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
            self, storage_mock, presenter_mock, filter_dto, condition_dtos,
            field_storage, mocker, field_type_dtos):
        # Arrange
        valid_field_ids = ['field_0']
        invalid_field_ids = ['field_1', 'field_2']
        template_id = filter_dto.template_id
        project_id = '1'
        field_ids = [condition_dto.field_id for condition_dto in condition_dtos]
        expected_response = Mock()
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[filter_dto.project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
        )
        storage_mock.get_field_ids_for_task_template. \
            return_value = valid_field_ids
        field_storage.get_field_type_dtos.return_value = field_type_dtos
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
        assert calls[1]['error'].field_ids == invalid_field_ids
        assert actual_response == expected_response

    def test_with_fields_not_have_access_to_user_return_error_message(
            self, storage_mock, presenter_mock, filter_dto, condition_dtos,
            field_storage,field_type_dtos,
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
        permitted_field_ids = ["field_1", "field_2"]
        project_id = '1'
        prepare_get_field_ids__user(mocker, user_roles)
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )

        storage_mock.get_field_ids_for_task_template. \
            return_value = field_ids
        storage_mock.validate_user_roles_with_field_ids_roles.\
            side_effect = UserNotHaveAccessToFields
        field_storage.get_field_type_dtos.return_value = field_type_dtos
        presenter_mock.get_response_for_user_not_have_access_to_fields. \
            return_value = expected_response
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[filter_dto.project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
        )
        # Act
        actual_response = interactor.create_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        presenter_mock.get_response_for_user_not_have_access_to_fields. \
            assert_called_once_with()
        assert actual_response == expected_response

    def test_create_filter_with_invalid_condition_type_for_strings(
            self, storage_mock, presenter_mock, filter_dto, condition_dtos_with_invalid_operation,
            field_storage, field_type_dtos,
            mocker, new_filter_dto, new_condition_dtos):
        # Arrange
        user_roles = [
            "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
        ]
        from ib_tasks.constants.enum import Operators
        invalid_condition = Operators.LTE.value
        expected_response = Mock()
        prepare_get_field_ids__user(mocker, user_roles)
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )
        field_storage.get_field_type_dtos.return_value = field_type_dtos
        presenter_mock.get_response_for_invalid_filter_condition. \
            return_value = expected_response
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[filter_dto.project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
        )
        # Act
        actual_response = interactor.create_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos_with_invalid_operation
        )

        # Assert
        presenter_mock.get_response_for_invalid_filter_condition.assert_called_once()
        calls = presenter_mock.get_response_for_invalid_filter_condition.call_args
        assert calls[1]['error'].condition == invalid_condition
        assert actual_response == expected_response

    def test_create_filter_with_invalid_condition_type_for_integers(
            self, storage_mock, presenter_mock, filter_dto,
            field_storage, field_type_dtos_with_type_number, condition_dtos_with_invalid_operation_for_integer,
            mocker, new_filter_dto, new_condition_dtos):
        # Arrange
        user_roles = [
            "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
        ]
        from ib_tasks.constants.enum import Operators
        invalid_condition = Operators.CONTAINS.value
        expected_response = Mock()
        prepare_get_field_ids__user(mocker, user_roles)
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )
        field_storage.get_field_type_dtos.return_value = field_type_dtos_with_type_number
        presenter_mock.get_response_for_invalid_filter_condition. \
            return_value = expected_response
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[filter_dto.project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
        )
        # Act
        actual_response = interactor.create_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos_with_invalid_operation_for_integer
        )

        # Assert
        presenter_mock.get_response_for_invalid_filter_condition.assert_called_once()
        calls = presenter_mock.get_response_for_invalid_filter_condition.call_args
        assert calls[1]['error'].condition == invalid_condition
        assert actual_response == expected_response

    def test_create_filter_with_valid_details_create_filter(
            self, storage_mock, presenter_mock, filter_dto, condition_dtos,
            field_storage, field_type_dtos,
            mocker, new_filter_dto, new_condition_dtos):
        # Arrange
        user_roles = [
            "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
        ]
        field_ids = [condition_dto.field_id for condition_dto in condition_dtos]
        expected_response = Mock()
        prepare_get_field_ids__user(mocker, user_roles)
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )

        storage_mock.get_field_ids_for_task_template. \
            return_value = field_ids
        field_storage.get_field_type_dtos.return_value = field_type_dtos
        storage_mock.create_filter.return_value = new_filter_dto, new_condition_dtos
        presenter_mock.get_response_for_create_filter. \
            return_value = expected_response
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[filter_dto.project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
        )
        # Act
        actual_response = interactor.create_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        presenter_mock.get_response_for_create_filter. \
            assert_called_once_with(
            filter_dto=new_filter_dto, condition_dtos=new_condition_dtos
        )
        assert actual_response == expected_response

    def test_update_filter_with_valid_details_create_filter(
            self, storage_mock, presenter_mock, update_filter_dto,
            condition_dtos, field_type_dtos,
            field_storage,
            mocker, new_filter_dto, new_condition_dtos):
        # Arrange
        filter_dto = update_filter_dto
        user_roles = [
            "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
        ]
        field_ids = [condition_dto.field_id for condition_dto in condition_dtos]
        prepare_get_field_ids__user(mocker,
                                                               field_ids)
        expected_response = Mock()
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )

        storage_mock.get_field_ids_for_task_template. \
            return_value = field_ids
        field_storage.get_field_type_dtos.return_value = field_type_dtos
        storage_mock.update_filter.return_value = new_filter_dto, new_condition_dtos
        presenter_mock.get_response_for_update_filter. \
            return_value = expected_response
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)
        project_id = '1'
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
        )
        # Act
        actual_response = interactor.update_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        presenter_mock.get_response_for_update_filter. \
            assert_called_once_with(
            filter_dto=new_filter_dto, condition_dtos=new_condition_dtos
        )
        assert actual_response == expected_response

    def test_with_invalid_filter_id_return_error_message(
            self, storage_mock, presenter_mock, update_filter_dto,
            condition_dtos,
            field_storage,
            mocker, new_filter_dto, new_condition_dtos):
        # Arrange
        filter_dto = update_filter_dto
        filter_id = filter_dto.filter_id
        expected_response = Mock()
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )

        storage_mock.validate_filter_id.side_effect = InvalidFilterId
        presenter_mock.get_response_for_invalid_filter_id. \
            return_value = expected_response

        # Act
        actual_response = interactor.update_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )
        project_id = '1'
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
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
            self, storage_mock, presenter_mock, update_filter_dto,
            condition_dtos,
            field_storage,
            mocker, new_filter_dto, new_condition_dtos):
        # Arrange
        filter_dto = update_filter_dto
        filter_id = filter_dto.filter_id
        user_id = filter_dto.user_id
        expected_response = Mock()
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )

        storage_mock.validate_user_with_filter_id.side_effect = UserNotHaveAccessToFilter
        presenter_mock.get_response_for_user_not_have_access_to_update_filter. \
            return_value = expected_response

        # Act
        actual_response = interactor.update_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )
        project_id = '1'
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
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
            self, storage_mock, presenter_mock, field_storage, mocker):
        # Arrange

        filter_id = 1
        user_id = 'user_id_0'
        expected_response = Mock()
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )
        project_id = '1'
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
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
            self, storage_mock, presenter_mock, field_storage):
        # Arrange

        filter_id = 1
        user_id = 'user_id_0'
        interactor = CreateOrUpdateOrDeleteFiltersInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock,
            field_storage=field_storage
        )

        # Act
        interactor.delete_filter_wrapper(
            filter_id=filter_id, user_id=user_id
        )

        # Assert
        storage_mock.delete_filter.assert_called_once_with(
            filter_id=filter_id,
            user_id=user_id
        )
