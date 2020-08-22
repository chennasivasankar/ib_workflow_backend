import factory

from ib_iam import models
from ib_iam.models import Role, Team, Company, Country, State, City, Project
from ib_iam.models.team_member_level import TeamMemberLevel
from ib_iam.models.user import UserDetails, UserTeam, UserRole


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    company_id = factory.Faker("uuid4")
    name = factory.sequence(lambda number: "company %s" % number)
    description = factory.sequence(lambda number: "description %s" % number)
    logo_url = factory.sequence(lambda number: "url %s" % number)


class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    team_id = factory.Faker("uuid4")
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
    cover_page_url = factory.sequence(lambda n: "url%d" % n)


class UserTeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserTeam

    user_id = factory.sequence(lambda number: "user%s" % number)
    team = factory.Iterator(models.Team.objects.all())
    team_member_level = None
    immediate_superior_team_user = None


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


class TeamMemberLevelFactory(factory.DjangoModelFactory):
    class Meta:
        model = TeamMemberLevel

    id = factory.Faker("uuid4")
    team = factory.SubFactory(TeamFactory)
    level_name = factory.Iterator([
        "Developer",
        "Software Developer Lead",
        "Engineer Manager",
        "Product Owner"
    ])
    level_hierarchy = factory.Iterator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.sequence(lambda counter: "country_name{}".format(counter))


class StateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = State

    name = factory.sequence(lambda counter: "state_name{}".format(counter))


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = factory.sequence(lambda counter: "city_name{}".format(counter))


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    project_id = factory.Sequence(lambda n: 'project %s' % n)
    name = factory.Sequence(lambda n: 'name %s' % n)
    description = factory.Sequence(lambda n: 'description %s' % n)
    logo_url = factory.Sequence(lambda n: 'logo %s' % n)
