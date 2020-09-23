import mock
import pytest

from ib_adhoc_tasks.adapters.task_service import TaskService
from ib_adhoc_tasks.interactors.get_task_ids_for_view_interactor import \
    GetTaskIdsForViewInteractor


class TestGetSubTasksInteractor:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.interactors.presenter_interfaces \
            .subtask_presenter_interface import GetSubTasksPresenterInterface
        return mock.create_autospec(GetSubTasksPresenterInterface)

    @pytest.fixture
    def interactor(self, storage):
        from ib_adhoc_tasks.interactors.get_subtasks_of_task_interactor import \
            SubTasksInteractor
        return SubTasksInteractor()

    @mock.patch.object(TaskService, "get_project_id_based_on_task_id")
    @mock.patch.object(TaskService, "get_subtask_ids_for_task_id")
    @mock.patch.object(TaskService, "get_task_complete_details_dto")
    def test_given_valid_details_returns_complete_task_details(
            self, project_id_mock, subtask_ids_for_task_id_mock,
            task_details_mock, group_by_info_list_view_dto, mocker,
            group_details_dtos, task_details_dtos, elastic_storage_mock,
            group_by_details_dtos, interactor, presenter_mock
    ):
        # todo come and correct this test
        # Arrange
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            GetSubtasksParameterDTOFactory
        get_subtasks_parameter_dto = GetSubtasksParameterDTOFactory()
        task_details_mock.return_value = task_details_dtos
        presenter_mock.get_response_for_get_subtasks_of_task.return_value \
            = mock.Mock()

        # Act
        response = interactor.get_tasks_for_list_view_wrapper(
            group_by_info_list_view_dto=group_by_info_list_view_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.get_task_details_group_by_info_response \
            .assert_called_once()
