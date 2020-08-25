"""
# user is not assigned to task
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase04AddReasonForMissingDueDateTimeAPITestCase(TestUtils):
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
        from ib_tasks.tests.factories.models import TaskStageHistoryModelFactory
        TaskStageHistoryModelFactory.reset_sequence()
        TaskStageHistoryModelFactory(task=tasks[0], stage_id=1)

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {
            'updated_due_date_time': '2020-08-26T11:30:45.34523',
            'reason_id': 1,
            'reason': 'string',
            'stage_id': 1,
            "task_id": "IBWF-1"
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
