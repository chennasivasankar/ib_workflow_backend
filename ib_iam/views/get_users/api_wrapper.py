from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


from ib_iam.interactors.get_users_list_interactor \
    import GetUsersDetailsInteractor
from ib_iam.presenters.get_users_list_presenter_implementation \
    import GetUsersListPresenterImplementation
from ib_iam.storages.user_storage_implementation import UserStorageImplementation


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
    from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
    pagination_dto = PaginationDTO(
        offset=offset,
        limit=limit
    )
    response = interactor.get_users_details_wrapper(
        user_id=user_id, pagination_dto=pagination_dto, presenter=presenter)

    return response
