from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.dtos import GetBoardsDTO
from ...interactors.get_boards_interactor import GetBoardsInteractor
from ...presenters.presenter_implementation import GetBoardsPresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    params = kwargs['query_params']
    offset = params['offset']
    limit = params['limit']

    boards_dto = GetBoardsDTO(
        user_id=user.id,
        offset=offset,
        limit=limit
    )
    storage = StorageImplementation()
    presenter = GetBoardsPresenterImplementation()

    interactor = GetBoardsInteractor(
        storage=storage
    )
    response = interactor.get_boards_wrapper(presenter=presenter,
                                             get_boards_dto=boards_dto)
    return response
