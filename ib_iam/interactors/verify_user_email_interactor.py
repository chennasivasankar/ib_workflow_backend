from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    VerifyEmailPresenterInterface


class EmailDoesNotExistException(Exception):
    pass


class EmailAlreadyVerifiedException(Exception):
    pass


class VerifyEmailInteractor:

    def link_verified_email_to_user_account_wrapper(
            self, user_id, presenter: VerifyEmailPresenterInterface):
        try:
            self.link_verified_email_to_user_account(user_id)
            return presenter.get_response_for_verified_email()
        except EmailDoesNotExistException:
            return presenter.raise_email_does_not_exist_to_verify_exception()
        except EmailAlreadyVerifiedException:
            return presenter.raise_email_already_verified_exception()

    def link_verified_email_to_user_account(self, user_id):
        from ib_iam.adapters.service_adapter import get_service_adapter
        adapter = get_service_adapter()
        user_profile_dto = adapter.user_service.get_user_profile_dto(
            user_id=user_id)
        self._validate_email_to_link_to_user_account(
            email=user_profile_dto.email,
            is_email_verified=user_profile_dto.is_email_verify
        )
        adapter.auth_service.update_is_email_verified_value_in_ib_user_profile_details(
            user_id=user_id, is_email_verified=True)

    @staticmethod
    def _validate_email_to_link_to_user_account(
            email: str, is_email_verified: bool):
        if not email:
            raise EmailDoesNotExistException()

        if is_email_verified:
            raise EmailAlreadyVerifiedException()
