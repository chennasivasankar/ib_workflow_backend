from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.get_user_options_interactor import GetUserOptionsDetails
from ib_iam.presenters.get_user_options_presenter_implementation \
    import GetUserOptionsPresenterImplementation
from ib_iam.storages.user_storage_implementation \
    import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = UserStorageImplementation()
    presenter = GetUserOptionsPresenterImplementation()
    interactor = GetUserOptionsDetails(storage=storage)

    user = kwargs['user']
    user_id = user.user_id

    response = interactor.get_configuration_details_wrapper(
        presenter=presenter, user_id=user_id)

    return response
