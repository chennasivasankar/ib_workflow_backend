import pytest


class TestValidateUserInATeam:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_user_not_belong_to_team(self, create_team, storage):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"

        # Assert
        from ib_iam.exceptions.custom_exceptions import UserNotBelongToTeam
        with pytest.raises(UserNotBelongToTeam):
            storage.validate_user_in_a_team(team_id=team_id, user_id=user_id)

    @pytest.mark.django_db
    def test_with_user_belong_to_team(self, create_user_teams, storage):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "10be920b-7b4c-49e7-8adb-41a0c18da848"

        # Act
        storage.validate_user_in_a_team(team_id=team_id, user_id=user_id)

        # Assert
        from ib_iam.models import TeamUser
        team_user_objects = TeamUser.objects.filter(
            team_id=team_id, user_id=user_id)

        is_team_user_objects_exists = team_user_objects.exists()
        assert is_team_user_objects_exists is True

    @pytest.fixture()
    def create_user_teams(self, create_team):
        team_object = create_team
        from ib_iam.tests.factories.models import TeamMemberLevelFactory
        team_member_level_object = TeamMemberLevelFactory(
            id="00be920b-7b4c-49e7-8adb-41a0c18da848",
            team=team_object,
            level_name="Developer",
            level_hierarchy=1
        )

        user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848",
            "30be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.tests.factories.models import TeamUserFactory
        user_team_objects = [
            TeamUserFactory(
                user_id=user_id,
                team=team_object,
                team_member_level=team_member_level_object
            )
            for user_id in user_ids
        ]
        return user_team_objects
