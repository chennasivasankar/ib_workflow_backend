from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_iam.interactors.delete_user_interactor import DeleteUserInteractor
from ib_iam.presenters.delete_user_presenter_implementation import \
    DeleteUserPresenterImplementation
from ib_iam.storages.delete_user_storage_implementation import \
    DeleteUserStorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = DeleteUserStorageImplementation()
    presenter = DeleteUserPresenterImplementation()
    interactor = DeleteUserInteractor(storage=storage)

    user = kwargs['user']
    user_id = user.user_id
    path_params = kwargs["path_params"]
    delete_user_id = path_params["user_id"]

    response = interactor.delete_user_wrapper(
        user_id=user_id, delete_user_id=delete_user_id, presenter=presenter)

    return response