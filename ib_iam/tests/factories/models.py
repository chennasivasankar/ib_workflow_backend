import factory

from ib_iam import models
from ib_iam.models import ProjectRole, Team, Company, Country, State, City, \
    Project, ProjectTeam, UserAuthToken
from ib_iam.models.team_member_level import TeamMemberLevel
from ib_iam.models.user import UserDetails, TeamUser, UserRole


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    company_id = factory.Faker("uuid4")
    name = factory.sequence(lambda number: "company %s" % number)
    description = factory.sequence(lambda number: "description %s" % number)
    logo_url = "http://sample.com"


class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    team_id = factory.Faker("uuid4")
    name = factory.sequence(lambda number: "team %s" % number)
    description = factory.sequence(lambda n: "team_description %d" % n)
    created_by = factory.sequence(lambda n: "user_id-%d" % n)


class UserDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDetails

    user_id = factory.sequence(lambda number: "user%s" % number)
    is_admin = False
    name = factory.Faker('name')
    company = factory.SubFactory(CompanyFactory)
    cover_page_url = "http://sample.com"


class TeamUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TeamUser

    user_id = factory.sequence(lambda number: "user%s" % number)
    team = factory.Iterator(models.Team.objects.all())
    team_member_level = None
    immediate_superior_team_user = None


class UserRoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserRole

    user_id = factory.sequence(lambda number: "user%s" % number)
    project_role = factory.Iterator(ProjectRole.objects.all())


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
    display_id = factory.Sequence(lambda n: 'display_id %s' % n)
    name = factory.Sequence(lambda n: 'name %s' % n)
    description = factory.Sequence(lambda n: 'description %s' % n)
    logo_url = "http://sample.com"


class ProjectRoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectRole
        django_get_or_create = ('role_id', 'name', 'description', 'project')

    role_id = factory.sequence(lambda number: "ROLE_%s" % number)
    name = factory.sequence(lambda number: "role %s" % number)
    description = factory.Sequence(lambda n: 'role description %s' % n)
    project = factory.SubFactory(ProjectFactory)


class ProjectTeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectTeam

    project = factory.SubFactory(ProjectFactory)
    team = factory.SubFactory(ProjectFactory)


class UserAuthTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserAuthToken

    user_id = factory.Sequence(lambda n: 'user_id_%s' % n)
    token = factory.Sequence(lambda n: 'user_token_%s' % n)
