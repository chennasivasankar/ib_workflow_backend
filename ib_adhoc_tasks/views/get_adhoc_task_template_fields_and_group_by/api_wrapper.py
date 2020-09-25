from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = str(user_object.user_id)
    project_id = kwargs["query_params"]["project_id"]
    view_type = kwargs["query_params"]["view_type"]

    from ib_adhoc_tasks.interactors \
        .get_adhoc_task_template_fields_and_group_by_interactor import \
        GetAdhocTaskTemplateFieldsAndGroupBy
    from ib_adhoc_tasks.storages.storage_implementation import \
        StorageImplementation
    from ib_adhoc_tasks.presenters \
        .get_adhoc_task_template_fields_and_group_by_presenter_implementation \
        import GetAdhocTaskTemplateFieldsAndGroupByPresenterImplementation
    storage = StorageImplementation()
    presenter = GetAdhocTaskTemplateFieldsAndGroupByPresenterImplementation()
    interactor = GetAdhocTaskTemplateFieldsAndGroupBy(storage=storage)

    return interactor.get_adhoc_task_template_fields_and_group_by_wrapper(
        project_id=project_id, user_id=user_id, view_type=view_type,
        presenter=presenter
    )
