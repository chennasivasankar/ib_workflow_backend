from unittest.mock import create_autospec

import pytest

from ib_tasks.adapters.dtos import ProjectRolesDTO
from ib_tasks.constants.enum import ActionTypes
from ib_tasks.exceptions.stage_custom_exceptions import \
    InvalidStageIdsListException
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
from ib_tasks.interactors.get_task_fields_and_actions.get_task_actions import \
    GetTaskActionsInteractor
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    StageActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskProjectDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_projects_mock
from ib_tasks.tests.factories.storage_dtos import (
    StageActionDetailsDTOFactory)


class TestGetActionsInteractor:

    @pytest.fixture
    def action_storage_mock(self):
        return create_autospec(ActionStorageInterface)

    @pytest.fixture()
    def get_actions_dtos(self):
        StageActionDetailsDTOFactory.reset_sequence()
        actions = StageActionDetailsDTOFactory.create_batch(
                size=2, stage_id="stage_id_1",
                action_type=ActionTypes.NO_VALIDATIONS.value)
        actions.append(StageActionDetailsDTOFactory(stage_id="stage_id_2",
                                                    action_type=ActionTypes.NO_VALIDATIONS.value))
        actions.append(StageActionDetailsDTOFactory(stage_id="stage_id_2",
                                                    action_type=ActionTypes.NO_VALIDATIONS.value))
        return actions

    @pytest.fixture
    def task_storage_mock(self):
        return create_autospec(TaskStorageInterface)

    @pytest.fixture
    def stage_storage_mock(self):
        return create_autospec(StageStorageInterface)

    @pytest.fixture
    def expected_output(self):
        return [
                StageActionDetailsDTO(action_id=1, name='name_1',
                                      stage_id='stage_id_1',
                                      button_text='button_text_1',
                                      button_color=None,
                                      action_type=ActionTypes.NO_VALIDATIONS.value,
                                      transition_template_id='template_id_1'),
                StageActionDetailsDTO(action_id=2, name='name_2',
                                      stage_id='stage_id_1',
                                      button_text='button_text_2',
                                      button_color=None,
                                      action_type=ActionTypes.NO_VALIDATIONS.value,
                                      transition_template_id='template_id_2'),
                StageActionDetailsDTO(action_id=3, name='name_3',
                                      stage_id='stage_id_2',
                                      button_text='button_text_3',
                                      button_color=None,
                                      action_type=ActionTypes.NO_VALIDATIONS.value,
                                      transition_template_id='template_id_3'),
                StageActionDetailsDTO(action_id=4, name='name_4',
                                      stage_id='stage_id_2',
                                      button_text='button_text_4',
                                      button_color=None,
                                      action_type=ActionTypes.NO_VALIDATIONS.value,
                                      transition_template_id='template_id_4')]

    @pytest.fixture
    def get_user_roles_mock(self):
        user_roles = [ProjectRolesDTO(
                project_id="project_id_1",
                roles=["FIN_PAYMENT_REQUESTER",
                       "FIN_PAYMENT_POC",
                       "FIN_PAYMENT_APPROVER",
                       "FIN_PAYMENTS_RP",
                       "FIN_FINANCE_RP"])]
        return user_roles

    def test_when_task_ids_is_invalid_raises_exception(self,
                                                       mocker,
                                                       task_storage_mock,
                                                       stage_storage_mock,
                                                       get_user_roles_mock,
                                                       action_storage_mock,
                                                       get_actions_dtos,
                                                       expected_output):
        # Arrange
        action_dtos = get_actions_dtos
        user_id = "user_id_1"
        task_project_dtos = [TaskProjectDTO(project_id="project_id_1",
                                            task_id=1),
                             TaskProjectDTO(project_id="project_id_1",
                                            task_id=2)]
        task_ids = [1, 2]
        stage_ids = ["stage_id_1", "stage_id_2"]
        user_roles = get_user_roles_mock
        user_roles_mock = get_user_role_ids_based_on_projects_mock(mocker)
        user_roles_mock.return_value = user_roles
        task_storage_mock.get_valid_task_ids.return_value = [1]
        action_storage_mock.get_actions_details.return_value = action_dtos
        interactor = GetTaskActionsInteractor(action_storage_mock,
                                              task_storage_mock,
                                              stage_storage_mock)

        # Act
        with pytest.raises(InvalidTaskIds) as err:
            interactor.get_task_actions(stage_ids=stage_ids,
                                        user_id=user_id,
                                        task_ids=task_ids)

        # Assert
        task_storage_mock.get_valid_task_ids.assert_called_once_with(task_ids)

    def test_when_stage_ids_is_invalid_raises_exception(self,
                                                        mocker,
                                                        task_storage_mock,
                                                        stage_storage_mock,
                                                        get_user_roles_mock,
                                                        action_storage_mock,
                                                        get_actions_dtos,
                                                        expected_output):
        # Arrange
        action_dtos = get_actions_dtos
        user_id = "user_id_1"
        task_ids = [1, 2]
        stage_ids = ["stage_id_1", "stage_id_2"]
        user_roles = get_user_roles_mock
        user_roles_mock = get_user_role_ids_based_on_projects_mock(mocker)
        stage_storage_mock.get_existing_stage_ids.return_values = [
                "stage_id_1"]
        user_roles_mock.return_value = user_roles
        task_storage_mock.get_valid_task_ids.return_value = [1, 2]
        action_storage_mock.get_actions_details.return_value = action_dtos
        interactor = GetTaskActionsInteractor(action_storage_mock,
                                              task_storage_mock,
                                              stage_storage_mock)

        # Act
        with pytest.raises(InvalidStageIdsListException) as err:
            interactor.get_task_actions(stage_ids=stage_ids,
                                        user_id=user_id,
                                        task_ids=task_ids)

        # Assert
        task_storage_mock.get_valid_task_ids.assert_called_once_with(task_ids)

    def test_get_actions_when_stage_has_no_permitted_actions(
            self,
            mocker,
            task_storage_mock,
            get_user_roles_mock,
            stage_storage_mock,
            action_storage_mock):
        # Arrange
        expected_output = []
        user_id = "user_id_1"
        task_ids = [1, 2]
        stage_ids = ["stage_id_1", "stage_id_2"]
        user_roles = get_user_roles_mock
        user_roles_mock = get_user_role_ids_based_on_projects_mock(mocker)
        user_roles_mock.return_value = user_roles
        task_storage_mock.get_valid_task_ids.return_value = [1, 2]
        stage_storage_mock.get_existing_stage_ids.return_value = stage_ids
        action_storage_mock.get_actions_details.return_value = []
        interactor = GetTaskActionsInteractor(action_storage_mock,
                                              task_storage_mock,
                                              stage_storage_mock)

        # Act
        response = interactor.get_task_actions(stage_ids=stage_ids,
                                               user_id=user_id,
                                               task_ids=task_ids)

        # Assert
        assert response == expected_output

    def test_get_actions_given_stage_details(self,
                                             mocker,
                                             task_storage_mock,
                                             stage_storage_mock,
                                             get_user_roles_mock,
                                             action_storage_mock,
                                             get_actions_dtos,
                                             expected_output):
        # Arrange
        action_dtos = get_actions_dtos
        user_id = "user_id_1"
        task_ids = [1, 2]
        stage_ids = ["stage_id_1", "stage_id_2"]
        user_roles = get_user_roles_mock
        user_roles_mock = get_user_role_ids_based_on_projects_mock(mocker)
        user_roles_mock.return_value = user_roles
        task_storage_mock.get_valid_task_ids.return_value = [1, 2]
        stage_storage_mock.get_existing_stage_ids.return_value = stage_ids
        action_storage_mock.get_actions_details.return_value = action_dtos
        interactor = GetTaskActionsInteractor(action_storage_mock,
                                              task_storage_mock,
                                              stage_storage_mock)

        # Act
        response = interactor.get_task_actions(stage_ids=stage_ids,
                                               user_id=user_id,
                                               task_ids=task_ids)

        # Assert
        task_storage_mock.get_valid_task_ids.assert_called_once_with(task_ids)
        stage_storage_mock.get_existing_stage_ids.assert_called_once_with(
                stage_ids)
        assert response == expected_output
