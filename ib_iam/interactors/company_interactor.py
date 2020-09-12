from ib_iam.exceptions.custom_exceptions import (CompanyNameAlreadyExists,
                                                 DuplicateUserIds,
                                                 InvalidCompanyId,
                                                 InvalidUserIds,
                                                 UserIsNotAdmin,
                                                 UserIdsAreInvalid)
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces \
    .add_company_presenter_interface import AddCompanyPresenterInterface
from ib_iam.interactors.presenter_interfaces \
    .delete_company_presenter_interface import DeleteCompanyPresenterInterface
from ib_iam.interactors.presenter_interfaces \
    .update_company_presenter_interface import UpdateCompanyPresenterInterface
from ib_iam.interactors.storage_interfaces \
    .company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.storage_interfaces.dtos import CompanyDTO, \
    CompanyNameLogoAndDescriptionDTO, CompanyWithCompanyIdAndUserIdsDTO, \
    CompanyWithUserIdsDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class CompanyInteractor(ValidationMixin):

    def __init__(self,
                 company_storage: CompanyStorageInterface,
                 user_storage: UserStorageInterface):
        self.user_storage = user_storage
        self.company_storage = company_storage

    def add_company_wrapper(
            self, user_id: str,
            company_with_user_ids_dto: CompanyWithUserIdsDTO,
            presenter: AddCompanyPresenterInterface):
        try:
            company_id = self.add_company(
                user_id=user_id,
                company_with_user_ids_dto=company_with_user_ids_dto)
            response = presenter.get_response_for_add_company(
                company_id=company_id)
        except UserIsNotAdmin:
            response = \
                presenter.get_user_has_no_access_response_for_add_company()
        except CompanyNameAlreadyExists as exception:
            response = presenter \
                .get_company_name_already_exists_response_for_add_company(
                exception)
        except DuplicateUserIds:
            response = presenter.get_duplicate_users_response_for_add_company()
        except UserIdsAreInvalid:
            response = presenter.get_invalid_users_response_for_add_company()
        return response

    def add_company(
            self, user_id: str,
            company_with_user_ids_dto: CompanyWithUserIdsDTO):
        self._validate_is_user_admin(user_id=user_id)
        self._validate_add_company_details(
            company_with_user_ids_dto=company_with_user_ids_dto)
        user_ids = company_with_user_ids_dto.user_ids
        company_name_logo_and_description_dto = \
            CompanyNameLogoAndDescriptionDTO(
                name=company_with_user_ids_dto.name,
                description=company_with_user_ids_dto.description,
                logo_url=company_with_user_ids_dto.logo_url)
        company_id = self.company_storage.add_company(
            company_name_logo_and_description_dto=
            company_name_logo_and_description_dto)
        self.company_storage.add_users_to_company(company_id=company_id,
                                                  user_ids=user_ids)
        return company_id

    def delete_company_wrapper(
            self, user_id: str, company_id: str,
            presenter: DeleteCompanyPresenterInterface):
        try:
            self.delete_company(user_id=user_id, company_id=company_id)
            response = presenter.get_success_response_for_delete_company()
        except UserIsNotAdmin:
            response = \
                presenter.get_user_has_no_access_response_for_delete_company()
        except InvalidCompanyId:
            response = \
                presenter.get_invalid_company_response_for_delete_company()
        return response

    def delete_company(self, user_id: str, company_id: str):
        self._validate_is_user_admin(user_id=user_id)
        self.company_storage.validate_is_company_exists(company_id=company_id)
        self.company_storage.delete_company(company_id=company_id)

    def update_company_details_wrapper(
            self,
            user_id: str,
            company_with_company_id_and_user_ids_dto:
            CompanyWithCompanyIdAndUserIdsDTO,
            presenter: UpdateCompanyPresenterInterface):
        try:
            self.update_company_details(
                user_id=user_id,
                company_with_company_id_and_user_ids_dto=
                company_with_company_id_and_user_ids_dto)
            response = presenter.get_success_response_for_update_company()
        except UserIsNotAdmin:
            response = \
                presenter.get_user_has_no_access_response_for_update_company()
        except InvalidCompanyId:
            response = \
                presenter.get_invalid_company_response_for_update_company()
        except DuplicateUserIds as exception:
            response = presenter \
                .get_duplicate_users_response_for_update_company(exception)
        except InvalidUserIds as exception:
            response = presenter \
                .get_invalid_users_response_for_update_company(exception)
        except CompanyNameAlreadyExists as exception:
            response = presenter \
                .get_company_name_already_exists_response_for_update_company(
                exception)
        return response

    def update_company_details(
            self, user_id: str,
            company_with_company_id_and_user_ids_dto:
            CompanyWithCompanyIdAndUserIdsDTO):
        self._validate_is_user_admin(user_id=user_id)
        self._validate_update_company_details(
            company_with_company_id_and_user_ids_dto=
            company_with_company_id_and_user_ids_dto)
        user_ids = company_with_company_id_and_user_ids_dto.user_ids
        company_id = company_with_company_id_and_user_ids_dto.company_id
        company_dto = CompanyDTO(
            company_id=company_with_company_id_and_user_ids_dto.company_id,
            name=company_with_company_id_and_user_ids_dto.name,
            description=company_with_company_id_and_user_ids_dto.description,
            logo_url=company_with_company_id_and_user_ids_dto.logo_url)
        self.company_storage.update_company_details(company_dto=company_dto)
        self.company_storage.delete_all_existing_employees_of_company(
            company_id=company_id)
        self.company_storage.add_users_to_company(user_ids=user_ids,
                                                  company_id=company_id)

    def _validate_add_company_details(
            self,
            company_with_user_ids_dto: CompanyWithUserIdsDTO):
        self._validate_duplicate_or_invalid_users(
            user_ids=company_with_user_ids_dto.user_ids)
        self._validate_is_company_name_already_exists_to_add_company(
            name=company_with_user_ids_dto.name)

    def _validate_update_company_details(
            self,
            company_with_company_id_and_user_ids_dto:
            CompanyWithCompanyIdAndUserIdsDTO):
        company_id = company_with_company_id_and_user_ids_dto.company_id
        self.company_storage.validate_is_company_exists(company_id=company_id)
        self._validate_duplicate_or_invalid_users(
            user_ids=company_with_company_id_and_user_ids_dto.user_ids)
        self._validate_is_company_name_already_exists_to_update_company(
            name=company_with_company_id_and_user_ids_dto.name,
            company_id=company_id)

    def _validate_is_company_name_already_exists_to_add_company(
            self, name: str):
        company_id = self.company_storage \
            .get_company_id_if_company_name_already_exists(name=name)
        is_company_name_already_exists = company_id is not None
        if is_company_name_already_exists:
            raise CompanyNameAlreadyExists(company_name=name)

    def _validate_is_company_name_already_exists_to_update_company(
            self, name, company_id):
        company_id_from_db = self.company_storage \
            .get_company_id_if_company_name_already_exists(name=name)
        is_company_name_exists = company_id_from_db is not None
        if is_company_name_exists:
            is_company_requested_name_already_assigned_to_other = \
                company_id_from_db != company_id
            if is_company_requested_name_already_assigned_to_other:
                raise CompanyNameAlreadyExists(company_name=name)
