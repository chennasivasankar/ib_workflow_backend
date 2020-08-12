from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_iam.interactors.get_users_list_interactor \
    import GetUsersDetailsInteractor
from ib_iam.presenters.get_users_list_presenter_implementation \
    import GetUsersListPresenterImplementation
from ib_iam.storages.user_storage_implementation import \
    UserStorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = UserStorageImplementation()
    presenter = GetUsersListPresenterImplementation()
    interactor = GetUsersDetailsInteractor(user_storage=storage)

    user = kwargs['user']
    user_id = user.user_id
    query_params = kwargs['query_params']
    offset = query_params["offset"]
    limit = query_params["limit"]
    search_query = query_params["search_query"]

    from ib_iam.interactors.dtos.dtos import SearchQueryAndTypeDTO
    from ib_iam.constants.enums import SearchType

    if search_query is None:
        search_query = ""

    search_query_and_type_dto = SearchQueryAndTypeDTO(
        search_query=search_query,
        search_type=SearchType.USER.value
    )

    from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
    pagination_dto = PaginationDTO(
        offset=offset,
        limit=limit
    )
    response = interactor.get_users_details_wrapper(
        user_id=user_id, pagination_dto=pagination_dto, presenter=presenter,
        search_query_and_type_dto=search_query_and_type_dto
    )

    return response
