"""
# TODO: Update snapshot asserts to get know what are the details getting
save in db
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TaskFactory


class TestCase03UpdateAssigneesOfDiffStagesForATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        TaskFactory.reset_sequence()
        TaskFactory()

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {
            "task_id": "IBWF-1",
            "stage_assignees": [
                {
                    "stage_id": 1,
                     "assignee_id": "123e4567-e89b-12d3-a456-42661417400",
                     "team_id": "123e4567-e89b-12d3-a456-426614174001"
                },
                {
                    "stage_id": 1,
                    "assignee_id": "123e4567-e89b-12d3-a456-42761417400",
                    "team_id": "123e4567-e89b-12d3-a456-426714174001"
                }
            ]
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
