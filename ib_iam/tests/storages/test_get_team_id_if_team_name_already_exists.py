import pytest

from ib_iam.models import Team
from ib_iam.storages.team_storage_implementation import TeamStorageImplementation


@pytest.mark.django_db
class TestIsTeamNameAlreadyExists:
    def test_given_team_name_already_exists_returns_team_id(
            self, create_users, create_teams
    ):
        sql_storage = TeamStorageImplementation()
        requested_name = "team1"
        expected_value = 'f2c02d98-f311-4ab2-8673-3daa00757002'
        print("*******************************")
        print(Team.objects.values())
        actual_value = sql_storage.get_team_id_if_team_name_already_exists(
            name=requested_name
        )

        assert actual_value == expected_value

    def test_given_team_name_does_not_exists_it_returns_none(
            self, create_users, create_teams
    ):
        sql_storage = TeamStorageImplementation()
        requested_name = "team10"
        expected_value = None

        actual_value = sql_storage.get_team_id_if_team_name_already_exists(
            name=requested_name
        )

        assert actual_value == expected_value

