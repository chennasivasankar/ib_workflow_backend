import pytest


class TestGetUserRoleDTOSOfATeam:

    @pytest.fixture()
    def user_storage(self):
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        return user_storage

    @pytest.mark.django_db
    def test_with_valid_details_return_response(
            self, create_project_teams, create_user_roles, user_storage
    ):
        # Arrange
        project_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        user_role_list = [{
            'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848',
            'role_id': 'ROLE_1',
            'name': 'NAME_1',
            'description': None
        }, {
            'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848',
            'role_id': 'ROLE_2',
            'name': 'NAME_2',
            'description': None
        }, {
            'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848',
            'role_id': 'ROLE_3',
            'name': 'NAME_3',
            'description': None
        }]
        from ib_iam.tests.factories.storage_dtos import UserRoleDTOFactory
        expected_user_role_dtos = [
            UserRoleDTOFactory(
                user_id=user_role_dict["user_id"],
                role_id=user_role_dict["role_id"],
                name=user_role_dict["name"],
                description=user_role_dict["description"]
            )
            for user_role_dict in user_role_list
        ]

        # Act
        response = user_storage.get_user_role_dtos_of_a_team(
            user_ids=user_ids, project_id=project_id
        )

        # Assert
        assert response == expected_user_role_dtos

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
    def create_project(self):
        project_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(1)
        project_object = ProjectFactory(project_id=project_id)
        return project_object

    @pytest.fixture()
    def create_project_teams(self, create_teams, create_project):
        project_object = create_project
        team_objects = create_teams
        from ib_iam.models import ProjectTeam
        # TODO:  user factory for project team
        project_teams = [
            ProjectTeam(
                project=project_object,
                team_id=team_objects[0].team_id
            ),
            ProjectTeam(
                project=project_object,
                team_id=team_objects[1].team_id
            )
        ]
        ProjectTeam.objects.bulk_create(project_teams)
        return project_teams

    @pytest.fixture()
    def create_project_roles(self):
        project_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
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
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "project_role": project_role_objects[0]
            },
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "project_role": project_role_objects[1]
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
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
