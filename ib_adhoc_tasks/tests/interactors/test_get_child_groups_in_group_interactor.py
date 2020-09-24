from unittest.mock import create_autospec, Mock

import pytest


class TestGetChildGroupsInGroupInteractor:

    @pytest.fixture()
    def elastic_storage_mock(self):
        from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface import \
            ElasticStorageInterface
        elastic_storage = create_autospec(ElasticStorageInterface)
        return elastic_storage

    @pytest.fixture()
    def interactor(self, elastic_storage_mock, storage_mock):
        from ib_adhoc_tasks.interactors.get_child_groups_in_group_interactor import \
            GetChildGroupsInGroupInteractor
        interactor = GetChildGroupsInGroupInteractor(
            elastic_storage=elastic_storage_mock,
            storage=storage_mock
        )
        return interactor

    @pytest.fixture
    def storage_mock(self):
        from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface \
            import \
            StorageInterface
        from mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from mock import create_autospec
        from ib_adhoc_tasks.interactors.presenter_interfaces.get_child_groups_in_group_presenter_interface import \
            GetChildGroupsInGroupPresenterInterface
        presenter = create_autospec(GetChildGroupsInGroupPresenterInterface)
        return presenter

    @pytest.fixture()
    def get_child_groups_in_group_input_dto(self):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            GetChildGroupsInGroupInputDTOFactory
        GetChildGroupsInGroupInputDTOFactory.reset_sequence(1)
        GetChildGroupsInGroupInputDTOFactory.group_by_value.reset()
        get_child_groups_in_group_input_dto = \
            GetChildGroupsInGroupInputDTOFactory()
        return get_child_groups_in_group_input_dto

    @staticmethod
    def add_child_group_by_display_name_to_dtos_mock(mocker):
        mock = mocker.patch(
            "ib_adhoc_tasks.interactors.get_task_ids_for_view_interactor.GetTaskIdsForViewInteractor.add_child_group_by_display_name_to_dtos"
        )
        return mock

    def test_with_valid_details_return_response(
            self, interactor, storage_mock, elastic_storage_mock,
            presenter_mock, get_child_groups_in_group_input_dto,
            prepare_group_details_dtos, mocker
    ):
        # Arrange
        total_child_groups_count = 10
        stage_ids = ['STAGE_1', 'STAGE_2']

        add_child_group_by_display_name_to_dtos_mock = \
            self.add_child_group_by_display_name_to_dtos_mock(mocker)
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_user_permitted_stage_ids_mock, get_user_role_ids_mock
        get_user_permitted_stage_ids_mock = get_user_permitted_stage_ids_mock(mocker)
        get_user_role_ids_mock(mocker)
        get_user_permitted_stage_ids_mock.return_value = stage_ids

        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        group_by_response_dtos = \
            GroupByResponseDTOFactory.create_batch(size=2)

        storage_mock.get_group_by_dtos.return_value = group_by_response_dtos

        expected_get_group_details_of_project_mock = \
            prepare_group_details_dtos, total_child_groups_count
        elastic_storage_mock.get_child_group_details_of_group.return_value = \
            expected_get_group_details_of_project_mock
        add_child_group_by_display_name_to_dtos_mock.return_value = \
            prepare_group_details_dtos

        expected_prepare_response_for_get_child_groups_in_group_mock = Mock()

        presenter_mock.prepare_response_for_get_child_groups_in_group. \
            return_value = expected_prepare_response_for_get_child_groups_in_group_mock

        # Act
        response = interactor.get_child_groups_in_group_wrapper(
            get_child_groups_in_group_input_dto=get_child_groups_in_group_input_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_prepare_response_for_get_child_groups_in_group_mock
        presenter_mock.prepare_response_for_get_child_groups_in_group. \
            assert_called_once_with(
            total_child_groups_count=total_child_groups_count,
            group_details_dtos=prepare_group_details_dtos
        )

    @pytest.fixture()
    def prepare_group_details_dtos(self):
        from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
            GroupDetailsDTO
        group_details_dtos = [
            GroupDetailsDTO(task_ids=[19], total_tasks=1,
                            group_by_value='need to pay debt',
                            group_by_display_name='need to pay debt',
                            child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                            child_group_by_display_name='PR_PAYMENT_REQUEST_DRAFTS'),
            GroupDetailsDTO(task_ids=[20], total_tasks=1,
                            group_by_value='need to pay friend',
                            group_by_display_name='need to pay friend',
                            child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                            child_group_by_display_name='PR_PAYMENT_REQUEST_DRAFTS'),
            GroupDetailsDTO(task_ids=[24], total_tasks=1,
                            group_by_value='purpose',
                            group_by_display_name='purpose',
                            child_group_by_value='PR_NEED_CLARIFICATION',
                            child_group_by_display_name='PR_NEED_CLARIFICATION'),
            GroupDetailsDTO(task_ids=[21], total_tasks=1,
                            group_by_value='sfsdd',
                            group_by_display_name='sfsdd',
                            child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                            child_group_by_display_name='PR_PAYMENT_REQUEST_DRAFTS'),
            GroupDetailsDTO(task_ids=[25], total_tasks=1,
                            group_by_value='sfsdfsd',
                            group_by_display_name='sfsdfsd',
                            child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                            child_group_by_display_name='PR_PAYMENT_REQUEST_DRAFTS')]
        return group_details_dtos
