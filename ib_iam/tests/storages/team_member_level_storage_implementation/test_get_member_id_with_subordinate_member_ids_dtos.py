import pytest


class TestMemberIdWithSubordinateMemberIdsDTO:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.fixture()
    def prepare_user_teams_subordinate_members(
            self, create_user_teams):
        from ib_iam.models import TeamUser

        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_id_with_immediate_superior_team_user_id_list = [{
            'user_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': None
        }, {
            'user_id': '20be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': 1
        }, {
            'user_id': '30be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': 1
        }, {
            'user_id': '40be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': None
        }, {
            'user_id': '50be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': 2
        }, {
            'user_id': '60be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': None
        }]
        for member_details_dict in member_id_with_immediate_superior_team_user_id_list:
            TeamUser.objects.filter(
                user_id=member_details_dict["user_id"],
                team_id=team_id
            ).update(
                immediate_superior_team_user_id=member_details_dict[
                    "immediate_superior_team_user_id"]
            )

    @pytest.mark.django_db
    def test_get_member_id_with_subordinate_member_ids_dtos(
            self, prepare_user_teams_subordinate_members, storage):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_id_with_subordinate_ids_list = [{
            'member_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
            'subordinate_member_ids': ['20be920b-7b4c-49e7-8adb-41a0c18da848',
                                       '30be920b-7b4c-49e7-8adb-41a0c18da848']
        }, {
            'member_id': '20be920b-7b4c-49e7-8adb-41a0c18da848',
            'subordinate_member_ids': ['50be920b-7b4c-49e7-8adb-41a0c18da848']
        }, {
            'member_id': '60be920b-7b4c-49e7-8adb-41a0c18da848',
            'subordinate_member_ids': []
        }]

        from ib_iam.tests.factories.storage_dtos import \
            MemberIdWithSubordinateMemberIdsDTOFactory
        expected_member_id_with_subordinate_member_ids_dtos = [
            MemberIdWithSubordinateMemberIdsDTOFactory(
                member_id=member_id_with_subordinate_ids_dict["member_id"],
                subordinate_member_ids=member_id_with_subordinate_ids_dict["subordinate_member_ids"]
            )
            for member_id_with_subordinate_ids_dict in
            member_id_with_subordinate_ids_list
        ]
        member_ids = [
            '10be920b-7b4c-49e7-8adb-41a0c18da848',
            '20be920b-7b4c-49e7-8adb-41a0c18da848',
            '60be920b-7b4c-49e7-8adb-41a0c18da848'
        ]

        # Act
        response = storage.get_member_id_with_subordinate_member_ids_dtos(
            team_id=team_id, member_ids=member_ids
        )

        # Assert
        assert response == expected_member_id_with_subordinate_member_ids_dtos
