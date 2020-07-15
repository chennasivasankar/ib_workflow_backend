from ib_iam.interactors.presenter_interfaces.presenter_interface import \
    AuthPresenterInterface


class UpdateUserPasswordInteractor:
    def update_user_password_wrapper(self, presenter: AuthPresenterInterface,
                                     token: str, password: str):
        try:
            self.update_user_password(token=token, password=password)
        except:
            pass

    def update_user_password(self, token, password):
        self._check_the_password_policy(password=password)

    def _check_the_password_policy(self, password):
        pass
