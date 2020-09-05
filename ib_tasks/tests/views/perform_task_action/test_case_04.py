"""
# TODO: Update test case description
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.models import TaskTemplateGoFs, TaskStageHistory
from ib_tasks.tests.factories.models import (TaskTemplateFactory,
                                             TaskTemplateStatusVariableFactory,
                                             GoFFactory,
                                             FieldFactory, StageModelFactory,
                                             StageActionFactory,
                                             TaskFactory,
                                             TaskStatusVariableFactory,
                                             TaskGoFFactory,
                                             TaskGoFFieldFactory,
                                             CurrentTaskStageModelFactory,
                                             GoFToTaskTemplateFactory,
                                             ActionPermittedRolesFactory,
                                             TaskTemplateInitialStageFactory,
                                             GoFRoleFactory, FieldRoleFactory,
                                             TaskStageHistoryFactory,
                                             TaskStageModelFactory)
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.assignees_details_service import \
    get_assignee_details_dtos_mock
from ...common_fixtures.adapters.auth_service import \
    (validate_if_user_is_in_project_mock, get_valid_project_ids_mock,
     get_projects_info_for_given_ids_mock)
from ...common_fixtures.interactors import prepare_get_field_ids__user


class TestCase01PerformTaskActionAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker, api_user):
        get_assignee_details_dtos_mock(mocker, str(api_user.user_id))
        get_valid_project_ids_mock(mocker, ['project_id_1'])
        validate_if_user_is_in_project_mock(mocker, True)
        get_projects_info_for_given_ids_mock(mocker)
        user_roles = ["role_0", "role_1", "role_2"]
        prepare_get_field_ids__user(mocker, user_roles)
        TaskTemplateInitialStageFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()
        TaskGoFFieldFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()
        TaskTemplateStatusVariableFactory.reset_sequence()
        TaskStatusVariableFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        TaskStageHistoryFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        TaskStageModelFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        self.create_task_templates(api_user)

    @staticmethod
    def create_task_templates(api_user):
        tts = TaskTemplateFactory.create_batch(3)
        TaskTemplateStatusVariableFactory.create_batch(
                4, task_template_id='template_1')
        import json
        gofs = GoFFactory.create_batch(3)
        ttg1 = TaskTemplateGoFs(task_template=tts[0], gof_id='gof_1', order=1)
        ttg2 = TaskTemplateGoFs(task_template=tts[0], gof_id='gof_2', order=1)
        ttg3 = TaskTemplateGoFs(task_template=tts[0], gof_id='gof_3', order=1)
        ttgs = [ttg1, ttg2, ttg3]
        TaskTemplateGoFs.objects.bulk_create(ttgs)
        fields = FieldFactory.create_batch(12, gof=factory.Iterator(gofs))

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
        path = 'ib_tasks.tests.populate.stage_actions_logic' \
               '.stage_1_action_name_1'
        action = StageActionFactory(stage=stage1, py_function_import_path=path)
        actions = StageActionFactory.create_batch(6, stage=factory.Iterator(
                stages))
        TaskStageHistoryFactory.create_batch(size=2, task_id=4,
                                             stage=stage1,
                                             assignee_id=api_user.user_id)
        TaskStageModelFactory(task_id=1, stage=stage1)
        task = TaskFactory(template_id='template_1')
        TaskStatusVariableFactory(task_id=4, variable='variable0',
                                  value="stage_id_0")
        TaskStatusVariableFactory(task_id=4, variable='variable1',
                                  value="stage_id_1")
        TaskStatusVariableFactory(task_id=4, variable='variable2',
                                  value="stage_id_2")
        TaskStatusVariableFactory(task_id=4, variable='variable3',
                                  value="stage_id_1")
        task_gofs = TaskGoFFactory.create_batch(
                6, task=task, gof_id=factory.Iterator(
                        ['gof_1', 'gof_2', 'gof_3', 'gof_4', 'gof_5', 'gof_6']
                )
        )
        TaskGoFFieldFactory.create_batch(
                6, task_gof=factory.Iterator(task_gofs),
                field=factory.Iterator(fields)
        )
        CurrentTaskStageModelFactory.create_batch(
                3, task=task,
                stage=factory.Iterator(stages)
        )

        ActionPermittedRolesFactory.create_batch(3, action=action)

    @pytest.mark.django_db
    def test_case(self, snapshot, mocker):
        path = 'ib_tasks.adapters.boards_service.BoardsService' \
               '.validate_board_id'
        mock_obj = mocker.patch(path)
        mock_obj.return_value = True
        roles_path = 'ib_iam.app_interfaces.service_interface' \
                     '.ServiceInterface.get_user_role_ids'
        roles_mock = mocker.patch(roles_path)
        roles_mock.return_value = ['role_1', 'role_2', 'role_3']
        path = 'ib_tasks.adapters.boards_service.BoardsService' \
               '.get_display_boards_and_column_details'
        board_mock = mocker.patch(path)
        from ib_tasks.tests.common_fixtures.interactors \
            import prepare_integration_task_boards_details
        task_board_dto = prepare_integration_task_boards_details()
        board_mock.return_value = task_board_dto

        body = {
                "task_id": "IBWF-4",
                "action_id": "1",
                "board_id": "board_1"
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
                body=body, path_params=path_params,
                query_params=query_params, headers=headers, snapshot=snapshot
        )
