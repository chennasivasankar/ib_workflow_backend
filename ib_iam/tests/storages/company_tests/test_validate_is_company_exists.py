import pytest
from ib_iam.exceptions.custom_exceptions import InvalidCompanyId
from ib_iam.storages.company_storage_implementation import (
    CompanyStorageImplementation
)


@pytest.fixture
def create_company():
    company_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
    from ib_iam.tests.factories.models import CompanyFactory
    CompanyFactory.create(company_id=company_id)
    return company_id


@pytest.mark.django_db
class TestValidateIsCompanyExists:
    def test_given_invalid_company_raises_invalid_company_id_exception(
            self, create_company
    ):
        storage = CompanyStorageImplementation()
        invalid_company_id = 'd81337b5-da0c-44e7-9773-245338c01ccc'

        with pytest.raises(InvalidCompanyId):
            storage.validate_is_company_exists(company_id=invalid_company_id)

    def test_given_company_exists_returns_none(
            self, create_company
    ):
        storage = CompanyStorageImplementation()
        company_id = create_company
        expected_result = None

        actual_result = \
            storage.validate_is_company_exists(company_id=company_id)

        assert actual_result == expected_result
