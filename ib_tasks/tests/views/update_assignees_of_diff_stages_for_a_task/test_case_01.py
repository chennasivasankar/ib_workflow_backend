"""
# Given Valid details
"""

import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.tests.factories.models import TaskFactory, StageFactory, \
    StagePermittedRolesFactory, TaskStageHistoryModelFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


@pytest.mark.django_db
class TestCase01UpdateAssigneesOfDiffStagesForATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        TaskFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()
        TaskStageHistoryModelFactory.reset_sequence()
        task_obj = TaskFactory()
        stage_objs = StageFactory.create_batch(size=4)
        StagePermittedRolesFactory.create_batch(
            size=6,
            stage=factory.Iterator(stage_objs)
        )
        TaskStageHistoryModelFactory.create_batch(
            size=2, task=task_obj,
            stage=factory.Iterator(stage_objs)
        )

    def test_case(self, snapshot, setup, mocker):
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        get_user_role_ids_based_on_project_mock(mocker)
        body = {
            "task_id": "IBWF-1",
            "stage_assignees": [
                {
                    "stage_id": 1,
                    "assignee_id": "123e4567-e89b-12d3-a456-426614174004",
                    "team_id": "123e4567-e89b-12d3-a456-426614174001"
                },
                {
                    "stage_id": 2,
                    "assignee_id": "123e4567-e89b-12d3-a456-427614174008",
                    "team_id": "123e4567-e89b-12d3-a456-426614174002"
                },
                {
                    "stage_id": 3,
                    "assignee_id": "123e4567-e89b-12d3-a476-427614174006",
                    "team_id": "123e4567-e89b-12d3-a456-426614174003"
                }
            ]
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        from ib_tasks.models import TaskStageHistory
        task_stage_objs = TaskStageHistory.objects.all()
        counter = 1
        for task_stage_obj in task_stage_objs:
            snapshot.assert_match(
                name=f'stage_{counter}', value=task_stage_obj.stage_id
            )
            snapshot.assert_match(
                name=f'assignee_{counter}', value=task_stage_obj.assignee_id
            )
            snapshot.assert_match(
                name=f'left_{counter}', value=task_stage_obj.left_at
            )
            counter += counter
