import pytest

from ib_iam.models import UserDetails
from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation

@pytest.fixture
def create_company():
    company_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
    from ib_iam.tests.factories.models import CompanyFactory
    company_object = CompanyFactory.create(company_id=company_id)
    return company_object


@pytest.fixture
def create_employees_to_company(create_company):
    company_object = create_company
    from ib_iam.tests.factories.models import UserDetailsFactory
    user_ids = ['2bdb417e-4632-419a-8ddd-085ea272c6eb',
                '4b8fb6eb-fa7d-47c1-8726-cd917901104e']
    for user_id in user_ids:
        UserDetailsFactory.create(user_id=user_id, company=company_object)
    return user_ids


@pytest.mark.django_db
class TestDeleteEmployeesFromCompany:

    def test_whether_it_deletes_given_employees_from_company(
            self, create_company, create_employees_to_company):
        storage = CompanyStorageImplementation()
        employee_ids_to_delete = create_employees_to_company
        company_id = create_company

        storage.delete_employees_from_company(
            company_id=company_id, employee_ids=employee_ids_to_delete)

        employee_objects = UserDetails.objects.filter(
            company_id=company_id, user_id__in=employee_ids_to_delete)
        assert list(employee_objects) == []

    def test_given_employees_it_deletes_only_those_employees_or_not(
            self, create_company, create_employees_to_company):
        storage = CompanyStorageImplementation()
        total_employee_ids = create_employees_to_company
        employee_ids_to_delete = ['2bdb417e-4632-419a-8ddd-085ea272c6eb']
        company_id = create_company

        storage.delete_employees_from_company(
            company_id=company_id, employee_ids=employee_ids_to_delete)

        employee_objects = UserDetails.objects.filter(
            company_id=company_id, user_id__in=total_employee_ids)
        assert len(employee_objects) == 1
