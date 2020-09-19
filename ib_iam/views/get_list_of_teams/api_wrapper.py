from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)
from ib_iam.presenters.team_presenter_implementation import (
    GetTeamsPresenterImplementation
)
from ib_iam.interactors.get_list_of_teams_interactor import (
    GetListOfTeamsInteractor
)
from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
from ...storages.user_storage_implementation import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = str(user_obj.user_id)
    query_params = kwargs["query_params"]
    offset = query_params.get("offset")
    limit = query_params.get("limit")

    team_storage = TeamStorageImplementation()
    user_storage = UserStorageImplementation()
    presenter = GetTeamsPresenterImplementation()
    interactor = GetListOfTeamsInteractor(team_storage=team_storage,
                                          user_storage=user_storage)

    pagination_dto = PaginationDTO(offset=offset, limit=limit)

    response = interactor.get_list_of_teams_wrapper(
        user_id=user_id,
        pagination_dto=pagination_dto,
        presenter=presenter)
    return response
