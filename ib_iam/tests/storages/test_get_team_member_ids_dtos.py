import pytest
from ib_iam.storages.team_storage_implementation import TeamStorageImplementation
from ib_iam.tests.factories import TeamMemberIdsDTOFactory

team_ids = [
    'f2c02d98-f311-4ab2-8673-3daa00757002',
]


@pytest.mark.django_db
class TestGetTeamMemberIdsDtos:

    def test_whether_it_returns_list_of_team_members_dtos(
            self, create_members, create_teams, snapshot
    ):
        sql_storage = TeamStorageImplementation()
        expected_dto = [
            TeamMemberIdsDTOFactory(
                team_id='f2c02d98-f311-4ab2-8673-3daa00757002',
                member_ids=[
                    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e'
                ]
            )
        ]
        actual_dto = sql_storage.get_team_member_ids_dtos(
            team_ids=team_ids
        )
        assert actual_dto == expected_dto
