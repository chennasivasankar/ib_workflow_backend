"""
as given valid data returns group_by_response dict
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetGroupByAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_given_valid_data_it_returns_group_by_response(
            self, setup, snapshot
    ):
        body = {}
        path_params = {"project_id": setup["project_id"]}
        query_params = {'view_type': 'KANBAN'}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.fixture
    def setup(self, api_user):
        project_id = "project_id_1"
        user_id = str(api_user.user_id)
        from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
        from ib_adhoc_tasks.constants.enum import ViewType
        GroupByInfoFactory.reset_sequence(1)
        GroupByInfoFactory.group_by.reset()
        GroupByInfoFactory.order.reset()
        GroupByInfoFactory.create_batch(
            size=2, user_id=user_id, view_type=ViewType.KANBAN.value
        )
        return {"project_id": project_id}
