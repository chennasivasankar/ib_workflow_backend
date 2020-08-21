import pytest


class TestAddLevelsToTeam:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.fixture()
    def prepare_team_member_level_dtos(self):
        level_list = [
            {
                "level_name": "Developer",
                "level_hierarchy": 0
            },
            {
                "level_name": "Software Developer Lead",
                "level_hierarchy": 1
            },
            {
                "level_name": "Engineer Manager",
                "level_hierarchy": 2
            },
            {
                "level_name": "Product Owner",
                "level_hierarchy": 3
            }
        ]

        from ib_iam.tests.factories.interactor_dtos import \
            TeamMemberLevelDTOFactory
        level_dtos = [
            TeamMemberLevelDTOFactory(
                team_member_level_name=level_dict["level_name"],
                level_hierarchy=level_dict["level_hierarchy"]
            )
            for level_dict in level_list
        ]
        return level_dtos

    @pytest.mark.django_db
    def test_with_valid_details_create_team_levels(
            self, storage, prepare_team_member_level_dtos, create_team, snapshot
    ):
        # Arrange
        team_id = create_team.team_id
        team_member_level_dtos = prepare_team_member_level_dtos

        # Act
        storage.add_team_member_levels(
            team_id=team_id, team_member_level_dtos=team_member_level_dtos
        )

        # Assert
        from ib_iam.models import TeamMemberLevel
        team_level_objects = TeamMemberLevel.objects.filter(team_id=team_id)

        team_level_details = team_level_objects.values(
            "level_name", "level_hierarchy")
        snapshot.assert_match(list(team_level_details), "add_team_levels")
