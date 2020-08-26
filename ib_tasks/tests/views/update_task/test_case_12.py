"""
test with user who does not have write permission for a gof
when there are gof write permission roles in db for given gofs
"""

import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.tests.factories.models import TaskFactory, GoFFactory, \
    TaskTemplateFactory, GoFToTaskTemplateFactory, FieldFactory, \
    GoFRoleFactory, StageFactory
from ib_tasks.tests.views.update_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase12UpdateTaskAPITestCase(TestUtils):
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
        StageFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        task_id = "IBWF-1"
        template_id = "TEMPLATE-1"
        stage_id = 1
        gof_ids = ["GOF-1", "GOF-2"]
        field_ids = ["FIELD-1", "FIELD-2", "FIELD-3", "FIELD-4"]
        gof_write_permission_roles = ["FIN_GOF_CREATOR"]
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        user_roles_mock_method = get_user_role_ids(mocker)

        StageFactory.create(id=stage_id)
        gofs = GoFFactory.create_batch(size=len(gof_ids),
                                       gof_id=factory.Iterator(gof_ids))
        gof_roles = GoFRoleFactory.create_batch(
            size=2, gof=factory.Iterator(gofs),
            role=factory.Iterator(gof_write_permission_roles),
            permission_type=PermissionTypes.WRITE.value
        )
        fields = [
            FieldFactory.create(field_id=field_ids[0], gof=gofs[0]),
            FieldFactory.create(field_id=field_ids[1], gof=gofs[0]),
            FieldFactory.create(field_id=field_ids[2], gof=gofs[1]),
            FieldFactory.create(field_id=field_ids[3], gof=gofs[1])
        ]

        task_template = TaskTemplateFactory.create(template_id=template_id)
        task_template_gofs = GoFToTaskTemplateFactory.create_batch(
            size=len(gofs), task_template=task_template,
            gof=factory.Iterator(gofs))
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
                "assignee_id": "assignee_id_1",
                "team_id": "team_1"
            },
            "task_gofs": [
                {
                    "gof_id": "GOF-1",
                    "same_gof_order": 0,
                    "gof_fields": [
                        {
                            "field_id": "FIELD-1",
                            "field_response": "new updated string"
                        },
                        {
                            "field_id": "FIELD-2",
                            "field_response":
                                "https://image.flaticon.com/icons/svg/1829/1829070.svg"
                        }
                    ]
                },
                {
                    "gof_id": "GOF-2",
                    "same_gof_order": 0,
                    "gof_fields": [
                        {
                            "field_id": "FIELD-3",
                            "field_response": "[\"interactors\"]"
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
