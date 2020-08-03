import pytest

from ib_iam.models import Company
from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation


@pytest.fixture
def create_company():
    company_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
    from ib_iam.tests.factories.models import CompanyFactory
    CompanyFactory.create(company_id=company_id)
    return company_id


@pytest.mark.django_db
class TestDeleteCompany:

    def test_whether_it_delete_an_existing_company(
            self, create_company
    ):
        storage = CompanyStorageImplementation()
        company_id = create_company

        storage.delete_company(
            company_id=company_id
        )

        company_objects = Company.objects.filter(company_id=company_id)
        assert list(company_objects) == []
