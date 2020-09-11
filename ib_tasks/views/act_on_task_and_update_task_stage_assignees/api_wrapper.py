from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ib_tasks.interactors.act_on_task_and_update_task_stage_assignees_interactor import \
    ActOnTaskAndUpdateTaskStageAssigneesInteractor

from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.storages.elasticsearch_storage_implementation import \
    ElasticSearchStorageImplementation
from ib_tasks.storages.gof_storage_implementation import GoFStorageImplementation
from ib_tasks.storages.task_stage_storage_implementation import \
    TaskStageStorageImplementation
from ib_tasks.storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation
from ib_tasks.storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    from ...interactors.stages_dtos import StageAssigneeDTO
    user = kwargs['user']
    user_id = user.user_id
    request_dict = kwargs['request_data']
    task_display_id = request_dict['task_id']
    action_id = int(request_dict['action_id'])
    board_id = request_dict['board_id']
    view_type = request_dict.get('view_type', None)
    stage_assignees = request_dict['stage_assignees']
    stage_assignee_dtos = \
        [StageAssigneeDTO(db_stage_id=each_stage_assignee_item['stage_id'],
                          assignee_id=each_stage_assignee_item['assignee_id'],
                          team_id=each_stage_assignee_item['team_id'])
         for
         each_stage_assignee_item in stage_assignees]
    from ib_tasks.storages.create_or_update_task_storage_implementation \
        import CreateOrUpdateTaskStorageImplementation
    from ib_tasks.storages.fields_storage_implementation \
        import FieldsStorageImplementation
    from ib_tasks.storages.storage_implementation \
        import StorageImplementation, StagesStorageImplementation
    from ib_tasks.presenters.\
        act_on_task_and_upadte_task_stage_assignees_presenter import \
        ActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation
    presenter = ActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation()

    field_storage = FieldsStorageImplementation()
    storage = StorageImplementation()
    stage_storage = StagesStorageImplementation()
    gof_storage = GoFStorageImplementation()
    create_task_storage = CreateOrUpdateTaskStorageImplementation()
    task_storage = TasksStorageImplementation()
    action_storage = ActionsStorageImplementation()
    task_stage_storage = TaskStageStorageImplementation()
    elastic_search_storage = ElasticSearchStorageImplementation()
    task_template_storage = TaskTemplateStorageImplementation()

    interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
        user_id=user_id, action_id=action_id,
        board_id=board_id, storage=storage, gof_storage=gof_storage,
        stage_storage=stage_storage, field_storage=field_storage,
        task_storage=task_storage, action_storage=action_storage,
        task_stage_storage=task_stage_storage, view_type=view_type,
        elasticsearch_storage=elastic_search_storage,
        create_task_storage=create_task_storage,
        task_template_storage=task_template_storage
    )

    response = interactor.\
        act_on_task_interactor_and_update_task_stage_assignees_wrapper(
        presenter=presenter, task_display_id=task_display_id,
        stage_assignee_dtos=stage_assignee_dtos)
    return response
