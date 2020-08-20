from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    email = request_data["email"]

    from ib_iam.presenters.auth_presenter_implementation import \
        SendVerifyEmailLinkPresenterImplementation
    presenter = SendVerifyEmailLinkPresenterImplementation()

    from ib_iam.interactors.send_verify_email_link_interactor import \
        SendVerifyEmailLinkInteractor
    interactor = SendVerifyEmailLinkInteractor()

    response = interactor.send_verify_email_link_wrapper(
        email=email, presenter=presenter)
    return response
