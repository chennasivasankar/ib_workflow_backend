from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs["path_params"]
    request_data = kwargs["request_data"]

    team_id = path_params["team_id"]
    level_hierarchy = path_params["level_hierarchy"]
    members = request_data["add_members_to_superior"]

    from ib_iam.interactors.dtos.dtos import \
        ImmediateSuperiorUserIdWithUserIdsDTO
    immediate_superior_user_id_with_member_ids_dtos = [
        ImmediateSuperiorUserIdWithUserIdsDTO(
            immediate_superior_user_id=member_dict[
                "immediate_superior_user_id"],
            member_ids=member_dict["member_ids"]
        )
        for member_dict in members
    ]

    from ib_iam.storages.team_member_level_storage_implementation import \
        TeamMemberLevelStorageImplementation
    team_member_level_storage = TeamMemberLevelStorageImplementation()

    from ib_iam.presenters.add_members_to_superiors_presenter_implementation import \
        AddMembersToSuperiorsPresenterImplementation
    presenter = AddMembersToSuperiorsPresenterImplementation()

    from ib_iam.interactors.add_members_to_superiors_interactor import \
        AddMembersToSuperiorsInteractor
    interactor = AddMembersToSuperiorsInteractor(
        team_member_level_storage=team_member_level_storage
    )

    response = interactor.add_members_to_superiors_wrapper(
        team_id=team_id, level_hierarchy=level_hierarchy, presenter=presenter,
        immediate_superior_user_id_with_member_ids_dtos=immediate_superior_user_id_with_member_ids_dtos
    )
    return response
