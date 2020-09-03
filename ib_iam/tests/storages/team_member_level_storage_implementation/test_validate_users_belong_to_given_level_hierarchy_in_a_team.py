import pytest


class TestValidateUsersBelongToGivenLevelHierarchyInATeam:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_invalid_level_hierarchy_of_a_team(
            self, storage, assign_users_to_levels
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "17be920b-7b4c-49e7-8adb-41a0c18da848",
            "27be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        level_hierarchy = 3

        # Assert
        from ib_iam.exceptions.custom_exceptions import \
            InvalidLevelHierarchyOfTeam
        with pytest.raises(InvalidLevelHierarchyOfTeam):
            storage.validate_users_belong_to_given_level_hierarchy_in_a_team(
                team_id=team_id, level_hierarchy=level_hierarchy,
                user_ids=user_ids
            )

    @pytest.mark.django_db
    def test_with_users_not_belong_to_level_raise_exception(
            self, storage, assign_users_to_levels
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "17be920b-7b4c-49e7-8adb-41a0c18da848",
            "27be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        level_hierarchy = 0
        expected_user_ids_not_belong_to_team_level = [
            "17be920b-7b4c-49e7-8adb-41a0c18da848",
            "27be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        # Assert
        from ib_iam.exceptions.custom_exceptions import UsersNotBelongToLevel
        with pytest.raises(UsersNotBelongToLevel) as err:
            storage.validate_users_belong_to_given_level_hierarchy_in_a_team(
                team_id=team_id, level_hierarchy=level_hierarchy,
                user_ids=user_ids
            )

        assert err.value.user_ids == expected_user_ids_not_belong_to_team_level
        assert err.value.level_hierarchy == level_hierarchy

    @pytest.mark.django_db
    def test_with_users_belong_to_level_did_not_raise_exception(
            self, storage, assign_users_to_levels
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        level_hierarchy = 0

        # Assert
        storage.validate_users_belong_to_given_level_hierarchy_in_a_team(
            team_id=team_id, level_hierarchy=level_hierarchy,
            user_ids=user_ids
        )

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
    def create_users_team(self, create_team):
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
    def assign_users_to_levels(
            self, create_users_team, create_team_member_levels):
        team_member_level_objects = create_team_member_levels
        from ib_iam.tests.factories.models import TeamUser
        TeamUser.objects.filter(
            user_id__in=[
                "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "77be920b-7b4c-49e7-8adb-41a0c18da848"
            ]
        ).update(team_member_level=team_member_level_objects[0])
        TeamUser.objects.filter(
            user_id__in=[
                "17be920b-7b4c-49e7-8adb-41a0c18da848",
                "27be920b-7b4c-49e7-8adb-41a0c18da848"
            ]
        ).update(team_member_level=team_member_level_objects[1])
        TeamUser.objects.filter(
            user_id__in=[
                "37be920b-7b4c-49e7-8adb-41a0c18da848"
            ]
        ).update(team_member_level=team_member_level_objects[2])
        return
