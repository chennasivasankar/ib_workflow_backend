import pytest

from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    PaginationDTO
from ib_iam.storages.team_storage_implementation import \
    TeamStorageImplementation
from ib_iam.tests.factories.storage_dtos import \
    TeamsWithTotalTeamsCountDTOFactory, TeamDTOFactory


@pytest.mark.django_db
class TestGetTeamsWithTotalTeamsCountDto:

    @pytest.fixture()
    def create_teams(self):
        team_details = [
            {"team_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
             "name": "Daru"},
            {"team_id": "aa66c40f-6d93-484a-b418-984716514c7b",
             "name": "Proyuga"},
            {"team_id": "c982032b-53a7-4dfa-a627-4701a5230765",
             "name": "Arogya"},
        ]
        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory.reset_sequence(1)
        team_objects = [
            TeamFactory.create(team_id=team["team_id"], name=team["name"])
            for team in team_details
        ]
        return team_objects

    @pytest.fixture()
    def team_dtos(self):
        team_details = [
            {
                "team_id": "c982032b-53a7-4dfa-a627-4701a5230765",
                "name": "Arogya", "description": "team_description 3"
            },
            {
                "team_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
                "name": "Daru", "description": "team_description 1"
            },
            {
                "team_id": "aa66c40f-6d93-484a-b418-984716514c7b",
                "name": "Proyuga", "description": "team_description 2"
            }
        ]
        TeamDTOFactory.reset_sequence(1)
        team_dtos = [
            TeamDTOFactory(
                team_id=team["team_id"], name=team["name"],
                description=team["description"]
            ) for team in team_details
        ]
        return team_dtos

    def test_given_admin_returns_list_of_teams(
            self, create_teams, team_dtos
    ):
        # Arrange
        storage = TeamStorageImplementation()
        pagination_dto = PaginationDTO(limit=5, offset=0)

        expected_dto = TeamsWithTotalTeamsCountDTOFactory(
            total_teams_count=3, teams=team_dtos
        )

        # Act
        actual_dto = storage.get_teams_with_total_teams_count_dto(
            pagination_dto=pagination_dto
        )

        # Arrange
        assert actual_dto == expected_dto
