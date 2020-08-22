"""
create task success test case
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import GoFFactory, GoFToTaskTemplateFactory


class TestCase01CreateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        from ib_tasks.tests.factories.models import \
            ActionPermittedRolesFactory, \
            StageModelFactory, TaskTemplateStatusVariableFactory, \
            TaskTemplateFactory, FieldFactory, \
            StageActionFactory, TaskTemplateInitialStageFactory

        TaskTemplateFactory.reset_sequence()
        TaskTemplateStatusVariableFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        FieldFactory.reset_sequence()
        StageActionFactory.reset_sequence(1)
        TaskTemplateInitialStageFactory.reset_sequence()

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        import json
        template_id = 'template_1'
        gof = GoFFactory.create()
        GoFToTaskTemplateFactory.create(task_template_id=template_id, gof=gof)

        TaskTemplateStatusVariableFactory.create_batch(
            4, task_template_id=template_id
        )
        FieldFactory.create_batch(3, gof=gof)

        stage = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable0==stage_id_0",
            card_info_kanban=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]),
            card_info_list=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]),
        )
        path = \
            'ib_tasks.tests.populate.stage_actions_logic.stage_1_action_name_3'
        action = StageActionFactory(stage=stage, py_function_import_path=path)
        TaskTemplateInitialStageFactory.create_batch(
            1, task_template_id=template_id, stage=stage
        )
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "project_id": "project_1",
            "task_template_id": "template_2",
            "action_id": 1,
            "title": "task_title",
            "description": "task_description",
            "start_date": "2099-12-31",
            "due_date": {
                "date": "2099-12-31",
                "time": "12:00:00"
            },
            "priority": "HIGH",
            "task_gofs": [
                {
                    "gof_id": "gof_1",
                    "same_gof_order": 1,
                    "gof_fields": [
                        {
                            "field_id": "FIELD_ID-0",
                            "field_response": "field_0_response"
                        }
                    ]
                }
            ]
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
