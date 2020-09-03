import pytest


class TestAddMembersToLevelsForATeam:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.fixture()
    def create_users_team(self):
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
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

    @pytest.fixture()
    def create_team_member_levels(self):
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

    @pytest.fixture()
    def prepare_team_member_level_id_with_member_ids_dtos(self):
        team_member_level_id_with_member_ids_list = [
            {
                "team_member_level_id": "00be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": [
                    "31be920b-7b4c-49e7-8adb-41a0c18da848",
                    "01be920b-7b4c-49e7-8adb-41a0c18da848",
                ]
            },
            {
                "team_member_level_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": [
                    "77be920b-7b4c-49e7-8adb-41a0c18da848",
                    "17be920b-7b4c-49e7-8adb-41a0c18da848",
                    "27be920b-7b4c-49e7-8adb-41a0c18da848",
                ]
            },
            {
                "team_member_level_id": "02be920b-7b4c-49e7-8adb-41a0c18da848",
                "member_ids": []
            }
        ]
        from ib_iam.tests.factories.interactor_dtos import \
            TeamMemberLevelIdWithMemberIdsDTOFactory
        team_member_level_id_with_member_ids_dtos = [
            TeamMemberLevelIdWithMemberIdsDTOFactory(
                team_member_level_id=details_dict["team_member_level_id"],
                member_ids=details_dict["member_ids"]
            )
            for details_dict in team_member_level_id_with_member_ids_list
        ]
        return team_member_level_id_with_member_ids_dtos

    @pytest.mark.django_db
    def test_add_members_to_levels_for_a_team(
            self, storage, create_team, create_users_team,
            create_team_member_levels, snapshot,
            prepare_team_member_level_id_with_member_ids_dtos
    ):
        # Arrange
        team_member_level_id_with_member_ids_dtos = \
            prepare_team_member_level_id_with_member_ids_dtos

        # Act
        storage.add_members_to_levels_for_a_team(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos
        )

        # Assert
        from ib_iam.models import TeamUser
        user_team_details = TeamUser.objects.values(
            "user_id", "team_member_level_id")
        for user_team_details_dict in user_team_details:
            user_team_details_dict["team_member_level_id"] = \
                str(user_team_details_dict["team_member_level_id"])

        snapshot.assert_match(list(user_team_details), "user_team_details")
