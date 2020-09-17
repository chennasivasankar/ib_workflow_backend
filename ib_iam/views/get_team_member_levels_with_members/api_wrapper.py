from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs["path_params"]
    user_object = kwargs["user"]

    user_id = user_object.user_id
    team_id = path_params["team_id"]

    from ib_iam.storages.team_member_level_storage_implementation import \
        TeamMemberLevelStorageImplementation
    team_member_level_storage = TeamMemberLevelStorageImplementation()

    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()

    from ib_iam.presenters.get_team_member_levels_with_members_presenter_implementation import \
        GetTeamMemberLevelsWithMembersPresenterImplementation
    presenter = GetTeamMemberLevelsWithMembersPresenterImplementation()

    from ib_iam.interactors.levels.get_team_member_levels_with_members_interactor import \
        GetTeamMemberLevelsWithMembersInteractor
    interactor = GetTeamMemberLevelsWithMembersInteractor(
        team_member_level_storage=team_member_level_storage,
        user_storage=user_storage
    )

    response = interactor.get_team_member_levels_with_members_wrapper(
        team_id=team_id, presenter=presenter, user_id=user_id
    )
    return response
