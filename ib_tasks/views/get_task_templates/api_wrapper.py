from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id
    from ib_tasks.storages.tasks_storage_implementation \
        import TasksStorageImplementation
    from ib_tasks.presenters.get_task_templates_presenter_implementation \
        import GetTaskTemplatesPresenterImplementation
    from ib_tasks.interactors.get_task_templates_interactor \
        import GetTaskTemplatesInteractor
    storage = TasksStorageImplementation()
    presenter = GetTaskTemplatesPresenterImplementation()
    interactor = GetTaskTemplatesInteractor(
        task_storage=storage
    )

    response = interactor.get_task_templates_wrapper(
        user_id=user_id, presenter=presenter
    )
    return response
