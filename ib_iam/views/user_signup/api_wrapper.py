from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    name = request_data["name"]
    email = request_data["email"]
    password = request_data["password"]

    from ib_iam.presenters.auth_presenter_implementation import \
        CreateUserAccountPresenterImplementation
    presenter = CreateUserAccountPresenterImplementation()
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()

    from ib_iam.interactors.sign_up_interactor import SignupInteractor
    interactor = SignupInteractor(user_storage=user_storage)

    response = interactor.signup_wrapper(
        presenter=presenter, email=email, name=name, password=password)
    return response
