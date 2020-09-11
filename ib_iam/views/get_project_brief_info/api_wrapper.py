from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]

    user_id = user_object.user_id

    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    from ib_iam.storages.project_storage_implementation import \
        ProjectStorageImplementation
    user_storage = UserStorageImplementation()
    project_storage = ProjectStorageImplementation()

    from ib_iam.presenters.get_project_brief_info_presenter_implementation import \
        GetProjectBriefInfoPresenterImplementation
    presenter = GetProjectBriefInfoPresenterImplementation()

    from ib_iam.interactors.get_project_brief_info_interactor import \
        GetProjectBriefInfoInteractor
    interactor = GetProjectBriefInfoInteractor(
        user_storage=user_storage, project_storage=project_storage
    )

    response = interactor.get_project_brief_info_wrapper(
        user_id=user_id, presenter=presenter
    )
    return response
