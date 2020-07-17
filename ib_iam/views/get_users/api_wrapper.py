from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from ib_iam.storages.storage_implementation \
    import StorageImplementation
from ib_iam.presenters.presenter_implementation \
    import PresenterImplementation
from ib_iam.interactors.get_users_details_inteactor \
    import GetUsersDetailsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetUsersDetailsInteractor(storage=storage)

    user = kwargs['user']
    user_id = user.id
    query_params = kwargs['query_params']
    offset = query_params["offset"]
    limit = query_params["limit"]
    response = interactor.get_users_details_wrapper(
        user_id=user_id, limit=limit, offset=offset, presenter=presenter)

    return response
