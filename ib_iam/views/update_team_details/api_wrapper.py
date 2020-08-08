from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.storages.team_storage_implementation import \
    TeamStorageImplementation
from ib_iam.presenters.update_team_presenter_implementation import \
    UpdateTeamPresenterImplementation
from ib_iam.interactors.team_interactor import TeamInteractor
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamWithTeamIdAndUserIdsDTO
from ib_iam.storages.user_storage_implementation import \
    UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = str(user_obj.user_id)
    request_data = kwargs["request_data"]
    team_id = kwargs["team_id"]
    name = request_data["name"]
    description = request_data["description"]
    user_ids = request_data["user_ids"]

    team_storage = TeamStorageImplementation()
    user_storage = UserStorageImplementation()
    presenter = UpdateTeamPresenterImplementation()
    interactor = TeamInteractor(team_storage=team_storage,
                                user_storage=user_storage)

    team_with_team_id_and_user_ids_dto = TeamWithTeamIdAndUserIdsDTO(
        team_id=team_id,
        name=name,
        description=description,
        user_ids=user_ids
    )
    response = interactor.update_team_details_wrapper(
        user_id=user_id,
        team_with_team_id_and_user_ids_dto=team_with_team_id_and_user_ids_dto,
        presenter=presenter
    )
    return response
