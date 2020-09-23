from unittest.mock import patch, Mock

import pytest

from ib_adhoc_tasks.adapters.iam_service import IamService, InvalidUserId, \
    InvalidUserForProject
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

    @pytest.fixture
    def group_by_info_list_view_dto_with_invalid_offset(self):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            GroupByInfoListViewDTOFactory
        GroupByInfoListViewDTOFactory.reset_sequence()
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            OffsetLimitDTOFactory
        return GroupByInfoListViewDTOFactory(
            task_offset_limit_dto=OffsetLimitDTOFactory(offset=-1),
            group_offset_limit_dto=OffsetLimitDTOFactory(offset=-10)
        )

    @pytest.fixture
    def group_by_info_list_view_dto_with_invalid_limit(self):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            GroupByInfoListViewDTOFactory
        GroupByInfoListViewDTOFactory.reset_sequence()
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            OffsetLimitDTOFactory
        return GroupByInfoListViewDTOFactory(
            task_offset_limit_dto=OffsetLimitDTOFactory(limit=-1),
            group_offset_limit_dto=OffsetLimitDTOFactory(limit=-10)
        )

    @patch.object(IamService, "get_valid_project_ids")
    def test_given_invalid_project_id_raise_exception(
            self, project_mock, storage_mock, elastic_storage_mock,
            group_by_info_list_view_dto, presenter_mock
    ):
        # Arrange
        project_mock.return_value = []
        interactor = GetTasksForListViewInteractor(
            storage=storage_mock,
            elastic_storage=elastic_storage_mock
        )
        mock_object = Mock()
        presenter_mock.raise_invalid_project_id.return_value = mock_object

        # Act
        response = interactor.get_tasks_for_list_view_wrapper(
            group_by_info_list_view_dto=group_by_info_list_view_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        project_mock.assert_called_once()
        presenter_mock.raise_invalid_project_id.assert_called_once()

    def test_given_invalid_offset_value(
            self, mocker, presenter_mock,  storage_mock, elastic_storage_mock,
            group_by_info_list_view_dto_with_invalid_offset
    ):
        # Arrange
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            validate_project_ids_mock
        validate_project_ids_mock(
            mocker)
        interactor = GetTasksForListViewInteractor(
            storage=storage_mock,
            elastic_storage=elastic_storage_mock
        )
        mock_object = Mock()
        presenter_mock.raise_invalid_offset_value.return_value = mock_object

        # Act
        response = interactor.get_tasks_for_list_view_wrapper(
            group_by_info_list_view_dto=group_by_info_list_view_dto_with_invalid_offset,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_offset_value.assert_called_once()

    def test_given_invalid_limit_value(
            self, mocker, presenter_mock,  storage_mock, elastic_storage_mock,
            group_by_info_list_view_dto_with_invalid_limit
    ):
        # Arrange
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            validate_project_ids_mock
        validate_project_ids_mock(
            mocker)
        interactor = GetTasksForListViewInteractor(
            storage=storage_mock,
            elastic_storage=elastic_storage_mock
        )
        mock_object = Mock()
        presenter_mock.raise_invalid_limit_value.return_value = mock_object

        # Act
        response = interactor.get_tasks_for_list_view_wrapper(
            group_by_info_list_view_dto=group_by_info_list_view_dto_with_invalid_limit,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_limit_value.assert_called_once()

    @patch.object(GetTaskIdsForViewInteractor, "get_task_ids_for_view")
    def test_given_invalid_user_raise_exception(
            self, user_mock, presenter_mock,  storage_mock,
            elastic_storage_mock, group_by_info_list_view_dto,
            group_by_details_dtos, mocker
    ):
        # Arrange
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            validate_project_ids_mock
        validate_project_ids_mock(
            mocker)
        invalid_user_exception = InvalidUserId()
        user_mock.side_effect = invalid_user_exception
        interactor = GetTasksForListViewInteractor(
            storage=storage_mock,
            elastic_storage=elastic_storage_mock
        )
        mock_object = Mock()
        presenter_mock.raise_invalid_user_id.return_value = mock_object

        # Act
        response = interactor.get_tasks_for_list_view_wrapper(
            group_by_info_list_view_dto=group_by_info_list_view_dto,
            presenter=presenter_mock
        )

        # Arrange
        assert response == mock_object
        user_mock.assert_called_once()
        presenter_mock.raise_invalid_user_id.assert_called_once()

    @patch.object(GetTaskIdsForViewInteractor, "get_task_ids_for_view")
    def test_given_user_not_exists_for_project_raise_exception(
            self, user_mock, presenter_mock, storage_mock,
            elastic_storage_mock, group_by_info_list_view_dto,
            group_by_details_dtos, mocker
    ):
        # Arrange
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            validate_project_ids_mock
        validate_project_ids_mock(
            mocker)
        invalid_user_exception = InvalidUserForProject()
        user_mock.side_effect = invalid_user_exception
        interactor = GetTasksForListViewInteractor(
            storage=storage_mock,
            elastic_storage=elastic_storage_mock
        )
        mock_object = Mock()
        presenter_mock.raise_invalid_user_for_project.return_value = mock_object

        # Act
        response = interactor.get_tasks_for_list_view_wrapper(
            group_by_info_list_view_dto=group_by_info_list_view_dto,
            presenter=presenter_mock
        )

        # Arrange
        assert response == mock_object
        user_mock.assert_called_once()
        presenter_mock.raise_invalid_user_for_project.assert_called_once()

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
            validate_project_ids_mock
        validate_project_ids_mock(
            mocker)
        total_groups_count = 3
        child_group_count_dtos = []
        group_details_mock.return_value = \
            group_details_dtos, total_groups_count, child_group_count_dtos
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
        storage_mock.get_group_by_details_dtos.assert_called_once_with(user_id)
        presenter_mock.get_task_details_group_by_info_response \
            .assert_called_once_with(
                group_details_dtos, task_details_dtos, total_groups_count
            )
