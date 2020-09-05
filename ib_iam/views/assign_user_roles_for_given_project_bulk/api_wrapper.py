from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs["path_params"]
    request_data = kwargs["request_data"]

    project_id = str(path_params["project_id"])
    users = request_data["users"]

    from ib_iam.tests.factories.interactor_dtos import \
        UserIdWithRoleIdsDTOFactory
    user_id_with_role_ids_dtos = [
        UserIdWithRoleIdsDTOFactory(
            user_id=str(user_dict["user_id"]),
            role_ids=user_dict["role_ids"]
        )
        for user_dict in users
    ]

    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()

    from ib_iam.presenters.assign_user_roles_for_given_project_bulk_presenter_implementation import \
        AssignUserRolesForGivenProjectBulkPresenterImplementation
    presenter = AssignUserRolesForGivenProjectBulkPresenterImplementation()

    from ib_iam.interactors.assign_user_roles_for_given_project_bulk_interactor import \
        AssignUserRolesForGivenProjectBulkInteractor
    interactor = AssignUserRolesForGivenProjectBulkInteractor(
        user_storage=user_storage
    )

    response = interactor.assign_user_roles_for_given_project_bulk_wrapper(
        project_id=project_id, presenter=presenter,
        user_id_with_role_ids_dtos=user_id_with_role_ids_dtos
    )
    return response