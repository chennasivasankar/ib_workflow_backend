import pytest
from ib_iam.tests.factories.storage_dtos import \
    CompanyNameLogoAndDescriptionDTOFactory
from ib_iam.models import Company
from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation
from ib_iam.tests.common_fixtures.adapters.uuid_mock import uuid_mock


@pytest.mark.django_db
class TestAddTeam:

    def test_given_valid_details_return_company_id(self, mocker):
        storage = CompanyStorageImplementation()
        company_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        mock = uuid_mock(mocker)
        mock.return_value = company_id
        company_name = "company1"
        company_description = "company_description1"
        company_logo_url = "logo_url1"
        expected_company_id = company_id
        CompanyNameLogoAndDescriptionDTOFactory.reset_sequence(1)
        company_name_logo_and_description_dto = CompanyNameLogoAndDescriptionDTOFactory()

        actual_company_id = storage.add_company(
            company_name_logo_and_description_dto=company_name_logo_and_description_dto)

        company_object = Company.objects.get(company_id=actual_company_id)
        assert actual_company_id == expected_company_id
        assert company_object.name == company_name
        assert company_object.description == company_description
        assert company_object.logo_url == company_logo_url
