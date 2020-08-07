from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.get_task_templates_fields_interactor import GetTaskTemplatesFieldsInteractor
from ...presenters.filter_presenter_implementation import FilterPresenterImplementation
from ...storages.fields_storage_implementation import FieldsStorageImplementation
from ...storages.gof_storage_implementation import GoFStorageImplementation
from ...storages.task_template_storage_implementation import TaskTemplateStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs['user']
    user_id = user_obj.user_id
    field_storage = FieldsStorageImplementation()
    task_template = TaskTemplateStorageImplementation()
    gof_storage = GoFStorageImplementation()
    task_storage = TasksStorageImplementation()
    interactor = GetTaskTemplatesFieldsInteractor(
        field_storage=field_storage,
        task_storage=task_storage,
        task_template_storage=task_template,
        gof_storage=gof_storage
    )
    presenter = FilterPresenterImplementation()
    response = \
        interactor.get_task_templates_fields_wrapper(
            user_id=user_id, presenter=presenter
        )

    return response
