"""
# Success Test Case
"""
import json

import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    prepare_permitted_user_details_mock
from ib_tasks.tests.factories.models import StagePermittedRolesFactory, \
    StageModelFactory, CurrentTaskStageModelFactory, StageActionFactory, \
    TaskStatusVariableFactory, ActionPermittedRolesFactory, TaskFactory, \
    TaskTemplateFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.adapter_dtos import ProjectDetailsDTOFactory, \
    UserIdWIthTeamDetailsDTOFactory


class TestCase01GetNextStagesRandomAssigneesOfATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker, api_user):
        from ib_tasks.tests.factories.storage_dtos import UserDetailsDTOFactory

        user_obj = api_user
        user_id = str(user_obj.user_id)
        StagePermittedRolesFactory.reset_sequence()
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        TaskStatusVariableFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        UserDetailsDTOFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        ProjectDetailsDTOFactory.reset_sequence()
        UserIdWIthTeamDetailsDTOFactory.reset_sequence()
        ProjectDetailsDTOFactory.reset_sequence()

        user_details_mock = prepare_permitted_user_details_mock(mocker)
        user_details_dtos = [
            UserDetailsDTOFactory(
                user_id="123e4567-e89b-12d3-a456-426614174000",
                profile_pic_url=None)
        ]
        user_details_mock.return_value = user_details_dtos
        stage1 = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable0==stage_id_0",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
        )
        stage2 = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable1==stage_id_1",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"])
        )
        stage3 = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable2==stage_id_2",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"])
        )
        stages = [stage1, stage2, stage3]
        StagePermittedRolesFactory.create_batch(6, stage=factory.Iterator(
            stages))
        path = \
            'ib_tasks.tests.populate.stage_actions_logic.stage_1_action_name_1'
        action = StageActionFactory(stage=stage1, py_function_import_path=path)
        actions = StageActionFactory.create_batch(6, stage=factory.Iterator(
            stages))

        task = TaskFactory(template_id='template_1')
        TaskStatusVariableFactory(task_id=1, variable='variable0',
                                  value="stage_id_0")
        TaskStatusVariableFactory(task_id=1, variable='variable1',
                                  value="stage_id_1")
        TaskStatusVariableFactory(task_id=1, variable='variable2',
                                  value="stage_id_2")
        TaskStatusVariableFactory(task_id=1, variable='variable3',
                                  value="stage_id_1")
        CurrentTaskStageModelFactory()
        ActionPermittedRolesFactory.create_batch(3, action=action)

    @pytest.mark.django_db
    def test_case(self, snapshot, setup, mocker):
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_team_info_for_given_user_ids_with_given_names_mock, \
            get_project_info_for_given_ids_mock

        get_team_info_for_given_user_ids_with_given_names_mock(
            mocker)
        get_project_info_for_given_ids_mock(mocker)
        project_ids_validation_mock = mocker.patch(
            'ib_tasks.adapters.auth_service.AuthService.validate_project_ids')
        project_ids_validation_mock.return_value = ['project_id_1']

        body = {"task_id": "IBWF-1", "action_id": 1}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
