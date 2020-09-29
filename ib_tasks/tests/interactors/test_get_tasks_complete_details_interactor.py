import pytest

from ib_tasks.constants.enum import ViewType
from ib_tasks.tests.interactors.super_storage_mock_class import StorageMockClass


class TestGetTasksCompleteDetailsInteractor(StorageMockClass):

    @pytest.fixture()
    def project_mock(self, mocker):
        path = 'ib_tasks.adapters.auth_service.AuthService.validate_project_ids'
        return mocker.patch(path)

    @pytest.fixture()
    def interactor(
            self, action_storage_mock, field_storage,
            task_storage, task_stage_storage, stage_storage
    ):
        from ib_tasks.interactors.get_tasks_complete_details_interactor \
            import GetTasksCompleteDetailsInteractor
        interactor = GetTasksCompleteDetailsInteractor(
            action_storage=action_storage_mock,
            field_storage=field_storage, task_storage=task_storage,
            task_stage_storage=task_stage_storage,
            stage_storage=stage_storage
        )
        return interactor

    @staticmethod
    def input_data(task_ids, project_id):
        from ib_tasks.interactors.dtos.dtos import TasksDetailsInputDTO
        user_id = "user_1"
        view_type = ViewType.KANBAN.value
        input_dto = TasksDetailsInputDTO(
            task_ids=task_ids, project_id=project_id,
            user_id=user_id, view_type=view_type
        )
        return input_dto

    def test_given_invalid_projects_raises_exception(self, interactor, project_mock):
        # Arrange
        project_id = "project_1"
        task_ids = [1, 2, 3]
        project_ids = []
        project_mock.return_value = project_ids
        input_dto = self.input_data(task_ids, project_id)

        # Act
        from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException
        with pytest.raises(InvalidProjectIdsException) as err:
            interactor.get_tasks_complete_details(input_dto)

        # Assert
        assert err.value.invalid_project_ids == [project_id]
        project_mock.assert_called_once_with([project_id])

    def set_up_storage(
            self, project_mock, project_ids,
            task_storage, task_ids
    ):
        project_mock.return_value = project_ids
        task_storage.get_valid_task_ids.return_value = task_ids

    def test_given_invalid_task_ids_raises_exception(
            self, interactor, project_mock, task_storage
    ):
        # Arrange
        project_id = "project_1"
        task_ids = [1, 2, 3]
        project_ids = [project_id]
        valid_task_ids = [1, 2]
        input_dto = self.input_data(task_ids, project_id)
        self.set_up_storage(project_mock, project_ids,
                            task_storage, valid_task_ids)

        # Act
        from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
        with pytest.raises(InvalidTaskIds) as err:
            interactor.get_tasks_complete_details(input_dto)

        # Assert
        assert err.value.invalid_task_ids == [3]
        task_storage.get_valid_task_ids.assert_called_once_with(task_ids=task_ids)

    def task_stage_response(self):
        from ib_tasks.tests.factories.interactor_dtos import GetTaskDetailsDTOFactory
        GetTaskDetailsDTOFactory.reset_sequence()
        task_stage_dtos = GetTaskDetailsDTOFactory.create_batch(2)
        return task_stage_dtos

    @pytest.fixture()
    def user_roles_mock(self, mocker):
        path = 'ib_tasks.interactors.user_role_validation_interactor.UserRoleValidationInteractor' \
               '.get_user_role_ids_for_project'
        mock_obj = mocker.patch(path)
        return mock_obj

    @pytest.fixture()
    def tasks_fields_and_actions(self, mocker):
        path = 'ib_tasks.interactors.get_task_fields_and_actions.GetTaskFieldsAndActionsInteractor' \
               '.get_task_fields_and_action'
        return mocker.patch(path)

    @pytest.fixture()
    def task_stage_assignee_mock(self, mocker):
        path = 'ib_tasks.interactors.get_stages_assignees_details_interactor.GetStagesAssigneesDetailsInteractor' \
               '.get_tasks_stage_assignee_details'
        return mocker.patch(path)

    def tasks_fields_and_actions_mock(self):
        from ib_tasks.tests.factories.presenter_dtos \
            import GetTaskStageCompleteDetailsDTOFactory
        GetTaskStageCompleteDetailsDTOFactory.reset_sequence()
        response = GetTaskStageCompleteDetailsDTOFactory.create_batch(2)
        return response

    def task_stage_assign_mock_response(self):
        from ib_tasks.tests.factories.interactor_dtos import AssigneeWithTeamDetailsDTOFactory
        from ib_tasks.tests.factories.interactor_dtos import TaskStageAssigneeTeamDetailsDTOFactory
        AssigneeWithTeamDetailsDTOFactory.reset_sequence(1)
        from ib_tasks.tests.factories.adapter_dtos import TeamInfoDTOFactory
        TeamInfoDTOFactory.reset_sequence(1)
        from ib_tasks.tests.factories.adapter_dtos import TeamDetailsDTOFactory
        TeamDetailsDTOFactory.reset_sequence(1)
        TaskStageAssigneeTeamDetailsDTOFactory.reset_sequence()
        return TaskStageAssigneeTeamDetailsDTOFactory.create_batch(2)

    def tasks_base_response(self):
        from ib_tasks.tests.factories.storage_dtos import TaskBaseDetailsDTOFactory
        TaskBaseDetailsDTOFactory.reset_sequence()
        return TaskBaseDetailsDTOFactory.create_batch(2)

    def set_up_valid_storage(
            self, project_mock, project_ids,
            task_storage, task_ids, task_stage_storage, task_stage_dtos, user_roles_mock,
            user_roles, stage_storage, stage_ids, tasks_fields_and_actions,
            task_stage_assignee_mock
    ):
        project_mock.return_value = project_ids
        task_storage.get_valid_task_ids.return_value = task_ids
        task_stage_storage.get_task_stage_details_dtos.return_value = task_stage_dtos
        user_roles_mock.return_value = user_roles
        stage_storage.get_permitted_stage_ids_given_stage_ids \
            .return_value = stage_ids
        tasks_stage_fields_and_actions_response = self.tasks_fields_and_actions_mock()
        tasks_fields_and_actions.return_value = tasks_stage_fields_and_actions_response
        task_stage_assignee_mock_response = self.task_stage_assign_mock_response()
        task_stage_assignee_mock.return_value = task_stage_assignee_mock_response
        tasks_base_response = self.tasks_base_response()
        task_storage.get_base_details_to_task_ids.return_value = tasks_base_response

    def expected_response(self, ):
        from ib_tasks.tests.factories.interactor_dtos import TasksCompleteDetailsDTOFactory
        TasksCompleteDetailsDTOFactory.reset_sequence(1)
        tasks_base_response = self.tasks_base_response()
        tasks_stage_fields_and_actions_response = self.tasks_fields_and_actions_mock()
        task_stage_assignee_mock_response = self.task_stage_assign_mock_response()
        return TasksCompleteDetailsDTOFactory(
            task_base_details_dtos=tasks_base_response,
            task_stage_assignee_dtos=task_stage_assignee_mock_response,
            task_stage_details_dtos=tasks_stage_fields_and_actions_response
        )

    def test_given_valid_details_returns_details(
            self, interactor, project_mock, task_storage,
            task_stage_storage, user_roles_mock, stage_storage,
            tasks_fields_and_actions, task_stage_assignee_mock
    ):
        # Arrange
        project_id = "project_1"
        task_ids = [1, 2]
        project_ids = [project_id]
        user_id = "user_1"
        user_roles = ["role_1", "role_2"]
        input_dto = self.input_data(task_ids, project_id)
        stage_ids = ["stage_id_1", "stage_id_2"]
        task_stage_dtos = self.task_stage_response()
        self.set_up_valid_storage(
            project_mock, project_ids, task_storage, task_ids,
            task_stage_storage, task_stage_dtos, user_roles_mock, user_roles,
            stage_storage, stage_ids, tasks_fields_and_actions,
            task_stage_assignee_mock
        )
        expected_response = self.expected_response()

        # Act
        response = interactor.get_tasks_complete_details(input_dto)

        # Assert
        assert response == expected_response
        user_roles_mock.assert_called_once_with(user_id=user_id, project_id=project_id)
        stage_storage.get_permitted_stage_ids_given_stage_ids.assert_called_once_with(
            user_roles=user_roles, stage_ids=stage_ids
        )
        tasks_fields_and_actions.assert_called_once_with(
            task_dtos=task_stage_dtos, user_id=user_id,
            view_type=ViewType.KANBAN.value
        )
        task_stage_assignee_mock.assert_called_once_with(
            task_stage_dtos=task_stage_dtos, project_id=project_id
        )
        task_storage.get_base_details_to_task_ids.assert_called_once_with(
            task_ids=task_ids
        )
