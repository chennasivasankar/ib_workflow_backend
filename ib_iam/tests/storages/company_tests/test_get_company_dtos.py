import pytest

from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation
from ib_iam.tests.factories.models import CompanyFactory


@pytest.mark.django_db
class TestGetCompanyDTOs:

    @pytest.fixture
    def company_objects(self):
        company_details = [
            {"company_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
             "name": "Proyuga"},
            {"company_id": "f2c02d98-f311-4ab2-8673-3daa00757003",
             "name": "Arogya"}
        ]
        CompanyFactory.reset_sequence(1)
        company_objects = [
            CompanyFactory(company_id=company["company_id"],
                           name=company["name"])
            for company in company_details
        ]
        return company_objects

    @pytest.fixture
    def company_details_for_dtos(self):
        company_details = [
            {
                "company_id": "f2c02d98-f311-4ab2-8673-3daa00757003",
                "name": "Arogya",
                "description": "description 2",
                "logo_url": "url 2"
            },
            {
                "company_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
                "name": "Proyuga",
                "description": "description 1",
                "logo_url": "url 1"
            }
        ]
        return company_details

    @pytest.fixture
    def company_dtos(self, company_details_for_dtos):
        from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
        CompanyDTOFactory.reset_sequence(1)
        company_dtos = [
            CompanyDTOFactory(company_id=company["company_id"],
                              name=company["name"],
                              description=company["description"],
                              logo_url=company["logo_url"]
                              )
            for company in company_details_for_dtos
        ]
        return company_dtos

    def test_whether_it_returns_list_of_company_dtos(
            self, company_objects, company_dtos):
        storage = CompanyStorageImplementation()
        expected_dtos = company_dtos

        actual_dtos = storage.get_company_dtos()

        assert actual_dtos == expected_dtos
