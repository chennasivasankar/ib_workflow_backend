from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = user_object.user_id
    request_data = kwargs["request_data"]
    current_and_new_password_dto = \
        _prepare_current_and_new_password_dto(request_data=request_data)

    from ib_iam.presenters.update_user_password_presenter_implementation import \
        UpdateUserPasswordPresenterImplementation
    presenter = UpdateUserPasswordPresenterImplementation()
    from ib_iam.interactors.update_user_password_interactor import \
        UpdateUserPassword
    interactor = UpdateUserPassword()

    response_data = interactor.update_user_password_wrapper(
        user_id=user_id,
        current_and_new_password_dto=current_and_new_password_dto,
        presenter=presenter)
    return response_data


def _prepare_current_and_new_password_dto(request_data):
    from ib_iam.interactors.update_user_password_interactor import \
        CurrentAndNewPasswordDTO
    current_and_new_password_dto = CurrentAndNewPasswordDTO(
        current_password=request_data["current_password"],
        new_password=request_data["new_password"]
    )
    return current_and_new_password_dto
