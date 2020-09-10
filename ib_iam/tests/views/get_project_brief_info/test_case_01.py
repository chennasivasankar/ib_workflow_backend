"""
Get Project Brief Info
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetProjectBriefInfoAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    def _get_or_create_user(self):
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_with_valid_details_return_response(
            self, snapshot, create_project_teams, create_team_users
    ):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.fixture()
    def create_teams(self):
        from ib_iam.tests.factories.models import TeamFactory
        team_ids = [
            "11be920b-7b4c-49e7-8adb-41a0c18da848",
            "21be920b-7b4c-49e7-8adb-41a0c18da848",
            "31be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        team_objects = [
            TeamFactory(
                team_id=team_id
            )
            for team_id in team_ids
        ]
        return team_objects

    @pytest.fixture()
    def create_projects(self, create_teams):
        from ib_iam.tests.factories.models import ProjectFactory
        project_ids = [
            "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
            "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5",
            "641bfcc5-e1ea-4231-b482-f7f34fb5c7c6"
        ]
        ProjectFactory.reset_sequence(1)
        project_objects = [
            ProjectFactory.create(project_id=project_id)
            for project_id in project_ids
        ]
        return project_objects

    @pytest.fixture()
    def create_project_teams(self, create_teams, create_projects):
        team_objects = create_teams
        project_objects = create_projects
        from ib_iam.tests.factories.models import ProjectTeamFactory
        project_team_list = [
            {
                "project": project_objects[0],
                "team": team_objects[0]
            },
            {
                "project": project_objects[0],
                "team": team_objects[1]
            },
            {
                "project": project_objects[1],
                "team": team_objects[0]
            }
        ]
        project_team_objects = [
            ProjectTeamFactory(
                project=project_team_dict["project"],
                team=project_team_dict["team"]
            )
            for project_team_dict in project_team_list
        ]
        return project_team_objects

    @pytest.fixture()
    def create_team_users(self, create_teams):
        team_objects = create_teams
        team_users_list = [
            {
                "user_id": "00be920b-7b4c-49e7-8adb-41a0c18da848",
                "team": team_objects[0]
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "team": team_objects[0]
            },
            {
                "user_id": "02be920b-7b4c-49e7-8adb-41a0c18da848",
                "team": team_objects[0]
            },
            {
                "user_id": "00be920b-7b4c-49e7-8adb-41a0c18da848",
                "team": team_objects[1]
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "team": team_objects[1]
            },
            {
                "user_id": "03be920b-7b4c-49e7-8adb-41a0c18da848",
                "team": team_objects[2]
            }
        ]
        from ib_iam.tests.factories.models import TeamUserFactory
        team_user_objects = [
            TeamUserFactory(
                user_id=team_users_dict["user_id"],
                team=team_users_dict["team"]
            )
            for team_users_dict in team_users_list
        ]
        return team_user_objects
