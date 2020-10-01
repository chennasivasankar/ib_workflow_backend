"""
test with invalid task display id
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TaskFactory


class TestCase01ValidateTaskFilledFieldsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self):
        task_id = "IBWF-1"

        TaskFactory.create(task_display_id=task_id)

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {'task_id': 'IBWF-2', 'action_id': "1"}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
