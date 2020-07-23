from typing import List

from ib_iam.exceptions import (
    UserHasNoAccess,
    CompanyNameAlreadyExists,
    InvalidUsers,
    DuplicateUsers,
    InvalidCompany
)
from ib_iam.interactors.presenter_interfaces \
    .add_company_presenter_interface import AddCompanyPresenterInterface
from ib_iam.interactors.presenter_interfaces.delete_company_presenter_interface import DeleteCompanyPresenterInterface
from ib_iam.interactors.storage_interfaces \
    .company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.storage_interfaces.dtos import (
    CompanyDetailsWithUserIdsDTO
)


class CompanyInteractor:

    def __init__(self, storage: CompanyStorageInterface):
        self.storage = storage

    def add_company_wrapper(
            self,
            user_id: str,
            company_details_with_user_ids_dto: CompanyDetailsWithUserIdsDTO,
            presenter: AddCompanyPresenterInterface
    ):
        try:
            company_id = self.add_company(
                user_id=user_id,
                company_details_with_user_ids_dto=company_details_with_user_ids_dto
            )
            response = presenter.get_response_for_add_company(company_id=company_id)
        except UserHasNoAccess:
            response = presenter.get_user_has_no_access_response_for_add_company()
        except CompanyNameAlreadyExists as exception:
            response = presenter \
                .get_company_name_already_exists_response_for_add_company(exception)
        except DuplicateUsers:
            response = presenter.get_duplicate_users_response_for_add_company()
        except InvalidUsers:
            response = presenter.get_invalid_users_response_for_add_company()
        return response

    def add_company(
            self,
            user_id: str,
            company_details_with_user_ids_dto: CompanyDetailsWithUserIdsDTO
    ):
        user_ids = company_details_with_user_ids_dto.user_ids
        self.storage.validate_is_user_admin(user_id=user_id)
        self._validate_add_company_details(
            company_details_with_user_ids_dto=company_details_with_user_ids_dto
        )
        company_id = self.storage.add_company(
            user_id=user_id,
            company_details_with_user_ids_dto=company_details_with_user_ids_dto
        )
        self.storage.add_users_to_company(
            company_id=company_id, user_ids=user_ids
        )
        return company_id

    def delete_company_wrapper(
            self, user_id: str, company_id: str,
            presenter: DeleteCompanyPresenterInterface
    ):
        try:
            self.delete_company(user_id=user_id, company_id=company_id)
            response = presenter.get_success_response_for_delete_company()
        except UserHasNoAccess:
            response = presenter.get_user_has_no_access_response_for_delete_company()
        except InvalidCompany:
            response = presenter.get_invalid_company_response_for_delete_company()
        return response

    def delete_company(self, user_id: str, company_id: str):
        self.storage.validate_is_user_admin(user_id=user_id)
        self.storage.validate_is_company_exists(company_id=company_id)
        self.storage.delete_company(company_id=company_id)

    def _validate_add_company_details(
            self,
            company_details_with_user_ids_dto: CompanyDetailsWithUserIdsDTO
    ):
        name = company_details_with_user_ids_dto.name
        self._validate_users(user_ids=company_details_with_user_ids_dto.user_ids)
        self._validate_is_company_name_already_exists(name=name)

    def _validate_users(self, user_ids):
        self._validate_is_duplicate_users_exists(user_ids=user_ids)
        self._validate_is_invalid_users_exists(user_ids=user_ids)

    @staticmethod
    def _validate_is_duplicate_users_exists(user_ids: List[str]):
        is_duplicate_user_ids_exist = len(user_ids) != len(set(user_ids))
        if is_duplicate_user_ids_exist:
            raise DuplicateUsers()

    def _validate_is_invalid_users_exists(self, user_ids: List[str]):
        user_ids_from_db = \
            self.storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=user_ids)
        is_invalid_users_found = len(user_ids) != len(user_ids_from_db)
        if is_invalid_users_found:
            raise InvalidUsers()

    def _validate_is_company_name_already_exists(self, name: str):
        company_id = \
            self.storage.get_company_id_if_company_name_already_exists(name=name)
        is_company_name_already_exists = company_id is not None
        if is_company_name_already_exists:
            raise CompanyNameAlreadyExists(company_name=name)
