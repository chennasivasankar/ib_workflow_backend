from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.user_id

    from ib_tasks.interactors.filter_interactor \
        import FilterInteractor
    from ib_tasks.storages.filter_storage_implementation \
        import FilterStorageImplementation
    storage = FilterStorageImplementation()
    from ib_tasks.presenters.filter_presenter_implementation \
        import FilterPresenterImplementation
    presenter = FilterPresenterImplementation()
    interactor = FilterInteractor(
        filter_storage=storage, presenter=presenter
    )

    response = interactor.get_filters_details(user_id=user_id)

    return response