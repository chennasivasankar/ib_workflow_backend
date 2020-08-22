import pytest


class TestAddMembersToSuperiors:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_add_members_to_superiors(self, storage, create_user_teams,
                                      snapshot):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = 0
        user_team_objects_of_level_one = create_user_teams
        immediate_superior_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848",
            "30be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        set_hierarchy_list = [{
                "immediate_superior_user_id": immediate_superior_user_ids[0],
                "member_ids": [
                    "40be920b-7b4c-49e7-8adb-41a0c18da848",
                    "50be920b-7b4c-49e7-8adb-41a0c18da848"
                ]
            }, {
                "immediate_superior_user_id": immediate_superior_user_ids[1],
                "member_ids": [
                    "60be920b-7b4c-49e7-8adb-41a0c18da848"
                ]
        }]

        from ib_iam.tests.factories.interactor_dtos import \
            ImmediateSuperiorUserIdWithUserIdsDTOFactory
        immediate_superior_user_id_with_member_ids_dtos = [
            ImmediateSuperiorUserIdWithUserIdsDTOFactory(
                immediate_superior_user_id=set_hierarchy_dict[
                    "immediate_superior_user_id"],
                member_ids=set_hierarchy_dict["member_ids"]
            )
            for set_hierarchy_dict in set_hierarchy_list
        ]

        # Act
        storage.add_members_to_superiors(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_user_id_with_member_ids_dtos
        )

        # Assert
        from ib_iam.models import UserTeam
        user_team_objects = UserTeam.objects.filter(
            team_id=team_id
        )
        user_team_list = user_team_objects.values(
            "id", "user_id", "team_member_level_id",
            "immediate_superior_team_user_id"
        )
        for user_team_dict in user_team_list:
            user_team_dict["team_member_level_id"] = \
                str(user_team_dict["team_member_level_id"])
        snapshot.assert_match(list(user_team_list), "user_team")
