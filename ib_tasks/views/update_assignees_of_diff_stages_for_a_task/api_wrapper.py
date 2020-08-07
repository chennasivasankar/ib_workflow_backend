from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.stages_dtos import StageAssigneeDTO, \
    TaskIdWithStageAssigneesDTO
from ...interactors.update_task_stage_assignees_interactor import \
    UpdateTaskStageAssigneesInteractor
from ...presenters.update_task_stage_assignees_presenter_impl import \
    UpdateTaskStageAssigneesPresenterImplementation
from ...storages.storage_implementation import StagesStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    params = kwargs['path_params']
    task_id = params['task_id']
    request_data = kwargs['request_data']
    stage_assignees = request_data['stage_assignees']
    stage_assignee_dtos = \
        [StageAssigneeDTO(db_stage_id=each_stage_assignee_item['stage_id'],
                          assignee_id=each_stage_assignee_item['assignee_id']) for
         each_stage_assignee_item in stage_assignees]

    task_id_with_stage_assignees_dto = TaskIdWithStageAssigneesDTO(
        task_id=task_id, stage_assignees=stage_assignee_dtos)

    stage_storage = StagesStorageImplementation()
    task_storage = TasksStorageImplementation()
    presenter = UpdateTaskStageAssigneesPresenterImplementation()

    interactor = UpdateTaskStageAssigneesInteractor(
        stage_storage=stage_storage, task_storage=task_storage)
    response = interactor. \
        update_task_stage_assignees_wrapper(presenter=presenter,
                                            task_id_with_stage_assignees_dto=
                                            task_id_with_stage_assignees_dto)
    return response
