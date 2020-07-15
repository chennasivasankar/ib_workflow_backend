from ib_iam.interactors.presenter_interfaces.presenter_interface import \
    AuthPresenterInterface


class InvalidEmail(Exception):
    pass


class UserAccountDoesNotExist(Exception):
    pass


class ResetPasswordLinkToEmailInteractor:

    def reset_password_link_to_user_email_wrapper(
            self, email: str, presenter: AuthPresenterInterface
    ):
        try:
            self.reset_password_link_to_email(email=email)
            return presenter \
                .get_success_response_for_reset_password_link_to_user_email()
        except InvalidEmail:
            return presenter.raise_invalid_email()
        except UserAccountDoesNotExist:
            response = presenter.raise_user_account_does_not_exist()
            return response

    def reset_password_link_to_email(self, email: str):
        is_email_empty = not email
        if is_email_empty:
            raise InvalidEmail
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        from ib_iam.conf.settings import LINK_TO_RESET_PASSWORD_EXPIRES_IN_SEC
        link_to_reset_password_expires_in_sec \
            = LINK_TO_RESET_PASSWORD_EXPIRES_IN_SEC
        user_token = service_adapter.auth_service.get_token_for_reset_password(
            email=email,
            expires_in_sec=link_to_reset_password_expires_in_sec
        )
        self.send_email_to_user_email(email=email, user_token=user_token)

    @staticmethod
    def send_email_to_user_email(email: str, user_token: str):
        from ib_iam.conf.settings import \
            LINK_TO_RESET_PASSWORD, EMAIL_SUBJECT, EMAIL_CONTENT
        link = LINK_TO_RESET_PASSWORD + user_token
        subject = EMAIL_SUBJECT
        content = EMAIL_CONTENT + link
        from ib_iam.adapters.email_service import EmailService
        email_service = EmailService()
        email_service.send_email_to_user(
            email=email, subject=subject, content=content
        )
