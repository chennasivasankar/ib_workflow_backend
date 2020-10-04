from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...interactors.users.get_user_invitation_code import \
    GetUserInvitationCodeInteractor
from ...presenters.auth_presenter_implementation import \
    AuthPresenterImplementation
from ...storages.user_storage_implementation import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # user_id = kwargs['user_dto'].user_id
    user = kwargs["user"]
    user_id = str(user.user_id)
    user_storage = UserStorageImplementation()
    presenter = AuthPresenterImplementation()
    interactor = GetUserInvitationCodeInteractor(user_storage=user_storage)
    response = interactor.get_user_invitation_code_wrapper(user_id, presenter)
    return response
