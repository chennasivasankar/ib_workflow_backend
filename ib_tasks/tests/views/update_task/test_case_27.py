"""
test with incorrect checkbox options in checkbox group field
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.constants.enum import PermissionTypes, FieldTypes
from ib_tasks.tests.factories.models import TaskFactory, GoFFactory, \
    TaskTemplateFactory, GoFToTaskTemplateFactory, FieldFactory, \
    GoFRoleFactory, FieldRoleFactory
from ib_tasks.tests.views.update_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase27UpdateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        task_id = "IBWF-1"
        template_id = "TEMPLATE-1"
        gof_id = "GOF-1"
        field_id = "FIELD-1"
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        user_roles_mock_method = get_user_role_ids(mocker)
        user_roles = user_roles_mock_method.return_value
        gof = GoFFactory.create(gof_id=gof_id)
        gof_role = GoFRoleFactory.create(
            role=user_roles[0], gof=gof,
            permission_type=PermissionTypes.WRITE.value)

        field = FieldFactory.create(
            field_id=field_id, gof=gof,
            field_type=FieldTypes.CHECKBOX_GROUP.value,
            field_values='["interactors", "storages"]'
        )

        field_role = FieldRoleFactory.create(
            role=user_roles[0], field=field,
            permission_type=PermissionTypes.WRITE.value)
        task_template = TaskTemplateFactory.create(template_id=template_id)
        task_template_gofs = GoFToTaskTemplateFactory.create(
            task_template=task_template, gof=gof)
        task = TaskFactory.create(
            task_display_id=task_id, template_id=task_template.template_id)

    @pytest.mark.django_db
    def test_case(self, snapshot, mocker):
        body = {
            "task_id": "IBWF-1",
            "title": "updated_title",
            "description": "updated_description",
            "start_date": "2020-09-08",
            "due_date": {
                "date": "2020-09-09",
                "time": "11:00:00"
            },
            "priority": "HIGH",
            "stage_assignee": {
                "stage_id": 1,
                "assignee_id": "assignee_id_1"
            },
            "task_gofs": [
                {
                    "gof_id": "GOF-1",
                    "same_gof_order": 0,
                    "gof_fields": [
                        {
                            "field_id": "FIELD-1",
                            "field_response": '["interactors", "views"]'
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
