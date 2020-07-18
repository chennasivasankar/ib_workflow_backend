from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.add_new_user_interactor import AddNewUserInteractor
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = AddNewUserInteractor(storage=storage)

    user = kwargs['user']
    user_id = user.id
    request_object = kwargs["request_data"]
    name = request_object['name']
    email = request_object['email']

    response = interactor.add_new_user_wrapper(
        user_id=user_id, name=name, email=email, presenter=presenter)

    return response
