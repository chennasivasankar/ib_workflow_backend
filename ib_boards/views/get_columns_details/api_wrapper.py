from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...interactors.dtos import ColumnParametersDTO, PaginationParametersDTO
from ...interactors.get_column_details_interactor import \
    GetColumnDetailsInteractor
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    request_body = kwargs['request_data']
    board_id = kwargs['board_id']
    params = kwargs['request_query_params']
    search_query = params.search_query
    offset = params['offset']
    limit = params['limit']
    project_id = request_body['project_id']

    from ib_boards.constants.enum import ViewType
    view_type = request_body.get('view_type', ViewType.KANBAN.value)

    column_params = ColumnParametersDTO(
        board_id=board_id,
        user_id=user.user_id,
        view_type=view_type,
        search_query=search_query,
        project_id=project_id
    )
    pagination_params = PaginationParametersDTO(
        offset=offset,
        limit=limit
    )

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetColumnDetailsInteractor(
        storage=storage
    )

    response = interactor.get_column_details_wrapper(presenter=presenter,
                                                     columns_parameters=column_params,
                                                     pagination_parameters=pagination_params)
    return response
