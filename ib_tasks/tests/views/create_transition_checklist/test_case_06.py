"""
test when given action which is not related to transition template then
 raises exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase06CreateTransitionChecklistAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        import json
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            TaskFactory, StageActionFactory, StageModelFactory, \
            ActionPermittedRolesFactory

        TaskTemplateFactory.reset_sequence()
        TaskFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()

        transition_template_id = "transition_template_1"
        stage_id = "stage_1"

        TaskTemplateFactory.create(
            template_id=transition_template_id, is_transition_template=True)
        TaskFactory.create(template_id=transition_template_id)
        stage = StageModelFactory(
            stage_id=stage_id,
            task_template_id='template_1',
            display_logic="variable0==stage_1",
            card_info_kanban=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]),
            card_info_list=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]))
        path = 'ib_tasks.tests.populate.' \
               'stage_actions_logic.stage_1_action_name_1_logic'
        action = StageActionFactory(stage=stage, py_function_import_path=path)
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            'task_id': 'IBWF-1',
            'transition_checklist_template_id': 'transition_template_1',
            'action_id': 1,
            'stage_id': 1,
            'transition_checklist_gofs': [
                {
                    'gof_id': 'gof_1',
                    'same_gof_order': 1,
                    'gof_fields': [
                        {
                            'field_id': 'field_1',
                            'field_response': 'iB_HUBS'
                        }
                    ]
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
