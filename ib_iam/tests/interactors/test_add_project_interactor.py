import mock
import pytest


class TestAddProjectInteractor:
    @pytest.fixture
    def project_storage(self):
        from ib_iam.interactors.storage_interfaces.project_storage_interface import (
            ProjectStorageInterface
        )
        storage = mock.create_autospec(ProjectStorageInterface)
        return storage

    @pytest.fixture
    def user_storage(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import (
            UserStorageInterface
        )
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def team_storage(self):
        from ib_iam.interactors.storage_interfaces.team_storage_interface import (
            TeamStorageInterface
        )
        storage = mock.create_autospec(TeamStorageInterface)
        return storage

    @pytest.fixture
    def presenter(self):
        from ib_iam.interactors.presenter_interfaces.add_project_presenter_interface import (
            AddProjectPresenterInterface
        )
        storage = mock.create_autospec(AddProjectPresenterInterface)
        return storage

    @pytest.fixture
    def interactor(self, project_storage, team_storage, user_storage):
        from ib_iam.interactors.project_interactor import ProjectInteractor
        interactor = ProjectInteractor(
            project_storage=project_storage,
            user_storage=user_storage, team_storage=team_storage
        )
        return interactor

    def test_given_user_is_not_admin_returns_user_has_no_access_response(
            self, project_storage, user_storage, interactor, presenter
    ):
        from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
        from ib_iam.tests.factories.storage_dtos import (
            ProjectWithoutIdDTOFactory
        )
        ProjectWithoutIdDTOFactory.reset_sequence(0)
        project_details = ProjectWithoutIdDTOFactory()
        user_id = "1"
        user_storage.is_user_admin.return_value = False
        presenter.get_user_has_no_access_response.return_value = mock.Mock()
        project_with_team_ids_and_roles_dto = ProjectWithTeamIdsAndRolesDTO(
            name=project_details.name, display_id=project_details.display_id,
            description=project_details.description,
            logo_url=project_details.logo_url, team_ids=[], roles=[]
        )

        interactor.add_project_wrapper(
            presenter=presenter, user_id=user_id,
            project_with_team_ids_and_roles_dto=project_with_team_ids_and_roles_dto
        )

        user_storage.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response.assert_called_once()

    def test_given_name_already_exists_returns_name_already_exists_response(
            self, project_storage, interactor, presenter
    ):
        from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
        from ib_iam.tests.factories.storage_dtos import \
            ProjectWithoutIdDTOFactory
        name = "project_1"
        user_id = "1"
        project_details = ProjectWithoutIdDTOFactory(name=name)
        project_storage.get_project_id.return_value = "project_2"
        presenter.get_project_name_already_exists_response.return_value = mock.Mock()
        project_with_team_ids_and_roles_dto = ProjectWithTeamIdsAndRolesDTO(
            name=project_details.name, display_id=project_details.display_id,
            description=project_details.description,
            logo_url=project_details.logo_url, team_ids=[], roles=[]
        )

        interactor.add_project_wrapper(
            presenter=presenter, user_id=user_id,
            project_with_team_ids_and_roles_dto=project_with_team_ids_and_roles_dto
        )

        project_storage.get_project_id.assert_called_once_with(name=name)
        presenter.get_project_name_already_exists_response.assert_called_once()

    def test_given_display_id_already_exists_returns_display_id_already_exists_response(
            self, project_storage, interactor, presenter
    ):
        from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
        from ib_iam.tests.factories.storage_dtos import (
            ProjectWithoutIdDTOFactory
        )
        display_id = "display_id 1"
        user_id = "1"
        project_details = ProjectWithoutIdDTOFactory(display_id=display_id)
        project_storage.get_project_id.return_value = None
        project_storage.is_exists_display_id.return_value = True
        presenter.get_project_display_id_already_exists_response.return_value = mock.Mock()
        project_with_team_ids_and_roles_dto = ProjectWithTeamIdsAndRolesDTO(
            name=project_details.name, display_id=project_details.display_id,
            description=project_details.description,
            logo_url=project_details.logo_url, team_ids=[], roles=[]
        )

        interactor.add_project_wrapper(
            presenter=presenter, user_id=user_id,
            project_with_team_ids_and_roles_dto=project_with_team_ids_and_roles_dto
        )

        project_storage.get_project_id.assert_called_once_with(
            name=project_details.name
        )
        project_storage.is_exists_display_id.assert_called_once_with(
            display_id=display_id
        )
        presenter.get_project_display_id_already_exists_response.assert_called_once()

    def test_given_duplicate_team_ids_returns_duplicate_team_ids_response(
            self, project_storage, team_storage, interactor, presenter
    ):
        from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
        from ib_iam.tests.factories.storage_dtos import (
            ProjectWithoutIdDTOFactory
        )
        team_ids = ["1", "1"]
        project_details = ProjectWithoutIdDTOFactory()
        project_storage.get_project_id.return_value = None
        project_storage.is_exists_display_id.return_value = False
        presenter.get_duplicate_team_ids_response.return_value = mock.Mock()
        project_with_team_ids_and_roles_dto = ProjectWithTeamIdsAndRolesDTO(
            name=project_details.name, display_id=project_details.display_id,
            description=project_details.description,
            logo_url=project_details.logo_url, team_ids=team_ids, roles=[]
        )

        interactor.add_project_wrapper(
            presenter=presenter, user_id="1",
            project_with_team_ids_and_roles_dto=project_with_team_ids_and_roles_dto
        )

        project_storage.get_project_id.assert_called_once_with(
            name=project_details.name
        )
        project_storage.is_exists_display_id.assert_called_once_with(
            display_id=project_details.display_id
        )
        presenter.get_duplicate_team_ids_response.assert_called_once()

    def test_given_invalid_team_ids_returns_invalid_team_ids_response(
            self, project_storage, team_storage, interactor, presenter):
        from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
        from ib_iam.tests.factories.storage_dtos import \
            ProjectWithoutIdDTOFactory
        team_ids = ["1", "2"]
        valid_team_ids = ["1"]
        user_id = "1"
        project_details = ProjectWithoutIdDTOFactory()
        project_storage.get_project_id.return_value = None
        project_storage.is_exists_display_id.return_value = False
        team_storage.get_valid_team_ids.return_value = valid_team_ids
        presenter.get_invalid_team_ids_response.return_value = mock.Mock()
        project_with_team_ids_and_roles_dto = ProjectWithTeamIdsAndRolesDTO(
            name=project_details.name, display_id=project_details.display_id,
            description=project_details.description,
            logo_url=project_details.logo_url, team_ids=team_ids, roles=[]
        )

        interactor.add_project_wrapper(
            presenter=presenter, user_id=user_id,
            project_with_team_ids_and_roles_dto=project_with_team_ids_and_roles_dto
        )

        project_storage.get_project_id.assert_called_once_with(
            name=project_details.name
        )
        project_storage.is_exists_display_id.assert_called_once_with(
            display_id=project_details.display_id
        )
        team_storage.get_valid_team_ids.assert_called_once_with(
            team_ids=team_ids
        )
        presenter.get_invalid_team_ids_response.assert_called_once()

    def test_given_duplicate_role_names_returns_duplicate_role_names_response(
            self, project_storage, team_storage, interactor, presenter
    ):
        from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
        from ib_iam.tests.factories.storage_dtos import (
            ProjectWithoutIdDTOFactory, RoleNameAndDescriptionDTOFactory
        )
        team_ids = ["1", "2"]
        user_id = "1"
        project_details = ProjectWithoutIdDTOFactory()
        roles = RoleNameAndDescriptionDTOFactory.create_batch(
            size=2, name="role 1"
        )
        project_storage.get_project_id.return_value = None
        project_storage.is_exists_display_id.return_value = False
        team_storage.get_valid_team_ids.return_value = team_ids
        presenter.get_duplicate_role_names_response.return_value = mock.Mock()
        project_with_team_ids_and_roles_dto = ProjectWithTeamIdsAndRolesDTO(
            name=project_details.name, display_id=project_details.display_id,
            description=project_details.description,
            logo_url=project_details.logo_url, team_ids=team_ids, roles=roles
        )

        interactor.add_project_wrapper(
            presenter=presenter, user_id=user_id,
            project_with_team_ids_and_roles_dto=project_with_team_ids_and_roles_dto
        )

        project_storage.get_project_id.assert_called_once_with(
            name=project_details.name
        )
        project_storage.is_exists_display_id.assert_called_once_with(
            display_id=project_details.display_id
        )
        team_storage.get_valid_team_ids.assert_called_once_with(
            team_ids=team_ids)
        presenter.get_duplicate_role_names_response.assert_called_once()

    def test_given_existing_role_names_returns_role_names_already_exists_response(
            self, project_storage, team_storage, interactor, presenter
    ):
        from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
        from ib_iam.tests.factories.storage_dtos import (
            ProjectWithoutIdDTOFactory, RoleNameAndDescriptionDTOFactory
        )
        team_ids = ["1", "2"]
        user_id = "1"
        project_details = ProjectWithoutIdDTOFactory()
        role_names = ["role 1"]
        roles = [
            RoleNameAndDescriptionDTOFactory(name=name) for name in role_names
        ]
        project_storage.get_project_id.return_value = None
        project_storage.is_exists_display_id.return_value = False
        team_storage.get_valid_team_ids.return_value = team_ids
        project_storage.get_valid_role_names.return_value = role_names
        presenter.get_role_names_already_exists_response.return_value = mock.Mock()
        project_with_team_ids_and_roles_dto = ProjectWithTeamIdsAndRolesDTO(
            name=project_details.name, display_id=project_details.display_id,
            description=project_details.description,
            logo_url=project_details.logo_url, team_ids=team_ids, roles=roles)

        interactor.add_project_wrapper(
            presenter=presenter, user_id=user_id,
            project_with_team_ids_and_roles_dto=project_with_team_ids_and_roles_dto
        )

        project_storage.get_project_id.assert_called_once_with(
            name=project_details.name
        )
        project_storage.is_exists_display_id.assert_called_once_with(
            display_id=project_details.display_id
        )
        team_storage.get_valid_team_ids.assert_called_once_with(
            team_ids=team_ids
        )
        project_storage.get_valid_role_names.assert_called_once_with(
            role_names=role_names
        )
        call_args = presenter.get_role_names_already_exists_response.call_args
        error_obj = call_args[0][0]
        actual_role_names_from_exception = error_obj.role_names
        assert actual_role_names_from_exception == role_names

    def test_add_project_returns_in_success_response(
            self, project_storage, team_storage, interactor, presenter
    ):
        from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
        from ib_iam.tests.factories.storage_dtos import \
            ProjectWithoutIdDTOFactory, RoleDTOFactory
        ProjectWithoutIdDTOFactory.reset_sequence(1)
        project_details = ProjectWithoutIdDTOFactory()
        project_id = "1"
        team_ids = ["1"]
        user_id = "1"
        roles = [RoleDTOFactory()]
        project_storage.get_project_id.return_value = None
        project_storage.is_exists_display_id.return_value = False
        team_storage.get_valid_team_ids.return_value = team_ids
        project_storage.get_valid_role_names.return_value = []
        project_storage.add_project.return_value = project_id
        presenter.get_success_response_for_add_project.return_value = mock.Mock()
        project_with_team_ids_and_roles_dto = ProjectWithTeamIdsAndRolesDTO(
            name=project_details.name, display_id=project_details.display_id,
            description=project_details.description,
            logo_url=project_details.logo_url, team_ids=team_ids, roles=roles
        )

        interactor.add_project_wrapper(
            presenter=presenter, user_id=user_id,
            project_with_team_ids_and_roles_dto=project_with_team_ids_and_roles_dto
        )

        project_storage.get_project_id.assert_called_once_with(
            name=project_details.name
        )
        project_storage.is_exists_display_id.assert_called_once_with(
            display_id=project_details.display_id
        )
        team_storage.get_valid_team_ids.assert_called_once_with(
            team_ids=team_ids
        )
        project_storage.add_project.assert_called_once_with(
            project_without_id_dto=project_details
        )
        project_storage.assign_teams_to_projects.assert_called_once_with(
            project_id=project_id, team_ids=team_ids
        )
        project_storage.add_project_roles.assert_called_once_with(
            project_id=project_id, roles=roles
        )
        presenter.get_success_response_for_add_project.assert_called_once()
