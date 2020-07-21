import pytest

from ib_iam.storages.storage_implementation import StorageImplementation
from ib_iam.tests.common_fixtures.storages import reset_sequence


@pytest.fixture()
def company_dtos():
    from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
    company_dtos = CompanyDTOFactory.create_batch(4)
    return company_dtos


@pytest.fixture()
def companies():
    reset_sequence()
    from ib_iam.tests.factories.models import CompanyFactory
    company_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                   "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    companies = [CompanyFactory.create(company_id=id) for id in company_ids]
    return companies


@pytest.fixture()
def teams():
    reset_sequence()
    from ib_iam.tests.factories.models import TeamFactory
    team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    teams = [TeamFactory.create(team_id=id) for id in team_ids]
    return teams


@pytest.fixture()
def roles():
    reset_sequence()
    role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    from ib_iam.tests.factories.models import RoleFactory
    roles = [RoleFactory.create(id=id) for id in role_ids]
    return roles


class TestGetConfigurationDetailsStorage:
    @pytest.mark.django_db
    def test_get_companies(self, companies):
        # Arrange
        storage = StorageImplementation()
        from ib_iam.interactors.storage_interfaces.dtos import CompanyDTO
        expected_ouput = [
            CompanyDTO(company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                       company_name='company 0'),
            CompanyDTO(company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332',
                       company_name='company 1')]

        # Act
        output = storage.get_companies()

        # Assert
        assert output == expected_ouput

    @pytest.mark.django_db
    def test_get_teams(self, teams):
        # Arrange
        storage = StorageImplementation()
        from ib_iam.interactors.storage_interfaces.dtos import TeamDTO
        expected_ouput = [
            TeamDTO(team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331', team_name='team 0'),
            TeamDTO(team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332', team_name='team 1')]


        # Act
        output = storage.get_teams()

        # Assert
        assert output == expected_ouput

    @pytest.mark.django_db
    def test_get_roles(self, roles):
        # Arrange
        storage = StorageImplementation()
        from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
        expected_ouput = [
            RoleDTO(id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331', role_name='role 0'),
            RoleDTO(id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332', role_name='role 1')]


        # Act
        output = storage.get_roles()

        # Assert
        assert output == expected_ouput