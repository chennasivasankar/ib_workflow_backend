import pytest

from ib_iam.tests.factories.models import UserDetailsFactory, CompanyFactory, \
    UserTeamFactory, TeamFactory, ProjectRoleFactory, UserRoleFactory

from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
from ib_iam.tests.factories.storage_dtos \
    import UserDTOFactory, UserTeamDTOFactory, UserCompanyDTOFactory, \
    UserRoleDTOFactory, CompanyIdAndNameDTOFactory, TeamDTOFactory, RoleDTOFactory


def reset_sequence():
    UserDetailsFactory.reset_sequence(0)
    CompanyFactory.reset_sequence(0)
    UserTeamFactory.reset_sequence(0)
    UserRoleFactory.reset_sequence(0)
    ProjectRoleFactory.reset_sequence(0)
    TeamFactory.reset_sequence(0)

    CompanyIdAndNameDTOFactory.reset_sequence(0)
    TeamDTOFactory.reset_sequence(0)
    RoleDTOFactory.reset_sequence(0)
    UserRoleDTOFactory.reset_sequence(0)
    UserProfileDTOFactory.reset_sequence(0)
    UserDTOFactory.reset_sequence(0)
    UserTeamDTOFactory.reset_sequence(0)
    UserCompanyDTOFactory.reset_sequence(0)


@pytest.fixture()
def user_not_admin():
    reset_sequence()
    user = UserDetailsFactory.create(
        user_id="user0", is_admin=False, company=None)
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
def users_role():
    reset_sequence()
    users = []
    roles = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
             "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    for role_id in roles:
        role = ProjectRoleFactory.create(id=role_id)
        for i in range(1, 4):
            user = UserRoleFactory.create(user_id=f"user{i}", project_role=role)
            users.append(user)
    return users


@pytest.fixture()
def companies():
    reset_sequence()
    companies = CompanyFactory.create_batch(3)
    return companies
