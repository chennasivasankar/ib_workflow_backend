from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_iam.interactors.users.get_users_list_interactor \
    import GetListOfUsersInteractor
from ib_iam.presenters.get_users_list_presenter_implementation \
    import GetUsersListPresenterImplementation
from ib_iam.storages.user_storage_implementation import \
    UserStorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = UserStorageImplementation()
    presenter = GetUsersListPresenterImplementation()
    interactor = GetListOfUsersInteractor(user_storage=storage)

    user = kwargs['user']
    user_id = user.user_id
    query_params = kwargs['query_params']
    offset = query_params["offset"]
    limit = query_params["limit"]
    name_search_query = query_params["search_query"]

    if name_search_query is None:
        name_search_query = ""

    from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
    pagination_dto = PaginationDTO(
        offset=offset,
        limit=limit
    )
    response = interactor.get_list_of_users_wrapper(
        user_id=user_id, pagination_dto=pagination_dto, presenter=presenter,
        name_search_query=name_search_query
    )

    return response
