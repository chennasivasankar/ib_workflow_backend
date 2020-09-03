import pytest


class TestValidateTeamId:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_team_id_not_exist_raise_exception(self, create_team, storage):
        # Arrange
        team_id = "01be920b-7b4c-49e7-8adb-41a0c18da848"

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        with pytest.raises(InvalidTeamId):
            storage.validate_team_id(team_id=team_id)

    @pytest.mark.django_db
    def test_with_team_id_exist_did_not_raise_exception(
            self, create_team, storage):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        # Act
        storage.validate_team_id(team_id=team_id)

        # Assert
        from ib_iam.models import Team
        team_objects = Team.objects.filter(team_id=team_id)
        is_team_objects_exists = team_objects.exists()

        assert is_team_objects_exists is True
