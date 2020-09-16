import pytest

from ib_iam.models import TeamUser


@pytest.mark.django_db
class TestDeleteMembersFromTeam:

    @pytest.fixture
    def storage(self):
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        return TeamStorageImplementation()

    def test_whether_it_returns_an_empty_users_list(
            self, create_members, create_teams, storage
    ):
        # Arrange
        team_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
        user_ids_to_delete = [
            '2bdb417e-4632-419a-8ddd-085ea272c6eb',
            '4b8fb6eb-fa7d-47c1-8726-cd917901104e'
        ]
        after_delete_total_no_of_object = 0

        # Act
        storage.delete_members_from_team(
            team_id=team_id, user_ids=user_ids_to_delete
        )

        # Assert
        total_team_user_objects = TeamUser.objects.filter(
            team_id=team_id, user_id__in=user_ids_to_delete
        ).count()

        assert total_team_user_objects == after_delete_total_no_of_object
