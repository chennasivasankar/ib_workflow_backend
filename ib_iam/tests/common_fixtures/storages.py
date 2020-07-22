import pytest

from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
from ib_iam.tests.factories.models import UserDetailsFactory, CompanyFactory, \
    UserTeamFactory, TeamFactory, RoleFactory, UserRoleFactory
from ib_iam.tests.factories.storage_dtos \
    import UserDTOFactory, UserTeamDTOFactory, UserCompanyDTOFactory, \
    UserRoleDTOFactory


def reset_sequence():
    UserDTOFactory.reset_sequence()
    UserTeamDTOFactory.reset_sequence()
    UserCompanyDTOFactory.reset_sequence()
    UserRoleDTOFactory.reset_sequence()
    UserProfileDTOFactory.reset_sequence(0)
    UserDetailsFactory.reset_sequence(0)
    CompanyFactory.reset_sequence(0)
    UserTeamFactory.reset_sequence(0)
    UserRoleFactory.reset_sequence(0)
    RoleFactory.reset_sequence(0)
    TeamFactory.reset_sequence(0)


@pytest.fixture()
def user_not_admin():
    reset_sequence()
    user = UserDetailsFactory.create(user_id="user0", is_admin=False)
    return user


@pytest.fixture()
def users_company():
    reset_sequence()
    users = []
    companies = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                 "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    for company_id in companies:
        company = CompanyFactory.create(company_id=company_id)
        for i in range(1, 4, 1):
            user = UserDetailsFactory.create(company=company)
            users.append(user)
    return users


@pytest.fixture()
def users_team():
    reset_sequence()
    users = []
    teams = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
             "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    for team_id in teams:
        team = TeamFactory.create(team_id=team_id)
        for i in range(1, 4):
            user = UserTeamFactory.create(user_id=f"user{i}", team=team)
            users.append(user)
    return users


@pytest.fixture()
def users_role():
    reset_sequence()
    users = []
    roles = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
             "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    for role_id in roles:
        role = RoleFactory.create(id=role_id)
        for i in range(1, 4):
            user = UserRoleFactory.create(user_id=f"user{i}", role=role)
            users.append(user)
    return users


@pytest.fixture()
def companies():
    reset_sequence()
    companies = CompanyFactory.create_batch(3)
    return companies


@pytest.fixture()
def company_dtos():
    from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
    company_dtos = CompanyDTOFactory.create_batch(3)
    return company_dtos


@pytest.fixture()
def team_dtos():
    from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
    team_dtos = TeamDTOFactory.create_batch(3)
    return team_dtos


@pytest.fixture()
def role_dtos():
    from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
    role_dtos = RoleDTOFactory.create_batch(3)
    return role_dtos


@pytest.fixture()
def configuration_details_dto():
    from ib_iam.interactors.presenter_interfaces.dtos \
        import ConfigurationDetailsDto
    configuration_details_dto = ConfigurationDetailsDto(
        companies=company_dtos,
        teams=team_dtos,
        roles=role_dtos
    )
    return configuration_details_dto
