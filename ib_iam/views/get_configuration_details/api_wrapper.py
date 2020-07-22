from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.get_user_options_interactor import GetUserOptionsDetails
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetUserOptionsDetails(storage=storage)

    user = kwargs['user']
    user_id = user.id


    response = interactor.get_configuration_details_wrapper(
        presenter=presenter, user_id=user_id)

    return response