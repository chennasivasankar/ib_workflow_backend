from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)
from ib_iam.presenters.update_team_presenter_implementation import (
    UpdateTeamPresenterImplementation
)
from ib_iam.interactors.team_interactor import (
    TeamInteractor
)
from ib_iam.interactors.storage_interfaces.dtos import TeamWithUserIdsDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    print("&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(1)
    user_obj = kwargs["user"]
    user_id = str(user_obj.id)
    request_data = kwargs["request_data"]
    team_id = kwargs["team_id"]
    name = request_data["name"]
    description = request_data["description"]
    user_ids = request_data["user_ids"]
    print(2)

    storage = TeamStorageImplementation()
    presenter = UpdateTeamPresenterImplementation()
    interactor = TeamInteractor(storage=storage)

    team_with_user_ids_dto = TeamWithUserIdsDTO(
        team_id=team_id,
        name=name,
        description=description,
        user_ids=user_ids
    )
    response = interactor.update_team_details_wrapper(
        user_id=user_id,
        team_with_user_ids_dto=team_with_user_ids_dto,
        presenter=presenter
    )
    return response
