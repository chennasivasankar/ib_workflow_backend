"""
test with invalid fields of a gof
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import (
    TaskFactory, StageActionFactory, StageFactory, GoFFactory,
    TaskTemplateFactory, FieldFactory, GoFToTaskTemplateFactory)


class TestCase18SaveAndActOnATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageFactory.reset_sequence()
        GoFFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        FieldFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        task_display_id = "IBWF-1"
        action_id = 1
        stage_id = 1
        gof_id = "gof_1"
        field_id = "FIELD_ID-1"
        template_id = "template_1"

        template = TaskTemplateFactory.create(template_id=template_id)
        task = TaskFactory.create(
            task_display_id=task_display_id, template_id=template_id)
        gof = GoFFactory.create(gof_id=gof_id)
        given_field = FieldFactory.create(field_id=field_id)
        field = FieldFactory.create(field_id="FIELD_ID-2", gof=gof)
        GoFToTaskTemplateFactory.create(task_template=template, gof=gof)
        stage = StageFactory.create(id=stage_id)
        action = StageActionFactory.create(
            id=action_id, stage=stage, action_type=None)

    @freeze_time("2020-09-09 12:00:00")
    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "task_id": "IBWF-1",
            "action_id": 1,
            "title": "updated_title",
            "description": "updated_description",
            "start_datetime": "2020-08-25 12:00:00",
            "due_datetime": "2020-09-20 12:00:00",
            "priority": "HIGH",
            "stage_assignee": {
                "stage_id": 1,
                "assignee_id": "assignee_id_1",
                "team_id": "team_alpha"
            },
            "task_gofs": [
                {
                    "gof_id": "gof_1",
                    "same_gof_order": 0,
                    "gof_fields": [
                        {
                            "field_id": "FIELD_ID-1",
                            "field_response": "field response as plain text"
                        }
                    ]
                }
            ]
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
