import factory, factory.django
from ib_iam.models import UserDetails, Team, TeamMember


class UserDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDetails

    user_id = factory.sequence(lambda n: "user_id-%d" % n)
    is_admin = False


class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    team_id = factory.Faker("uuid4")
    name = factory.sequence(lambda n: "team%d" % n)
    description = factory.sequence(lambda n: "team_description%d" % n)
    created_by = factory.sequence(lambda n: "user_id-%d" % n)


class TeamMemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TeamMember

    team = factory.SubFactory(TeamFactory)
    member_id = factory.sequence(lambda n: "user_id-%d" % n)
