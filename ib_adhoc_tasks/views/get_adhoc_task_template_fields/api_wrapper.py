from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    user_id = str(user.user_id)
    project_id = kwargs["query_params"]["project_id"]

    from ib_adhoc_tasks.interactors \
        .get_adhoc_task_template_fields_interactor import \
        AdhocTaskTemplateFieldsInteractor
    from ib_adhoc_tasks.presenters \
        .get_adhoc_task_template_fields_presenter_implementation import \
        GetAdhocTaskTemplateFieldsPresenterImplementation
    interactor = AdhocTaskTemplateFieldsInteractor()
    presenter = GetAdhocTaskTemplateFieldsPresenterImplementation()

    return interactor.get_adhoc_task_template_fields_wrapper(
        project_id=project_id, user_id=user_id, presenter=presenter
    )
