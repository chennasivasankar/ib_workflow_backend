from typing import List, Optional

from ib_iam.interactors.storage_interfaces.company_storage_interface import \
    CompanyStorageInterface
from ib_iam.interactors.storage_interfaces.dtos import \
    CompanyNameLogoAndDescriptionDTO, CompanyDTO, CompanyIdWithEmployeeIdsDTO
from ib_iam.models import UserDetails, Company


class CompanyStorageImplementation(CompanyStorageInterface):

    def get_company_dtos(self) -> List[CompanyDTO]:
        from django.db.models.functions import Lower
        company_objects = Company.objects.all().order_by(Lower('name'))
        company_dtos = [
            self._convert_company_object_to_company_dto(
                company_object=company_object
            ) for company_object in company_objects
        ]
        return company_dtos

    def get_company_employee_ids_dtos(self, company_ids: List[str]) -> \
            List[CompanyIdWithEmployeeIdsDTO]:
        company_employees = \
            UserDetails.objects.filter(company_id__in=company_ids).values_list(
                'company_id', 'user_id')
        from collections import defaultdict
        company_employee_ids_dictionary = defaultdict(list)
        for company_employee in company_employees:
            company_id = str(company_employee[0])
            company_employee_ids_dictionary[company_id].extend([
                company_employee[1]])
        company_employee_ids_dtos = [
            CompanyIdWithEmployeeIdsDTO(
                company_id=company_id,
                employee_ids=company_employee_ids_dictionary[company_id]
            ) for company_id in company_ids
        ]
        return company_employee_ids_dtos

    @staticmethod
    def _convert_company_object_to_company_dto(company_object) -> CompanyDTO:
        company_dto = CompanyDTO(
            company_id=str(company_object.company_id),
            name=company_object.name,
            description=company_object.description,
            logo_url=company_object.logo_url)
        return company_dto

    def get_company_id_if_company_name_already_exists(
            self, name: str
    ) -> Optional[str]:
        try:
            company_object = Company.objects.get(name=name)
            return str(company_object.company_id)
        except Company.DoesNotExist:
            return None

    def add_company(
            self,
            company_name_logo_and_description_dto: CompanyNameLogoAndDescriptionDTO
    ):
        company_object = Company.objects.create(
            name=company_name_logo_and_description_dto.name,
            description=company_name_logo_and_description_dto.description,
            logo_url=company_name_logo_and_description_dto.logo_url)
        return str(company_object.company_id)

    def add_users_to_company(self, company_id: str, user_ids: List[str]):
        UserDetails.objects.filter(user_id__in=user_ids) \
            .update(company_id=company_id)

    def validate_is_company_exists(self, company_id: str):
        from ib_iam.exceptions.custom_exceptions import InvalidCompanyId
        try:
            Company.objects.get(company_id=company_id)
        except Company.DoesNotExist:
            raise InvalidCompanyId()

    def delete_company(self, company_id: str):
        Company.objects.filter(company_id=company_id).delete()

    def update_company_details(self, company_dto: CompanyDTO):
        Company.objects.filter(company_id=company_dto.company_id) \
            .update(name=company_dto.name,
                    description=company_dto.description,
                    logo_url=company_dto.logo_url)

    def delete_all_existing_employees_of_company(self, company_id: str):
        UserDetails.objects.filter(company_id=company_id).update(company=None)
