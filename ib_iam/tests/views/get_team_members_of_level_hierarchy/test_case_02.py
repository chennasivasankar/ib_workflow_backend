"""
All exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02GetTeamMembersOfLevelHierarchyAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

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

        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 0
        body = {}
        path_params = {
            "team_id": team_id,
            "level_hierarchy": level_hierarchy
        }
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

        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 0
        body = {}
        path_params = {
            "team_id": team_id,
            "level_hierarchy": level_hierarchy
        }
        query_params = {}

        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_invalid_level_hierarchy_of_team_return_response(
            self, snapshot, prepare_user_teams_setup
    ):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=True)

        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 4
        body = {}
        path_params = {
            "team_id": team_id,
            "level_hierarchy": level_hierarchy
        }
        query_params = {}

        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.fixture()
    def prepare_create_team_setup(self):
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

    @pytest.fixture()
    def prepare_user_teams_setup(self, prepare_create_team_setup):
        team_object = prepare_create_team_setup
        from ib_iam.tests.factories.models import TeamMemberLevelFactory
        team_member_level_object = TeamMemberLevelFactory(
            id="00be920b-7b4c-49e7-8adb-41a0c18da848",
            team=team_object,
            level_name="SDL",
            level_hierarchy=1
        )
        user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848",
            "30be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.tests.factories.models import TeamUserFactory
        user_team_objects_of_level_one = [
            TeamUserFactory(
                user_id=user_id,
                team=team_object,
                team_member_level=team_member_level_object
            )
            for user_id in user_ids
        ]

        team_member_level_object = TeamMemberLevelFactory(
            id="10be920b-7b4c-49e7-8adb-41a0c18da848",
            team=team_object,
            level_name="Developer",
            level_hierarchy=0
        )
        user_ids = [
            "40be920b-7b4c-49e7-8adb-41a0c18da848",
            "50be920b-7b4c-49e7-8adb-41a0c18da848",
            "60be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.tests.factories.models import TeamUserFactory
        user_team_objects = [
            TeamUserFactory(
                user_id=user_id,
                team=team_object,
                team_member_level=team_member_level_object
            )
            for user_id in user_ids
        ]
        return user_team_objects_of_level_one
