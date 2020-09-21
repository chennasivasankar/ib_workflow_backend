"""
Add project specific details
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01AssignUserRolesForGivenProjectBulkAPITestCase(TestUtils):
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
    def test_with_valid_details_then_assign_user_roles_bulk_for_given_project(
            self, snapshot, create_user_roles, create_project_teams,
            create_user_teams
    ):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=True)

        project_id = "project_id"
        user_id_with_role_ids_list = [
            {
                "user_id": "40be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": [
                    "ROLE_3", "ROLE_4"
                ]
            },
            {
                "user_id": "50be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": []
            },
            {
                "user_id": "60be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": [
                    "ROLE_1"
                ]
            }
        ]
        body = {
            'users': user_id_with_role_ids_list
        }
        path_params = {"project_id": project_id}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            snapshot=snapshot
               )

        from ib_iam.models import UserRole
        project_user_roles_list = UserRole.objects.filter(
            project_role__project_id=project_id
        ).values("user_id", "project_role_id")

        snapshot.assert_match(
            list(project_user_roles_list), "project_user_roles")

    @pytest.fixture()
    def create_project(self):
        project_id = "project_id"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(1)
        project_object = ProjectFactory(project_id=project_id)
        return project_object

    @pytest.fixture()
    def create_project_roles(self, create_project):
        project_id = "project_id"
        project_role_list = [
            {
                "project_id": project_id,
                "role_id": "ROLE_1",
                "name": "NAME_1",
                "description": "description"
            },
            {
                "project_id": project_id,
                "role_id": "ROLE_2",
                "name": "NAME_2",
                "description": "description"
            },
            {
                "project_id": project_id,
                "role_id": "ROLE_3",
                "name": "NAME_3",
                "description": "description"
            },
            {
                "project_id": project_id,
                "role_id": "ROLE_4",
                "name": "NAME_4",
                "description": "description"
            }
        ]
        from ib_iam.tests.factories.models import ProjectRoleFactory
        project_role_objects = [
            ProjectRoleFactory(
                project_id=project_role_dict["project_id"],
                role_id=project_role_dict["role_id"],
                name=project_role_dict["name"],
                description=project_role_dict["description"]
            )
            for project_role_dict in project_role_list
        ]
        return project_role_objects

    @pytest.fixture()
    def create_user_roles(self, create_project_roles):
        project_role_objects = create_project_roles
        user_role_list = [
            {
                "user_id": "40be920b-7b4c-49e7-8adb-41a0c18da848",
                "project_role": project_role_objects[0]
            },
            {
                "user_id": "40be920b-7b4c-49e7-8adb-41a0c18da848",
                "project_role": project_role_objects[1]
            },
            {
                "user_id": "50be920b-7b4c-49e7-8adb-41a0c18da848",
                "project_role": project_role_objects[2]
            }
        ]
        from ib_iam.tests.factories.models import UserRoleFactory
        user_role_objects = [
            UserRoleFactory(
                user_id=user_role_dict["user_id"],
                project_role=user_role_dict["project_role"]
            )
            for user_role_dict in user_role_list
        ]
        return user_role_objects

    @pytest.fixture()
    def create_teams(self):
        from ib_iam.tests.factories.models import TeamFactory
        team1_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        team2_id = "90ae920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
        team_objects = [
            TeamFactory(
                team_id=team1_id,
                name="name",
                description="description",
                created_by=user_id
            ),
            TeamFactory(
                team_id=team2_id,
                name="Tech Team",
                description="description",
                created_by=user_id
            )
        ]
        return team_objects

    @pytest.fixture()
    def create_project_teams(self, create_teams, create_project):
        project_object = create_project
        team_objects = create_teams
        from ib_iam.tests.factories.models import ProjectTeamFactory
        project_teams = [
            ProjectTeamFactory(project=project_object, team=team_objects[0]),
            ProjectTeamFactory(project=project_object, team=team_objects[1])
        ]
        return project_teams

    @pytest.fixture()
    def create_user_teams(self, create_teams):
        team_objects = create_teams
        user_ids = [
            "40be920b-7b4c-49e7-8adb-41a0c18da848",
            "50be920b-7b4c-49e7-8adb-41a0c18da848",
            "60be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.tests.factories.models import TeamUserFactory
        user_team_objects = [
            TeamUserFactory(user_id=user_id, team=team_objects[0])
            for user_id in user_ids
        ]
        return user_team_objects
