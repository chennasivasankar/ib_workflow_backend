"""
#
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.models import UserTaskDelayReason
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

UserTaskDelayReason


class TestCase01GetReasonsForMissingTaskDueDateTimeAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture()
    def setup(self, api_user, mocker):
        from ib_tasks.tests.common_fixtures.adapters.assignees_details_service import \
            assignee_details_dtos_mock
        from ib_tasks.tests.factories.adapter_dtos import AssigneeDetailsDTOFactory
        AssigneeDetailsDTOFactory.reset_sequence()
        # AssigneeDetailsDTOFactory(assignee_id=api_user.user_id)
        user_dtos = assignee_details_dtos_mock(mocker, api_user.user_id)
        from ib_tasks.tests.factories.models import TaskFactory

        TaskFactory.reset_sequence()
        tasks = TaskFactory.create_batch(size=2)
        from ib_tasks.tests.factories.models import TaskStageFactory
        TaskStageFactory.reset_sequence()
        TaskStageFactory(task=tasks[0], assignee_id=api_user.user_id)
        from ib_tasks.tests.factories.models import TaskDueDetailsFactory
        TaskDueDetailsFactory.reset_sequence()
        TaskDueDetailsFactory(user_id=api_user.user_id, task=tasks[0])
        TaskDueDetailsFactory.create_batch(size=3, task=tasks[0])

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {}
        path_params = {"task_id": 1}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
