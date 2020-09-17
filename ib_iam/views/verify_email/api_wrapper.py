from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = str(kwargs["user"].user_id)
    from ib_iam.presenters.verify_email_presenter_implementation import \
        VerifyEmailPresenterImplementation
    presenter = VerifyEmailPresenterImplementation()

    from ib_iam.interactors.verify_user_email_interactor import \
        VerifyEmailInteractor
    interactor = VerifyEmailInteractor()

    response = interactor.link_verified_email_to_user_account_wrapper(
        user_id=user_id, presenter=presenter)
    return response
