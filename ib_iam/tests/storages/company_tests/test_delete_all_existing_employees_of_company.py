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
class TestDeleteAllExistingEmployeesOfCompany:

    def test_whether_it_deletes_relation_of_all_existing_employees_or_not(
            self, create_company, create_employees_to_company):
        storage = CompanyStorageImplementation()
        company_id = create_company

        storage.delete_all_existing_employees_of_company(
            company_id=company_id)

        employee_objects = UserDetails.objects.filter(
            company_id=company_id)
        assert len(employee_objects) == 0
