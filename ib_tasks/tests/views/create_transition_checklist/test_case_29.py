"""
test with invalid url for image uploader field raises exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase29CreateTransitionChecklistAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        import json
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            TaskFactory, StageActionFactory, StageModelFactory, \
            ActionPermittedRolesFactory, GoFFactory, FieldFactory, \
            GoFToTaskTemplateFactory, GoFRoleFactory, FieldRoleFactory

        TaskTemplateFactory.reset_sequence()
        TaskFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()

        transition_template_id = "transition_template_1"
        stage_id = "stage_1"
        gof_id = "gof_1"
        field_id = "field_1"

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
            transition_template=transition_template_obj,
            action_type=None
        )
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        gof_obj = GoFFactory.create(gof_id=gof_id)

        from ib_tasks.constants.enum import FieldTypes
        field_obj = FieldFactory.create(
            field_id=field_id, gof=gof_obj,
            field_type=FieldTypes.IMAGE_UPLOADER.value,
            allowed_formats="[\".pdf\", \".doc\"]"
        )

        GoFToTaskTemplateFactory.create(
            gof=gof_obj, task_template=transition_template_obj)

        from ib_tasks.constants.enum import PermissionTypes
        GoFRoleFactory.create(
            gof=gof_obj, permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER"
        )
        FieldRoleFactory.create(
            field=field_obj, role="FIN_PAYMENT_REQUESTER",
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
                            'field_response': "http://google.com/"
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
