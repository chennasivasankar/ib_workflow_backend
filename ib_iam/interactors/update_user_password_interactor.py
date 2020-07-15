from ib_iam.interactors.presenter_interfaces.presenter_interface import \
    AuthPresenterInterface


class TokenDoesNotExist(Exception):
    pass


class NotStrongPassword(Exception):
    pass


class TokenHasExpired(Exception):
    pass


class UpdateUserPasswordInteractor:
    def update_user_password_wrapper(self, presenter: AuthPresenterInterface,
                                     token: str, password: str):
        try:
            return self.update_user_password_response(
                password=password, presenter=presenter, token=token
            )
        except TokenDoesNotExist:
            return presenter.raise_token_does_not_exists()
        except NotStrongPassword:
            return presenter.raise_not_a_strong_password()
        except TokenHasExpired:
            return presenter.raise_token_has_expired()

    def update_user_password_response(self, password: str, token: str,
                                      presenter: AuthPresenterInterface
                                      ):
        self.update_user_password(token=token, password=password)
        return presenter.get_update_user_password_success_response()

    @staticmethod
    def update_user_password(token: str, password: str):
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        service_adapter.auth_service.update_user_password(
            token=token, password=password
        )
