import pytest
from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation


@pytest.fixture
def create_companies():
    from ib_iam.tests.factories.models import CompanyFactory
    company_name = "company1"
    company_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
    CompanyFactory.create(company_id=company_id, name=company_name)
    return company_id, company_name


@pytest.mark.django_db
class TestGetCompanyIdIfCompanyNameAlreadyExists:
    def test_given_company_name_already_exists_it_returns_company_id(
            self, create_companies
    ):
        storage = CompanyStorageImplementation()
        expected_company_id, existing_company_name = create_companies

        actual_company_id = storage.get_company_id_if_company_name_already_exists(
            name=existing_company_name
        )

        assert actual_company_id == expected_company_id

    def test_given_company_name_does_not_exists_it_returns_none(
            self, create_companies
    ):
        storage = CompanyStorageImplementation()
        requested_name = "company0"
        expected_value = None

        actual_value = storage.get_company_id_if_company_name_already_exists(
            name=requested_name
        )

        assert actual_value == expected_value
