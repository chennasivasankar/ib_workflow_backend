import mock
import pytest


class TestAddProjectsInteractor:

    @pytest.fixture
    def project_storage(self):
        from ib_iam.interactors.storage_interfaces \
            .project_storage_interface import ProjectStorageInterface
        project_storage = mock.create_autospec(ProjectStorageInterface)
        return project_storage

    @pytest.fixture
    def user_storage(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        return mock.create_autospec(UserStorageInterface)

    @pytest.fixture
    def team_storage(self):
        from ib_iam.interactors.storage_interfaces \
            .team_storage_interface import TeamStorageInterface
        project_storage = mock.create_autospec(TeamStorageInterface)
        return project_storage

    @pytest.fixture
    def presenter(self):
        from ib_iam.interactors.presenter_interfaces \
            .get_projects_presenter_interface import \
            GetProjectsPresenterInterface
        presenter = mock.create_autospec(GetProjectsPresenterInterface)
        return presenter

    @pytest.fixture
    def interactor(self, project_storage, team_storage, user_storage):
        from ib_iam.interactors.get_projects_interactor import \
            GetProjectsInteractor
        interactor = GetProjectsInteractor(
            project_storage=project_storage, team_storage=team_storage,
            user_storage=user_storage
        )
        return interactor

    @pytest.fixture
    def expected_list_of_project_dtos(self):
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        ProjectDTOFactory.reset_sequence(1)
        project_dtos = [ProjectDTOFactory(project_id="1")]
        return project_dtos

    @pytest.fixture()
    def expected_project_team_ids_dtos(self):
        from ib_iam.interactors.storage_interfaces.dtos import \
            ProjectTeamIdsDTO
        project_team_ids_dtos = [
            ProjectTeamIdsDTO(project_id="1", team_ids=["2"])]
        return project_team_ids_dtos

    @pytest.fixture
    def expected_list_of_team_dtos(self):
        from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
        TeamDTOFactory.reset_sequence(2)
        team_dtos = [TeamDTOFactory() for _ in range(1)]
        return team_dtos

    @pytest.fixture
    def expected_project_role_dtos(self):
        from ib_iam.tests.factories.storage_dtos import ProjectRoleDTOFactory
        ProjectRoleDTOFactory.reset_sequence(1)
        project_role_dtos = [ProjectRoleDTOFactory() for _ in range(2)]
        return project_role_dtos

    @pytest.fixture
    def pagination_dto(self):
        from ib_iam.tests.factories.storage_dtos import PaginationDTOFactory
        return PaginationDTOFactory()

    # TODO: Use assert_called_with
    def test_get_projects_returns_projects_response(
            self, project_storage, interactor, presenter, team_storage,
            expected_list_of_project_dtos, expected_project_team_ids_dtos,
            expected_list_of_team_dtos, expected_project_role_dtos,
            pagination_dto, user_storage
    ):
        # Arrange
        project_ids = ["1"]
        team_ids = ["2"]
        user_id = "1"
        total_projects_count = 1
        from ib_iam.interactors.storage_interfaces.dtos import (
            ProjectsWithTotalCountDTO
        )
        project_storage.get_projects_with_total_count_dto.return_value = \
            ProjectsWithTotalCountDTO(
                projects=expected_list_of_project_dtos,
                total_projects_count=total_projects_count
            )
        user_storage.is_user_admin.return_value = True
        project_storage.get_project_team_ids_dtos \
            .return_value = expected_project_team_ids_dtos
        team_storage.get_team_dtos.return_value = expected_list_of_team_dtos
        project_storage.get_all_project_roles.return_value = expected_project_role_dtos
        from ib_iam.interactors.presenter_interfaces.dtos import \
            ProjectsWithTeamsAndRolesDTO
        project_with_teams_dto = ProjectsWithTeamsAndRolesDTO(
            total_projects_count=total_projects_count,
            project_dtos=expected_list_of_project_dtos,
            project_team_ids_dtos=expected_project_team_ids_dtos,
            team_dtos=expected_list_of_team_dtos,
            project_role_dtos=expected_project_role_dtos)
        presenter.get_response_for_get_projects.return_value = mock.Mock()

        # Act
        interactor.get_projects_wrapper(
            presenter=presenter, pagination_dto=pagination_dto, user_id=user_id
        )

        # Assert
        project_storage.get_projects_with_total_count_dto \
            .assert_called_once_with(pagination_dto=pagination_dto)
        project_storage.get_project_team_ids_dtos.assert_called_once_with(
            project_ids)
        team_storage.get_team_dtos.assert_called_once_with(team_ids)
        project_storage.get_all_project_roles.assert_called_once()
        presenter.get_response_for_get_projects.assert_called_once_with(
            project_with_teams_dto=project_with_teams_dto)

    def test_with_user_not_admin_returns_unauthorized_response(
            self, project_storage, interactor, presenter, team_storage,
            user_storage, pagination_dto
    ):
        # Arrange
        user_id = "1"
        user_storage.is_user_admin.return_value = False
        presenter.response_for_user_have_not_permission_exception \
            .return_value = mock.Mock()

        # Act
        interactor.get_projects_wrapper(
            user_id=user_id, pagination_dto=pagination_dto, presenter=presenter
        )

        # Assert
        user_storage.is_user_admin.assert_called_once_with(
            user_id=user_id)
        presenter.response_for_user_have_not_permission_exception \
            .assert_called_once()

    def test_invalid_limit_returns_invalid_limit_response(
            self, project_storage, interactor, presenter, team_storage,
            user_storage, pagination_dto
    ):
        # Arrange
        pagination_dto.limit = -1
        user_id = "1"
        presenter.response_for_invalid_limit_exception.return_value = mock.Mock()

        # Act
        interactor.get_projects_wrapper(
            user_id=user_id, pagination_dto=pagination_dto, presenter=presenter
        )

        # Arrange
        presenter.response_for_invalid_limit_exception.assert_called_once()

    def test_invalid_offset_returns_invalid_offset_response(
            self, project_storage, interactor, presenter, team_storage,
            user_storage, pagination_dto
    ):
        # Arrange
        pagination_dto.offset = -1
        user_id = "1"
        presenter.response_for_invalid_offset_exception.return_value = mock.Mock()

        # Act
        interactor.get_projects_wrapper(
            user_id=user_id, pagination_dto=pagination_dto, presenter=presenter
        )

        # Arrange
        presenter.response_for_invalid_offset_exception.assert_called_once()
