import pytest


class TestGetTeamMemberLevelIds:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_for_having_team_member_levels_return_level_ids(
            self, storage, create_team_member_levels
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_team_member_level_ids = [
            "00be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "02be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        # Act
        team_member_level_ids = storage.get_team_member_level_ids(
            team_id=team_id)

        # Assert
        assert team_member_level_ids == expected_team_member_level_ids

    @pytest.mark.django_db
    def test_for_having_no_team_member_levels_return_empty_list(
            self, storage, create_team
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_team_member_level_ids = []

        # Act
        team_member_level_ids = storage.get_team_member_level_ids(
            team_id=team_id)

        # Assert
        assert team_member_level_ids == expected_team_member_level_ids

    @pytest.fixture()
    def create_team_member_levels(self, create_team):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_list = [
            {
                "id": "00be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_name": "Developer",
                "level_hierarchy": 0
            },
            {
                "id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_name": "Software Developer Lead",
                "level_hierarchy": 1
            },
            {
                "id": "02be920b-7b4c-49e7-8adb-41a0c18da848",
                "team_id": team_id,
                "level_name": "Engineer Manager",
                "level_hierarchy": 2
            }
        ]
        from ib_iam.tests.factories.models import TeamMemberLevelFactory
        team_member_level_objects = [
            TeamMemberLevelFactory(
                id=team_member_level_dict["id"],
                team_id=team_member_level_dict["team_id"],
                level_name=team_member_level_dict["level_name"],
                level_hierarchy=team_member_level_dict["level_hierarchy"]
            )
            for team_member_level_dict in team_member_level_list
        ]
        return team_member_level_objects
