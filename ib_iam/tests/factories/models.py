import uuid

import factory

from ib_iam import models
from ib_iam.models import Role, Team, Company
from ib_iam.models.user import UserDetails, UserTeam, UserRole


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    company_id = factory.LazyFunction(uuid.uuid4)
    name = factory.sequence(lambda number: "company %s" % number)
    description = factory.sequence(lambda number: "description %s" % number)
    logo_url = factory.sequence(lambda number: "url %s" % number)


class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    team_id = factory.LazyFunction(uuid.uuid4)
    name = factory.sequence(lambda number: "team %s" % number)
    description = factory.sequence(lambda n: "team_description %d" % n)
    created_by = factory.sequence(lambda n: "user_id-%d" % n)


class RoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Role

    id = factory.Faker("uuid4")
    role_id = factory.sequence(lambda number: "ROLE_%s" % number)
    name = factory.sequence(lambda number: "role %s" % number)
    description = factory.Sequence(lambda n: 'payment_description%s' % n)


class UserDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDetails

    user_id = factory.sequence(lambda number: "user%s" % number)
    is_admin = False
    name = factory.Faker('name')
    company = factory.SubFactory(CompanyFactory)


class UserTeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserTeam

    user_id = factory.sequence(lambda number: "user%s" % number)
    team = factory.Iterator(models.Team.objects.all())


class UserRoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserRole

    user_id = factory.sequence(lambda number: "user%s" % number)
    role = factory.Iterator(Role.objects.all())


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDetails

    user_id = factory.sequence(lambda n: n)
    is_admin = False
