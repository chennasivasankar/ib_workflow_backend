import pytest


class TestGetUserStatusForGivenProjects:
    @pytest.fixture
    def projects_set_up(self):
        project_ids = ["1", "2"]
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(0)
        project_objects = [
            ProjectFactory.create(
                project_id=project_id
            ) for project_id in project_ids
        ]
        return project_objects

    @pytest.fixture
    def teams_set_up(self):
        team_ids = [
            "b953895a-b77b-4a60-b94d-e4ee6a9b8c3a",
            "b953895a-b77b-4a60-b94d-e4ee6a9b8c31"
        ]
        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory.reset_sequence(0)
        team_objects = [
            TeamFactory.create(team_id=team_id)
            for team_id in team_ids
        ]
        return team_objects

    @pytest.fixture
    def project_teams_set_up(self, projects_set_up, teams_set_up):
        project_team_ids = [
            {
                "project_id": "1",
                "team_id": "b953895a-b77b-4a60-b94d-e4ee6a9b8c3a"
            },
            {
                "project_id": "1",
                "team_id": "b953895a-b77b-4a60-b94d-e4ee6a9b8c31"
            },
            {
                "project_id": "2",
                "team_id": "b953895a-b77b-4a60-b94d-e4ee6a9b8c31"
            }
        ]
        from ib_iam.tests.factories.models import ProjectTeamFactory
        ProjectTeamFactory.reset_sequence(0)
        from ib_iam.models import Project
        from ib_iam.models import Team
        project_team_objects = [
            ProjectTeamFactory.create(
                project=Project.objects.get(
                    project_id=project_team["project_id"]),
                team=Team.objects.get(team_id=project_team["team_id"])
            ) for project_team in project_team_ids
        ]
        return project_team_objects

    @pytest.fixture
    def team_users_set_up(self, teams_set_up):
        team_users = [
            {
                "team_id": "b953895a-b77b-4a60-b94d-e4ee6a9b8c3a",
                "user_id": "1"
            }
        ]
        from ib_iam.tests.factories.models import TeamUserFactory
        from ib_iam.models import Team
        team_user_objects = [
            TeamUserFactory.create(
                user_id=team_user["user_id"],
                team=Team.objects.get(team_id=team_user["team_id"])
            ) for team_user in team_users
        ]
        return team_user_objects

    @pytest.fixture
    def user_set_up(self):
        user_id = "1"
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.reset_sequence(0)
        return UserDetailsFactory.create(user_id=user_id)

    @pytest.fixture()
    def service_interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    @pytest.mark.django_db
    def test_with_valid_details_then_return_response(
            self, project_teams_set_up, team_users_set_up, service_interface,
            user_set_up
    ):
        user_id = "1"
        project_ids = ["1", "2"]
        project_ids = list(set(project_ids))
        from ib_iam.interactors.dtos.dtos import \
            UserIdWithProjectIdAndStatusDTO
        valid_user_exist_project_ids = ["1"]
        expected_result = [
            UserIdWithProjectIdAndStatusDTO(
                user_id=user_id,
                project_id=project_id,
                is_exist=project_id in valid_user_exist_project_ids
            ) for project_id in project_ids
        ]

        result = service_interface.get_user_status_for_given_projects(
            user_id=user_id, project_ids=project_ids)

        assert expected_result == result

    @pytest.mark.django_db
    def test_with_invalid_user_id_then_raise_exception(
            self, project_teams_set_up, team_users_set_up, service_interface,
    ):
        user_id = "1"
        project_ids = ["1", "2"]

        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        with pytest.raises(InvalidUserId):
            service_interface.get_user_status_for_given_projects(
                user_id=user_id, project_ids=project_ids)

    @pytest.mark.django_db
    def test_with_invalid_project_ids_then_raise_exception(
            self, service_interface, user_set_up
    ):
        user_id = "1"
        project_ids = ["1", "2"]
        project_ids = list(set(project_ids))

        from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
        with pytest.raises(InvalidProjectIds) as err:
            service_interface.get_user_status_for_given_projects(
                user_id=user_id, project_ids=project_ids)

        assert err.value.project_ids == project_ids
