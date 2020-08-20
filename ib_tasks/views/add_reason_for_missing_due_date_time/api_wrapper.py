from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_tasks.interactors.add_task_due_details_interactor import AddTaskDueDetailsInteractor
from ib_tasks.interactors.task_dtos import TaskDueParametersDTO
from ib_tasks.presenters.task_due_delay_presenter_implementation import TaskDueDetailsPresenterImplementation
from ib_tasks.storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    request_params = kwargs['request_data']
    reason_id = request_params['reason_id']
    reason = request_params['reason']
    updated_due_datetime = request_params['updated_due_date_time']
    task_id = request_params['task_id']

    parameters = TaskDueParametersDTO(
        user_id=user.user_id,
        reason_id=reason_id,
        reason=reason,
        due_date_time=updated_due_datetime
    )

    storage = StorageImplementation()
    presenter = TaskDueDetailsPresenterImplementation()
    from ib_tasks.storages.tasks_storage_implementation import TasksStorageImplementation
    task_storage = TasksStorageImplementation()
    interactor = AddTaskDueDetailsInteractor(storage=storage,
                                             task_storage=task_storage)
    response = interactor.add_task_due_details_wrapper(presenter=presenter,
                                                       due_details=parameters,
                                                       task_display_id=task_id)
    return response
