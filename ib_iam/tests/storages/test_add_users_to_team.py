import pytest
from ib_iam.models import UserTeam
from ib_iam.storages.team_storage_implementation import \
    TeamStorageImplementation


@pytest.mark.django_db
class TestAddUsersToTeam:

    def test_given_valid_details_return_nothing(self, create_teams):
        storage = TeamStorageImplementation()
        team_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        user_ids = [
            '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a',
            '8bcf545d-4573-4bc2-b037-16c856d37287'
        ]
        no_of_members_added = 2

        storage.add_users_to_team(
            team_id=team_id,
            user_ids=user_ids
        )

        team_member_objects = UserTeam.objects.filter(
            team_id=team_id,
            user_id__in=user_ids
        )
        assert len(team_member_objects) == no_of_members_added
