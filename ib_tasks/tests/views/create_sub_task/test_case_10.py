"""
test with due date value None when action type is not NO_VALIDATIONS
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    get_valid_project_ids_mock as auth_service_project_ids_mock
from ib_tasks.tests.factories.models import TaskFactory, TaskTemplateFactory, \
    TaskTemplateInitialStageFactory, StageModelFactory, \
    ProjectTaskTemplateFactory, StageActionFactory
from ib_tasks.tests.views.create_sub_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase10CreateSubTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, api_user, mocker):
        TaskTemplateFactory.reset_sequence()
        TaskFactory.reset_sequence()
        TaskTemplateInitialStageFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        ProjectTaskTemplateFactory.reset_sequence()
        StageActionFactory.reset_sequence()

        project_id = "project_1"
        template_id = "template_1"
        parent_task_display_id = "IBWF-1"
        stage_id = 1
        action_id = 1

        auth_service_project_ids_mock(mocker, [project_id])

        template_obj = TaskTemplateFactory.create(template_id=template_id)
        ProjectTaskTemplateFactory.create(
            project_id=project_id, task_template=template_obj)
        stage = StageModelFactory(
            stage_id=stage_id, stage_color="blue",
            task_template_id=template_id)
        action = StageActionFactory(
            id=action_id, stage=stage, action_type=None)
        TaskTemplateInitialStageFactory.create(
            task_template_id=template_id, stage=stage)
        parent_task = TaskFactory.create(
            task_display_id=parent_task_display_id)

    @freeze_time("2020-09-09 12:00:00")
    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "project_id": "project_1",
            "task_template_id": "template_1",
            "action_id": 1,
            "parent_task_id": "IBWF-1",
            "title": "Sub Task",
            "description": None,
            "start_datetime": "2020-09-09 12:00:00",
            "due_datetime": None,
            "priority": "HIGH",
            "task_gofs": [
                {
                    "gof_id": "FIN_PAYMENT_REQUESTER_DETAILS",
                    "same_gof_order": 1,
                    "gof_fields": [
                        {
                            "field_id": "FIN_PAYMENT_REQUESTER_FIELD",
                            "field_response": "field response"
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
