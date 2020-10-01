from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...interactors.validate_task_fields_filled_or_not import \
    TaskFieldsFilledValidationInteractor
from ...presenters.validate_task_fields_presenter import \
    ValidateTaskFieldsPresenterImplementation
from ...storages.action_storage_implementation import \
    ActionsStorageImplementation
from ...storages.create_or_update_task_storage_implementation import \
    CreateOrUpdateTaskStorageImplementation
from ...storages.fields_storage_implementation import \
    FieldsStorageImplementation
from ...storages.gof_storage_implementation import GoFStorageImplementation
from ...storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].user_id
    request_data = kwargs['request_data']
    task_id = request_data.get('task_id')
    action_id = int(request_data.get('action_id'))

    field_storage = FieldsStorageImplementation()
    gof_storage = GoFStorageImplementation()
    create_task_storage = CreateOrUpdateTaskStorageImplementation()
    task_storage = TasksStorageImplementation()
    action_storage = ActionsStorageImplementation()
    task_template_storage = TaskTemplateStorageImplementation()
    presenter = ValidateTaskFieldsPresenterImplementation()

    interactor = TaskFieldsFilledValidationInteractor(
        create_task_storage=create_task_storage, field_storage=field_storage,
        task_storage=task_storage, action_storage=action_storage,
        task_template_storage=task_template_storage, gof_storage=gof_storage)
    response = interactor.validate_task_filled_fields_wrapper(
        task_id, action_id, user_id, presenter)
    return response
