"""
Raises TeamNameAlreadyExists exception as
the requested name is already assigned to another team
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03AddTeamAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {'name': 'team1', 'description': '',  'user_ids': []}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture()
    def setup(self, api_user):
        user_obj = api_user
        user_id = str(user_obj.user_id)
        from ib_iam.tests.factories.models import (
            UserFactory, TeamFactory
        )
        UserFactory.reset_sequence(1)
        TeamFactory.reset_sequence(1)
        UserFactory.create(user_id=user_id, is_admin=True)
        TeamFactory.create(name="team1")
