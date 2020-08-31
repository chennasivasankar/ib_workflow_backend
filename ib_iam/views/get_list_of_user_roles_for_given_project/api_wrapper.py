from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs["path_params"]

    project_id = str(path_params["project_id"])

    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()

    from ib_iam.presenters.get_list_of_user_roles_for_given_project_presenter_implementation import \
        GetListOfUserRolesForGivenProjectPresenterImplementation
    presenter = GetListOfUserRolesForGivenProjectPresenterImplementation()

    from ib_iam.interactors.get_list_of_user_roles_for_given_project_interactor import \
        GetListOfUserRolesForGivenProjectInteractor
    interactor = GetListOfUserRolesForGivenProjectInteractor(
        user_storage=user_storage
    )

    response = interactor.get_specific_project_details_wrapper(
        project_id=project_id, presenter=presenter
    )
    return response
