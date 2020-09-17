import dataclasses

from ib_iam.interactors.presenter_interfaces \
    .auth_presenter_interface import \
    UpdateUserPasswordPresenterInterface


@dataclasses.dataclass
class CurrentAndNewPasswordDTO:
    current_password: str
    new_password: str


class UpdateUserPasswordInteractor:

    def update_user_password_wrapper(
            self, user_id: str,
            current_and_new_password_dto: CurrentAndNewPasswordDTO,
            presenter: UpdateUserPasswordPresenterInterface
    ):
        from ib_iam.exceptions.custom_exceptions import InvalidNewPassword, \
            InvalidCurrentPassword, CurrentPasswordMismatch
        try:
            self.update_user_password(
                user_id=user_id,
                current_and_new_password_dto=current_and_new_password_dto
            )
            response = presenter.get_success_response_for_update_user_password()
        except InvalidNewPassword:
            response = presenter.response_for_invalid_new_password_exception()
        except InvalidCurrentPassword:
            response = presenter.response_for_invalid_current_password_exception()
        except CurrentPasswordMismatch:
            response = presenter.response_for_current_password_mismatch_exception()
        return response

    @staticmethod
    def update_user_password(
            user_id: str,
            current_and_new_password_dto: CurrentAndNewPasswordDTO
    ):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        service_adapter.auth_service.update_user_password(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto
        )
