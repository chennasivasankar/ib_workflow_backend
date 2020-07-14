from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']

    email = request_data['email']
    password = request_data['password']
    from ib_iam.adapters.auth_service import EmailAndPasswordDTO
    email_and_password_dto = EmailAndPasswordDTO(
        email=email,
        password=password
    )
    from ib_iam.interactors.user_login_interactor import LoginInteractor
    interactor = LoginInteractor()

    from ib_iam.presenters.presenter_implementation import LoginPresenterImplementation
    presenter = LoginPresenterImplementation()

    response = interactor.login_wrapper(presenter=presenter,
                                        email_and_password_dto=email_and_password_dto)
    return response
