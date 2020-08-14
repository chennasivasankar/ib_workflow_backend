"""
# TODO: invalid task id raises exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02AddReasonForMissingDueDateTimeAPITestCase(TestUtils):
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
        TaskLogFactory(task=tasks[0], user_id=api_user.user_id)

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {
            'updated_due_date_time': '2020-09-10T11:30:45.34523',
            'reason_id': 1,
            'reason': 'string',
            "task_id": "iBWF-3"
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
