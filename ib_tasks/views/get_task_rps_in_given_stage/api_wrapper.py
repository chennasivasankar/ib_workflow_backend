from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from ib_tasks.storages.storage_implementation import StorageImplementation, StagesStorageImplementation
from ib_tasks.presenters.get_task_rps_presenter_implementation import \
    GetTaskRpsPresenterImplementation
from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation
from ib_tasks.interactors.task_dtos import GetTaskRPsParametersDTO
from ib_tasks.interactors.get_task_related_rps_in_given_stage import \
    GetTaskRPsInteractor
from ...storages.task_stage_storage_implementation import TaskStageStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    request_params = kwargs['request_data']
    task_id = request_params['task_id']
    stage_id = request_params['stage_id']

    parameters = GetTaskRPsParametersDTO(
        task_id=task_id,
        user_id=user.user_id,
        stage_id=stage_id
    )
    storage = StorageImplementation()

    task_storage = TasksStorageImplementation()
    stage_storage = StagesStorageImplementation()
    task_stage_storage = TaskStageStorageImplementation()
    presenter = GetTaskRpsPresenterImplementation()

    interactor = GetTaskRPsInteractor(
        storage=storage, task_storage=task_storage,
        stage_storage=stage_storage, task_stage_storage=task_stage_storage
    )
    response = interactor.get_task_rps_wrapper(presenter, parameters)

    return response
