from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.add_new_user_interactor import AddNewUserInteractor
from ib_iam.storages.storage_implementation import StorageImplementation
from ib_iam.presenters.add_new_user_presenter_implementation \
    import AddUserPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = AddUserPresenterImplementation()
    interactor = AddNewUserInteractor(storage=storage)

    user = kwargs['user']
    user_id = user.user_id
    request_object = kwargs["request_data"]
    name = request_object['name']
    email = request_object['email']
    company_id = request_object['company_id']
    teams = request_object['team_ids']
    roles = request_object['role_ids']

    response = interactor.add_new_user_wrapper(
        user_id=user_id, name=name, email=email, company_id=company_id,
        roles=roles, teams=teams,presenter=presenter)

    return response