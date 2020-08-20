"""
test with duplicate field ids of a gof
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.tests.factories.models import TaskFactory, GoFFactory, \
    TaskTemplateFactory, GoFToTaskTemplateFactory, FieldFactory
from ib_tasks.tests.views.update_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase09UpdateTaskAPITestCase(TestUtils):
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

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        task_id = "IBWF-1"
        template_id = "TEMPLATE-1"
        gof_ids = ["GOF-1", "GOF-2"]
        field_ids = ["FIELD-1", "FIELD-2", "FIELD-3", "FIELD-4"]

        import factory
        gofs = GoFFactory.create_batch(size=len(gof_ids),
                                       gof_id=factory.Iterator(gof_ids))
        fields = FieldFactory.create_batch(
            size=len(field_ids), field_id=factory.Iterator(field_ids))
        task_template = TaskTemplateFactory.create(template_id=template_id)
        task_template_gofs = GoFToTaskTemplateFactory.create_batch(
            size=len(gofs), task_template=task_template,
            gof=factory.Iterator(gofs))
        task = TaskFactory.create(
            task_display_id=task_id, template_id=task_template.template_id)

    @pytest.mark.django_db
    def test_case(self, snapshot):
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
                            "field_response": "new updated string"
                        },
                        {
                            "field_id": "FIELD-1",
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
