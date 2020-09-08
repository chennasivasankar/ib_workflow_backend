"""
test with invalid field ids raises exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase09CreateTransitionChecklistAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        import json
        import factory
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            TaskFactory, StageActionFactory, StageModelFactory, \
            ActionPermittedRolesFactory, GoFFactory

        TaskTemplateFactory.reset_sequence()
        TaskFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        GoFFactory.reset_sequence()

        transition_template_id = "transition_template_1"
        stage_id = "stage_1"
        gof_ids = ["gof_1", "gof_2"]

        transition_template = TaskTemplateFactory.create(
            template_id=transition_template_id, is_transition_template=True)
        TaskFactory.create(template_id=transition_template_id)
        stage = StageModelFactory(
            stage_id=stage_id,
            task_template_id=transition_template_id,
            display_logic="variable0==stage_1",
            card_info_kanban=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]),
            card_info_list=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]))
        path = 'ib_tasks.tests.populate.' \
               'stage_actions_logic.stage_1_action_name_1_logic'
        action = StageActionFactory(
            stage=stage, py_function_import_path=path,
            transition_template=transition_template
        )
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        GoFFactory.create_batch(size=2, gof_id=factory.Iterator(gof_ids))

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
                        },
                        {
                            'field_id': 'field_2',
                            'field_response': 'iB_HUBS'
                        }
                    ]
                },
                {
                    'gof_id': 'gof_2',
                    'same_gof_order': 1,
                    'gof_fields': [
                        {
                            'field_id': 'field_3',
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
