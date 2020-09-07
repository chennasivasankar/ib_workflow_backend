"""
# Invalid Method
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TaskFactory, StageActionFactory


class TestCase05GetNextStagesRandomAssigneesOfATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        TaskFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        TaskFactory()
        StageActionFactory(py_function_import_path="ib_tasks.tests.views.stage_action_logic.hello")

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {
            'task_id': "IBWF-1",
            'action_id': 1
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
