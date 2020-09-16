import pytest
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)
from ib_iam.tests.factories.storage_dtos import TeamUserIdsDTOFactory

team_ids = [
    'f2c02d98-f311-4ab2-8673-3daa00757002'
]


@pytest.mark.django_db
class TestGetTeamUserIdsDtos:

    def test_whether_it_returns_list_of_team_members_dtos(
            self, create_members, create_teams
    ):
        # Arrange
        storage = TeamStorageImplementation()
        expected_dto = [
            TeamUserIdsDTOFactory(
                team_id='f2c02d98-f311-4ab2-8673-3daa00757002',
                user_ids=[
                    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e'
                ]
            )
        ]

        # Act
        actual_dto = storage.get_team_user_ids_dtos(
            team_ids=team_ids
        )

        # Assert
        assert actual_dto == expected_dto
