import pytest

from ib_iam.models import TeamUser


@pytest.mark.django_db
class TestAddUsersToTeam:

    @pytest.fixture
    def storage(self):
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        return TeamStorageImplementation()

    @pytest.fixture()
    def create_teams(self):
        team_details = [
            {
                "team_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
                "name": "Daru"
            },
            {
                "team_id": "aa66c40f-6d93-484a-b418-984716514c7b",
                "name": "Proyuga"
            },
            {
                "team_id": "c982032b-53a7-4dfa-a627-4701a5230765",
                "name": "Arogya"
            }
        ]
        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory.reset_sequence(1)
        team_objects = [
            TeamFactory.create(team_id=team["team_id"], name=team["name"])
            for team in team_details
        ]
        return team_objects

    def test_given_valid_details_return_nothing(
            self, create_teams, storage, snapshot
    ):
        # Arrange
        team_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        user_ids = [
            '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a',
            '8bcf545d-4573-4bc2-b037-16c856d37287'
        ]
        no_of_members_added = 2

        # Act
        storage.add_users_to_team(
            team_id=team_id, user_ids=user_ids
        )

        # Assert
        team_member_objects = TeamUser.objects.filter(
            team_id=team_id, user_id__in=user_ids
        ).values()

        assert len(team_member_objects) == no_of_members_added
        snapshot.assert_match(team_member_objects, "team_users", )
