from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...storages.action_storage_implementation import \
    ActionsStorageImplementation
from ...storages.elasticsearch_storage_implementation import \
    ElasticSearchStorageImplementation
from ...storages.task_stage_storage_implementation import \
    TaskStageStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.user_id
    request_dict = kwargs['request_data']
    task_id = request_dict['task_id']
    action_id = int(request_dict['action_id'])
    board_id = request_dict['board_id']
    from ib_tasks.storages.create_or_update_task_storage_implementation \
        import CreateOrUpdateTaskStorageImplementation
    from ib_tasks.storages.fields_storage_implementation \
        import FieldsStorageImplementation
    from ib_tasks.storages.storage_implementation \
        import StorageImplementation, StagesStorageImplementation
    from ib_tasks.interactors.user_action_on_task_interactor \
        import UserActionOnTaskInteractor
    from ib_tasks.presenters.user_action_on_task_presenter_implementation \
        import UserActionOnTaskPresenterImplementation
    presenter = UserActionOnTaskPresenterImplementation()
    field_storage = FieldsStorageImplementation()
    storage = StorageImplementation()
    stage_storage = StagesStorageImplementation()
    gof_storage = CreateOrUpdateTaskStorageImplementation()
    task_storage = TasksStorageImplementation()
    action_storage = ActionsStorageImplementation()
    task_stage_storage = TaskStageStorageImplementation()
    elastic_search_storage = ElasticSearchStorageImplementation()
    interactor = UserActionOnTaskInteractor(
        user_id=user_id, action_id=action_id,
        board_id=board_id, storage=storage, gof_storage=gof_storage,
        stage_storage=stage_storage, field_storage=field_storage,
        task_storage=task_storage, action_storage=action_storage,
        task_stage_storage=task_stage_storage,
        elasticsearch_storage=elastic_search_storage
    )

    response = interactor.user_action_on_task_wrapper(
        presenter=presenter, task_display_id=task_id
    )
    return response
