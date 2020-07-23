import pytest

from ib_iam.models import TeamMember
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)

team_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'


@pytest.mark.django_db
class TestGetTeamMemberIds:

    def test_whether_it_returns_list_of_team_members_dtos(
            self, create_members, create_teams
    ):
        storage = TeamStorageImplementation()
        user_ids_to_delete = [
            '2bdb417e-4632-419a-8ddd-085ea272c6eb',
            '4b8fb6eb-fa7d-47c1-8726-cd917901104e'
        ]

        storage.delete_members_from_team(
            team_id=team_id, user_ids=user_ids_to_delete
        )

        team_objects = TeamMember.objects.filter(
            team_id=team_id, user_id__in=user_ids_to_delete
        )
        assert list(team_objects) == []
