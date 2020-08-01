import pytest
from ib_iam.models import Company
from ib_iam.storages.company_storage_implementation import CompanyStorageImplementation


@pytest.fixture
def create_company():
    from ib_iam.tests.factories.models import CompanyFactory
    company_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
    CompanyFactory.create(company_id=company_id)
    return company_id


@pytest.fixture
def create_users():
    from ib_iam.tests.factories.models import UserDetailsFactory
    user_ids = [
        '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a',
        '8bcf545d-4573-4bc2-b037-16c856d37287'
    ]
    for user_id in user_ids:
        UserDetailsFactory.create(user_id=user_id)
    return user_ids


@pytest.mark.django_db
class TestAddUsersToCompany:

    def test_given_valid_details_return_nothing(
            self, create_users, create_company):
        storage = CompanyStorageImplementation()
        company_id = create_company
        user_ids = create_users
        no_of_employees_added = 2

        storage.add_users_to_company(
            company_id=company_id,
            user_ids=user_ids
        )

        from django.db.models import Count
        company_member_object, = Company.objects.filter(
            company_id=company_id).annotate(no_of_employees=Count("users"))
        assert company_member_object.no_of_employees == no_of_employees_added
