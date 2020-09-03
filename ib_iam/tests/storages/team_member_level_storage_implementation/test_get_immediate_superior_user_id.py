import pytest


class TestGetImmediateSuperiorUserId:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_valid_details_return_immediate_superior_user_id(
            self, create_team, storage):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        immediate_superior_user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_iam.tests.factories.models import TeamUserFactory
        immediate_superior_user_object = TeamUserFactory(
            team_id=team_id, user_id=immediate_superior_user_id
        )

        TeamUserFactory(
            team_id=team_id, user_id=user_id,
            immediate_superior_team_user=immediate_superior_user_object
        )

        # Act
        response = storage.get_immediate_superior_user_id(
            team_id=team_id, user_id=user_id
        )

        # Assert
        assert response == immediate_superior_user_id

    @pytest.mark.django_db
    def test_with_valid_details_return_None(
            self, create_team, storage):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_iam.tests.factories.models import TeamUserFactory
        TeamUserFactory(
            team_id=team_id, user_id=user_id
        )

        # Act
        response = storage.get_immediate_superior_user_id(
            team_id=team_id, user_id=user_id
        )

        # Assert
        assert response is None
