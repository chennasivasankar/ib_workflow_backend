from unittest.mock import create_autospec

import pytest

from ib_tasks.adapters.dtos import ProjectRolesDTO
from ib_tasks.constants.enum import ActionTypes
from ib_tasks.interactors.get_task_actions import GetTaskActionsInteractor
from ib_tasks.interactors.storage_interfaces.action_storage_interface import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.actions_dtos import StageActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskProjectDTO
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_projects_mock
from ib_tasks.tests.factories.storage_dtos import (
    StageActionDetailsDTOFactory)


class TestGetFieldsAndActionsInteractor:

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
    def expected_output(self):
        return [
            StageActionDetailsDTO(action_id=1, name='name_1', stage_id='stage_id_1', button_text='button_text_1',
                                  button_color=None, action_type=ActionTypes.NO_VALIDATIONS.value,
                                  transition_template_id='template_id_1'),
            StageActionDetailsDTO(action_id=2, name='name_2', stage_id='stage_id_1', button_text='button_text_2',
                                  button_color=None, action_type=ActionTypes.NO_VALIDATIONS.value,
                                  transition_template_id='template_id_2'),
            StageActionDetailsDTO(action_id=3, name='name_3', stage_id='stage_id_2', button_text='button_text_3',
                                  button_color=None, action_type=ActionTypes.NO_VALIDATIONS.value,
                                  transition_template_id='template_id_3'),
            StageActionDetailsDTO(action_id=4, name='name_4', stage_id='stage_id_2', button_text='button_text_4',
                                  button_color=None, action_type=ActionTypes.NO_VALIDATIONS.value,
                                  transition_template_id='template_id_4')]

    def test_get_actions_given_stage_details(self,
                                             mocker,
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
        stage_ids = ["stage_id_1", "stage_id_2"]
        user_roles = [ProjectRolesDTO(
            project_id="project_id_1",
            roles=["FIN_PAYMENT_REQUESTER",
                   "FIN_PAYMENT_POC",
                   "FIN_PAYMENT_APPROVER",
                   "FIN_PAYMENTS_RP",
                   "FIN_FINANCE_RP"])]
        user_roles_mock = get_user_role_ids_based_on_projects_mock(mocker)
        user_roles_mock.return_value = user_roles
        action_storage_mock.get_actions_details.return_value = action_dtos
        interactor = GetTaskActionsInteractor(action_storage_mock)

        # Act
        response = interactor.get_task_actions(stage_ids=stage_ids,
                                               user_id=user_id,
                                               task_project_dtos=task_project_dtos)

        # Assert
        assert response == expected_output
