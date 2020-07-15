import factory, factory.django
from ib_iam.interactors.storage_interfaces.dtos import (
    MemberDTO,
    BasicTeamDTO,
    TeamMembersDTO
)
from ib_iam.tests.storages.conftest import member3_id, member2_id, member1_id


class BasicTeamDTOFactory(factory.Factory):
    class Meta:
        model = BasicTeamDTO

    team_id = factory.Faker("uuid4")
    name = factory.sequence(lambda n: "team%d" % n)
    description = factory.sequence(lambda n: "team_desc%d" % n)


class TeamMembersDTOFactory(factory.Factory):
    class Meta:
        model = TeamMembersDTO

    team_id = factory.Faker("uuid4")
    member_ids = [member1_id, member2_id, member3_id]


class MemberDTOFactory(factory.Factory):
    class Meta:
        model = MemberDTO

    member_id = factory.Faker("uuid4")
    name = factory.sequence(lambda n: "user%d" % n)
    profile_pic_url = factory.sequence(lambda n: "profile_pic_url%d" % n)
