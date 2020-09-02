import pytest

from ib_iam.models import TeamUser, Team
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)


@pytest.mark.django_db
class TestDeleteTeam:

    def test_whether_it_returns_list_of_team_members_dtos(
            self, create_teams
    ):
        storage = TeamStorageImplementation()
        team_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'

        storage.delete_team(
            team_id=team_id
        )

        team_objects = Team.objects.filter(team_id=team_id)
        assert list(team_objects) == []
