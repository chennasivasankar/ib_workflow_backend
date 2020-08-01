import pytest
from ib_iam.storages.company_storage_implementation import (
    CompanyStorageImplementation)
from ib_iam.tests.factories.storage_dtos import \
    CompanyIdWithEmployeeIdsDTOFactory

company_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
user_ids = ['2bdb417e-4632-419a-8ddd-085ea272c6eb',
            '4b8fb6eb-fa7d-47c1-8726-cd917901104e']


@pytest.fixture
def create_company():
    from ib_iam.tests.factories.models import CompanyFactory
    company_object = CompanyFactory.create(company_id=company_id)
    return company_object


@pytest.fixture
def create_employees(create_company):
    company_object = create_company
    from ib_iam.tests.factories.models import UserDetailsFactory
    user_objects = [
        UserDetailsFactory.create(company=company_object, user_id=user_id)
        for user_id in user_ids
    ]
    return user_objects


@pytest.mark.django_db
class TestGetCompanyEmployeeIdsDtos:

    def test_whether_it_returns_list_of_company_employee_ids_dtos(
            self, create_employees
    ):
        storage = CompanyStorageImplementation()
        expected_dto = [
            CompanyIdWithEmployeeIdsDTOFactory(
                company_id='f2c02d98-f311-4ab2-8673-3daa00757002',
                employee_ids=[
                    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e']
            )
        ]

        actual_dto = storage.get_company_employee_ids_dtos(
            company_ids=[company_id])

        assert actual_dto == expected_dto
