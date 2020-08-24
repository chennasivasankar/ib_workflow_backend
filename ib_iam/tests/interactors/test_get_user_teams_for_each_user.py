import pytest
from mock import create_autospec


class TestGetUserTeamsForEachUser:

    @pytest.fixture
    def user_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        mock = create_autospec(UserStorageInterface)
        return mock

    @pytest.fixture
    def team_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.team_storage_interface import \
            TeamStorageInterface
        mock = create_autospec(TeamStorageInterface)
        return mock

    def test_get_user_teams_dtos_for_valid_user_ids_return_response(
            self, user_storage_mock, team_storage_mock):
        user_ids = ["1", "2"]
        user_teams = [
            {
                "user_id": "1",
                "team_id": "11"
            },
            {
                "user_id": "1",
                "team_id": "12"
            },
            {
                "user_id": "2",
                "team_id": "11"
            },
            {
                "user_id": "2",
                "team_id": "12"
            }
        ]
        from ib_iam.interactors.team_interactor import TeamInteractor
        user_storage_mock.get_valid_user_ids.return_value = user_ids
        from ib_iam.tests.factories.storage_dtos import UserTeamDTOFactory
        UserTeamDTOFactory.reset_sequence(0)
        user_team_dtos = [
            UserTeamDTOFactory(
                user_id=user_team["user_id"], team_id=user_team["team_id"]
            ) for user_team in user_teams
        ]
        user_storage_mock.get_team_details_of_users_bulk.return_value = \
            user_team_dtos

        interactor = TeamInteractor(
            user_storage=user_storage_mock, team_storage=team_storage_mock)

        response = interactor.get_user_teams_for_each_user(user_ids=user_ids)

        user_storage_mock.get_team_details_of_users_bulk.assert_called_once_with(
            user_ids=user_ids)

    def test_get_user_teams_dtos_for_invalid_user_ids_raise_invalid_user_ids_response(
            self, user_storage_mock, team_storage_mock):
        user_ids = ["1", "2", "3"]
        valid_user_ids = ["1"]
        from ib_iam.interactors.team_interactor import TeamInteractor
        user_storage_mock.get_valid_user_ids.return_value = valid_user_ids

        interactor = TeamInteractor(
            user_storage=user_storage_mock, team_storage=team_storage_mock)

        from ib_iam.exceptions.custom_exceptions import InvalidUserIds
        with pytest.raises(InvalidUserIds):
            interactor.get_user_teams_for_each_user(user_ids=user_ids)

        user_storage_mock.get_valid_user_ids.assert_called_once_with(
            user_ids=user_ids)
