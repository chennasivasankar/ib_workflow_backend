from mock import create_autospec

from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from ib_iam.interactors.team_interactor import TeamInteractor


class TestGetValidTeamIds:

    # TODO: assert the storage calls
    def test_get_valid_team_ids_returns_team_ids(self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        interactor = TeamInteractor(team_storage=team_storage,
                                    user_storage=user_storage)
        team_ids = ["1", "2", "3"]
        expected_team_ids = ["1", "2"]
        team_storage.get_valid_team_ids.return_value = expected_team_ids

        actual_team_ids = interactor.get_valid_team_ids(team_ids=team_ids)

        assert actual_team_ids == expected_team_ids
