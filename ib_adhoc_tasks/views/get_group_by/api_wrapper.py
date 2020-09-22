from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = str(user_object.user_id)
    project_id = kwargs["project_id"]

    from ib_adhoc_tasks.interactors.group_by_interactor import \
        GroupByInteractor
    from ib_adhoc_tasks.storages.storage_implementation import \
        StorageImplementation
    from ib_adhoc_tasks.presenters.get_group_by_presenter_implementation import \
        GetGroupByPresenterImplementation
    storage = StorageImplementation()
    presenter = GetGroupByPresenterImplementation()
    interactor = GroupByInteractor(storage=storage)

    return interactor.get_group_by_wrapper(
        project_id=project_id, user_id=user_id,
        presenter=presenter
    )
