import mock
import pytest

from ib_iam.interactors.project_interactor import ProjectInteractor
from ib_iam.storages.project_storage_implementation import \
    ProjectStorageImplementation
from ib_iam.tests.factories.adapter_dtos import ProjectTeamUserDTOFactory


class TestGetTeamDetailsForGivenProjectTeamUserDetailsDto:

    def test_given_invalid_project_raises_invalid_project_exception(self):
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        project_storage = mock.create_autospec(ProjectStorageImplementation)
        interactor = ProjectInteractor(project_storage=project_storage)
        project_id = "1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id)
        project_storage \
            .get_valid_project_ids_from_given_project_ids \
            .return_value = []

        with pytest.raises(InvalidProjectId):
            interactor \
                .get_team_details_for_given_project_team_user_details_dto(
                project_team_user_dto=project_team_user_dto)

        project_storage.get_valid_project_ids_from_given_project_ids \
            .assert_called_once_with(project_ids=[project_id])

    def test_given_team_not_exists_in_project_raises_team_not_exists_exception(
            self):
        from ib_iam.exceptions.custom_exceptions import \
            TeamNotExistsInGivenProject
        project_storage = mock.create_autospec(ProjectStorageImplementation)
        interactor = ProjectInteractor(project_storage=project_storage)
        project_id = "1"
        team_id = "1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id, team_id=team_id)
        project_storage.get_valid_project_ids_from_given_project_ids \
            .return_value = [project_id]
        project_storage.is_team_exists_in_project.return_value = False

        with pytest.raises(TeamNotExistsInGivenProject):
            interactor \
                .get_team_details_for_given_project_team_user_details_dto(
                project_team_user_dto=project_team_user_dto)

        project_storage.get_valid_project_ids_from_given_project_ids \
            .assert_called_once_with(project_ids=[project_id])
        project_storage.is_team_exists_in_project.assert_called_once_with(
            project_id=project_id, team_id=team_id)

    def test_user_not_exists_in_team_raises_user_not_exists__in_team_exception(
            self):
        from ib_iam.exceptions.custom_exceptions import \
            UserNotExistsInGivenTeam
        project_storage = mock.create_autospec(ProjectStorageImplementation)
        interactor = ProjectInteractor(project_storage=project_storage)
        project_id = "1"
        team_id = "1"
        user_id = "1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id, team_id=team_id, user_id=user_id)
        project_storage.get_valid_project_ids_from_given_project_ids \
            .return_value = [project_id]
        project_storage.is_user_exists_in_team.return_value = False

        with pytest.raises(UserNotExistsInGivenTeam):
            interactor \
                .get_team_details_for_given_project_team_user_details_dto(
                project_team_user_dto=project_team_user_dto)

        project_storage.get_valid_project_ids_from_given_project_ids \
            .assert_called_once_with(project_ids=[project_id])
        project_storage.is_team_exists_in_project.assert_called_once_with(
            project_id=project_id, team_id=team_id)
        project_storage.is_user_exists_in_team.assert_called_once_with(
            team_id=team_id, user_id=user_id)

    def test_given_valid_details_returns_user_id_with_team_id_and_name_dto(
            self):
        project_storage = mock.create_autospec(ProjectStorageImplementation)
        interactor = ProjectInteractor(project_storage=project_storage)
        project_id = "1"
        team_id = "1"
        user_id = "1"
        name = "team1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id, team_id=team_id, user_id=user_id)
        project_storage.get_valid_project_ids_from_given_project_ids \
            .return_value = [project_id]
        project_storage.get_team_name.return_value = name
        from ib_iam.app_interfaces.dtos import UserIdWithTeamIDAndNameDTO
        expected_user_id_with_team_id_and_name_dto = \
            UserIdWithTeamIDAndNameDTO(user_id=user_id,
                                       team_id=team_id,
                                       name=name)

        actual_user_id_with_team_id_and_name_dto = interactor \
            .get_team_details_for_given_project_team_user_details_dto(
            project_team_user_dto=project_team_user_dto)

        project_storage.get_valid_project_ids_from_given_project_ids \
            .assert_called_once_with(project_ids=[project_id])
        project_storage.is_team_exists_in_project.assert_called_once_with(
            project_id=project_id, team_id=team_id)
        project_storage.is_user_exists_in_team.assert_called_once_with(
            team_id=team_id, user_id=user_id)
        project_storage.get_team_name.assert_called_once_with(team_id=team_id)
        assert actual_user_id_with_team_id_and_name_dto == \
               expected_user_id_with_team_id_and_name_dto
