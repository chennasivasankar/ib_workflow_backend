from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    email = request_data["email"]

    from ib_iam.interactors.auth.reset_password_link_to_email_interactor import \
        SendResetPasswordLinkToEmailInteractor
    interactor = SendResetPasswordLinkToEmailInteractor()

    from ib_iam.presenters.auth_presenter_implementation import \
        AuthPresenterImplementation
    presenter = AuthPresenterImplementation()
    response = interactor.send_reset_password_link_to_user_email_wrapper(
        presenter=presenter,
        email=email
    )
    return response
