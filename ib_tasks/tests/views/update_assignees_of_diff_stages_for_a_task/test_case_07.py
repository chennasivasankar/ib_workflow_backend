"""
# TODO: Update snapshot asserts to get know what are the details getting
save in db
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.adapters.roles_service import RolesService
from ib_tasks.tests.factories.models import TaskFactory, StageFactory, \
    StagePermittedRolesFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase07UpdateAssigneesOfDiffStagesForATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        TaskFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()
        TaskFactory()
        stage_objs = StageFactory.create_batch(size=4)
        import factory
        StagePermittedRolesFactory.create_batch(size=6, stage=factory.Iterator(
            stage_objs))

    @pytest.mark.django_db
    @patch.object(RolesService, "get_user_role_ids_based_on_project")
    def test_case(self, role_ids_mock, snapshot, setup):
        user_roles = ["FIN_PAYMENT_POC"]
        role_ids_mock.return_value = user_roles
        body = {
            "task_id": "IBWF-1",
            "stage_assignees": [
                {
                    "stage_id": 1,
                    "assignee_id": "123e4567-e89b-12d3-a456-426614174000",
                    "team_id": "123e4567-e89b-12d3-a456-426614174001"
                },
                {
                    "stage_id": 2,
                    "assignee_id": "123e4567-e89b-12d3-a456-42761417400",
                    "team_id": "123e4567-e89b-12d3-a456-426714174001"
                },
                {
                    "stage_id": 3,
                    "assignee_id": "123e4567-e89b-12d3-a476-42761417400",
                    "team_id": "123e4567-e89b-12d3-a458-426714174001"
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
