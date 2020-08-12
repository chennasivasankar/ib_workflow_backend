from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.get_task_stages_history import GetTaskStagesHistory
from ...presenters.get_task_stage_history_presenter_implementation \
    import GetTaskStageHistoryPresenterImplementation
from ...storages.task_stage_storage_implementation import TaskStageStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    task_id = int(kwargs['task_id'])
    task_stage = TaskStageStorageImplementation()
    task_storage = TasksStorageImplementation()
    presenter = GetTaskStageHistoryPresenterImplementation()
    interactor = GetTaskStagesHistory(
        task_storage=task_storage, stage_storage=task_stage
    )
    response = interactor.get_task_stages_history_wrapper(
        task_id=task_id, presenter=presenter
    )
    return response