import pytest


class TestGetUserStatusForGivenProject:
    @pytest.fixture
    def project_storage(self):
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        project_storage = ProjectStorageImplementation()
        return project_storage

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
        project_team_objects = [
            ProjectTeamFactory.create(
                project_id=project_team["project_id"],
                team_id=project_team["team_id"]
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

    @pytest.mark.django_db
    def test_get_user_status_for_given_project_ids_then_return_response_dtos(
            self, project_storage, project_teams_set_up, team_users_set_up,
    ):
        user_id = "1"
        project_ids = ["1", "2"]
        from ib_iam.interactors.dtos.dtos import \
            UserIdWithProjectIdAndStatusDTO
        expected_result = [
            UserIdWithProjectIdAndStatusDTO(
                user_id="1", project_id="1", is_exist=True
            ),
            UserIdWithProjectIdAndStatusDTO(
                user_id="1", project_id="2", is_exist=False
            )
        ]
        expected_result_after_sorted = sorted(
            expected_result, key=lambda _object: _object.project_id)

        result = project_storage.get_user_status_for_given_projects(
            user_id=user_id, project_ids=project_ids)
        actual_result_after_sorted = sorted(
            result, key=lambda _object: _object.project_id)

        assert expected_result_after_sorted == actual_result_after_sorted

    @pytest.mark.django_db
    def test_get_user_status_for_given_project_ids_return_empty_list(
            self, project_storage
    ):
        user_id = "1"
        project_ids = ["1", "2"]
        from ib_iam.interactors.dtos.dtos import \
            UserIdWithProjectIdAndStatusDTO
        expected_result = [
            UserIdWithProjectIdAndStatusDTO(
                user_id="1", project_id="1", is_exist=False
            ),
            UserIdWithProjectIdAndStatusDTO(
                user_id="1", project_id="2", is_exist=False
            )
        ]
        expected_result_after_sorted = sorted(
            expected_result, key=lambda _object: _object.project_id)

        result = project_storage.get_user_status_for_given_projects(
            user_id=user_id, project_ids=project_ids)

        assert expected_result_after_sorted == result

