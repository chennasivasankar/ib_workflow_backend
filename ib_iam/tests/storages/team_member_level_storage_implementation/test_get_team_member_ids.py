import pytest


class TestGetTeamMemberIds:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_team_having_members_return_member_ids(
            self, storage, create_users_team
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_user_ids = [
            "21be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848",
            "17be920b-7b4c-49e7-8adb-41a0c18da848",
            "27be920b-7b4c-49e7-8adb-41a0c18da848",
            "37be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        # Act
        user_ids = storage.get_team_member_ids(team_id=team_id)

        # Assert
        assert user_ids == expected_user_ids

    @pytest.mark.django_db
    def test_with_team_no_having_members_return_empty_list(
            self, storage, create_team
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_user_ids = []

        # Act
        user_ids = storage.get_team_member_ids(team_id=team_id)

        # Assert
        assert user_ids == expected_user_ids

    @pytest.fixture()
    def create_users_team(self, create_team):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_ids = [
            "21be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848",
            "17be920b-7b4c-49e7-8adb-41a0c18da848",
            "27be920b-7b4c-49e7-8adb-41a0c18da848",
            "37be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        from ib_iam.tests.factories.models import TeamUserFactory
        user_team_objects = [
            TeamUserFactory(
                user_id=user_id, team_id=team_id
            )
            for user_id in user_ids
        ]
        return user_team_objects
