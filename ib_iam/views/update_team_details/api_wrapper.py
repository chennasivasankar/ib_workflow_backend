from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)
from ib_iam.presenters.team_presenter_implementation import (
    TeamPresenterImplementation
)
from ib_iam.interactors.team_interactor import (
    TeamInteractor
)
from ib_iam.interactors.storage_interfaces.dtos import UpdateTeamParametersDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = str(user_obj.id)
    request_data = kwargs["request_data"]
    team_id = request_data["team_id"]
    name = request_data["name"]
    description = request_data["description"]

    storage = TeamStorageImplementation()
    presenter = TeamPresenterImplementation()
    interactor = TeamInteractor(storage=storage)

    update_team_parameters_dto = UpdateTeamParametersDTO(
        team_id=team_id,
        name=name,
        description=description
    )

    response = interactor.get_list_of_teams_wrapper(
        user_id=user_id,
        update_team_parameters_dto=update_team_parameters_dto,
        presenter=presenter
    )
    return response
