from ib_iam.adapters.services import get_service_adapter
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import GetCompaniesPresenterInterface
from ib_iam.interactors.storage_interfaces \
    .company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import CompanyWithEmployeesDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, CompanyDTO, CompanyEmployeeIdsDTO, MemberDTO)
from ib_iam.adapters.dtos import UserProfileDTO
from typing import List
from ib_iam.exceptions.custom_exceptions import (
    UserHasNoAccess, InvalidLimit, InvalidOffset)


class GetListOfCompaniesInteractor:

    def __init__(self, storage: CompanyStorageInterface):
        self.storage = storage

    def get_list_of_companies_wrapper(
            self,
            user_id: str,
            pagination_dto: PaginationDTO,
            presenter: GetCompaniesPresenterInterface
    ):
        try:
            company_details_dtos = self.get_list_of_companies(
                user_id=user_id, pagination_dto=pagination_dto)
            response = presenter.get_response_for_get_companies(
                company_details_dtos=company_details_dtos)
        except UserHasNoAccess:
            response = presenter \
                .get_user_has_no_access_response_for_get_companies()
        return response

    def get_list_of_companies(
            self, user_id: str, pagination_dto: PaginationDTO):
        self.storage.validate_is_user_admin(user_id=user_id)
        company_dtos = self.storage.get_company_dtos()
        company_ids = self._get_company_ids_from_company_dtos(
            company_dtos=company_dtos)
        company_member_ids_dtos = self.storage.get_company_employee_ids_dtos(
            company_ids=company_ids)
        employee_ids = self._get_all_member_ids_from_company_member_ids_dtos(
            company_member_ids_dtos=company_member_ids_dtos
        )
        member_dtos = self._get_members_dtos_from_service(
            member_ids=member_ids
        )
        company_with_memebers_dtos = CompanyWithMembersDetailsDTO(
            total_companies_count=companies_with_total_companies_count
                .total_companies_count,
            company_dtos=companies_with_total_companies_count.companies,
            company_member_ids_dtos=company_member_ids_dtos,
            member_dtos=member_dtos
        )
        return company_with_memebers_dtos

    @staticmethod
    def _get_company_ids_from_company_dtos(
            company_dtos: List[CompanyDTO]
    ) -> List[str]:
        company_ids = [
            company_dto.company_id for company_dto in company_dtos
        ]
        return company_ids

    @staticmethod
    def _get_all_member_ids_from_company_member_ids_dtos(
            company_member_ids_dtos: List[CompanyMemberIdsDTO]
    ):
        member_ids = []
        for company_member_ids_dto in company_member_ids_dtos:
            member_ids.extend(company_member_ids_dto.member_ids)
        unique_member_ids = list(set(member_ids))
        return unique_member_ids

    def _get_members_dtos_from_service(self, member_ids: List[str]):
        service = get_service_adapter()
        user_dtos = service.user_service.get_basic_user_dtos(
            user_ids=member_ids
        )
        member_dtos = self._convert_user_dtos_to_member_dtos(
            user_dtos=user_dtos
        )
        return member_dtos

    @staticmethod
    def _convert_user_dtos_to_member_dtos(
            user_dtos: List[UserProfileDTO]
    ) -> List[MemberDTO]:
        member_dtos = [
            MemberDTO(member_id=user_dto.user_id,
                      name=user_dto.name,
                      profile_pic_url=user_dto.profile_pic_url
                      ) for user_dto in user_dtos
        ]
        return member_dtos
