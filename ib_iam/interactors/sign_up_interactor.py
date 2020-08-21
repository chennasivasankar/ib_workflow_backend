from ib_iam.exceptions.custom_exceptions import InvalidEmail, \
    InvalidNameLength, NameShouldNotContainsNumbersSpecCharacters, \
    UserAccountDoesNotExist
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    CreateUserAccountPresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class AccountWithThisEmailAlreadyExistsException(Exception):
    pass


class PasswordDoesNotMatchedWithCriteriaException(Exception):
    pass


class InvalidDomainException(Exception):
    pass


class SignupInteractor(ValidationMixin):

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def signup_wrapper(self, presenter: CreateUserAccountPresenterInterface,
                       email: str, name: str, password: str):

        try:
            self.create_user_account(email=email, name=name, password=password)
            response = presenter.get_response_for_create_user_account()
        except AccountWithThisEmailAlreadyExistsException:
            response = presenter.raise_account_already_exists_exception()
        except PasswordDoesNotMatchedWithCriteriaException:
            response = presenter. \
                raise_password_not_matched_with_criteria_exception()
        except InvalidEmail:
            response = presenter.raise_invalid_email_exception()
        except InvalidDomainException:
            response = presenter.raise_invalid_domain_exception()
        except InvalidNameLength:
            response = presenter \
                .raise_invalid_name_length_exception()
        except NameShouldNotContainsNumbersSpecCharacters:
            response = presenter. \
                raise_name_should_not_contain_special_characters_exception()
        return response

    def create_user_account(self, email: str, password: str, name: str):
        self._validate_create_user_account_details(
            email=email, password=password, name=name)
        from ib_iam.adapters.service_adapter import get_service_adapter
        adapter = get_service_adapter()
        # try:
        #     user_id = adapter.user_service.get_user_id_for_given_email(
        #         email=email)
        #     is_active_user_account = adapter.user_service.is_active_user_account(
        #         email=email)
        #     if not is_active_user_account:
        #         adapter.user_service.activate_user_account(user_id=user_id)
        #     else:
        #         raise AccountWithThisEmailAlreadyExistsException
        # except UserAccountDoesNotExist:
        user_id = self._create_user_account(email=email, password=password,
                                            name=name)
        adapter.auth_service.update_is_email_verified_value_in_ib_user_profile_details(
            user_id=user_id, is_email_verified=False)
        self.user_storage.create_user(user_id=user_id, is_admin=False,
                                      name=name)
        from ib_iam.interactors.send_verify_email_link_interactor import \
            SendVerifyEmailLinkInteractor
        interactor = SendVerifyEmailLinkInteractor()
        interactor.send_verification_email(
            user_id=user_id, name=name, email=email)

    @staticmethod
    def _create_user_account(email: str, password: str,
                             name: str) -> str:
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = service_adapter.user_service.create_user_account_with_email(
            email=email, password=password)

        from ib_users.interactors.user_profile_interactor import \
            CreateUserProfileDTO
        user_profile_dto = CreateUserProfileDTO(
            name=name, email=email, is_email_verified=False)
        service_adapter.user_service.create_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto)
        return user_id

    def _validate_create_user_account_details(
            self, name: str, email: str, password: str):
        self._validate_name_and_throw_exception(name=name)
        self._validate_email(email=email)
        self._validate_password_criteria(password=password)

    @staticmethod
    def _validate_email(email: str):
        import re
        from ib_iam.constants.config import EMAIL_DOMAIN_VALIDATION_EXPRESSION
        pattern = EMAIL_DOMAIN_VALIDATION_EXPRESSION

        from ib_iam.constants.config import VALID_EMAIL_DOMAINS
        valid_domains = VALID_EMAIL_DOMAINS
        domain = re.search(pattern, email).group(1)
        if domain not in valid_domains:
            raise InvalidDomainException()

    @staticmethod
    def _validate_password_criteria(password: str):
        from ib_iam.constants.config import PASSWORD_VALIDATION_EXPRESSION
        pattern = PASSWORD_VALIDATION_EXPRESSION
        import re
        if not re.match(pattern, password):
            raise PasswordDoesNotMatchedWithCriteriaException
