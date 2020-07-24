from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    query_params = kwargs["query_params"]
    token = query_params["token"]
    request_data = kwargs["request_data"]
    password = request_data["password"]

    from ib_iam.interactors.update_user_password_interactor import \
        UpdateUserPasswordInteractor
    interactor = UpdateUserPasswordInteractor()

    from ib_iam.presenters.auth_presenter_implementation import \
        AuthPresenterImplementation
    presenter = AuthPresenterImplementation()
    response = interactor.update_user_password_wrapper(presenter=presenter,
                                                       reset_password_token=token,
                                                       password=password
                                                       )
    return response
