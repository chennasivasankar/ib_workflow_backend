"""
test with invalid field ids raises exception
"""
import json

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.constants.enum import FieldTypes
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import StageActionFactory, StageModelFactory, \
    StagePermittedRolesFactory


class TestCase04UpdateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        import factory
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            GoFFactory, GoFRoleFactory, TaskFactory, TaskGoFFactory, \
            GoFToTaskTemplateFactory

        TaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)
        template_id = "template_1"
        gofs = GoFFactory.create_batch(size=2)
        task_template = TaskTemplateFactory.create(template_id=template_id)
        GoFToTaskTemplateFactory.create_batch(
            size=2, task_template=task_template, gof=factory.Iterator(gofs)
        )
        gof_ids = [gof.gof_id for gof in gofs]

        task_obj = TaskFactory.create(
            template_id="template_1")
        TaskGoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_ids), task=task_obj
        )
        stage = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable0==stage_id_0",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
        )

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "task_id": 1,
            "title": "updated_title",
            "description": "updated_description",
            "start_date": "2099-12-31",
            "due_date": {
                "date": "2099-12-31",
                "time": "12:00:00"
            },
            "priority": "HIGH",
            "stage_assignee": {
                "stage_id": 1,
                "assignee_id": "assignee_id_1"
            },
            "task_gofs": [
                {
                    "gof_id": "gof_1",
                    "same_gof_order": 0,
                    "gof_fields": [
                        {
                            "field_id": "FIELD_ID-0",
                            "field_response": "new updated string"
                        },
                        {
                            "field_id": "FIELD_ID-1",
                            "field_response":
                                "https://image.flaticon.com/icons/svg/1829/1829070.svg"
                        }
                    ]
                },
                {
                    "gof_id": "gof_2",
                    "same_gof_order": 0,
                    "gof_fields": [
                        {
                            "field_id": "FIELD_ID-2",
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
