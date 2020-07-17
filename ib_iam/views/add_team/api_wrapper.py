from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.add_team_interactor import AddTeamInteractor
from ib_iam.interactors.storage_interfaces.dtos import AddTeamParametersDTO
from ib_iam.presenters.team_presenter_implementation import TeamPresenterImplementation
from ib_iam.storages.team_storage_implementation import TeamStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = str(user_obj.id)
    request_data = kwargs["request_data"]
    name = request_data["name"]
    description = request_data["description"]

    storage = TeamStorageImplementation()
    presenter = TeamPresenterImplementation()
    interactor = AddTeamInteractor(storage=storage)

    add_team_params_dto = AddTeamParametersDTO(
        name=name,
        description=description
    )

    response_data = interactor.add_team_wrapper(
        user_id=user_id,
        add_team_params_dto=add_team_params_dto,
        presenter=presenter
    )
    print("in wrapper")
    print(response_data)
    print(response_data.content)
    print("given up")
    return response_data
