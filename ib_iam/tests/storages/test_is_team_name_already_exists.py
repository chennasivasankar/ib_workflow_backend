import pytest

from ib_iam.models import Team
from ib_iam.storages.team_storage_implementation import TeamStorageImplementation


@pytest.mark.django_db
class TestIsTeamNameAlreadyExists:
    def test_given_team_name_already_exists_it_returns_true(
            self, create_users, create_teams
    ):
        sql_storage = TeamStorageImplementation()
        requested_name = "team1"
        expected_value = True

        actual_value = sql_storage.is_team_name_already_exists(name=requested_name)

        assert actual_value == expected_value

    def test_given_team_name_does_not_exists_it_returns_false(
            self, create_users, create_teams
    ):
        sql_storage = TeamStorageImplementation()
        requested_name = "team0"
        expected_value = False

        actual_value = sql_storage.is_team_name_already_exists(name=requested_name)

        assert actual_value == expected_value

