import mock
import pytest


class TestUpdateProjectIneractor:

    @pytest.fixture
    def project_storage(self):
        from ib_iam.interactors.storage_interfaces \
            .project_storage_interface import ProjectStorageInterface
        storage = mock.create_autospec(ProjectStorageInterface)
        return storage

    @pytest.fixture
    def user_storage(self):
        from ib_iam.interactors.storage_interfaces \
            .user_storage_interface import UserStorageInterface
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def team_storage(self):
        from ib_iam.interactors.storage_interfaces \
            .team_storage_interface import TeamStorageInterface
        storage = mock.create_autospec(TeamStorageInterface)
        return storage

    @pytest.fixture
    def presenter(self):
        from ib_iam.interactors.presenter_interfaces.update_project_presenter_interface import \
            UpdateProjectPresenterInterface
        storage = mock.create_autospec(UpdateProjectPresenterInterface)
        return storage

    @pytest.fixture
    def interactor(self, project_storage, team_storage, user_storage):
        from ib_iam.interactors.project_interactor import ProjectInteractor
        interactor = ProjectInteractor(project_storage=project_storage,
                                       user_storage=user_storage,
                                       team_storage=team_storage)
        return interactor

    @pytest.fixture
    def roles(self):
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_ids = ["role1", None]
        roles = [RoleDTOFactory(role_id=role_id) for role_id in role_ids]
        return roles

    # todo remove it while removing transaction tag update_project interactor
    @pytest.mark.django_db
    def test_update_project_returns_success_response(
            self, project_storage, interactor, presenter, roles):
        from ib_iam.interactors.dtos.dtos import CompleteProjectDetailsDTO
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_id = "1"
        ProjectDTOFactory.reset_sequence(1)
        project_dto = ProjectDTOFactory(project_id=project_id)
        team_ids = ["1", "2"]
        team_ids_from_db = ["1", "3"]
        team_ids_to_add = ["2"]
        team_ids_to_be_removed = ["3"]
        project_storage.get_valid_team_ids.return_value = team_ids_from_db
        role_ids_from_db = ["role1", "role2"]
        roles_to_be_updated = [roles[0]]
        role_ids_to_be_deleted = ["role2"]
        from ib_iam.interactors.storage_interfaces.dtos import \
            UserIdAndTeamIdsDTO
        user_id_and_team_ids_dtos = [
            UserIdAndTeamIdsDTO(user_id="1", team_ids=["1", "2", "3"]),
            UserIdAndTeamIdsDTO(user_id="2", team_ids=["3"])
        ]
        user_ids = ["2"]
        from ib_iam.interactors.storage_interfaces.dtos import \
            RoleNameAndDescriptionDTO
        roles_to_be_created = [RoleNameAndDescriptionDTO(
            name=roles[1].name, description=roles[1].description)]
        project_storage.get_project_role_ids.return_value = role_ids_from_db
        project_storage.get_user_team_ids_dtos_for_given_project \
            .return_value = user_id_and_team_ids_dtos
        presenter.get_success_response_for_update_project \
            .return_value = mock.Mock()
        complete_project_details_dto = CompleteProjectDetailsDTO(
            project_id=project_id,
            name=project_dto.name,
            description=project_dto.description,
            logo_url=project_dto.logo_url,
            team_ids=team_ids,
            roles=roles)

        interactor.update_project_wrapper(
            presenter=presenter,
            complete_project_details_dto=complete_project_details_dto)

        project_storage.update_project.assert_called_once_with(
            project_dto=project_dto)
        project_storage.get_valid_team_ids.assert_called_once_with(
            project_id=project_id)
        project_storage.assign_teams_to_projects.assert_called_once_with(
            project_id=project_id, team_ids=team_ids_to_add)
        project_storage.remove_teams_from_project.assert_called_once_with(
            project_id=project_id, team_ids=team_ids_to_be_removed)
        project_storage.get_user_team_ids_dtos_for_given_project \
            .assert_called_once_with(project_id=project_id)
        project_storage.remove_user_roles_related_to_given_project_and_user \
            .assert_called_once_with(project_id=project_id, user_ids=user_ids)
        project_storage.add_project_roles.assert_called_once_with(
            project_id=project_id, roles=roles_to_be_created)
        project_storage.update_project_roles.assert_called_once_with(
            roles=roles_to_be_updated)
        project_storage.delete_project_roles.assert_called_once_with(
            role_ids=role_ids_to_be_deleted)
        presenter.get_success_response_for_update_project.assert_called_once()
