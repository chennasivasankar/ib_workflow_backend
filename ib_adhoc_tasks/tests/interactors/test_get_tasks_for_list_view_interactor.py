from unittest.mock import patch, Mock

import pytest

from ib_adhoc_tasks.adapters.task_service import TaskService
from ib_adhoc_tasks.interactors.get_task_ids_for_view_interactor import \
    GetTaskIdsForViewInteractor
from ib_adhoc_tasks.interactors.get_tasks_for_list_view_interactor import \
    GetTasksForListViewInteractor


class TestGetTasksForListViewInteractor:

    @pytest.fixture
    def presenter_mock(self):
        from mock import create_autospec
        from ib_adhoc_tasks.interactors.presenter_interfaces \
            .get_tasks_for_list_view_presenter_interface import \
            GetTasksForListViewPresenterInterface
        presenter = create_autospec(GetTasksForListViewPresenterInterface)
        return presenter

    @pytest.fixture
    def storage_mock(self):
        from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface \
            import \
            StorageInterface
        from mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def elastic_storage_mock(self):
        from mock import create_autospec
        from ib_adhoc_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import \
            ElasticStorageInterface
        elastic_storage = create_autospec(ElasticStorageInterface)
        return elastic_storage

    @pytest.fixture
    def group_by_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByDetailsDTOFactory
        group_by_details_dtos = GroupByDetailsDTOFactory.create_batch(size=1)
        return group_by_details_dtos

    @pytest.fixture
    def group_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupDetailsDTOFactory
        group_details_dtos = GroupDetailsDTOFactory.create_batch(size=4)
        return group_details_dtos

    @pytest.fixture
    def task_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TasksCompleteDetailsDTOFactory
        return TasksCompleteDetailsDTOFactory()

    @pytest.fixture
    def group_by_info_list_view_dto(self):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            GroupByInfoListViewDTOFactory
        GroupByInfoListViewDTOFactory.reset_sequence()
        return GroupByInfoListViewDTOFactory()


    @patch.object(TaskService, "get_task_complete_details_dto")
    @patch.object(GetTaskIdsForViewInteractor, "get_task_ids_for_view")
    def test_given_valid_details_returns_group_details_dtos_and_task_details_dtos(
            self, group_details_mock, task_details_mock,
            group_by_info_list_view_dto, mocker, storage_mock, presenter_mock,
            group_details_dtos, task_details_dtos, elastic_storage_mock,
            group_by_details_dtos
    ):
        # Arrange
        user_id = group_by_info_list_view_dto.user_id
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            validate_project_ids_for_kanban_view_mock
        validate_project_ids_for_kanban_view_mock(
            mocker)
        group_details_mock.return_value = group_details_dtos
        task_details_mock.return_value = task_details_dtos
        interactor = GetTasksForListViewInteractor(
            storage=storage_mock,
            elastic_storage=elastic_storage_mock
        )
        mock_object = Mock()
        presenter_mock.get_task_details_group_by_info_response.return_value \
            = mock_object
        storage_mock.get_group_by_details_dtos.return_value = \
            group_by_details_dtos

        # Act
        response = interactor.get_tasks_for_list_view_wrapper(
            group_by_info_list_view_dto=group_by_info_list_view_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.get_task_details_group_by_info_response \
            .assert_called_once()

