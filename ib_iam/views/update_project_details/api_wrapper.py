from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ib_iam.interactors.dtos.dtos import CompleteProjectDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_iam.interactors.dtos.dtos import CompleteProjectDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    complete_project_details_dto = \
        _convert_to_complete_project_details_dto(kwargs)

    from ib_iam.storages.project_storage_implementation import \
        ProjectStorageImplementation
    project_storage = ProjectStorageImplementation()
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()
    from ib_iam.storages.team_storage_implementation import \
        TeamStorageImplementation
    team_storage = TeamStorageImplementation()
    from ib_iam.presenters.update_project_presenter_implementation import \
        UpdateProjectPresenterImplementation
    presenter = UpdateProjectPresenterImplementation()
    from ib_iam.interactors.project_interactor import ProjectInteractor
    interactor = ProjectInteractor(project_storage=project_storage,
                                   team_storage=team_storage,
                                   user_storage=user_storage)

    response_data = interactor.update_project_wrapper(
        presenter=presenter,
        complete_project_details_dto=complete_project_details_dto)

    return response_data


def _convert_to_complete_project_details_dto(kwargs) \
        -> CompleteProjectDetailsDTO:
    request_data = kwargs["request_data"]
    roles = request_data["roles"]
    role_dtos = [_convert_to_role_dtos(role) for role in roles]
    project_with_team_ids_and_roles_dto = CompleteProjectDetailsDTO(
        project_id=kwargs["path_params"]["project_id"],
        name=request_data["name"],
        description=request_data.get("description", None),
        logo_url=request_data.get("logo_url", None),
        team_ids=request_data["team_ids"],
        roles=role_dtos)
    return project_with_team_ids_and_roles_dto


def _convert_to_role_dtos(role) -> RoleDTO:
    from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
    role_dto = RoleDTO(
        role_id=role.get("role_id", None),
        name=role["role_name"],
        description=role.get("description", None))
    return role_dto
