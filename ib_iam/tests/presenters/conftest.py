import pytest
from ib_iam.tests.factories import (
    TeamDTOFactory, TeamMemberIdsDTOFactory, MemberDTOFactory
)
from ib_iam.tests.factories.presenter_dtos import (
    TeamWithMembersDetailsDTOFactory
)

team_ids = [
    "f2c02d98-f311-4ab2-8673-3daa00757002",
    "aa66c40f-6d93-484a-b418-984716514c7b",
    "c982032b-53a7-4dfa-a627-4701a5230765"
]
member_ids = [
    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
    '548a803c-7b48-47ba-a700-24f2ea0d1280',
    '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
    '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'
]


@pytest.fixture()
def get_list_of_team_dtos():
    TeamDTOFactory.reset_sequence(1)
    TeamMemberIdsDTOFactory.reset_sequence(1)
    MemberDTOFactory.reset_sequence(1)

    teams_dtos = [
        TeamDTOFactory(team_id=team_id) for team_id in team_ids
    ]
    team_member_ids_dtos = [
        TeamMemberIdsDTOFactory(team_id=team_id) for team_id in team_ids
    ]
    members_dtos = [
        MemberDTOFactory(member_id=member_id) for member_id in member_ids
    ]

    teams_dto = TeamWithMembersDetailsDTOFactory(
        total_teams_count=3,
        team_dtos=teams_dtos,
        team_member_ids_dtos=team_member_ids_dtos,
        member_dtos=members_dtos
    )
    return teams_dto
