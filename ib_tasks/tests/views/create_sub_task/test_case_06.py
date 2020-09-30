"""
test with invalid project id
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    get_valid_project_ids_mock as auth_service_project_ids_mock
from ib_tasks.tests.factories.models import TaskFactory, TaskTemplateFactory, \
    TaskTemplateInitialStageFactory, StageModelFactory, \
    StageActionFactory
from ib_tasks.tests.views.create_sub_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase06CreateSubTaskAPITestCase(TestUtils):
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
        StageActionFactory.reset_sequence()

        valid_project_id = "project_2"
        template_id = "template_1"
        parent_task_display_id = "IBWF-1"
        stage_id = 1
        action_id = 1

        template_obj = TaskTemplateFactory.create(template_id=template_id)
        stage = StageModelFactory(
            stage_id=stage_id, stage_color="blue",
            task_template_id=template_id)
        action = StageActionFactory(
            id=action_id, stage=stage, action_type=None)
        TaskTemplateInitialStageFactory.create(
            task_template_id=template_id, stage=stage)
        parent_task = TaskFactory.create(
            task_display_id=parent_task_display_id)

        auth_service_project_ids_mock(mocker, [valid_project_id])

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