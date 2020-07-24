from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist, \
    InvalidEmail
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    AuthPresenterInterface


class SendResetPasswordLinkToEmailInteractor:

    def send_reset_password_link_to_user_email_wrapper(
            self, email: str, presenter: AuthPresenterInterface
    ):
        try:
            self.send_reset_password_link_to_user_email(email=email)
            response = presenter \
                .get_success_response_for_reset_password_link_to_user_email()
        except InvalidEmail:
            response = presenter.raise_exception_for_invalid_email()
        except UserAccountDoesNotExist:
            response \
                = presenter.raise_exception_for_user_account_does_not_exists()
        return response

    def send_reset_password_link_to_user_email(self, email: str):
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        from django.conf import settings
        reset_password_token_expiry_time_in_seconds \
            = settings.RESET_PASSWORD_LINK_EXPIRY_IN_SECONDS
        reset_password_token = service_adapter.auth_service.get_reset_password_token(
            email=email,
            expires_in_sec=reset_password_token_expiry_time_in_seconds
        )
        self.send_reset_password_mail_to_user_email(
            email=email, reset_password_token=reset_password_token
        )

    @staticmethod
    def send_reset_password_mail_to_user_email(email: str,
                                               reset_password_token: str):

        from django.conf import settings
        reset_password_link = settings.RESET_PASSWORD_LINK
        email_subject = settings.EMAIL_SUBJECT
        email_body_template = settings.RESET_PASSWORD_EMAIL_BODY_TEMPLATE
        final_reset_password_link = reset_password_link + reset_password_token
        from ib_iam.adapters.email_service import EmailService
        email_service = EmailService()
        data = {"reset_password_link": final_reset_password_link}
        email_service.send_email_to_user(
            email=email, subject=email_subject,
            email_body_template=email_body_template, data=data
        )
