import pytest

from ib_iam.storages.get_user_options_storage_implementation import GetUserOptionsStorageImplementation
from ib_iam.tests.common_fixtures.storages import reset_sequence


class TestGetUserOptionsDetailsStorage:
    @pytest.fixture()
    def companies(self):
        reset_sequence()
        from ib_iam.tests.factories.models import CompanyFactory
        company_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                       "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        companies = [CompanyFactory.create(company_id=company_id) for
                     company_id in company_ids]
        return companies

    @pytest.fixture()
    def teams(self):
        reset_sequence()
        from ib_iam.tests.factories.models import TeamFactory
        team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        teams = [TeamFactory.create(team_id=team_id) for team_id in team_ids]
        return teams

    @pytest.fixture()
    def roles(self):
        reset_sequence()
        role_ids = ["1", "2"]
        from ib_iam.tests.factories.models import RoleFactory
        roles = [RoleFactory.create(role_id=role_id) for role_id in role_ids]
        return roles

    @pytest.mark.django_db
    def test_get_companies(self, companies):
        # Arrange
        storage = GetUserOptionsStorageImplementation()
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
        storage = GetUserOptionsStorageImplementation()
        from ib_iam.interactors.storage_interfaces.dtos import TeamDTO
        expected_ouput = [
            TeamDTO(team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                    team_name='team 0'),
            TeamDTO(team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332',
                    team_name='team 1')]

        # Act
        output = storage.get_teams()

        # Assert
        assert output == expected_ouput

    @pytest.mark.django_db
    def test_get_roles(self, roles):
        # Arrange
        storage = GetUserOptionsStorageImplementation()
        from ib_iam.interactors.storage_interfaces.dtos import RoleIdAndNameDTO
        expected_ouput = [
            RoleIdAndNameDTO(role_id='1', name='role 0'),
            RoleIdAndNameDTO(role_id='2', name='role 1')]

        # Act
        output = storage.get_roles()

        # Assert
        assert output == expected_ouput
