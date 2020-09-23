from unittest.mock import patch, Mock

import pytest

from ib_adhoc_tasks.adapters.iam_service import IamService
from ib_adhoc_tasks.adapters.task_service import TaskService
from ib_adhoc_tasks.interactors.get_task_ids_for_view_interactor import \
    GetTaskIdsForViewInteractor
from ib_adhoc_tasks.interactors.get_tasks_for_kanban_view_interactor import \
    GetTasksForKanbanViewInteractor


class TestGetTasksForKanbanViewInteractor:

    @pytest.fixture
    def presenter_mock(self):
        from mock import create_autospec
        from ib_adhoc_tasks.interactors.presenter_interfaces \
            .get_tasks_for_kanban_view_presenter_interface import \
            GetTasksForKanbanViewPresenterInterface
        presenter = create_autospec(GetTasksForKanbanViewPresenterInterface)
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
    def group_by_info_kanban_view_dto(self):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            GroupByInfoKanbanViewDTOFactory
        GroupByInfoKanbanViewDTOFactory.reset_sequence()
        return GroupByInfoKanbanViewDTOFactory()

    @pytest.fixture
    def group_by_details_dto_when_selected_two_options(self):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByDetailsDTOFactory
        group_by_details_dtos = GroupByDetailsDTOFactory.create_batch(size=2)
        return group_by_details_dtos

    @pytest.fixture
    def group_by_details_dto_when_selected_one_options(self):
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
    def child_group_count_dtos(self):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            ChildGroupCountDTOFactory
        return ChildGroupCountDTOFactory.create_batch(size=10)

    @pytest.fixture
    def task_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TasksCompleteDetailsDTOFactory
        return TasksCompleteDetailsDTOFactory()

    @pytest.fixture
    def task_details_with_group_by_info_dto(
            self, task_details_dtos, child_group_count_dtos,
            group_details_dtos
    ):
        from ib_adhoc_tasks.interactors.presenter_interfaces \
            .get_tasks_for_kanban_view_presenter_interface import \
            TaskDetailsWithGroupByInfoDTO
        task_details_with_group_by_info_dto = TaskDetailsWithGroupByInfoDTO(
            group_details_dtos=group_details_dtos,
            total_groups_count=3,
            child_group_count_dtos=child_group_count_dtos,
            task_details_dtos=task_details_dtos
        )
        return task_details_with_group_by_info_dto

    @patch.object(IamService, 'get_valid_project_ids')
    def test_given_invalid_project_id_raise_exception(
            self, project_service_mock, storage_mock, elastic_storage_mock,
            group_by_info_kanban_view_dto, presenter_mock
    ):
        # Arrange
        project_service_mock.return_value = []
        interactor = GetTasksForKanbanViewInteractor(
            storage=storage_mock,
            elastic_storage=elastic_storage_mock
        )
        mock_object = Mock()
        presenter_mock.raise_invalid_project_id.return_value = mock_object

        # Act
        response = interactor.get_tasks_for_kanban_view_wrapper(
            group_by_info_kanban_view_dto=group_by_info_kanban_view_dto,
            presenter=presenter_mock
        )

        # Assert
        assert mock_object == response
        project_service_mock.assert_called_once()
        presenter_mock.raise_invalid_project_id.assert_called_once()

    @patch.object(TaskService, "get_task_complete_details_dto")
    @patch.object(GetTaskIdsForViewInteractor, "get_task_ids_for_view")
    def test_given_valid_details_when_selected_two_group_by_options_return_group_details_dtos(
            self, get_task_ids_mock, task_details_mock,
            group_by_info_kanban_view_dto, task_details_dtos,
            presenter_mock, mocker, group_details_dtos,
            storage_mock, elastic_storage_mock, child_group_count_dtos,
            group_by_details_dto_when_selected_two_options,
            task_details_with_group_by_info_dto
    ):
        # Arrange
        total_groups_count = 3

        user_id = group_by_info_kanban_view_dto.user_id
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            validate_project_ids_for_kanban_view_mock
        validate_project_ids_for_kanban_view_mock(
            mocker)
        get_task_ids_mock.return_value = \
            group_details_dtos, total_groups_count, child_group_count_dtos
        storage_mock.get_group_by_details_dtos.return_value = \
            group_by_details_dto_when_selected_two_options
        task_details_mock.return_value = task_details_dtos
        interactor = GetTasksForKanbanViewInteractor(
            storage=storage_mock,
            elastic_storage=elastic_storage_mock
        )
        mock_object = Mock()
        presenter_mock.get_task_details_group_by_info_response.return_value \
            = mock_object

        # Act
        response = interactor.get_tasks_for_kanban_view_wrapper(
            group_by_info_kanban_view_dto=group_by_info_kanban_view_dto,
            presenter=presenter_mock
        )

        # Assert
        assert mock_object == response
        storage_mock.get_group_by_details_dtos.assert_called_once_with(user_id)
        presenter_mock.get_task_details_group_by_info_response \
            .assert_called_once_with(task_details_with_group_by_info_dto)

    @patch.object(TaskService, "get_task_complete_details_dto")
    @patch.object(GetTaskIdsForViewInteractor, "get_task_ids_for_view")
    def test_given_valid_details_when_selected_one_group_by_options_return_group_details_dtos(
            self, get_task_ids_mock, task_details_mock,
            group_by_info_kanban_view_dto, task_details_dtos,
            presenter_mock, mocker, group_details_dtos,
            storage_mock, elastic_storage_mock, child_group_count_dtos,
            group_by_details_dto_when_selected_one_options,
            task_details_with_group_by_info_dto
    ):
        # Arrange
        total_groups_count = 3

        user_id = group_by_info_kanban_view_dto.user_id
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            validate_project_ids_for_kanban_view_mock
        validate_project_ids_for_kanban_view_mock(
            mocker)
        get_task_ids_mock.return_value = \
            group_details_dtos, total_groups_count, child_group_count_dtos
        storage_mock.get_group_by_details_dtos.return_value = \
            group_by_details_dto_when_selected_one_options
        task_details_mock.return_value = task_details_dtos
        interactor = GetTasksForKanbanViewInteractor(
            storage=storage_mock,
            elastic_storage=elastic_storage_mock
        )
        mock_object = Mock()
        presenter_mock.get_task_details_group_by_info_response.return_value \
            = mock_object

        # Act
        response = interactor.get_tasks_for_kanban_view_wrapper(
            group_by_info_kanban_view_dto=group_by_info_kanban_view_dto,
            presenter=presenter_mock
        )

        # Assert
        assert mock_object == response
        storage_mock.get_group_by_details_dtos.assert_called_once_with(user_id)
        presenter_mock.get_task_details_group_by_info_response \
            .assert_called_once_with(task_details_with_group_by_info_dto)
