from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs["path_params"]

    team_id = path_params["team_id"]
    level_hierarchy = path_params["level_hierarchy"]

    from ib_iam.storages.team_member_level_storage_implementation import \
        TeamMemberLevelStorageImplementation
    team_member_level_storage = TeamMemberLevelStorageImplementation()

    from ib_iam.presenters.get_team_members_of_level_hierarchy_presenter_implementation import \
        GetTeamMembersOfLevelHierarchyPresenterImplementation
    presenter = GetTeamMembersOfLevelHierarchyPresenterImplementation()

    from ib_iam.interactors.get_team_members_of_level_hierarchy_interactor import \
        GetTeamMembersOfLevelHierarchyInteractor
    interactor = GetTeamMembersOfLevelHierarchyInteractor(
        team_member_level_storage=team_member_level_storage
    )

    response = interactor.get_team_members_of_level_hierarchy_wrapper(
        team_id=team_id, level_hierarchy=level_hierarchy, presenter=presenter
    )
    return response
