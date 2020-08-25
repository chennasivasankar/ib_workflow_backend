"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetTaskRpsInGivenStageAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture
    def setup(self, api_user, mocker):
        from ib_tasks.tests.factories.models import TaskFactory
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_immediate_superior_user_id_mock
        superior_id = "123e4567-e89b-12d3-a456-426614174002"
        superior_mock = get_immediate_superior_user_id_mock(mocker)
        superior_mock.side_effect = [superior_id, "123e4567-e89b-12d3-a456-426614174003"]
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_user_dtos_given_user_ids_mock
        user_details_mock = get_user_dtos_given_user_ids_mock(mocker)
        TaskFactory.reset_sequence()
        tasks = TaskFactory.create_batch(size=2)
        from ib_tasks.tests.factories.models import TaskStageHistoryModelFactory
        TaskStageHistoryModelFactory.reset_sequence()
        TaskStageHistoryModelFactory(task=tasks[0], assignee_id=api_user.user_id, stage_id=1)

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {'task_id': 'IBWF-1', 'stage_id': 'stage_id_0'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
