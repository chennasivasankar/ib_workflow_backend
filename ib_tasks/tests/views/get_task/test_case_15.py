"""
 raises exception when task is a transition checklist task
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TaskFactory, TaskTemplateFactory


class TestCase15GetTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write', 'read']}}

    @pytest.fixture
    def reset_factories(self):
        TaskFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()

    @pytest.fixture
    def setup(self, reset_factories, api_user):
        user_id = api_user.user_id
        task_template_obj = TaskTemplateFactory(is_transition_template=True)
        TaskFactory(
            task_display_id="IBWF-1", project_id="project0",
            created_by=user_id, template_id=task_template_obj.template_id
        )

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {}
        path_params = {}
        query_params = {'task_id': "IBWF-1"}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )