from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]

    access_token = request_data["access_token"]
    refresh_token = request_data["refresh_token"]

    from ib_iam.presenters.get_refresh_auth_tokens_presenter_implementation import \
        GetRefreshTokensPresenterImplementation
    presenter = GetRefreshTokensPresenterImplementation()

    from ib_iam.interactors.get_refresh_auth_tokens_interactor import \
        GetRefreshTokensInteractor
    interactor = GetRefreshTokensInteractor()

    response = interactor.get_refresh_auth_tokens_wrapper(
        access_token=access_token, refresh_token=refresh_token,
        presenter=presenter
    )
    return response
