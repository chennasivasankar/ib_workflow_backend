from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    from ib_iam.storages.project_storage_implementation import \
        ProjectStorageImplementation
    from ib_iam.presenters.get_projects_presenter_implementation import \
        GetProjectsPresenterImplementation
    from ib_iam.interactors.get_projects_interactor import \
        GetProjectsInteractor
    project_storage = ProjectStorageImplementation()
    presenter = GetProjectsPresenterImplementation()
    interactor = GetProjectsInteractor(project_storage=project_storage)
    response = interactor.get_projects_wrapper(presenter=presenter)
    return response
