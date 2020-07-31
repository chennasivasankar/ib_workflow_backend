import pytest

from ib_iam.storages.user_storage_implementation import UserStorageImplementation
from ib_iam.tests.common_fixtures.storages import reset_sequence


class TestGetUserOptionsDetailsStorage:
    @pytest.fixture()
    def companies(self):
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_company_factory
        reset_sequence_company_factory()
        from ib_iam.tests.factories.models import CompanyFactory
        company_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                       "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        companies = [CompanyFactory.create(company_id=company_id) for
                     company_id in company_ids]
        return companies

    @pytest.fixture()
    def teams(self):
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_team_factory
        reset_sequence_team_factory()
        from ib_iam.tests.factories.models import TeamFactory
        team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        teams = [TeamFactory.create(team_id=team_id) for team_id in team_ids]
        return teams

    @pytest.fixture()
    def roles(self):
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_role_factory
        reset_sequence_role_factory()
        role_ids = ["1", "2"]
        from ib_iam.tests.factories.models import RoleFactory
        roles = [RoleFactory.create(role_id=role_id) for role_id in role_ids]
        return roles

    @pytest.mark.django_db
    def test_get_companies(self, companies):
        # Arrange
        storage = UserStorageImplementation()
        from ib_iam.interactors.storage_interfaces.dtos import CompanyIdAndNameDTO
        expected_ouput = [
            CompanyIdAndNameDTO(company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                                company_name='company 0'),
            CompanyIdAndNameDTO(company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332',
                                company_name='company 1')]

        # Act
        output = storage.get_companies()

        # Assert
        assert output == expected_ouput

    @pytest.mark.django_db
    def test_get_teams(self, teams):
        # Arrange
        storage = UserStorageImplementation()
        from ib_iam.interactors.storage_interfaces.dtos import TeamIdAndNameDTO
        expected_ouput = [
            TeamIdAndNameDTO(team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                             team_name='team 0'),
            TeamIdAndNameDTO(team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332',
                             team_name='team 1')]

        # Act
        output = storage.get_teams()

        # Assert
        assert output == expected_ouput

    @pytest.mark.django_db
    def test_get_roles(self, roles):
        # Arrange
        storage = UserStorageImplementation()
        from ib_iam.interactors.storage_interfaces.dtos import RoleIdAndNameDTO
        expected_ouput = [
            RoleIdAndNameDTO(role_id='1', name='role 0'),
            RoleIdAndNameDTO(role_id='2', name='role 1')]

        # Act
        output = storage.get_roles()

        # Assert
        assert output == expected_ouput