import pytest
from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation
from ib_iam.models import Company
from ib_iam.interactors.storage_interfaces.dtos import \
    CompanyWithUserIdsDTO


@pytest.fixture
def create_company():
    company_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
    from ib_iam.tests.factories.models import CompanyFactory
    company_object = CompanyFactory.create(company_id=company_id)
    return company_object


@pytest.mark.django_db
class TeatUpdateCompanyDetails:
    def test_whether_it_updates_the_company_details(self, create_company):
        company_id = create_company
        expected_company_name = "new team"
        expected_description = "description"
        expected_logo_url = ""
        storage = CompanyStorageImplementation()
        company_with_user_ids_dto = CompanyWithUserIdsDTO(
            company_id=company_id,
            name=expected_company_name,
            description=expected_description,
            logo_url=expected_logo_url
        )

        storage.update_team_details(
            company_with_user_ids_dto=company_with_user_ids_dto)

        company_object = Company.objects.get(company_id=company_id)
        assert company_object.name == expected_company_name
        assert company_object.description == expected_description
        assert company_object.logo_url == expected_logo_url
