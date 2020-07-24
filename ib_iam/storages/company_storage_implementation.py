from typing import List
from ib_iam.interactors.storage_interfaces.company_storage_interface import \
    CompanyStorageInterface
from ib_iam.models import UserDetails, Company
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDTO, CompanyWithEmployeesCountDTO, CompanyDetailsWithUserIdsDTO,
    CompanyWithUserIdsDTO
)


class CompanyStorageImplementation(CompanyStorageInterface):

    def validate_is_user_admin(self, user_id: str):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        try:
            UserDetails.objects.get(user_id=user_id, is_admin=True)
        except UserDetails.DoesNotExist:
            raise UserHasNoAccess

    def get_company_dtos(self) -> List[CompanyDTO]:
        company_objects = Company.objects.all()
        company_dtos = [
            self._convert_company_object_to_company_dto(
                company_object=company_object
            ) for company_object in company_objects
        ]
        return company_dtos

    def get_company_with_employees_count_dtos(self) -> \
            List[CompanyWithEmployeesCountDTO]:
        from django.db.models import Count
        company_with_employees_count_objects = \
            Company.objects.all().annotate(employees_count=Count("users"))
        company_with_employees_count_dtos = [
            self._convert_company_with_employees_count_object_to_dto(
                company_with_employees_count_object=company_with_employees_count_object)
            for company_with_employees_count_object in company_with_employees_count_objects
        ]
        return company_with_employees_count_dtos

    @staticmethod
    def _convert_company_object_to_company_dto(company_object) -> CompanyDTO:
        company_dto = CompanyDTO(
            company_id=str(company_object.company_id),
            name=company_object.name,
            description=company_object.description,
            logo_url=company_object.logo_url
        )
        return company_dto

    @staticmethod
    def _convert_company_with_employees_count_object_to_dto(
            company_with_employees_count_object) -> CompanyWithEmployeesCountDTO:
        company_with_employees_count_dto = CompanyWithEmployeesCountDTO(
            company_id=str(company_with_employees_count_object.company_id),
            no_of_employees=company_with_employees_count_object.employees_count
        )
        return company_with_employees_count_dto

    def get_valid_user_ids_among_the_given_user_ids(self, user_ids: List[str]):
        user_ids = UserDetails.objects.filter(user_id__in=user_ids) \
            .values_list('user_id', flat=True)
        return list(user_ids)

    def get_company_id_if_company_name_already_exists(self, name: str):
        try:
            company_object = Company.objects.get(name=name)
            return str(company_object.company_id)
        except Company.DoesNotExist:
            return None

    def add_company(
            self,
            user_id: str,
            company_details_with_user_ids_dto: CompanyDetailsWithUserIdsDTO
    ):
        company_object = Company.objects.create(
            name=company_details_with_user_ids_dto.name,
            description=company_details_with_user_ids_dto.description,
            logo_url=company_details_with_user_ids_dto.logo_url
        )
        return str(company_object.company_id)

    def add_users_to_company(self, company_id: str, user_ids: List[str]):
        UserDetails.objects.filter(user_id__in=user_ids) \
            .update(company_id=company_id)

    def validate_is_company_exists(self, company_id: str):
        pass

    def delete_company(self, company_id: str):
        pass

    def update_company_details(
            self, company_with_user_ids_dto: CompanyWithUserIdsDTO
    ):
        pass

    def get_member_ids_of_company(self, company_id: str):
        pass

    def delete_members_from_company(self, company_id: str, member_ids: List[str]):
        pass
