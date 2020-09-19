"""
test with start date is ahead of due_date
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from ib_tasks.tests.factories.models import TaskFactory, StageFactory
from ib_tasks.tests.views.update_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase05UpdateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskFactory.reset_sequence()
        StageFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        task_id = "IBWF-1"
        stage_id = 1

        StageFactory.create(id=stage_id)
        TaskFactory.create(task_display_id=task_id)

    @freeze_time("2020-09-09 12:00:00")
    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "task_id": "IBWF-1",
            "title": "updated_title",
            "description": "updated_description",
            "start_datetime": "2020-09-20 00:00:00",
            "due_datetime": "2020-08-20 00:00:00",
            "priority": "HIGH",
            "stage_assignee": {
                "stage_id": 1,
                "assignee_id": "assignee_id_1",
                "team_id": "team_1"
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
