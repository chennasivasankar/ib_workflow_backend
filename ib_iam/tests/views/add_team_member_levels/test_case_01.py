"""
Add team member levels
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01AddTeamMemberLevelsAPITestCase(TestUtils):
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

    @pytest.fixture()
    def prepare_team_setup(self):
        from ib_iam.tests.factories.models import TeamFactory
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
        team_object = TeamFactory(
            team_id=team_id,
            name="name",
            description="description",
            created_by=user_id
        )
        return team_object

    @pytest.mark.django_db
    def test_add_team_member_levels(self, prepare_team_setup, snapshot):
        from ib_iam.models import UserDetails
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        UserDetails.objects.create(user_id=user_id, is_admin=True)

        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_levels = [
            {
                "level_name": "Developer",
                "level_hierarchy": 0
            },
            {
                "level_name": "Software Developer Lead",
                "level_hierarchy": 1
            },
            {
                "level_name": "Engineer Manager",
                "level_hierarchy": 2
            },
            {
                "level_name": "Product Owner",
                "level_hierarchy": 3
            }
        ]
        body = {
            'team_member_levels': team_member_levels
        }
        path_params = {"team_id": team_id}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
