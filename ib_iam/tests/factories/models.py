import uuid

import factory, factory.django
from ib_iam.models import UserDetails, Team, TeamMember, Company


class UserFactory(factory.django.DjangoModelFactory):
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


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    company_id = factory.LazyFunction(uuid.uuid4)
    name = factory.sequence(lambda number: "company %s" % number)


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    company_id = factory.LazyFunction(uuid.uuid4)
    name = factory.sequence(lambda number: "company %s" % number)
    description = factory.sequence(lambda number: "description %s" % number)
    logo_url = factory.sequence(lambda number: "url %s" % number)


class UserDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDetails

    user_id = factory.sequence(lambda number: "user%s" % number)
    is_admin = False
    company = factory.SubFactory(CompanyFactory)
