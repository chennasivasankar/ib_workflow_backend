from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_account_obj = kwargs['user']
    user_id = user_account_obj.user_id

    from ib_tasks.storages.tasks_storage_implementation \
        import TasksStorageImplementation
    from ib_tasks.storages.task_template_storage_implementation import \
        TaskTemplateStorageImplementation
    from ib_tasks.storages.gof_storage_implementation import \
        GoFStorageImplementation
    from ib_tasks.storages.fields_storage_implementation import \
        FieldsStorageImplementation
    from ib_tasks.storages.storage_implementation import \
        StagesStorageImplementation
    from ib_tasks.presenters.get_task_templates_presenter_implementation \
        import GetTaskTemplatesPresenterImplementation
    from ib_tasks.interactors.get_task_templates_interactor \
        import GetTaskTemplatesInteractor

    task_storage = TasksStorageImplementation()
    task_template_storage = TaskTemplateStorageImplementation()
    gof_storage = GoFStorageImplementation()
    field_storage = FieldsStorageImplementation()
    stage_storage = StagesStorageImplementation()
    presenter = GetTaskTemplatesPresenterImplementation()

    interactor = GetTaskTemplatesInteractor(
        task_storage=task_storage,
        task_template_storage=task_template_storage,
        gof_storage=gof_storage,
        field_storage=field_storage,
        stage_storage=stage_storage
    )
    response = interactor.get_task_templates_wrapper(
        user_id=user_id, presenter=presenter
    )
    return response
