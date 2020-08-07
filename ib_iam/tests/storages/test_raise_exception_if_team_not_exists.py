import pytest
from ib_iam.exceptions.custom_exceptions import InvalidTeamId
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)

team_id = "f2c02d98-f311-4ab2-8673-3daa00757002"


@pytest.mark.django_db
class TestRaiseExceptionIfTeamNotExists:
    def test_given_invalid_team_raises_invalid_team_id_exception(
            self, create_users, create_teams
    ):
        storage = TeamStorageImplementation()
        invalid_team_id = 'd81337b5-da0c-44e7-9773-245338c01ccc'

        with pytest.raises(InvalidTeamId):
            storage.raise_exception_if_team_not_exists(team_id=invalid_team_id)

    def test_given_team_exists_returns_none(
            self, create_users, create_teams
    ):
        storage = TeamStorageImplementation()
        expected_result = None

        actual_result = \
            storage.raise_exception_if_team_not_exists(team_id=team_id)

        assert actual_result == expected_result
