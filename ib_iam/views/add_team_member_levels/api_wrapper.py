from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs["path_params"]
    request_data = kwargs["request_data"]

    team_id = path_params["team_id"]
    team_member_levels = request_data["team_member_levels"]

    from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO
    team_member_level_dtos = [
        TeamMemberLevelDTO(
            team_member_level_name=team_member_level_dict["level_name"],
            level_hierarchy=team_member_level_dict["level_hierarchy"]
        )
        for team_member_level_dict in team_member_levels
    ]

    from ib_iam.storages.team_member_level_storage_implementation import \
        TeamMemberLevelStorageImplementation
    team_member_level_storage = TeamMemberLevelStorageImplementation()

    from ib_iam.presenters.add_levels_presenter_implementation import \
        AddTeamMemberLevelsPresenterImplementation
    presenter = AddTeamMemberLevelsPresenterImplementation()

    from ib_iam.interactors.add_team_member_levels_interactor import \
        AddTeamMemberLevelsInteractor
    interactor = AddTeamMemberLevelsInteractor(
        team_member_level_storage=team_member_level_storage
    )

    response = interactor.add_team_member_levels_wrapper(
        team_id=team_id, team_member_level_dtos=team_member_level_dtos,
        presenter=presenter
    )
    return response
