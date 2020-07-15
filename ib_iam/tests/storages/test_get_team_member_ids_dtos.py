import pytest
from ib_iam.storages.team_storage_implementation import TeamStorageImplementation
from ib_iam.tests.storages.conftest import (
    team1_id, team2_id, team3_id
)


@pytest.mark.django_db
class TestGetTeamMemberIdsDtos:

    def test_whether_it_returns_list_of_team_members_dtos(
            self, snapshot, create_members
    ):
        sql_storage = TeamStorageImplementation()
        team_ids = [team1_id, team2_id, team3_id]

        result = sql_storage.get_team_member_ids_dtos(
            team_ids=team_ids
        )

        snapshot.assert_match(result, "result")
