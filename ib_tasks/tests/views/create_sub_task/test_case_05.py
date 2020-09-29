"""
test with invalid action id
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from ib_tasks.tests.factories.models import TaskFactory, TaskTemplateFactory, \
    TaskTemplateInitialStageFactory, StageModelFactory
from ib_tasks.tests.views.create_sub_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase05CreateSubTaskAPITestCase(TestUtils):
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

        template_id = "template_1"
        parent_task_display_id = "IBWF-1"
        stage_id = 1

        template_obj = TaskTemplateFactory.create(template_id=template_id)
        stage = StageModelFactory(
            stage_id=stage_id, stage_color="blue",
            task_template_id=template_id)
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
            "start_datetime": None,
            "due_datetime": None,
            "priority": None,
            "task_gofs": []
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
