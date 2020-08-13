from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.storages.team_storage_implementation import \
    TeamStorageImplementation
from ib_iam.presenters.delete_team_presenter_implementation import \
    DeleteTeamPresenterImplementation
from ib_iam.interactors.team_interactor import TeamInteractor
from ...storages.user_storage_implementation import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = str(user_obj.user_id)
    team_id = kwargs["team_id"]

    team_storage = TeamStorageImplementation()
    user_storage = UserStorageImplementation()
    presenter = DeleteTeamPresenterImplementation()
    interactor = TeamInteractor(team_storage=team_storage,
                                user_storage=user_storage)

    response = interactor.delete_team_wrapper(
        user_id=user_id,
        team_id=team_id,
        presenter=presenter)
    return response
