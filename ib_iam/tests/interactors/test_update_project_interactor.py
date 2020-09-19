import mock
import pytest
from ib_iam.interactors.dtos.dtos import CompleteProjectDetailsDTO


class TestUpdateProjectInteractor:
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
        from ib_iam.interactors.presenter_interfaces.project_presenter_interface import (
            UpdateProjectPresenterInterface
        )
        storage = mock.create_autospec(UpdateProjectPresenterInterface)
        return storage

    @pytest.fixture
    def interactor(self, project_storage, team_storage, user_storage):
        from ib_iam.interactors.project_interactor import ProjectInteractor
        interactor = ProjectInteractor(
            project_storage=project_storage, user_storage=user_storage,
            team_storage=team_storage
        )
        return interactor

    @pytest.fixture
    def roles(self):
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        RoleDTOFactory.reset_sequence(1)
        role_ids = ["role1", None]
        roles = [RoleDTOFactory(role_id=role_id) for role_id in role_ids]
        return roles

    @pytest.fixture
    def duplicate_roles(self):
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        RoleDTOFactory.reset_sequence(1)
        role_ids = ["role1", "role1"]
        roles = [RoleDTOFactory(role_id=role_id) for role_id in role_ids]
        return roles

    @pytest.fixture
    def roles_for_role_names_already_exists(self):
        roles_dictionary = [
            {"role_id": "role1", "name": "payment2"},
            {"role_id": "role2", "name": "payment3"}
        ]
        from ib_iam.interactors.storage_interfaces.dtos import RoleIdAndNameDTO
        roles = [
            RoleIdAndNameDTO(role_id=role["role_id"], name=role["name"])
            for role in roles_dictionary
        ]
        return roles

    def test_given_user_is_not_admin_returns_user_has_no_access_response(
            self, project_storage, user_storage, interactor, presenter
    ):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_dto = ProjectDTOFactory()
        user_id = "1"
        user_storage.is_user_admin.return_value = False
        presenter.response_for_invalid_project_id_exception.return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_dto.project_id,
            name=project_dto.name, description=project_dto.description,
            logo_url=project_dto.logo_url, team_ids=[], roles=[]
        )

        # Act
        interactor.update_project_wrapper(
            presenter=presenter, user_id=user_id,
            complete_project_details_dto=complete_project_details_dto
        )

        # Assert
        user_storage.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.response_for_user_has_no_access_exception.assert_called_once()

    def test_given_invalid_project_returns_invalid_project_response(
            self, project_storage, user_storage, interactor, presenter
    ):
        # Arrange
        user_id = "1"
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_dto = ProjectDTOFactory()
        user_storage.is_valid_project_id.return_value = False
        presenter.response_for_invalid_project_id_exception.return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_dto.project_id,
            name=project_dto.name, description=project_dto.description,
            logo_url=project_dto.logo_url, team_ids=[], roles=[]
        )

        # Act
        interactor.update_project_wrapper(
            presenter=presenter, user_id=user_id,
            complete_project_details_dto=complete_project_details_dto
        )

        # Assert
        user_storage.is_valid_project_id.assert_called_once_with(
            project_id=project_dto.project_id
        )
        presenter.response_for_invalid_project_id_exception.assert_called_once()

    def test_given_name_already_exists_returns_name_already_exists_response(
            self, project_storage, user_storage, interactor, presenter
    ):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        name = "name 1"
        user_id = "1"
        ProjectDTOFactory.reset_sequence(1)
        project_dto = ProjectDTOFactory(name=name)
        project_storage.get_project_id.return_value = "project 2"
        presenter.response_for_project_name_already_exists_exception \
            .return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_dto.project_id, name=project_dto.name,
            description=project_dto.description, logo_url=project_dto.logo_url,
            team_ids=[], roles=[]
        )

        # Act
        interactor.update_project_wrapper(
            presenter=presenter, user_id=user_id,
            complete_project_details_dto=complete_project_details_dto
        )

        # Assert
        project_storage.get_project_id.assert_called_once_with(name=name)
        presenter.response_for_project_name_already_exists_exception.assert_called_once()

    def test_given_duplicate_team_ids_returns_duplicate_team_ids_response(
            self, project_storage, user_storage, interactor, presenter
    ):
        # Arrange
        user_id = "1"
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_dto = ProjectDTOFactory()
        project_storage.get_project_id.return_value = None
        presenter.response_for_duplicate_team_ids_exception.return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_dto.project_id, name=project_dto.name,
            description=project_dto.description, logo_url=project_dto.logo_url,
            team_ids=["1", "1"], roles=[]
        )

        # Act
        interactor.update_project_wrapper(
            presenter=presenter, user_id=user_id,
            complete_project_details_dto=complete_project_details_dto
        )

        # Assert
        presenter.response_for_duplicate_team_ids_exception.assert_called_once()

    def test_given_invalid_team_ids_returns_invalid_team_ids_response(
            self, project_storage, user_storage, team_storage, interactor,
            presenter
    ):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_dto = ProjectDTOFactory()
        team_ids = ["1", "2"]
        valid_team_ids = ["1"]
        project_storage.get_project_id.return_value = None
        team_storage.get_valid_team_ids.return_value = valid_team_ids
        presenter.response_for_invalid_team_ids_exception.return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_dto.project_id, name=project_dto.name,
            description=project_dto.description, logo_url=project_dto.logo_url,
            team_ids=team_ids, roles=[]
        )

        # Act
        interactor.update_project_wrapper(
            presenter=presenter, user_id="1",
            complete_project_details_dto=complete_project_details_dto
        )

        # Assert
        team_storage.get_valid_team_ids.assert_called_once_with(
            team_ids=team_ids
        )
        presenter.response_for_invalid_team_ids_exception.assert_called_once()

    def test_given_duplicate_role_ids_returns_duplicate_role_ids_response(
            self, project_storage, user_storage, team_storage, interactor,
            presenter, duplicate_roles
    ):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_dto = ProjectDTOFactory()
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = RoleDTOFactory.create_batch(role_id="1", size=2)
        project_storage.get_project_id.return_value = None
        presenter.response_for_duplicate_role_ids_exception.return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_dto.project_id, name=project_dto.name,
            description=project_dto.description, logo_url=project_dto.logo_url,
            team_ids=[], roles=role_dtos
        )

        # Act
        interactor.update_project_wrapper(
            presenter=presenter, user_id="1",
            complete_project_details_dto=complete_project_details_dto
        )

        # Assert
        presenter.response_for_duplicate_role_ids_exception.assert_called_once()

    def test_given_invalid_role_ids_returns_invalid_role_ids_response(
            self, project_storage, user_storage, team_storage, interactor,
            presenter, roles
    ):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_id = "project_1"
        project_dto = ProjectDTOFactory(project_id=project_id)
        role_ids = ["4", "5"]
        project_storage.get_project_id.return_value = None
        project_storage.get_project_role_ids.return_value = role_ids
        presenter.response_for_invalid_role_ids_exception.return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_dto.project_id, name=project_dto.name,
            description=project_dto.description, logo_url=project_dto.logo_url,
            team_ids=[], roles=roles
        )

        # Act
        interactor.update_project_wrapper(
            presenter=presenter, user_id="1",
            complete_project_details_dto=complete_project_details_dto
        )

        # Assert
        presenter.response_for_invalid_role_ids_exception.assert_called_once()

    def test_given_duplicate_role_names_returns_duplicate_role_names_response(
            self, project_storage, user_storage, team_storage, interactor,
            presenter
    ):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import (
            ProjectDTOFactory, RoleDTOFactory)
        project_id = "project_1"
        project_dto = ProjectDTOFactory(project_id=project_id)
        team_ids = ["1", "2"]
        role_ids = ["1", "2"]
        roles = [RoleDTOFactory.create(role_id=role_id, name="role 1")
                 for role_id in role_ids]
        project_storage.get_project_id.return_value = None
        project_storage.get_project_role_ids.return_value = role_ids
        team_storage.get_valid_team_ids.return_value = team_ids
        presenter.response_for_duplicate_role_names_exception \
            .return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_dto.project_id,
            name=project_dto.name,
            description=project_dto.description,
            logo_url=project_dto.logo_url,
            team_ids=team_ids,
            roles=roles)

        # Act
        interactor.update_project_wrapper(
            presenter=presenter, user_id="1",
            complete_project_details_dto=complete_project_details_dto
        )

        # Assert
        presenter.response_for_duplicate_role_names_exception.assert_called_once()

    def test_given_role_names_already_exists_returns_role_names_already_exists_response(
            self, project_storage, user_storage, team_storage, interactor,
            presenter, roles, roles_for_role_names_already_exists
    ):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_id = "project_1"
        project_dto = ProjectDTOFactory(project_id=project_id)
        team_ids = ["1", "2"]
        role_ids = ["role1", "role2"]
        expected_names_that_already_exists = ['payment2']
        project_storage.get_project_id.return_value = None
        project_storage.get_project_role_ids.return_value = role_ids
        team_storage.get_valid_team_ids.return_value = team_ids
        user_storage.get_roles.return_value = roles_for_role_names_already_exists
        presenter.response_for_role_names_already_exists_exception \
            .return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_dto.project_id,
            name=project_dto.name, description=project_dto.description,
            logo_url=project_dto.logo_url, team_ids=team_ids, roles=roles
        )

        # Act
        interactor.update_project_wrapper(
            presenter=presenter, user_id="1",
            complete_project_details_dto=complete_project_details_dto
        )

        # Assert
        user_storage.get_roles.assert_called_once()
        call_args = presenter.response_for_role_names_already_exists_exception.call_args
        error_obj = call_args[0][0]
        actual_names_that_already_exists = error_obj.role_names
        assert actual_names_that_already_exists == \
               expected_names_that_already_exists

    def test_update_project_returns_success_response(
            self, project_storage, user_storage, team_storage, interactor,
            presenter, roles
    ):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_id = "1"
        ProjectDTOFactory.reset_sequence(1)
        project_dto = ProjectDTOFactory(project_id=project_id)
        team_ids = ["1", "2"]
        team_ids_from_db = ["1", "3"]
        team_ids_to_add = ["2"]
        team_ids_to_be_removed = ["3"]
        user_storage.is_valid_project_id.return_value = True
        project_storage.get_project_id.return_value = None
        team_storage.get_valid_team_ids.return_value = team_ids
        project_storage.get_team_ids.return_value = team_ids_from_db
        role_ids_from_db = ["role1", "role2"]
        roles_to_be_updated = [roles[0]]
        role_ids_to_be_deleted = ["role2"]
        from ib_iam.interactors.storage_interfaces.dtos import (
            UserIdAndTeamIdsDTO
        )
        user_id_and_team_ids_dtos = [
            UserIdAndTeamIdsDTO(user_id="1", team_ids=["1", "2", "3"]),
            UserIdAndTeamIdsDTO(user_id="2", team_ids=["3"])
        ]
        user_ids = ["2"]
        from ib_iam.interactors.storage_interfaces.dtos import (
            RoleNameAndDescriptionDTO
        )
        roles_to_be_created = [
            RoleNameAndDescriptionDTO(
                name=roles[1].name, description=roles[1].description
            )
        ]
        project_storage.get_project_role_ids.return_value = role_ids_from_db
        project_storage.get_user_id_with_teams_ids_dtos.return_value = \
            user_id_and_team_ids_dtos
        presenter.get_success_response_for_update_project.return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_dto.project_id, name=project_dto.name,
            description=project_dto.description, logo_url=project_dto.logo_url,
            team_ids=team_ids, roles=roles
        )

        # Act
        interactor.update_project_wrapper(
            presenter=presenter, user_id="1",
            complete_project_details_dto=complete_project_details_dto
        )

        # Assert
        project_storage.update_project.assert_called_once_with(
            project_dto=project_dto
        )
        project_storage.get_team_ids.assert_called_once_with(
            project_id=project_id
        )
        project_storage.assign_teams_to_projects.assert_called_once_with(
            project_id=project_id, team_ids=team_ids_to_add
        )
        project_storage.remove_teams.assert_called_once_with(
            project_id=project_id, team_ids=team_ids_to_be_removed
        )
        project_storage.get_user_id_with_teams_ids_dtos.assert_called_once_with(
            project_id=project_id
        )
        project_storage.remove_user_roles.assert_called_once_with(
            project_id=project_id, user_ids=user_ids
        )
        project_storage.add_project_roles.assert_called_once_with(
            project_id=project_id, roles=roles_to_be_created
        )
        project_storage.update_project_roles.assert_called_once_with(
            roles=roles_to_be_updated
        )
        project_storage.delete_project_roles.assert_called_once_with(
            role_ids=role_ids_to_be_deleted
        )
        presenter.get_success_response_for_update_project.assert_called_once()
