"""
# TODO: Update test case description
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TaskFactory, StageActionFactory, \
    StageModelFactory, TaskStatusVariableFactory


class TestCase06GetNextStagesRandomAssigneesOfATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        TaskFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        task_obj = TaskFactory()
        stage_obj = StageModelFactory(stage_id="VENDOR_PENDING_RP_APPROVAL")
        StageActionFactory(
            stage=stage_obj,
            name="Reject",
            py_function_import_path="ib_tasks.tests.views.stage_action_logic.VENDOR_PENDING_RP_APPROVAL_Reject"
        )
        TaskStatusVariableFactory(
            task_id=task_obj.id,
            variable="variable1",
            value="VENDOR_REJECTED"
        )

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
