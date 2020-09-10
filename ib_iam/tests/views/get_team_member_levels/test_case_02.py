"""
All exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02GetTeamMemberLevelsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    def _get_or_create_user(self):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_with_user_not_admin_return_response(
            self, snapshot
    ):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=False)

        team_id = "01be920b-7b4c-49e7-8adb-41a0c18da848"
        body = {}
        path_params = {"team_id": team_id}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_invalid_team_id_return_response(
            self, snapshot
    ):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=True)

        team_id = "01be920b-7b4c-49e7-8adb-41a0c18da848"
        body = {}
        path_params = {"team_id": team_id}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
