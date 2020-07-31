from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.edit_user_interactor import EditUserInteractor
from ib_iam.presenters.edit_user_presenter_implementation import EditUserPresenterImplementation
from ib_iam.storages.user_storage_implementation import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = UserStorageImplementation()
    presenter = EditUserPresenterImplementation()
    interactor = EditUserInteractor(storage=storage)

    admin_user_id = kwargs['user'].user_id
    user_id = kwargs["path_params"]["user_id"]
    request_object = kwargs["request_data"]
    name = request_object['name']
    email = request_object['email']
    company_id = request_object['company_id']
    teams = request_object['team_ids']
    roles = request_object['role_ids']
    response = interactor.edit_user_wrapper(
        admin_user_id=admin_user_id, user_id=user_id, name=name,
        email=email, company_id=company_id,
        roles=roles, teams=teams, presenter=presenter)
    return response