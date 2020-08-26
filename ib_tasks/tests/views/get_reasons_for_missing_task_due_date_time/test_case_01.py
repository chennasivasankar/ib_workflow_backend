"""
# TODO: invalid task id raises exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetReasonsForMissingTaskDueDateTimeAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture()
    def setup(self, api_user):
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.reset_sequence()
        tasks = TaskFactory.create_batch(size=2)
        from ib_tasks.tests.factories.models import TaskLogFactory
        TaskLogFactory.reset_sequence()
        TaskLogFactory(task=tasks[0], assignee_id=api_user.user_id)
        from ib_tasks.tests.factories.models import TaskDueDetailsFactory
        TaskDueDetailsFactory.reset_sequence()
        TaskDueDetailsFactory(user_id=api_user.user_id, task=tasks[0])
        TaskDueDetailsFactory.create_batch(size=5, task=tasks[0])

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {"task_id": "iBWF-1", 'stage_id': 1}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
