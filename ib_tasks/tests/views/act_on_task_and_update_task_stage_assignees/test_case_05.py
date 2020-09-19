"""
# Given Valid details
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.models import TaskTemplateGoFs, ProjectTaskTemplate
from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    TaskTemplateStatusVariableFactory, GoFFactory, \
    FieldFactory, StageModelFactory, StageActionFactory, \
    TaskFactory, TaskStatusVariableFactory, TaskGoFFactory, \
    TaskGoFFieldFactory, \
    CurrentTaskStageModelFactory, GoFToTaskTemplateFactory, \
    ActionPermittedRolesFactory, \
    TaskTemplateInitialStageFactory, GoFRoleFactory, FieldRoleFactory, \
    StagePermittedRolesFactory, ProjectTaskTemplateFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase05ActOnTaskAndUpdateTaskStageAssigneesAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
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
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()
        ProjectTaskTemplateFactory.reset_sequence()

    @pytest.fixture()
    def setup(self, reset_sequence):
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
        path = 'ib_tasks.tests.populate.stage_actions_logic.stage_1_action_name_1'
        action = StageActionFactory(stage=stage1, py_function_import_path=path)
        actions = StageActionFactory.create_batch(6, stage=factory.Iterator(
            stages))
        task = TaskFactory(template_id='template_1', task_display_id="IBWF-1")

    @pytest.mark.django_db
    def test_case(self, snapshot, setup, mocker):
        user_path = 'ib_tasks.adapters.auth_service.AuthService.validate_if_user_is_in_project'
        mock_obj = mocker.patch(user_path)
        mock_obj.return_value = True
        body = {
            "task_id": "IBWF-1",
            "action_id": "8",
            "board_id": "board_1",
            "stage_assignees": [
                {
                    "stage_id": 1,
                    "assignee_id": "123e4567-e89b-12d3-a456-426614174004",
                    "team_id": "123e4567-e89b-12d3-a456-426614174001"
                }
            ]
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

