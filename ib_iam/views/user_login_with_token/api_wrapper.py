from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    token = kwargs["query_params"]["token"]
    request_data = kwargs["request_data"]
    is_request_data_not_none = request_data is not None
    name = None
    if is_request_data_not_none:
        name = request_data.get("name", None)
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    from ib_iam.storages.team_storage_implementation import \
        TeamStorageImplementation
    from ib_iam.storages.project_storage_implementation import \
        ProjectStorageImplementation
    user_storage = UserStorageImplementation()
    team_storage = TeamStorageImplementation()
    project_storage = ProjectStorageImplementation()
    from ib_iam.interactors.auth.user_login_with_token_interactor import \
        LoginWithTokenInteractor
    interactor = LoginWithTokenInteractor(
        user_storage=user_storage,
        team_storage=team_storage,
        project_storage=project_storage
    )
    from ib_iam.presenters.login_with_user_token_presenter_implementation import \
        LoginWithUserTokePresenterImplementation
    presenter = LoginWithUserTokePresenterImplementation()

    response = interactor.login_with_token_wrapper(
        presenter=presenter, token=token, name=name
    )
    return response
