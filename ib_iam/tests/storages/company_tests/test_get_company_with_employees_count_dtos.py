import pytest

from ib_iam.interactors.storage_interfaces.dtos import CompanyDTO, CompanyWithEmployeesCountDTO
from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation
from ib_iam.tests.factories.models import CompanyFactory, UserDetailsFactory


@pytest.mark.django_db
class TestGetCompanyDTOs:

    def test_whether_it_returns_list_of_company_dtos(self):
        company_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
        storage = CompanyStorageImplementation()
        CompanyFactory.reset_sequence(1)
        UserDetailsFactory.reset_sequence(1)
        company_object = CompanyFactory.create(company_id=company_id)
        UserDetailsFactory.create_batch(size=3, company=company_object)
        from ib_iam.models import UserDetails
        UserDetails.objects.values()
        expected_dtos = [
            CompanyWithEmployeesCountDTO(
                company_id=company_id,
                no_of_employees=3
            )
        ]

        actual_dtos = storage.get_company_with_employees_count_dtos()

        assert actual_dtos == expected_dtos
