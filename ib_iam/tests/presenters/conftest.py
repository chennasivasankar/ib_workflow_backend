import pytest
from ib_iam.tests.factories.storage_dtos import (
    TeamDTOFactory, TeamUserIdsDTOFactory, BasicUserDetailsDTOFactory
)
from ib_iam.tests.factories.presenter_dtos import (
    TeamWithMembersDetailsDTOFactory
)

team_ids = [
    "f2c02d98-f311-4ab2-8673-3daa00757002",
    "aa66c40f-6d93-484a-b418-984716514c7b",
    "c982032b-53a7-4dfa-a627-4701a5230765"
]
user_ids = [
    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
    '548a803c-7b48-47ba-a700-24f2ea0d1280',
    '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
    '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'
]


@pytest.fixture()
def get_list_of_team_dtos():
    TeamDTOFactory.reset_sequence(1)
    TeamUserIdsDTOFactory.reset_sequence(1)
    BasicUserDetailsDTOFactory.reset_sequence(1)

    teams_dtos = [
        TeamDTOFactory(team_id=team_id) for team_id in team_ids
    ]
    team_user_ids_dtos = [
        TeamUserIdsDTOFactory(team_id=team_id) for team_id in team_ids
    ]
    user_dtos = [
        BasicUserDetailsDTOFactory(user_id=user_id) for user_id in user_ids
    ]

    teams_dto = TeamWithMembersDetailsDTOFactory(
        total_teams_count=3,
        team_dtos=teams_dtos,
        team_user_ids_dtos=team_user_ids_dtos,
        user_dtos=user_dtos
    )
    return teams_dto