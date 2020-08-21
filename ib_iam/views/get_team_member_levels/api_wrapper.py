from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs["path_params"]

    team_id = path_params["team_id"]

    from ib_iam.storages.team_member_level_storage_implementation import \
        TeamMemberLevelStorageImplementation
    team_member_level_storage = TeamMemberLevelStorageImplementation()

    from ib_iam.presenters.get_levels_presenter_implementation import \
        GetTeamMemberLevelsPresenterImplementation
    presenter = GetTeamMemberLevelsPresenterImplementation()

    from ib_iam.interactors.get_team_member_levels_interactor import \
        GetTeamMemberLevelsInteractor
    interactor = GetTeamMemberLevelsInteractor(
        team_member_level_storage=team_member_level_storage
    )

    response = interactor.get_team_member_levels_wrapper(
        team_id=team_id, presenter=presenter
    )
    return response