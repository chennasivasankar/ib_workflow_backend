from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...interactors.get_next_stages_random_assignees_of_a_task_interactor \
    import \
    GetNextStagesRandomAssigneesOfATaskInteractor
from ...presenters.get_next_stages_random_assignees_of_a_task_presenter_impl \
    import \
    GetNextStagesRandomAssigneesOfATaskPresenterImpl
from ...storages.action_storage_implementation import \
    ActionsStorageImplementation
from ...storages.storage_implementation import StagesStorageImplementation, \
    StorageImplementation
from ...storages.task_stage_storage_implementation import \
    TaskStageStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    task_id = request_data['task_id']
    action_id = request_data['action_id']
    stage_storage = StagesStorageImplementation()
    task_storage = TasksStorageImplementation()
    action_storage = ActionsStorageImplementation()
    storage = StorageImplementation()
    presenter = GetNextStagesRandomAssigneesOfATaskPresenterImpl()
    task_stage_storage = TaskStageStorageImplementation()

    interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
        stage_storage=stage_storage, task_storage=task_storage,
        storage=storage, action_storage=action_storage,
        task_stage_storage=task_stage_storage
    )
    response = interactor. \
        get_next_stages_random_assignees_of_a_task_wrapper(
            presenter=presenter, action_id=action_id, task_display_id=task_id)
    return response
