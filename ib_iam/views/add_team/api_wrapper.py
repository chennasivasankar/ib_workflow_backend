from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.team_interactor import TeamInteractor
from ib_iam.interactors.storage_interfaces.dtos import (
    TeamDetailsWithUserIdsDTO
)
from ib_iam.presenters.team_presenter_implementation import (
    TeamPresenterImplementation
)
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = str(user_obj.id)
    request_data = kwargs["request_data"]
    name = request_data["name"]
    description = request_data["description"]
    user_ids = request_data["user_ids"]

    storage = TeamStorageImplementation()
    presenter = TeamPresenterImplementation()
    interactor = TeamInteractor(storage=storage)

    team_details_with_user_ids_dto = TeamDetailsWithUserIdsDTO(
        name=name,
        description=description,
        user_ids=user_ids
    )

    response_data = interactor.add_team_wrapper(
        user_id=user_id,
        team_details_with_user_ids_dto=team_details_with_user_ids_dto,
        presenter=presenter
    )
    return response_data
