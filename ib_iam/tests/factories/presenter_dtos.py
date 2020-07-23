import factory

from ib_iam.interactors.presenter_interfaces.dtos import \
    CompleteUsersDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO


class CompleteUserDetailsDTOFactory(factory.Factory):
    class Meta:
        model = CompleteUsersDetailsDTO

    user_id = factory.sequence(lambda number: "user%s" % number)
    name = factory.sequence(lambda number: "user%s" % number)
    email = factory.sequence(lambda number: "useremail%s@gmail.com" % number)
    teams = factory.SubFactory(UserTeamDTO)


import factory, factory.django
from ib_iam.interactors.presenter_interfaces.dtos import \
    TeamWithMembersDetailsDTO
from ib_iam.tests.factories.storage_dtos import (
    TeamDTOFactory, TeamMemberIdsDTOFactory, MemberDTOFactory
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

team_dtos = [
    TeamDTOFactory(team_id=team_id) for team_id in team_ids
]
team_member_ids_dtos = [
    TeamMemberIdsDTOFactory(team_id=team_id) for team_id in team_ids
]
members_dtos = [
    MemberDTOFactory(member_id=member_id) for member_id in member_ids
]


class TeamWithMembersDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TeamWithMembersDetailsDTO

    total_teams_count = 0
    team_dtos = factory.Iterator([
        [team_dtos[0], team_dtos[1]],
        [team_dtos[2], team_dtos[0]],
    ])
    team_member_ids_dtos = factory.Iterator([
        [team_member_ids_dtos[0], team_member_ids_dtos[1]],
        [team_member_ids_dtos[2], team_member_ids_dtos[0]]
    ])
    member_dtos = factory.Iterator([
        [members_dtos[1], members_dtos[2], members_dtos[0]],
        [members_dtos[1], members_dtos[2], members_dtos[0]]
    ])
