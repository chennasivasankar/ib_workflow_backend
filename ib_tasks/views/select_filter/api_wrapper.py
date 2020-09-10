from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.user_id
    request_dict = kwargs['request_data']
    filter_id = request_dict['filter_id']
    action = request_dict['action']

    from ib_tasks.storages.filter_storage_implementation \
        import FilterStorageImplementation
    storage = FilterStorageImplementation()
    from ib_tasks.presenters.filter_presenter_implementation \
        import FilterPresenterImplementation
    presenter = FilterPresenterImplementation()
    from ib_tasks.interactors.filters.update_filter_status import \
        UpdateFilerStatusInteractor
    interactor = UpdateFilerStatusInteractor(
        filter_storage=storage,
        presenter=presenter
    )
    response = interactor.update_filter_select_status_wrapper(
        user_id=user_id, filter_id=filter_id, filter_status=action
    )
    return response
