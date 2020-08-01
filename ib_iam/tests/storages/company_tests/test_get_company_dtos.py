import pytest

from ib_iam.interactors.storage_interfaces.dtos import CompanyDTO
from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation
from ib_iam.tests.factories.models import CompanyFactory


@pytest.mark.django_db
class TestGetCompanyDTOs:

    def test_whether_it_returns_list_of_company_dtos(self):
        company_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
        storage = CompanyStorageImplementation()
        CompanyFactory.reset_sequence(1)
        CompanyFactory(company_id=company_id)
        expected_dtos = [
            CompanyDTO(
                company_id=company_id,
                name="company 1",
                description="description 1",
                logo_url="url 1"
            )
        ]

        actual_dtos = storage.get_company_dtos()

        assert actual_dtos == expected_dtos
