import pytest
from ib_iam.exceptions import InvalidTeamId
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)
from ib_iam.tests.storages.conftest import team1_id


@pytest.mark.django_db
class TestIsValidTeam:
    def test_given_invalid_team_raises_invalid_team_id_exception(
            self, create_users, create_teams
    ):
        sql_storage = TeamStorageImplementation()
        invalid_team_id = 'd81337b5-da0c-44e7-9773-245338c01ccc'

        with pytest.raises(InvalidTeamId):
            sql_storage.is_valid_team(team_id=invalid_team_id)

    def test_given_team_exists_returns_none(
            self, create_users, create_teams
    ):
        sql_storage = TeamStorageImplementation()
        expected_result = None

        actual_result = sql_storage.is_valid_team(team_id=team1_id)

        assert actual_result == expected_result

