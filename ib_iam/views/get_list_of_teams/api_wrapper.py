from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)
from ib_iam.presenters.team_presenter_implementation import (
    TeamPresenterImplementation
)
from ib_iam.interactors.get_list_of_teams_interactor import (
    GetListOfTeamsInteractor
)
from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = user_obj.id
    request_query_params = kwargs["request_query_params"].__dict__
    offset = request_query_params.get("offset")
    limit = request_query_params.get("limit")

    storage = TeamStorageImplementation()
    presenter = TeamPresenterImplementation()
    interactor = GetListOfTeamsInteractor(storage=storage)

    pagination_dto = PaginationDTO(
        offset=offset,
        limit=limit
    )

    response_data = interactor.get_list_of_teams_wrapper(
        user_id=user_id,
        pagination_dto=pagination_dto,
        presenter=presenter
    )
    return response_data
