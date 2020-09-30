import pytest


class TestGetOrCreateTeamWithIdAndName:

    @pytest.fixture()
    def team_storage(self):
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        team_storage = TeamStorageImplementation()
        return team_storage

    @pytest.mark.django_db
    def test_for_create_team_return_response(self, team_storage):
        # Arrange
        team_id = "1c9979b2-3323-4cb6-88d6-b497175c549e"
        name = "TEAM_NAME"

        # Act
        is_created = team_storage.get_or_create_team_with_id_and_name(
            name=name, team_id=team_id
        )

        # Assert
        from ib_iam.models import Team
        expected_team_object_id = Team.objects.filter(name=name)[0].team_id

        assert is_created is True
        assert team_id == str(expected_team_object_id)

    @pytest.mark.django_db
    def test_for_get_team_return_response(self, team_storage):
        # Arrange
        team_id = "1c9979b2-3323-4cb6-88d6-b497175c549e"
        name = "TEAM_NAME"

        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory(team_id=team_id, name=name)

        # Act
        is_created = team_storage.get_or_create_team_with_id_and_name(
            name=name, team_id=team_id
        )

        # Assert
        from ib_iam.models import Team
        expected_team_object_id = Team.objects.filter(team_id=team_id)[0].team_id

        assert is_created is False
        assert team_id == str(expected_team_object_id)
