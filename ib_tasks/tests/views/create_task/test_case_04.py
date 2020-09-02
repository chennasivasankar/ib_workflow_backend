"""
test with invalid action raises exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase04CreateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        from ib_tasks.tests.factories.models import \
            ProjectTaskTemplateFactory, TaskTemplateFactory

        ProjectTaskTemplateFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()

        template_id = 'template_1'
        project_id = "project_1"

        TaskTemplateFactory.create(template_id=template_id)
        ProjectTaskTemplateFactory.create(
            task_template_id=template_id, project_id=project_id)

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "project_id": "project_1",
            "task_template_id": "template_1",
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
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
