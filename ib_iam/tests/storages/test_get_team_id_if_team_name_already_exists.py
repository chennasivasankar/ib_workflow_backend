import pytest
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)


@pytest.mark.django_db
class TestIsTeamNameAlreadyExists:
    def test_given_team_name_already_exists_it_returns_team_id(
            self, create_users, create_teams
    ):
        storage = TeamStorageImplementation()
        requested_name = "team1"
        expected_value = "f2c02d98-f311-4ab2-8673-3daa00757002"

        actual_value = storage.get_team_id_if_team_name_already_exists(
            name=requested_name
        )

        assert actual_value == expected_value

    def test_given_team_name_does_not_exists_it_returns_none(
            self, create_users, create_teams
    ):
        storage = TeamStorageImplementation()
        requested_name = "team0"
        expected_value = None

        actual_value = storage.get_team_id_if_team_name_already_exists(
            name=requested_name
        )

        assert actual_value == expected_value
