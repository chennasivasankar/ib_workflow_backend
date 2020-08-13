"""
# TODO: Update test case description
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.tests.factories.models import (
    TaskFactory,
    StageModelFactory,
    CurrentTaskStageModelFactory,
    StageActionFactory, TaskStageHistoryModelFactory,
)
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase04GetTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write', 'read']}}

    @pytest.fixture
    def reset_factories(self):
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        TaskStageHistoryModelFactory.reset_sequence()

    @pytest.fixture
    def setup(self, reset_factories):
        task_obj = TaskFactory()
        stage_objs = StageModelFactory.create_batch(size=10)
        CurrentTaskStageModelFactory.create_batch(
            size=3, task=task_obj, stage=factory.Iterator(stage_objs)
        )
        TaskStageHistoryModelFactory.create_batch(
            size=3, task=task_obj, stage=factory.Iterator(stage_objs),
            assignee_id=None
        )
        StageActionFactory.create_batch(
            size=20, stage=factory.Iterator(stage_objs)
        )

    @pytest.mark.django_db
    def test_case(self, snapshot, setup, mocker):
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)
        from ib_tasks.tests.common_fixtures.adapters\
            .assignees_details_service \
            import assignee_details_dtos_mock
        assignee_details_dtos_mock(mocker)
        body = {}
        path_params = {}
        query_params = {'task_id': "IBWF-1"}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
