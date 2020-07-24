from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    user_id = str(user.user_id)
    from ib_iam.storages.storage_implementation import StorageImplementation
    storage = StorageImplementation()

    from ib_iam.presenters.get_user_profile_presenter_implementation import \
        GetUserProfilePresenterImplementation
    presenter = GetUserProfilePresenterImplementation()
    from ib_iam.interactors.get_user_profile_interactor import \
        GetUserProfileInteractor
    interactor = GetUserProfileInteractor(
        storage=storage
    )
    response = interactor.get_user_profile_wrapper(
        user_id=user_id, presenter=presenter
    )
    return response
