import pytest
from ib_iam.tests.factories.storage_dtos import (
    BasicTeamDTOFactory, TeamMembersDTOFactory, MemberDTOFactory
)
from ib_iam.tests.factories.presenter_dtos import (
    TeamWithMembersDetailsDTOFactory
)
from ib_iam.tests.storages.conftest import (
    team1_id, team2_id, team3_id, member1_id, member2_id,
    member3_id, member4_id
)


@pytest.fixture()
def get_list_of_team_dtos():
    BasicTeamDTOFactory.reset_sequence(1)
    TeamMembersDTOFactory.reset_sequence(1)
    MemberDTOFactory.reset_sequence(1)
    teams_dtos = [
        BasicTeamDTOFactory(team_id=team1_id),
        BasicTeamDTOFactory(team_id=team2_id),
        BasicTeamDTOFactory(team_id=team3_id),
    ]
    team_member_ids_dtos = [
        TeamMembersDTOFactory(team_id=team1_id, member_ids=[member1_id, member2_id, member3_id]),
        TeamMembersDTOFactory(team_id=team2_id, member_ids=[member4_id, member1_id]),
        TeamMembersDTOFactory(team_id=team3_id, member_ids=[member2_id, member3_id, member4_id])
    ]
    members_dtos = [
        MemberDTOFactory(
            member_id=member_id
        ) for member_id in [member1_id, member2_id, member3_id, member4_id]
    ]

    teams_dto = TeamWithMembersDetailsDTOFactory(
        total_teams = 3,
        team_dtos=teams_dtos,
        team_member_ids_dtos=team_member_ids_dtos,
        member_dtos=members_dtos
    )
    return teams_dto
