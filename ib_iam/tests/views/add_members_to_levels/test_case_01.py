"""
successfully created the team member levels
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01AddMembersToLevelsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(
            self, create_team, create_users_team,
            create_team_member_levels, snapshot):
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
        response = self.make_api_call(body=body,
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

        from ib_iam.tests.factories.models import UserTeamFactory
        user_team_objects = [
            UserTeamFactory(
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
                "level_name": "Developer",
                "level_hierarchy": 0
            },
            {
                "id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_name": "Software Developer Lead",
                "level_hierarchy": 1
            },
            {
                "id": "02be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_name": "Engineer Manager",
                "level_hierarchy": 2
            }
        ]
        from ib_iam.tests.factories.models import TeamMemberLevelFactory
        team_member_level_objects = [
            TeamMemberLevelFactory(
                id=team_member_level_dict["id"],
                team_id=team_member_level_dict["team_id"],
                level_name=team_member_level_dict["level_name"],
                level_hierarchy=team_member_level_dict["level_hierarchy"]
            )
            for team_member_level_dict in team_member_level_list
        ]
        return team_member_level_objects
