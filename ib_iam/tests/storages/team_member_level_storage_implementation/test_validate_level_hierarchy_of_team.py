import pytest


class TestValidateLevelHierarchyOfTeam:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_invalid_level_hierarchy_of_team_raise_exception(
            self, storage, create_team_member_levels
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 3

        # Assert
        from ib_iam.exceptions.custom_exceptions import \
            InvalidLevelHierarchyOfTeam
        with pytest.raises(InvalidLevelHierarchyOfTeam):
            storage.validate_level_hierarchy_of_team(
                team_id=team_id, level_hierarchy=level_hierarchy
            )

    @pytest.mark.django_db
    def test_with_valid_level_hierarchy_of_team_did_not_raise_exception(
            self, storage, create_team_member_levels
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 2

        # Act
        storage.validate_level_hierarchy_of_team(
            team_id=team_id, level_hierarchy=level_hierarchy
        )

        # Assert
        from ib_iam.models import TeamMemberLevel
        team_member_level_objects = TeamMemberLevel.objects.filter(
            team_id=team_id, level_hierarchy=level_hierarchy
        )
        is_team_member_level_objects_exists = \
            team_member_level_objects.exists()

        assert is_team_member_level_objects_exists is True

    @pytest.fixture()
    def create_team_member_levels(self, create_team):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_list = [
            {
                "id": "00be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_hierarchy": 0
            },
            {
                "id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_hierarchy": 1
            },
            {
                "id": "02be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_hierarchy": 2
            }
        ]
        from ib_iam.tests.factories.models import TeamMemberLevelFactory
        team_member_level_objects = [
            TeamMemberLevelFactory(
                id=team_member_level_dict["id"],
                team_id=team_member_level_dict["team_id"],
                level_hierarchy=team_member_level_dict["level_hierarchy"]
            )
            for team_member_level_dict in team_member_level_list
        ]
        return team_member_level_objects
