import pytest
from ib_iam.storages.team_storage_implementation import TeamStorageImplementation
from ib_iam.interactors.storage_interfaces.team_storage_interface import PaginationDTO
from ib_iam.tests.factories.storage_dtos import TeamsWithTotalTeamsCountDTOFactory, TeamDTOFactory

team_ids = [
    'f2c02d98-f311-4ab2-8673-3daa00757002',
    'aa66c40f-6d93-484a-b418-984716514c7b',
    'c982032b-53a7-4dfa-a627-4701a5230765'
]


@pytest.mark.django_db
class TestGetTeamsWithTotalTeamsCountDto:

    def test_given_admin_returns_list_of_teams(
            self, create_teams
    ):
        storage = TeamStorageImplementation()
        pagination_dto = PaginationDTO(limit=5, offset=0)
        TeamDTOFactory.reset_sequence(1)
        team_dtos = [
            TeamDTOFactory(team_id=team_id) for team_id in team_ids
        ]
        expected_dto = TeamsWithTotalTeamsCountDTOFactory(
            total_teams_count=3,
            teams=team_dtos)

        actual_dto = storage.get_teams_with_total_teams_count_dto(
            pagination_dto=pagination_dto)

        assert actual_dto == expected_dto
