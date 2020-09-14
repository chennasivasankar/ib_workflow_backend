"""
test with invalid date format raises exception
"""
import datetime

import freezegun
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase29CreateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        import json
        from ib_tasks.tests.factories.models import \
            ProjectTaskTemplateFactory, TaskTemplateFactory, \
            StageModelFactory, ActionPermittedRolesFactory, \
            StageActionFactory, GoFFactory, FieldFactory, \
            GoFToTaskTemplateFactory, GoFRoleFactory, FieldRoleFactory

        ProjectTaskTemplateFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()

        template_id = 'template_1'
        project_id = "project_1"
        stage_id = "stage_1"
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(mocker, [project_id])
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(mocker, [project_id])

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        get_user_role_ids_based_on_project_mock(mocker)

        task_template_obj = TaskTemplateFactory.create(template_id=template_id)
        ProjectTaskTemplateFactory.create(
            task_template_id=template_id, project_id=project_id)
        stage = StageModelFactory(
            stage_id=stage_id,
            task_template_id='template_1',
            display_logic="variable0==stage_1",
            card_info_kanban=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]),
            card_info_list=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]))
        path = 'ib_tasks.tests.populate.' \
               'stage_actions_logic.stage_1_action_name_1_logic'
        action = StageActionFactory(
            stage=stage, py_function_import_path=path,
            action_type=None
        )
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        gof_obj = GoFFactory.create()

        from ib_tasks.constants.constants import FieldTypes
        field_obj = FieldFactory.create(
            gof=gof_obj, field_type=FieldTypes.DATE.value)
        GoFToTaskTemplateFactory.create(
            task_template=task_template_obj, gof=gof_obj)

        from ib_tasks.constants.enum import PermissionTypes
        GoFRoleFactory.create(
            gof=gof_obj, permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER"
        )
        FieldRoleFactory.create(
            field=field_obj, permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER"
        )

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        'date', ["31-2099-12", "2099-31-12", "31-12-2099", "12-31-2099"])
    @freezegun.freeze_time(datetime.datetime(2020, 8, 31, 5, 4, 54))
    def test_case(self, snapshot, date):
        body = {
            "project_id": "project_1",
            "task_template_id": "template_1",
            "action_id": 1,
            "title": "task_title",
            "description": "task_description",
            "start_datetime": "2020-09-20 00:00:00",
            "due_datetime": "2020-10-31 00:00:00",
            "priority": "HIGH",
            "task_gofs": [
                {
                    "gof_id": "gof_1",
                    "same_gof_order": 1,
                    "gof_fields": [
                        {
                            "field_id": "FIELD_ID-0",
                            "field_response": date
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
