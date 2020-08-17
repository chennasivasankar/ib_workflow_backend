"""
# TODO: Update test case description
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.adapter_dtos import AssigneeDetailsDTOFactory
from ...factories.models import TaskStageHistoryModelFactory, TaskFactory
from ...factories.storage_dtos import TaskStageHistoryDTOFactory, LogDurationDTOFactory


class TestCase01GetStagesHistoryToTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture()
    @freeze_time('2012-10-10')
    def setup(self):
        TaskFactory.reset_sequence(1)
        task = TaskFactory(task_display_id="IBWF-1")
        TaskStageHistoryDTOFactory.reset_sequence(1)
        TaskStageHistoryModelFactory.reset_sequence(1)
        LogDurationDTOFactory.reset_sequence(1)
        AssigneeDetailsDTOFactory.reset_sequence(1)
        TaskStageHistoryModelFactory(task=task)
        TaskStageHistoryModelFactory(left_at=None, task=task)

    @freeze_time('2012-10-10')
    @pytest.mark.django_db
    def test_case(self, snapshot, mocker, setup):
        body = {"task_id": "IBWF-1"}
        path_params = {}
        query_params = {}
        headers = {}
        path1 = 'ib_tasks.adapters.assignees_details_service.AssigneeDetailsService.get_log_duration_dtos'
        log_mock = mocker.patch(path1)
        log_dtos = LogDurationDTOFactory.create_batch(2)
        log_mock.return_value = log_dtos
        path2 = 'ib_tasks.adapters.assignees_details_service.AssigneeDetailsService.get_assignees_details_dtos'
        user_mock_mock = mocker.patch(path2)
        user_dtos = [
            AssigneeDetailsDTOFactory(),
            AssigneeDetailsDTOFactory()
        ]
        # time_mock = mocker.patch('datetime.datetime.now')
        # time_mock.return_value = datetime(2012, 10, 20)
        user_mock_mock.return_value = user_dtos
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )