import uuid

import factory, factory.django
from ib_iam.models import User, Team, TeamMember


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.sequence(lambda n: n)
    user_id = factory.sequence(lambda n: "user_id-%d" % n)
    is_admin = False

    class Params:
        admin = factory.Trait(
            is_admin=True
        )


class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    team_id = factory.Faker("uuid4")
    name = factory.sequence(lambda n: "team_name%d" % n)
    description = factory.sequence(lambda n: "team_desc%d" % n)
    created_by = factory.sequence(lambda n: "user_id-%d" % n)


class TeamMemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TeamMember

    team = factory.SubFactory(TeamFactory)
    member_id = factory.sequence(lambda n: "user_id-%d" % n)
