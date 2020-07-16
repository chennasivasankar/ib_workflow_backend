from ib_iam.adapters.auth_service import EmailAndPasswordDTO, TokensDTO
from ib_iam.interactors.DTOs.common_dtos import InvalidEmail, \
    UserAccountDoesNotExist
from ib_iam.interactors.presenter_interfaces.presenter_interface import \
    AuthPresenterInterface


class IncorrectPassword(Exception):
    pass


class PasswordMinLength(Exception):
    pass


class PasswordAtLeastOneSpecialCharacter(Exception):
    pass


class LoginInteractor:
    def login_wrapper(self, presenter: AuthPresenterInterface,
                      email_and_password_dto: EmailAndPasswordDTO
                      ):
        try:
            response = self._get_login_response(
                email_and_password_dto=email_and_password_dto,
                presenter=presenter
            )
            return response
        except InvalidEmail:
            return presenter.raise_exception_for_invalid_email()
        except IncorrectPassword:
            return presenter.raise_exception_for_incorrect_password()
        except UserAccountDoesNotExist:
            return presenter.raise_exception_for_user_account_does_not_exists()
        except PasswordMinLength:
            return presenter.raise_exception_for_password_min_length_required()
        except PasswordAtLeastOneSpecialCharacter:
            return presenter.raise_exception_for_password_at_least_one_special_character_required()

    def _get_login_response(self, email_and_password_dto: EmailAndPasswordDTO,
                            presenter: AuthPresenterInterface
                            ):
        tokens_dto = self.get_tokens_dto(
            email_and_password_dto=email_and_password_dto
        )
        response = presenter.prepare_response_for_tokens_dto(tokens_dto)
        return response

    @staticmethod
    def get_tokens_dto(email_and_password_dto: EmailAndPasswordDTO) \
            -> TokensDTO:
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        tokens_dto = service_adapter.auth_service. \
            get_tokens_dto_for_given_email_and_password_dto(
            email_and_password_dto=email_and_password_dto
        )
        return tokens_dto
