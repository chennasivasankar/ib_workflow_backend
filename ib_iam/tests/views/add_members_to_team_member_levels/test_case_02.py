"""
All Exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02AddMembersToLevelsAPITestCase(TestUtils):
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
    def test_with_user_is_not_admin_return_response(self, snapshot):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=False)

        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_id_with_member_ids_list = [
            {
                "team_member_level_id": "00be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": [
                    "31be920b-7b4c-49e7-8adb-41a0c18da848",
                    "01be920b-7b4c-49e7-8adb-41a0c18da848",
                ]
            },
            {
                "team_member_level_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": [
                    "77be920b-7b4c-49e7-8adb-41a0c18da848",
                    "17be920b-7b4c-49e7-8adb-41a0c18da848",
                    "27be920b-7b4c-49e7-8adb-41a0c18da848",
                ]
            },
            {
                "team_member_level_id": "02be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": []
            }
        ]
        body = {
            'members': team_member_level_id_with_member_ids_list
        }
        path_params = {"team_id": team_id}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_invalid_team_id_return_response(self, snapshot):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=True)

        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_id_with_member_ids_list = [
            {
                "team_member_level_id": "00be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": [
                    "31be920b-7b4c-49e7-8adb-41a0c18da848",
                    "01be920b-7b4c-49e7-8adb-41a0c18da848",
                ]
            },
            {
                "team_member_level_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": [
                    "77be920b-7b4c-49e7-8adb-41a0c18da848",
                    "17be920b-7b4c-49e7-8adb-41a0c18da848",
                    "27be920b-7b4c-49e7-8adb-41a0c18da848",
                ]
            },
            {
                "team_member_level_id": "02be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": []
            }
        ]
        body = {
            'members': team_member_level_id_with_member_ids_list
        }
        path_params = {"team_id": team_id}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_team_member_level_ids_not_found_return_response(
            self, snapshot, create_team, create_users_team,
            create_team_member_levels
    ):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=True)

        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_id_with_member_ids_list = [
            {
                "team_member_level_id": "00be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": [
                    "31be920b-7b4c-49e7-8adb-41a0c18da848",
                    "01be920b-7b4c-49e7-8adb-41a0c18da848",
                ]
            },
            {
                "team_member_level_id": "91be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": [
                    "77be920b-7b4c-49e7-8adb-41a0c18da848",
                    "17be920b-7b4c-49e7-8adb-41a0c18da848",
                    "27be920b-7b4c-49e7-8adb-41a0c18da848",
                ]
            },
            {
                "team_member_level_id": "92be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": []
            }
        ]
        body = {
            'members': team_member_level_id_with_member_ids_list
        }
        path_params = {"team_id": team_id}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_team_member_ids_not_found_return_response(
            self, create_team, create_users_team,
            create_team_member_levels, snapshot):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=True)

        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_id_with_member_ids_list = [
            {
                "team_member_level_id": "00be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": [
                    "31be920b-7b4c-49e7-8adb-41a0c18da848",
                    "01be920b-7b4c-49e7-8adb-41a0c18da848",
                ]
            },
            {
                "team_member_level_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": [
                    "77be920b-7b4c-49e7-8adb-41a0c18da848",
                    "97be920b-7b4c-49e7-8adb-41a0c18da848",
                    "97be920b-7b4c-49e7-8adb-41a0c18da848",
                ]
            },
            {
                "team_member_level_id": "02be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": []
            }
        ]
        body = {
            'members': team_member_level_id_with_member_ids_list
        }
        path_params = {"team_id": team_id}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.fixture()
    def create_team(self):
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
    def create_users_team(self):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848",
            "17be920b-7b4c-49e7-8adb-41a0c18da848",
            "27be920b-7b4c-49e7-8adb-41a0c18da848",
            "37be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        from ib_iam.tests.factories.models import TeamUserFactory
        user_team_objects = [
            TeamUserFactory(
                user_id=user_id, team_id=team_id
            )
            for user_id in user_ids
        ]
        return user_team_objects

    @pytest.fixture()
    def create_team_member_levels(self):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_list = [
            {
                "id": "00be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_hierarchy": 0
            },
            {
                "id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_hierarchy": 1
            },
            {
                "id": "02be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_hierarchy": 2
            }
        ]
        from ib_iam.tests.factories.models import TeamMemberLevelFactory
        team_member_level_objects = [
            TeamMemberLevelFactory(
                id=team_member_level_dict["id"],
                team_id=team_member_level_dict["team_id"],
                level_hierarchy=team_member_level_dict["level_hierarchy"]
            )
            for team_member_level_dict in team_member_level_list
        ]
        return team_member_level_objects
