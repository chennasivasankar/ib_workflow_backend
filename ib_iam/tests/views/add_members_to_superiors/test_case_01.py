"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01AddMembersToSuperiorsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, snapshot, prepare_user_teams_setup):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = 0
        user_team_objects_of_level_one = prepare_user_teams_setup
        add_members_to_superior = [{
            "immediate_superior_user_id": user_team_objects_of_level_one[0].user_id,
            "member_ids": [
                "40be920b-7b4c-49e7-8adb-41a0c18da848",
                "50be920b-7b4c-49e7-8adb-41a0c18da848"
            ]
        }, {
            "immediate_superior_user_id": user_team_objects_of_level_one[1].user_id,
            "member_ids": [
                "60be920b-7b4c-49e7-8adb-41a0c18da848"
            ]
        }]

        body = {
            'add_members_to_superior': add_members_to_superior
        }
        path_params = {
            "team_id": team_id,
            "level_hierarchy": member_level_hierarchy
        }
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            snapshot=snapshot)

        from ib_iam.models import UserTeam
        user_team_objects = UserTeam.objects.filter(
            team_id=team_id
        )
        user_team_list = user_team_objects.values(
            "id", "user_id", "team_member_level_id",
            "immediate_superior_team_user_id"
        )
        for user_team_dict in user_team_list:
            user_team_dict["team_member_level_id"] = \
                str(user_team_dict["team_member_level_id"])
        snapshot.assert_match(list(user_team_list), "user_team")

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
        from ib_iam.tests.factories.models import UserTeamFactory
        user_team_objects_of_level_one = [
            UserTeamFactory(
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
        from ib_iam.tests.factories.models import UserTeamFactory
        user_team_objects = [
            UserTeamFactory(
                user_id=user_id,
                team=team_object,
                team_member_level=team_member_level_object
            )
            for user_id in user_ids
        ]
        return user_team_objects_of_level_one
