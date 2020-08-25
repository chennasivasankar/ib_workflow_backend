import pytest


class TestGetUserTeamDTOSForGivenProjectAndUserTeams:
    @pytest.fixture
    def set_up(self):
        project_id = "FA"
        user_id = "1123"
        team_id = "b953895a-b77b-4a60-b94d-e4ee6a9b8c3a"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(0)
        project_object = ProjectFactory.create(project_id=project_id)
        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory.reset_sequence(0)
        team_object = TeamFactory.create(team_id=team_id)
        from ib_iam.tests.factories.models import ProjectTeamFactory
        ProjectTeamFactory.reset_sequence(0)
        project_team_object = ProjectTeamFactory.create(
            team_id=team_id, project_id=project_id)
        from ib_iam.tests.factories.models import UserTeamFactory
        UserTeamFactory.reset_sequence(0)
        user_team_object = UserTeamFactory.create(team=team_object,
                                                  user_id=user_id)
        return project_object, team_object, user_team_object, project_team_object

    @pytest.mark.django_db
    def test_get_user_team_dtos_given_valid_detail_then_return_user_team_dtos(
            self, set_up):
        project_id = "FA"
        user_id = "1123"
        team_id = "b953895a-b77b-4a60-b94d-e4ee6a9b8c3a"
        from ib_iam.app_interfaces.dtos import UserIdWithTeamIdDTO
        user_team_ids_dto = UserIdWithTeamIdDTO(user_id=user_id,
                                                team_id=team_id)
        from ib_iam.app_interfaces.dtos import ProjectTeamsAndUsersDTO
        project_teams_and_users_dto = ProjectTeamsAndUsersDTO(
            project_id=project_id,
            user_id_with_team_id_dtos=[user_team_ids_dto]
        )
        from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO
        expected_result = [
            UserTeamDTO(user_id=user_id, team_id=team_id, team_name="team 0")
        ]
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        actual_result = service_interface.get_user_team_dtos_for_given_project_teams_and_users_details_dto(
            project_teams_and_users_dto=project_teams_and_users_dto)

        assert expected_result == actual_result
