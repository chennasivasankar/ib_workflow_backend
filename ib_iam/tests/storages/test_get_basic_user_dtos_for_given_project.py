import pytest


class TestGetTeamBasicUserDTOS:

    @pytest.fixture()
    def user_storage(self):
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        return user_storage

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
    def create_user_teams(self, create_teams):
        team_objects = create_teams
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.tests.factories.models import UserTeamFactory
        user_team_objects = [
            UserTeamFactory(
                user_id=user_ids[0],
                team=team_objects[0]
            ),
            UserTeamFactory(
                user_id=user_ids[1],
                team=team_objects[0]
            ),
            UserTeamFactory(
                user_id=user_ids[2],
                team=team_objects[1]
            )
        ]
        return user_team_objects

    @pytest.fixture()
    def create_user_details(self):
        user_details_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_1",
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_2",
            },
            {
                "user_id": "77be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_3",
            }
        ]
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_details_objects = [
            UserDetailsFactory(
                user_id=user_details_dict["user_id"],
                name=user_details_dict["name"]
            )
            for user_details_dict in user_details_list
        ]
        return user_details_objects

    @pytest.mark.django_db
    def test_with_valid_team_id_return_response(
            self, user_storage, create_user_details, create_user_teams,
            create_project_teams
    ):
        # Arrange
        project_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        basic_user_details_list = [{
            'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848',
            'name': 'user_1',
            'profile_pic_url': None
        }, {
            'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848',
            'name': 'user_2',
            'profile_pic_url': None
        }, {
            'user_id': '77be920b-7b4c-49e7-8adb-41a0c18da848',
            'name': 'user_3',
            'profile_pic_url': None
        }]
        from ib_iam.tests.factories.storage_dtos import \
            BasicUserDetailsDTOFactory
        expected_basic_user_details_dtos = [
            BasicUserDetailsDTOFactory(
                user_id=basic_user_details_dict["user_id"],
                name=basic_user_details_dict["name"],
                profile_pic_url=basic_user_details_dict["profile_pic_url"]
            )
            for basic_user_details_dict in basic_user_details_list
        ]

        # Act
        response = user_storage.get_basic_user_dtos_for_given_project(
            project_id=project_id
        )

        # Assert
        assert response == expected_basic_user_details_dtos
