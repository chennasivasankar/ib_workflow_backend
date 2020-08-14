import pytest


class TestGetLevelDetailsDTOs:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.level_storage_implementation import \
            LevelStorageImplementation
        storage = LevelStorageImplementation()
        return storage

    @pytest.fixture()
    def create_team_levels(self):
        from ib_iam.tests.factories.models import TeamMemberLevelFactory
        TeamMemberLevelFactory.create_batch(3)

        from ib_iam.tests.factories.models import TeamFactory
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
        team_object = TeamFactory(
            team_id=team_id,
            name="name",
            description="description",
            created_by=user_id
        )
        team_member_level_list = [
            {
                "level_id": "91be920b-7b4c-49e7-8adb-41a0c18da848",
                "level_name": "Developer",
                "level_hierarchy": 0,
                "team": team_object
            },
            {
                "level_id": "11be920b-7b4c-49e7-8adb-41a0c18da848",
                "level_name": "Software Developer Lead",
                "level_hierarchy": 1,
                "team": team_object
            },
            {
                "level_id": "21be920b-7b4c-49e7-8adb-41a0c18da848",
                "level_name": "Engineer Manager",
                "level_hierarchy": 2,
                "team": team_object
            },
            {
                "level_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "level_name": "Product Owner",
                "level_hierarchy": 3,
                "team": team_object
            }
        ]
        team_member_level_objects = [
            TeamMemberLevelFactory(
                id=team_member_level_dict["level_id"],
                team=team_member_level_dict["team"],
                level_name=team_member_level_dict["level_name"],
                level_hierarchy=team_member_level_dict["level_hierarchy"]
            )
            for team_member_level_dict in team_member_level_list
        ]
        return team_member_level_objects

    @pytest.mark.django_db
    def test_with_valid_details_return_reponse(
            self, storage, create_team_levels
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_details_list = [{
            'level_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
            'level_name': 'Developer',
            'level_hierarchy': 0
        }, {
            'level_id': '11be920b-7b4c-49e7-8adb-41a0c18da848',
            'level_name': 'Software Developer Lead',
            'level_hierarchy': 1
        }, {
            'level_id': '21be920b-7b4c-49e7-8adb-41a0c18da848',
            'level_name': 'Engineer Manager',
            'level_hierarchy': 2
        }, {
            'level_id': '31be920b-7b4c-49e7-8adb-41a0c18da848',
            'level_name': 'Product Owner',
            'level_hierarchy': 3
        }]
        from ib_iam.tests.factories.storage_dtos import TeamMemberLevelDetailsDTOFactory
        level_details_dtos = [
            TeamMemberLevelDetailsDTOFactory(
                team_member_level_id=level_details_dict["level_id"],
                team_member_level_name=level_details_dict["level_name"],
                level_hierarchy=level_details_dict["level_hierarchy"]
            )
            for level_details_dict in level_details_list
        ]

        # Act
        response = storage.get_team_member_level_details_dtos(team_id=team_id)

        # Assert
        assert response == level_details_dtos
