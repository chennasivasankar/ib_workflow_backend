import json

import pytest

from ib_iam.constants.enums import StatusCode
from ib_iam.constants.exception_messages import INVALID_LIMIT_VALUE, \
    INVALID_OFFSET_VALUE, USER_HAS_NO_ACCESS_TO_GET_PROJECTS


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
            project_teams_set_up, project_roles_setup
    ):
        from ib_iam.presenters.get_projects_presenter_implementation import \
            GetProjectsPresenterImplementation
        presenter = GetProjectsPresenterImplementation()
        total_projects_count = len(projects_set_up)
        from ib_iam.interactors.presenter_interfaces.dtos import \
            ProjectsWithTeamsAndRolesDTO
        project_with_teams_dto = ProjectsWithTeamsAndRolesDTO(
            total_projects_count=total_projects_count,
            project_dtos=projects_set_up,
            project_team_ids_dtos=project_teams_set_up,
            team_dtos=teams_set_up,
            project_role_dtos=project_roles_setup)

        http_response = presenter.get_response_for_get_projects(
            project_with_teams_dto=project_with_teams_dto)

        response = json.loads(http_response.content)

        snapshot.assert_match(response, "projects")

    def test_response_for_invalid_limit_exception(self):
        # Arrange
        from ib_iam.presenters.get_projects_presenter_implementation import (
            GetProjectsPresenterImplementation
        )
        presenter = GetProjectsPresenterImplementation()
        expected_response = INVALID_LIMIT_VALUE[0]
        expected_res_status = INVALID_LIMIT_VALUE[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.response_for_invalid_limit_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_response_for_invalid_offset_exception(self):
        # Arrange
        from ib_iam.presenters.get_projects_presenter_implementation import (
            GetProjectsPresenterImplementation
        )
        presenter = GetProjectsPresenterImplementation()
        expected_response = INVALID_OFFSET_VALUE[0]
        expected_res_status = INVALID_OFFSET_VALUE[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.response_for_invalid_offset_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_response_for_user_have_not_permission_exception(self):
        # Arrange
        from ib_iam.presenters.get_projects_presenter_implementation import (
            GetProjectsPresenterImplementation
        )
        presenter = GetProjectsPresenterImplementation()
        expected_response = USER_HAS_NO_ACCESS_TO_GET_PROJECTS[0]
        expected_res_status = USER_HAS_NO_ACCESS_TO_GET_PROJECTS[1]
        expected_http_status_code = StatusCode.FORBIDDEN.value

        # Act
        result = presenter.response_for_user_have_not_permission_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
