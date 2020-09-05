"""
test when user does not have write permission for gof raises exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase12CreateTransitionChecklistAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        import json
        import factory
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            TaskFactory, StageActionFactory, StageModelFactory, \
            ActionPermittedRolesFactory, GoFFactory, FieldFactory, \
            GoFToTaskTemplateFactory, GoFRoleFactory

        TaskTemplateFactory.reset_sequence()
        TaskFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()

        transition_template_id = "transition_template_1"
        stage_id = "stage_1"
        gof_ids = ["gof_1", "gof_2"]
        field_ids = ["field_1", "field_2", "field_3"]

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        transition_template_obj = TaskTemplateFactory.create(
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
            transition_template=transition_template_obj
        )
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        gof_objs = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_ids))
        FieldFactory.create_batch(
            size=2, field_id=factory.Iterator([field_ids[0], field_ids[1]]),
            gof=gof_objs[0])
        FieldFactory.create(field_id=field_ids[2], gof=gof_objs[1])
        GoFToTaskTemplateFactory.create_batch(
            size=2, gof=factory.Iterator(gof_objs),
            task_template=transition_template_obj)

        from ib_tasks.constants.enum import PermissionTypes
        GoFRoleFactory.create_batch(
            size=2, gof=factory.Iterator(gof_objs), role="FIN_EXAMPLE_ROLE",
            permission_type=PermissionTypes.WRITE.value
        )

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
