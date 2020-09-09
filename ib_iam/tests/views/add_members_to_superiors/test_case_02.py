"""
All exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02AddMembersToSuperiorsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_with_invalid_team_id_return_response(
            self, snapshot, prepare_user_teams_setup
    ):
        team_id = "01be920b-7b4c-49e7-8adb-41a0c18da848"
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

    @pytest.mark.django_db
    def test_invalid_level_hierarchy_of_team_return_response(
            self, snapshot, prepare_user_teams_setup
    ):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = 3
        user_team_objects_of_level_one = prepare_user_teams_setup
        add_members_to_superior = [{
            "immediate_superior_user_id": user_team_objects_of_level_one[
                0].user_id,
            "member_ids": [
                "40be920b-7b4c-49e7-8adb-41a0c18da848",
                "50be920b-7b4c-49e7-8adb-41a0c18da848"
            ]
        }, {
            "immediate_superior_user_id": user_team_objects_of_level_one[
                1].user_id,
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

    @pytest.mark.django_db
    def test_team_member_ids_not_found_return_response(
            self, snapshot, prepare_user_teams_setup
    ):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = 0
        user_team_objects_of_level_one = prepare_user_teams_setup
        add_members_to_superior = [{
            "immediate_superior_user_id": user_team_objects_of_level_one[
                0].user_id,
            "member_ids": [
                "10be920b-7b4c-49e7-8adb-41a0c18da848",
                "50be920b-7b4c-49e7-8adb-41a0c18da848"
            ]
        }, {
            "immediate_superior_user_id": user_team_objects_of_level_one[
                1].user_id,
            "member_ids": [
                "70be920b-7b4c-49e7-8adb-41a0c18da848"
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

    @pytest.mark.django_db
    def test_subordinate_users_not_belong_to_team_member_level_return_response(
            self, snapshot, prepare_user_teams_setup
    ):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = 1
        user_team_objects_of_level_one = prepare_user_teams_setup
        add_members_to_superior = [{
            "immediate_superior_user_id": user_team_objects_of_level_one[
                0].user_id,
            "member_ids": [
                "40be920b-7b4c-49e7-8adb-41a0c18da848",
                "50be920b-7b4c-49e7-8adb-41a0c18da848"
            ]
        }, {
            "immediate_superior_user_id": user_team_objects_of_level_one[
                1].user_id,
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

    @pytest.mark.django_db
    def test_superior_users_not_belong_to_team_member_level_return_response(
            self, snapshot, prepare_user_teams_setup
    ):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = 0
        user_team_objects_of_level_one = prepare_user_teams_setup
        add_members_to_superior = [{
            "immediate_superior_user_id": user_team_objects_of_level_one[
                0].user_id,
            "member_ids": [
                "40be920b-7b4c-49e7-8adb-41a0c18da848",
                "50be920b-7b4c-49e7-8adb-41a0c18da848"
            ]
        }, {
            "immediate_superior_user_id": user_team_objects_of_level_one[
                1].user_id,
            "member_ids": [
                "60be920b-7b4c-49e7-8adb-41a0c18da848"
            ]
        }]

        from ib_iam.tests.factories.models import TeamMemberLevelFactory
        TeamMemberLevelFactory(
            id="70be920b-7b4c-49e7-8adb-41a0c18da848",
            team_id=team_id,
            level_name="EM",
            level_hierarchy=1
        )
        from ib_iam.models import TeamMemberLevel
        TeamMemberLevel.objects.filter(
            id="00be920b-7b4c-49e7-8adb-41a0c18da848"
        ).update(level_hierarchy=3)

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
