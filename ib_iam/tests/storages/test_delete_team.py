import pytest

from ib_iam.models import Team


@pytest.mark.django_db
class TestDeleteTeam:

    @pytest.fixture
    def storage(self):
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        return TeamStorageImplementation()

    def test_whether_it_returns_list_of_team_members_dtos(
            self, create_teams, storage
    ):
        # Arrange
        team_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'

        # Act
        storage.delete_team(team_id=team_id)

        # Assert
        with pytest.raises(Team.DoesNotExist):
            Team.objects.get(team_id=team_id)
