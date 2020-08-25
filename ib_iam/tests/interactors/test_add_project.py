import mock
import pytest


class TestAddProjectIneractor:

    @pytest.fixture
    def project_storage(self):
        from ib_iam.interactors.storage_interfaces.project_storage_interface import \
            ProjectStorageInterface
        storage = mock.create_autospec(ProjectStorageInterface)
        return storage

    @pytest.fixture
    def user_storage(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def team_storage(self):
        from ib_iam.interactors.storage_interfaces.team_storage_interface import \
            TeamStorageInterface
        storage = mock.create_autospec(TeamStorageInterface)
        return storage

    @pytest.fixture
    def presenter(self):
        from ib_iam.interactors.presenter_interfaces.add_project_presenter_interface import \
            AddProjectPresenterInterface
        storage = mock.create_autospec(AddProjectPresenterInterface)
        return storage

    @pytest.fixture
    def interactor(self, project_storage, team_storage, user_storage):
        from ib_iam.interactors.project_interactor import ProjectInteractor
        interactor = ProjectInteractor(project_storage=project_storage,
                                       user_storage=user_storage,
                                       team_storage=team_storage)
        return interactor

    def test_add_project_returns_project_id_in_success_response(
            self, project_storage, interactor, presenter):
        from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
        from ib_iam.tests.factories.storage_dtos import \
            ProjectWithoutIdDTOFactory, RoleDTOFactory
        ProjectWithoutIdDTOFactory.reset_sequence(1)
        project_details = ProjectWithoutIdDTOFactory()
        project_id = "1"
        team_ids = ["1"]
        roles = [RoleDTOFactory()]
        project_storage.add_project.return_value = project_id
        presenter.get_success_response_for_add_project \
            .return_value = mock.Mock()
        project_with_team_ids_and_roles_dto = ProjectWithTeamIdsAndRolesDTO(
            name=project_details.name,
            description=project_details.description,
            logo_url=project_details.logo_url,
            team_ids=team_ids,
            roles=roles)

        interactor.add_project_wrapper(presenter=presenter,
                                       project_with_team_ids_and_roles_dto=
                                       project_with_team_ids_and_roles_dto)

        project_storage.add_project.assert_called_once_with(
            project_without_id_dto=project_details)
        project_storage.assign_teams_to_projects.assert_called_once_with(
            project_id=project_id, team_ids=team_ids)
        project_storage.add_project_roles.assert_called_once_with(
            project_id=project_id, roles=roles)
