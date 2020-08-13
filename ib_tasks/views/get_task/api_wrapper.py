from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_tasks.storages.create_or_update_task_storage_implementation \
        import CreateOrUpdateTaskStorageImplementation
from ib_tasks.interactors.get_task_interactor \
    import GetTaskInteractor
from ib_tasks.presenters.get_task_presenter_implementation \
    import GetTaskPresenterImplementation
from ib_tasks.storages.fields_storage_implementation \
    import FieldsStorageImplementation
from ...storages.action_storage_implementation import \
    ActionsStorageImplementation
from ...storages.storage_implementation import StorageImplementation
from ...storages.task_stage_storage_implementation import \
    TaskStageStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs['user']
    query_params_dict = kwargs['query_params']
    task_display_id = query_params_dict['task_id']
    user_id = user_obj.user_id

    storage = CreateOrUpdateTaskStorageImplementation()
    stages_storage = FieldsStorageImplementation()
    presenter = GetTaskPresenterImplementation()
    task_storage1 = StorageImplementation()
    task_stage_storage = TaskStageStorageImplementation()
    action_storage = ActionsStorageImplementation()
    task_storage = TasksStorageImplementation()
    interactor = GetTaskInteractor(
        storage=storage, stages_storage=stages_storage,
        task_storage1=task_storage1, action_storage=action_storage,
        task_stage_storage=task_stage_storage, task_storage=task_storage
    )
    response = interactor.get_task_details_wrapper(
       user_id=user_id, task_display_id=task_display_id, presenter=presenter
    )
    return response
