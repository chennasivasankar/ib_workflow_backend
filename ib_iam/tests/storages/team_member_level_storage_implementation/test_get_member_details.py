import pytest


class TestGetMemberDetails:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

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

    @pytest.mark.django_db
    def test_get_member_details_return_response(self, storage,
                                                create_user_teams):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 1
        members_list = [{
            'member_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': None
        }, {
            'member_id': '20be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': None
        }, {
            'member_id': '30be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': None
        }]
        from ib_iam.tests.factories.storage_dtos import MemberDTOFactory
        expected_member_dtos = [
            MemberDTOFactory(
                member_id=members_dict["member_id"],
                immediate_superior_team_user_id=members_dict[
                    "immediate_superior_team_user_id"]
            )
            for members_dict in members_list
        ]

        # Act
        response = storage.get_member_details(
            team_id=team_id, level_hierarchy=level_hierarchy
        )

        # Assert
        assert response == expected_member_dtos
