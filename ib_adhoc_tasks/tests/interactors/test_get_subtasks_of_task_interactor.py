import mock
import pytest

from ib_adhoc_tasks.adapters.task_service import TaskService


class TestGetSubTasksInteractor:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.interactors.presenter_interfaces \
            .subtask_presenter_interface import GetSubTasksPresenterInterface
        return mock.create_autospec(GetSubTasksPresenterInterface)

    @pytest.fixture
    def interactor(self):
        from ib_adhoc_tasks.interactors.get_subtasks_of_task_interactor import \
            SubTasksInteractor
        return SubTasksInteractor()

    @pytest.fixture
    def task_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TasksCompleteDetailsDTOFactory
        return TasksCompleteDetailsDTOFactory()

    @mock.patch.object(TaskService, "get_task_id")
    @mock.patch.object(TaskService, "get_project_id_based_on_task_id")
    @mock.patch.object(TaskService, "get_subtask_ids_for_task_id")
    @mock.patch.object(TaskService, "get_task_complete_details_dto")
    def test_given_valid_details_returns_complete_task_details(
            self, task_details_mock, subtask_ids_for_task_id_mock, project_id_mock,
            get_task_id_mock, task_details_dtos, interactor, presenter
    ):
        # Arrange
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            GetSubtasksParameterDTOFactory
        get_subtasks_parameter_dto = GetSubtasksParameterDTOFactory()
        project_id = "project_id_1"
        subtask_ids = [1, 2, 3]
        task_id = 1
        get_task_id_mock.return_value = task_id
        project_id_mock.return_value = project_id
        subtask_ids_for_task_id_mock.return_value = subtask_ids
        task_details_mock.return_value = task_details_dtos
        mock_object = mock.Mock
        presenter.get_response_for_get_subtasks_of_task.return_value \
            = mock_object

        # Act
        response = interactor.get_subtasks_of_task_wrapper(
            get_subtasks_parameter_dto=get_subtasks_parameter_dto,
            presenter=presenter
        )

        # Assert
        assert response == mock_object
        presenter.get_response_for_get_subtasks_of_task \
            .assert_called_once_with(
            complete_subtasks_details_dto=task_details_dtos,
            subtask_ids=subtask_ids
        )
