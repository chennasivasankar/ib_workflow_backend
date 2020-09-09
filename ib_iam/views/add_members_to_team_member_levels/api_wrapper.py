from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs["path_params"]
    request_data = kwargs["request_data"]

    team_id = path_params["team_id"]
    members = request_data["members"]

    from ib_iam.interactors.dtos.dtos import TeamMemberLevelIdWithMemberIdsDTO
    team_member_level_id_with_member_ids_dtos = [
        TeamMemberLevelIdWithMemberIdsDTO(
            team_member_level_id=str(member_dict["team_member_level_id"]),
            member_ids=list(map(str, member_dict["member_ids"]))
        )
        for member_dict in members
    ]

    from ib_iam.storages.team_member_level_storage_implementation import \
        TeamMemberLevelStorageImplementation
    team_member_level_storage = TeamMemberLevelStorageImplementation()

    from ib_iam.presenters.add_members_to_team_member_levels_presenter_implementation import \
        AddMembersToTeamMemberLevelsPresenterImplementation
    presenter = AddMembersToTeamMemberLevelsPresenterImplementation()

    from ib_iam.interactors.add_members_to_team_member_levels_interactor import \
        AddMembersToTeamMemberLevelsInteractor
    interactor = AddMembersToTeamMemberLevelsInteractor(
        team_member_level_storage=team_member_level_storage
    )

    response = interactor.add_members_to_team_member_levels_wrapper(
        team_id=team_id, presenter=presenter,
        team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos
    )
    return response
