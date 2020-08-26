from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    project_with_team_ids_and_roles_dto = \
        _convert_to_project_with_team_ids_and_roles_dto(kwargs)

    from ib_iam.storages.project_storage_implementation import \
        ProjectStorageImplementation
    project_storage = ProjectStorageImplementation()
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()
    from ib_iam.storages.team_storage_implementation import \
        TeamStorageImplementation
    team_storage = TeamStorageImplementation()
    from ib_iam.presenters.add_project_presenter_implementation import \
        AddProjectPresenterImplementation
    presenter = AddProjectPresenterImplementation()
    from ib_iam.interactors.project_interactor import ProjectInteractor
    interactor = ProjectInteractor(project_storage=project_storage,
                                   team_storage=team_storage,
                                   user_storage=user_storage)

    response_data = interactor.add_project_wrapper(
        presenter=presenter,
        project_with_team_ids_and_roles_dto=project_with_team_ids_and_roles_dto
    )

    return response_data


def _convert_to_project_with_team_ids_and_roles_dto(kwargs):
    request_data = kwargs["request_data"]
    roles = request_data["roles"]
    role_dtos = [_convert_to_role_dtos(role) for role in roles]
    from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
    project_with_team_ids_and_roles_dto = ProjectWithTeamIdsAndRolesDTO(
        name=request_data["name"],
        description=request_data.get("description", None),
        logo_url=request_data.get("logo_url", None),
        team_ids=request_data["team_ids"],
        roles=role_dtos)
    return project_with_team_ids_and_roles_dto


def _convert_to_role_dtos(role):
    from ib_iam.interactors.storage_interfaces.dtos import \
        RoleNameAndDescriptionDTO
    role_dto = RoleNameAndDescriptionDTO(
        name=role["role_name"],
        description=role.get("description", None)
    )
    return role_dto
