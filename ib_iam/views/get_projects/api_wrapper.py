from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = str(user_obj.user_id)
    query_params = kwargs["query_params"]
    offset = query_params.get("offset")
    limit = query_params.get("limit")
    from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
    pagination_dto = PaginationDTO(offset=offset, limit=limit)
    from ib_iam.storages.project_storage_implementation import \
        ProjectStorageImplementation
    from ib_iam.presenters.get_projects_presenter_implementation import \
        GetProjectsPresenterImplementation
    from ib_iam.interactors.get_projects_interactor import \
        GetProjectsInteractor
    project_storage = ProjectStorageImplementation()
    from ib_iam.storages.team_storage_implementation import \
        TeamStorageImplementation
    team_storage = TeamStorageImplementation()
    presenter = GetProjectsPresenterImplementation()
    interactor = GetProjectsInteractor(
        project_storage=project_storage, team_storage=team_storage
    )
    response = interactor.get_projects_wrapper(
        presenter=presenter, user_id=user_id, pagination_dto=pagination_dto
    )
    return response
