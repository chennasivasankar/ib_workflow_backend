import json

import pytest


class TestGetProjectsPresenterImplementation:

    @pytest.fixture
    def projects_set_up(self):
        project_ids = ["f2c02d98-f311-4ab2-8673-3daa00757002"]
        from ib_iam.tests.factories.storage_dtos import \
            ProjectWithDisplayIdDTOFactory
        ProjectWithDisplayIdDTOFactory.reset_sequence(1)
        project_dtos = [ProjectWithDisplayIdDTOFactory(project_id=project_id)
                        for project_id in project_ids]
        return project_dtos

    @pytest.fixture
    def project_teams_set_up(self):
        team_ids = ["f2c02d98-f311-4ab2-8673-3daa00757002"]
        from ib_iam.interactors.storage_interfaces.dtos import \
            ProjectTeamIdsDTO
        project_team_ids_dtos = [
            ProjectTeamIdsDTO(
                project_id="f2c02d98-f311-4ab2-8673-3daa00757002",
                team_ids=team_ids)]
        return project_team_ids_dtos

    @pytest.fixture
    def project_roles_setup(self):
        role_ids = ["f2c02d98-f311-4ab2-8673-3daa00757002"]
        from ib_iam.tests.factories.storage_dtos import ProjectRoleDTOFactory
        ProjectRoleDTOFactory.reset_sequence(1)
        project_role_dtos = [ProjectRoleDTOFactory(
            project_id="f2c02d98-f311-4ab2-8673-3daa00757002",
            role_id=role_id) for role_id in role_ids]
        return project_role_dtos

    @pytest.fixture
    def teams_set_up(self):
        team_ids = ['f2c02d98-f311-4ab2-8673-3daa00757002']
        from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
        TeamDTOFactory.reset_sequence(1)
        team_dtos = [TeamDTOFactory(team_id=team_id) for team_id in team_ids]
        return team_dtos

    def test_get_response_for_get_projects_returns_projects(
            self, snapshot, projects_set_up, teams_set_up,
            project_teams_set_up, project_roles_setup):
        from ib_iam.presenters.get_projects_presenter_implementation import \
            GetProjectsPresenterImplementation
        json_presenter = GetProjectsPresenterImplementation()
        total_projects_count = len(projects_set_up)
        from ib_iam.interactors.presenter_interfaces.dtos import \
            ProjectWithTeamsDTO
        project_with_teams_dto = ProjectWithTeamsDTO(
            total_projects_count=total_projects_count,
            project_dtos=projects_set_up,
            project_team_ids_dtos=project_teams_set_up,
            team_dtos=teams_set_up,
            project_role_dtos=project_roles_setup)

        http_response = json_presenter.get_response_for_get_projects(
            project_with_teams_dto=project_with_teams_dto)

        response = json.loads(http_response.content)

        snapshot.assert_match(response, "projects")
