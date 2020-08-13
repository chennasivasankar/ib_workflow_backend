import dataclasses

from ib_iam.interactors.presenter_interfaces \
    .update_user_password_presenter_interface import \
    UpdateUserPasswordPresenterInterface


@dataclasses.dataclass
class CurrentAndNewPasswordDTO:
    current_password: str
    new_password: str


class UpdateUserPassword:

    def update_user_password_wrapper(
            self, user_id: str,
            current_and_new_password_dto: CurrentAndNewPasswordDTO,
            presenter: UpdateUserPasswordPresenterInterface):
        from ib_iam.exceptions.custom_exceptions import InvalidNewPassword, \
            InvalidCurrentPassword, CurrentPasswordMismatch
        try:
            self.update_user_password(
                user_id=user_id,
                current_and_new_password_dto=current_and_new_password_dto)
            response = presenter.get_success_response_for_update_user_password()
        except InvalidNewPassword:
            response = presenter.raise_invalid_new_password_exception()
        except InvalidCurrentPassword:
            response = presenter.raise_invalid_current_password_exception()
        except CurrentPasswordMismatch:
            response = presenter.raise_current_password_mismatch_exception()
        return response

    @staticmethod
    def update_user_password(
            user_id: str,
            current_and_new_password_dto: CurrentAndNewPasswordDTO):
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        service_adapter.auth_service.update_user_password(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto)
