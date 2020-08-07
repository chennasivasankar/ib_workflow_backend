from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_boards.interactors.dtos import StarOrUnstarParametersDTO
from ...interactors.star_or_unstar_given_board_interactor import \
    StarOrUnstarBoardInteractor
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    board_id = kwargs["board_id"]
    request_params = kwargs['request_data']
    action = request_params['action']
    parameters = StarOrUnstarParametersDTO(
        board_id=board_id,
        user_id=user.user_id,
        action=action
    )
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = StarOrUnstarBoardInteractor(storage=storage)

    response = interactor.star_or_unstar_board_wrapper(presenter=presenter,
                                                       parameters=parameters)
    return response
