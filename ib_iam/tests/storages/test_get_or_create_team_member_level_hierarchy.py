import pytest


class TestGetOrCreateTeamMemberLevelHierarchy:

    @pytest.fixture()
    def team_member_level_storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        team_member_level_storage = TeamMemberLevelStorageImplementation()
        return team_member_level_storage

    @pytest.mark.django_db
    def test_for_create_team_member_level_return_response(
            self, team_member_level_storage
    ):
        # Arrange
        team_id = "1c9979b2-3323-4cb6-88d6-b497175c549e"
        level_hierarchy = 0
        level_name = "Developer"

        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory(team_id=team_id)

        # Act
        team_member_level_id = \
            team_member_level_storage.get_or_create_team_member_level_hierarchy(
                team_id=team_id, level_hierarchy=level_hierarchy,
                level_name=level_name
            )

        # Assert
        from ib_iam.models import TeamMemberLevel
        team_member_level_object = TeamMemberLevel.objects.filter(
            team_id=team_id, level_hierarchy=level_hierarchy,
            level_name=level_name
        )[0]
        expected_team_member_level_id = team_member_level_object.id

        assert team_member_level_id == str(expected_team_member_level_id)

    @pytest.mark.django_db
    def test_for_get_team_member_level_return_response(
            self, team_member_level_storage
    ):
        # Arrange
        team_id = "1c9979b2-3323-4cb6-88d6-b497175c549e"
        level_hierarchy = 0
        level_name = "Developer"

        from ib_iam.tests.factories.models import TeamFactory
        team_object = TeamFactory(team_id=team_id)

        from ib_iam.tests.factories.models import TeamMemberLevelFactory
        TeamMemberLevelFactory(team=team_object)

        # Act
        team_member_level_id = \
            team_member_level_storage.get_or_create_team_member_level_hierarchy(
                team_id=team_id, level_hierarchy=level_hierarchy,
                level_name=level_name
            )

        # Assert
        from ib_iam.models import TeamMemberLevel
        team_member_level_object = TeamMemberLevel.objects.filter(
            team_id=team_id, level_hierarchy=level_hierarchy,
            level_name=level_name
        )[0]
        expected_team_member_level_id = team_member_level_object.id

        assert team_member_level_id == str(expected_team_member_level_id)
