from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...interactors.dtos import ColumnTasksParametersDTO
from ...interactors.get_column_tasks_interactor import GetColumnTasksInteractor
from ...presenters.presenter_implementation import \
    GetColumnTasksPresenterImplementation, \
    GetColumnTasksListViewPresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    column_id = kwargs['column_id']
    params = kwargs['request_query_params']
    offset = params['offset']
    limit = params['limit']
    search_query = params.search_query
    request_body = kwargs['request_data']

    from ib_boards.constants.enum import ViewType
    view_type = request_body.get('view_type', ViewType.KANBAN.value)

    storage = StorageImplementation()
    presenter = GetColumnTasksListViewPresenterImplementation()
    from ib_boards.interactors.get_column_tasks_in_list_view import \
        GetColumnTasksInteractorListView
    interactor = GetColumnTasksInteractorListView(
        storage=storage
    )
    column_tasks_parameters = ColumnTasksParametersDTO(
        user_id=user.user_id,
        column_id=column_id,
        offset=offset,
        limit=limit,
        view_type=view_type,
        search_query=search_query
    )
    response = interactor.get_column_tasks_wrapper(
        presenter=presenter, column_tasks_parameters=column_tasks_parameters
    )
    return response