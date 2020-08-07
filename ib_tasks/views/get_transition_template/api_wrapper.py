from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_account_obj = kwargs['user']
    user_id = user_account_obj.user_id
    transition_template_id = kwargs['transition_template_id']

    from ib_tasks.storages.tasks_storage_implementation \
        import TasksStorageImplementation
    from ib_tasks.storages.task_template_storage_implementation import \
        TaskTemplateStorageImplementation
    from ib_tasks.storages.gof_storage_implementation import \
        GoFStorageImplementation
    from ib_tasks.storages.fields_storage_implementation import \
        FieldsStorageImplementation
    from ib_tasks.presenters.get_transition_template_presenter_implementation \
        import GetTransitionTemplatePresenterImplementation
    from ib_tasks.interactors.get_transition_template_interactor \
        import GetTransitionTemplateInteractor

    task_storage = TasksStorageImplementation()
    task_template_storage = TaskTemplateStorageImplementation()
    gof_storage = GoFStorageImplementation()
    field_storage = FieldsStorageImplementation()
    presenter = GetTransitionTemplatePresenterImplementation()

    interactor = GetTransitionTemplateInteractor(
        task_storage=task_storage,
        task_template_storage=task_template_storage,
        gof_storage=gof_storage,
        field_storage=field_storage
    )
    response = interactor.get_transition_template_wrapper(
        user_id=user_id, presenter=presenter,
        transition_template_id=transition_template_id
    )
    return response
