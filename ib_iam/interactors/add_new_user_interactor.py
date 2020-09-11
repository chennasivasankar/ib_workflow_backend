from typing import List

from ib_iam.exceptions.custom_exceptions import (
    UserIsNotAdmin, InvalidEmailAddress,
    UserAccountAlreadyExistWithThisEmail,
    NameShouldNotContainsNumbersSpecCharacters, RoleIdsAreInvalid,
    InvalidCompanyId, TeamIdsAreInvalid, InvalidNameLength
)
from ib_iam.interactors.dtos.dtos import AddUserDetailsDTO
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.add_new_user_presenter_inerface \
    import AddUserPresenterInterface
from ib_iam.interactors.storage_interfaces.elastic_storage_interface \
    import ElasticSearchStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface \
    import UserStorageInterface
from ib_iam.adapters.dtos import UserProfileDTO


class AddNewUserInteractor(ValidationMixin):

    def __init__(
            self, user_storage: UserStorageInterface,
            elastic_storage: ElasticSearchStorageInterface
    ):
        self.user_storage = user_storage
        self.elastic_storage = elastic_storage

    def add_new_user_wrapper(
            self, user_id: str, add_user_details_dto: AddUserDetailsDTO,
            presenter: AddUserPresenterInterface
    ):
        try:
            self.add_new_user(
                user_id=user_id, add_user_details_dto=add_user_details_dto
            )
            response = presenter.response_for_add_user_response()
        except UserIsNotAdmin:
            response = presenter.response_for_user_is_not_admin_exception()
        except InvalidNameLength:
            response = presenter.response_for_invalid_name_length_exception()
        except InvalidEmailAddress:
            response = presenter.response_for_invalid_email_exception()
        except UserAccountAlreadyExistWithThisEmail:
            response = presenter.response_for_user_account_already_exists_exception()
        except NameShouldNotContainsNumbersSpecCharacters:
            response = presenter.response_for_name_contains_special_character_exception()
        except RoleIdsAreInvalid:
            response = presenter.response_for_invalid_role_ids_exception()
        except InvalidCompanyId:
            response = presenter.response_for_invalid_company_ids_exception()
        except TeamIdsAreInvalid:
            response = presenter.response_for_invalid_team_ids_exception()
        return response

    def add_new_user(
            self, user_id: str, add_user_details_dto: AddUserDetailsDTO
    ):
        self._validate_add_new_user_details(
            user_id=user_id, add_user_details_dto=add_user_details_dto
        )
        email = add_user_details_dto.email
        name = add_user_details_dto.name
        company_id = add_user_details_dto.company_id
        team_ids = add_user_details_dto.team_ids
        new_user_id = self._create_user_in_ib_users(email, name)
        is_admin = False

        self.user_storage.create_user(
            is_admin=is_admin, company_id=company_id,
            user_id=new_user_id, name=name
        )
        self.user_storage.add_user_to_the_teams(
            user_id=new_user_id, team_ids=team_ids
        )
        self._create_elastic_user(user_id=new_user_id, name=name)
        self._send_email_verify_link(
            user_id=new_user_id, name=name, email=email
        )

    def _create_elastic_user(self, user_id: str, name: str):
        elastic_user_id = self.elastic_storage.create_elastic_user(
            user_id=user_id, name=name
        )
        self.elastic_storage.create_elastic_user_intermediary(
            elastic_user_id=elastic_user_id, user_id=user_id
        )

    @staticmethod
    def _send_email_verify_link(user_id: str, name: str, email: str):
        from ib_iam.interactors.send_verify_email_link_interactor import \
            SendVerifyEmailLinkInteractor
        interactor = SendVerifyEmailLinkInteractor()
        interactor.send_verification_email(
            user_id=user_id, name=name, email=email
        )

    def _validate_add_new_user_details(
            self, user_id: str, add_user_details_dto: AddUserDetailsDTO
    ):
        name = add_user_details_dto.name
        email = add_user_details_dto.email
        team_ids = add_user_details_dto.team_ids
        company_id = add_user_details_dto.company_id
        self._validate_is_user_admin(user_id=user_id)
        self._validate_name_and_throw_exception(name=name)
        self._validate_email_and_throw_exception(email=email)
        self._validate_team_ids(team_ids=team_ids)
        if company_id is not None:
            self._validate_company_id(company_id=company_id)

    def _create_user_in_ib_users(self, email: str, name: str) -> str:
        new_user_id = self._create_user_account_with_email(email=email)
        self._create_user_profile(user_id=new_user_id, email=email, name=name)
        return new_user_id

    @staticmethod
    def _validate_email_and_throw_exception(email: str):
        import re
        from ib_iam.constants.config import EMAIL_VALIDATION_PATTERN
        email_valid_pattern = EMAIL_VALIDATION_PATTERN
        is_invalid_email = not bool(re.match(email_valid_pattern, email))
        if is_invalid_email:
            raise InvalidEmailAddress()

    @staticmethod
    def _create_user_account_with_email(email: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = service_adapter.user_service. \
            create_user_account_with_email(email=email)
        return user_id

    @staticmethod
    def _create_user_profile(user_id: str, email: str, name: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_profile_dto = UserProfileDTO(
            name=name, email=email, user_id=user_id
        )
        service_adapter.user_service.create_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto
        )
        service_adapter.auth_service.update_is_email_verified_value_in_ib_user(
            user_id=user_id, is_email_verified=False
        )

    def _validate_team_ids(self, team_ids: List[str]):
        are_exists_invalid_ids = not self.user_storage.check_are_valid_team_ids(
            team_ids=team_ids
        )
        if are_exists_invalid_ids:
            raise TeamIdsAreInvalid()

    def _validate_company_id(self, company_id: str):
        is_invalid = not self.user_storage.check_is_exists_company_id(
            company_id=company_id
        )
        if is_invalid:
            raise InvalidCompanyId()
