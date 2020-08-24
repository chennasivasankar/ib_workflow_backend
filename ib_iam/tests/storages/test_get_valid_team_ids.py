import pytest


class TestGetValidTeamIds:

    @pytest.mark.django_db
    def test_get_valid_team_ids_returns_team_ids(self):
        # Arrange
        team_ids = ["eca1a0c1-b9ef-4e59-b415-60a28ef17b10",
                    "abc1a0c1-b9ef-4e59-b415-60a28ef17b10",
                    "1231a0c1-b9ef-4e59-b415-60a28ef17b10"]
        expected_team_ids = ["abc1a0c1-b9ef-4e59-b415-60a28ef17b10",
                             "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"]
        from ib_iam.tests.factories.models import TeamFactory
        for team_id in expected_team_ids:
            TeamFactory.create(team_id=team_id)

        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        storage = TeamStorageImplementation()

        # Act
        actual_team_ids = storage.get_valid_team_ids(team_ids=team_ids)

        # Assert
        assert actual_team_ids == expected_team_ids
