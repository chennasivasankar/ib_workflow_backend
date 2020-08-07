from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...interactors.dtos import ColumnTasksParametersDTO
from ...interactors.get_column_tasks_interactor import GetColumnTasksInteractor
from ...presenters.presenter_implementation import \
    GetColumnTasksPresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    column_id = kwargs['column_id']
    params = kwargs['request_query_params']
    offset = params['offset']
    limit = params['limit']
    request_body = params['request_data']
    view_type = request_body['view_type']

    storage = StorageImplementation()
    presenter = GetColumnTasksPresenterImplementation()
    interactor = GetColumnTasksInteractor(
        storage=storage
    )
    column_tasks_parameters = ColumnTasksParametersDTO(
        user_id=user.user_id,
        column_id=column_id,
        offset=offset,
        limit=limit,
        view_type=view_type
    )
    response = interactor.get_column_tasks_wrapper(
        presenter=presenter, column_tasks_parameters=column_tasks_parameters
    )
    return response
