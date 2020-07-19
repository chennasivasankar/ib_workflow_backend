import factory, factory.django
from ib_iam.interactors.storage_interfaces.dtos import (
    MemberDTO,
    TeamDTO,
    TeamMemberIdsDTO,
    TeamNameAndDescriptionDTO,
    PaginationDTO,
    TeamsWithTotalTeamsCountDTO,
    UpdateTeamParametersDTO
)

member_ids = [
    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
    '548a803c-7b48-47ba-a700-24f2ea0d1280',
    '4b8fb6eb-fa7d-47c1-8726-cd917901104e'
]


class TeamDTOFactory(factory.Factory):
    class Meta:
        model = TeamDTO

    team_id = factory.Faker("uuid4")
    name = factory.sequence(lambda n: "team%d" % n)
    description = factory.sequence(lambda n: "team_description%d" % n)


class TeamMemberIdsDTOFactory(factory.Factory):
    class Meta:
        model = TeamMemberIdsDTO

    team_id = factory.Faker("uuid4")
    member_ids = factory.Iterator([
        [member_ids[1], member_ids[2]],
        [member_ids[0], member_ids[1]],
        [member_ids[0], member_ids[2]]
    ])


class MemberDTOFactory(factory.Factory):
    class Meta:
        model = MemberDTO

    member_id = factory.sequence(lambda n: "user_id-%d" % n)
    name = factory.sequence(lambda n: "user%d" % n)
    profile_pic_url = factory.sequence(lambda n: "url%d" % n)


class TeamNameAndDescriptionDTOFactory(factory.Factory):
    class Meta:
        model = TeamNameAndDescriptionDTO

    name = factory.sequence(lambda n: "team%d" % n)
    description = factory.sequence(lambda n: "team_description%d" % n)


class PaginationDTOFactory(factory.Factory):
    class Meta:
        model = PaginationDTO

    limit = factory.Iterator([5, 6, 3])
    offset = factory.Iterator([4, 3, 10])


team_ids = [
    "f2c02d98-f311-4ab2-8673-3daa00757002",
    "aa66c40f-6d93-484a-b418-984716514c7b",
    "c982032b-53a7-4dfa-a627-4701a5230765"
]
team_dtos = [
    TeamDTOFactory(team_id=team_id) for team_id in team_ids
]


class TeamsWithTotalTeamsCountDTOFactory(factory.Factory):
    class Meta:
        model = TeamsWithTotalTeamsCountDTO

    teams = factory.Iterator([
        [team_dtos[0], team_dtos[1]],
        [team_dtos[1], team_dtos[2]]
    ])
    total_teams_count = 2


class UpdateTeamParametersDTOFactory(factory.Factory):
    class Meta:
        model = UpdateTeamParametersDTO

    team_id = factory.Faker("uuid4")
    name = factory.sequence(lambda n: "team%d" % n)
    description = factory.sequence(lambda n: "team_description%d" % n)