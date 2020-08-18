from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    SendVerifyEmailLinkPresenterInterface


class AccountDoesNotExists(Exception):
    pass


class EmailAlreadyVerifiedException(Exception):
    pass


class SendVerifyEmailLinkInteractor:

    def send_verify_email_link_wrapper(
            self, email: str,
            presenter: SendVerifyEmailLinkPresenterInterface):
        try:
            self.send_verify_email_link(email=email)
        except AccountDoesNotExists:
            return presenter.raise_account_does_not_exist_exception()
        except EmailAlreadyVerifiedException:
            return presenter.raise_email_already_verified_exception()
        # TODO validate email pattern

    def send_verify_email_link(self, email: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        adapter = get_service_adapter()

        user_id = adapter.user_service.get_user_id_for_given_email(email=email)
        user_profile_dto = adapter.user_service.get_user_profile_dto(
            user_id=user_id)
        self._validate_email_verification(user_profile_dto.is_email_verify)
        self.send_verification_email(user_id=user_id, email=email,
                                     name=user_profile_dto.name)

    @staticmethod
    def send_verification_email(user_id: str, email: str, name: str):
        from django.conf import settings
        from ib_iam.adapters.service_adapter import get_service_adapter
        adapter = get_service_adapter()

        expiry_in_seconds = settings.USER_VERIFICATION_EMAIL_EXPIRY_IN_SECONDS
        verification_link = settings.USER_VERIFICATION_EMAIL_LINK
        auth_token_dto = adapter.auth_service.create_auth_tokens_for_user(
            user_id=user_id, expiry_in_seconds=expiry_in_seconds
        )
        access_token = auth_token_dto.access_token
        verification_url = verification_link + str(access_token)
        from ib_iam.services.email_service_implementation import \
            EmailSenderImpl
        email_sender = EmailSenderImpl(
            subject=settings.VERIFY_USER_EMAIL_SUBJECT,
            email_body_template=settings.VERIFY_USER_EMAIL_BODY_TEMPLATE.format(
                verification_url=verification_url)
        )

        email_sender.send_email(
            email=email,
            data={}
        )

    @staticmethod
    def _validate_email_verification(is_email_verified: bool):
        if is_email_verified:
            raise EmailAlreadyVerifiedException()
