from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    token = kwargs["query_params"]["token"]
    from ib_iam.interactors.auth.user_login_interactor import LoginInteractor
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    storage = UserStorageImplementation()
    interactor = LoginInteractor(storage=storage)

    from ib_iam.presenters.login_with_user_token_presenter_implementation import \
        LoginWithUserTokePresenterImplementation
    presenter = LoginWithUserTokePresenterImplementation()

    response = interactor.login_with_token_wrapper(
        presenter=presenter, token=token
    )
    return response
