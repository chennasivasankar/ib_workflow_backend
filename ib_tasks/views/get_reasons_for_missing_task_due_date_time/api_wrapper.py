from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_tasks.interactors.get_task_due_missing_reasons import \
    GetTaskDueMissingReasonsInteractor
from ib_tasks.presenters.task_due_delay_presenter_implementation import \
    TaskDueDetailsPresenterImplementation
from ib_tasks.storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    task_id=request_data['task_id']
    user = kwargs["user"]

    storage = StorageImplementation()
    from ib_tasks.storages.tasks_storage_implementation import TasksStorageImplementation
    task_storage = TasksStorageImplementation()
    presenter = TaskDueDetailsPresenterImplementation()
    interactor = GetTaskDueMissingReasonsInteractor(storage=storage,
                                                    task_storage=task_storage)

    response = interactor.get_task_due_missing_reasons_wrapper(presenter=presenter,
                                                               task_display_id=task_id,
                                                               user_id=user.user_id)
    return response
