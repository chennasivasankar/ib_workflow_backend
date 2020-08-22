"""
create task failure test case INVALID_GOFS_OF_TASK_TEMPLATE
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import StageActionFactory, TaskTemplateFactory, \
    GoFFactory, FieldFactory, GoFToTaskTemplateFactory


class TestCase01CreateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture
    def reset_sequence(self):
        TaskTemplateFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self, reset_sequence):
        task_template_obj = TaskTemplateFactory()
        StageActionFactory()
        GoFFactory.create_batch(size=2)
        FieldFactory.create_batch(size=2)
        GoFToTaskTemplateFactory.create_btach(task_template=task_template_obj, )

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "project_id": "project_1",
            "task_template_id": "template_1",
            "action_id": 1,
            "title": "task_title",
            "description": "task_description",
            "start_date": "2018-12-31",
            "due_date": {
                "date": "2019-12-31",
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
                },
                {
                    "gof_id": "gof_2",
                    "same_gof_order": 1,
                    "gof_fields": [
                        {
                            "field_id": "FIELD_ID-1",
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
