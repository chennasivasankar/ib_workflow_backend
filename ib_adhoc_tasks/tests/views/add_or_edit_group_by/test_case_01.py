"""
As given valid data it creates or updates respected group by
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01AddOrEditGroupByAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_adds_and_returns_group_by_response_dto(self, snapshot):
        body = {
            'view_type': 'LIST',
            'group_by_key': "ASSIGNEE",
            'order': 1,
            'group_by_id': None
        }
        path_params = {"project_id": "ibgroup"}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_edits_and_returns_group_by_response_dto(self, setup, snapshot):
        body = {
            'view_type': 'KANBAN',
            'group_by_key': "STAGE",
            'order': 2,
            'group_by_id': setup["group_by_id"]
        }
        path_params = {"project_id": setup["project_id"]}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.fixture
    def setup(self, api_user):
        project_id = "project_id_1"
        group_by_id = 1
        user_id = str(api_user.user_id)
        from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
        from ib_adhoc_tasks.constants.enum import ViewType
        GroupByInfoFactory(
            user_id=user_id, view_type=ViewType.KANBAN.value, order=1
        )
        return {"project_id": project_id, "group_by_id": group_by_id}
