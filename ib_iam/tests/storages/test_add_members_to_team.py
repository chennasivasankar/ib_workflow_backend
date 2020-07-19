import pytest
from ib_iam.models import TeamMember
from ib_iam.tests.factories import TeamFactory
from ib_iam.storages.team_storage_implementation import TeamStorageImplementation


@pytest.mark.django_db
class TestAddMembersToTeam:

    def test_given_valid_details_return_team_id(self, create_teams):
        storage = TeamStorageImplementation()

        user_id = "155f3fa1-e4eb-4bfa-89e7-ca80edd23a6e"
        team_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        member_ids = [
            '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a',
            '8bcf545d-4573-4bc2-b037-16c856d37287'
        ]
        no_of_members_added = 2

        storage.add_members_to_team(
            team_id=team_id,
            member_ids=member_ids
        )

        team_member_objects = TeamMember.objects.filter(
            team_id=team_id,
            member_id__in=member_ids
        )
        assert len(team_member_objects) == no_of_members_added
