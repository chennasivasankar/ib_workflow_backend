import mock
import pytest

from ib_iam.interactors.project_interactor import ProjectInteractor
from ib_iam.tests.factories.adapter_dtos import ProjectTeamUserDTOFactory


class TestGetTeamDetailsForGivenProjectTeamUserDetailsDTO:

    @pytest.fixture
    def project_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.project_storage_interface import \
            ProjectStorageInterface
        return mock.create_autospec(ProjectStorageInterface)

    @pytest.fixture
    def user_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        return mock.create_autospec(UserStorageInterface)

    @pytest.fixture
    def team_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.team_storage_interface import \
            TeamStorageInterface
        return mock.create_autospec(TeamStorageInterface)

    @pytest.fixture
    def init_interactor(
            self, project_storage_mock, user_storage_mock, team_storage_mock):
        return ProjectInteractor(
            project_storage=project_storage_mock,
            user_storage=user_storage_mock,
            team_storage=team_storage_mock
        )

    def test_given_invalid_project_raises_invalid_project_exception(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock):
        interactor = init_interactor
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        project_id = "1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id)
        project_storage_mock.get_valid_project_ids.return_value = []

        with pytest.raises(InvalidProjectId):
            interactor.get_team_details_for_given_project_team_user_details_dto(
                project_team_user_dto=project_team_user_dto)

        project_storage_mock.get_valid_project_ids \
            .assert_called_once_with(project_ids=[project_id])

    def test_given_invalid_team_raises_invalid_team_exception(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock):
        interactor = init_interactor
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        project_id = "1"
        team_id = "1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id, team_id=team_id)
        project_storage_mock.get_valid_project_ids.return_value = [project_id]
        team_storage_mock.is_team_exist.return_value = False

        with pytest.raises(InvalidTeamId):
            interactor.get_team_details_for_given_project_team_user_details_dto(
                project_team_user_dto=project_team_user_dto)

        team_storage_mock.is_team_exist.assert_called_once_with(
            team_id=team_id)

    def test_given_team_not_exists_in_project_raises_team_not_exists_exception(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock):
        interactor = init_interactor
        from ib_iam.exceptions.custom_exceptions import \
            TeamNotExistsInGivenProject
        project_id = "1"
        team_id = "1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id, team_id=team_id)
        project_storage_mock.get_valid_project_ids.return_value = [project_id]
        project_storage_mock.is_team_exists_in_project.return_value = False

        with pytest.raises(TeamNotExistsInGivenProject):
            interactor.get_team_details_for_given_project_team_user_details_dto(
                project_team_user_dto=project_team_user_dto)

        project_storage_mock.is_team_exists_in_project.assert_called_once_with(
            project_id=project_id, team_id=team_id)

    def test_given_invalid_user_raises_invalid_user_exception(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock):
        interactor = init_interactor
        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        project_id = "1"
        team_id = "1"
        user_id = "1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id, team_id=team_id, user_id=user_id)
        project_storage_mock.get_valid_project_ids.return_value = [project_id]
        # project_storage_mock.is_team_exists_in_project.return_value = False
        user_storage_mock.is_user_exist.return_value = False

        with pytest.raises(InvalidUserId):
            interactor.get_team_details_for_given_project_team_user_details_dto(
                project_team_user_dto=project_team_user_dto)

        user_storage_mock.is_user_exist.assert_called_once_with(
            user_id=user_id)

    def test_user_not_exists_in_team_raises_user_not_exists_in_team_exception(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock):
        interactor = init_interactor
        from ib_iam.exceptions.custom_exceptions import \
            UserNotExistsInGivenTeam
        project_id = "1"
        team_id = "1"
        user_id = "1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id, team_id=team_id, user_id=user_id)
        project_storage_mock.get_valid_project_ids.return_value = [project_id]
        project_storage_mock.is_user_exists_in_team.return_value = False

        with pytest.raises(UserNotExistsInGivenTeam):
            interactor.get_team_details_for_given_project_team_user_details_dto(
                project_team_user_dto=project_team_user_dto)

        project_storage_mock.is_user_exists_in_team.assert_called_once_with(
            team_id=team_id, user_id=user_id)

    def test_given_valid_details_returns_user_id_with_team_id_and_name_dto(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock):
        interactor = init_interactor
        project_id = "1"
        team_id = "1"
        user_id = "1"
        team_name = "team1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id, team_id=team_id, user_id=user_id)
        project_storage_mock.get_valid_project_ids.return_value = [project_id]
        project_storage_mock.get_team_name.return_value = team_name
        from ib_iam.interactors.storage_interfaces.dtos import \
            TeamWithUserIdDTO
        expected_team_with_user_id_dto = TeamWithUserIdDTO(
            user_id=user_id, team_id=team_id, team_name=team_name)

        actual_team_with_user_id_dto = interactor \
            .get_team_details_for_given_project_team_user_details_dto(
            project_team_user_dto=project_team_user_dto)

        project_storage_mock.get_team_name.assert_called_once_with(
            team_id=team_id)
        assert actual_team_with_user_id_dto == expected_team_with_user_id_dto
