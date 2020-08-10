from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    AuthPresenterInterface


class PasswordMinLength(Exception):
    pass


class PasswordAtLeastOneSpecialCharacter(Exception):
    pass


class TokenDoesNotExist(Exception):
    pass


class TokenHasExpired(Exception):
    pass


class ResetUserPasswordInteractor:
    def reset_user_password_wrapper(self, presenter: AuthPresenterInterface,
                                    reset_password_token: str, password: str):
        try:
            response = self.reset_user_password_response(
                password=password, presenter=presenter,
                reset_password_token=reset_password_token
            )
        except TokenDoesNotExist:
            response = presenter.raise_exception_for_token_does_not_exists()
        except TokenHasExpired:
            response = presenter.raise_exception_for_token_has_expired()
        except PasswordMinLength:
            response = presenter.raise_exception_for_password_min_length_required()
        except PasswordAtLeastOneSpecialCharacter:
            response = presenter.raise_exception_for_password_at_least_one_special_character_required()
        return response

    def reset_user_password_response(
            self, password: str, reset_password_token: str,
            presenter: AuthPresenterInterface):
        self.reset_user_password_with_reset_password_token(
            reset_password_token=reset_password_token,
            password=password)
        return presenter.get_update_user_password_success_response()

    @staticmethod
    def reset_user_password_with_reset_password_token(
            reset_password_token: str, password: str):
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        service_adapter.auth_service. \
            update_user_password_with_reset_password_token(
            reset_password_token=reset_password_token, password=password)
