from ib_iam.adapters.services import get_service_adapter
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import GetCompaniesPresenterInterface
from ib_iam.interactors.storage_interfaces \
    .company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.presenter_interfaces\
    .get_companies_presenter_interface import CompanyWithEmployeesDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, CompanyDTO, CompanyEmployeeIdsDTO, MemberDTO
)
from ib_iam.adapters.dtos import UserProfileDTO
from typing import List
from ib_iam.exceptions.custom_exceptions import (
    UserHasNoAccess, InvalidLimit, InvalidOffset
)


class GetListOfCompanysInteractor:

    def __init__(self, storage: CompanyStorageInterface):
        self.storage = storage

    def get_list_of_companys_wrapper(
            self,
            user_id: str,
            pagination_dto: PaginationDTO,
            presenter: CompanyPresenterInterface
    ):
        try:
            company_details_dtos = self.get_list_of_companys(
                user_id=user_id, pagination_dto=pagination_dto
            )
            response = presenter.get_response_for_get_list_of_companys(
                company_details_dtos=company_details_dtos
            )
        except UserHasNoAccess:
            response = presenter \
                .get_user_has_no_access_response_for_get_list_of_companys()
        except InvalidLimit:
            response = \
                presenter.get_invalid_limit_response_for_get_list_of_companys()
        except InvalidOffset:
            response = \
                presenter.get_invalid_offset_response_for_get_list_of_companys()
        return response

    def get_list_of_companys(self, user_id: str, pagination_dto: PaginationDTO):
        self._validate_pagination_details(pagination_dto=pagination_dto)
        self.storage.validate_is_user_admin(user_id=user_id)
        companys_with_total_companys_count = \
            self.storage.get_companys_with_total_companys_count_dto(
                pagination_dto=pagination_dto
            )
        company_ids = self._get_company_ids_from_company_dtos(
            company_dtos=companys_with_total_companys_count.companys
        )

        company_member_ids_dtos = self.storage.get_company_member_ids_dtos(
            company_ids=company_ids
        )
        member_ids = self._get_all_member_ids_from_company_member_ids_dtos(
            company_member_ids_dtos=company_member_ids_dtos
        )
        member_dtos = self._get_members_dtos_from_service(
            member_ids=member_ids
        )
        company_with_memebers_dtos = CompanyWithMembersDetailsDTO(
            total_companys_count=companys_with_total_companys_count
                .total_companys_count,
            company_dtos=companys_with_total_companys_count.companys,
            company_member_ids_dtos=company_member_ids_dtos,
            member_dtos=member_dtos
        )
        return company_with_memebers_dtos

    @staticmethod
    def _validate_pagination_details(pagination_dto: PaginationDTO):
        if pagination_dto.limit <= 0:
            raise InvalidLimit()
        if pagination_dto.offset < 0:
            raise InvalidOffset()

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
