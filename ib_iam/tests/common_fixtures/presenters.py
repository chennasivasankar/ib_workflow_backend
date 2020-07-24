import pytest


@pytest.fixture()
def company_dtos():
    from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
    company_dtos = CompanyDTOFactory.create_batch(3)
    return company_dtos


@pytest.fixture()
def team_dtos():
    from ib_iam.tests.factories.storage_dtos import TeamIdAndNameDTOFactory
    team_dtos = TeamIdAndNameDTOFactory.create_batch(3)
    return team_dtos


@pytest.fixture()
def role_dtos():
    from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
    role_dtos = RoleDTOFactory.create_batch(3)
    return role_dtos
