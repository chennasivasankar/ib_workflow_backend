from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_boards.constants.enum import ViewType
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.storages.fields_storage_implementation import \
    FieldsStorageImplementation
from .validator_class import ValidatorClass
from ...presenters.get_all_tasks_overview_for_user_presenter_impl import \
    GetFilteredTasksOverviewForUserPresenterImplementation
from ...storages.storage_implementation import StagesStorageImplementation
from ...storages.task_stage_storage_implementation import \
    TaskStageStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_account_obj = kwargs['user']
    user_id = user_account_obj.user_id
    params = kwargs['query_params']
    offset = params['offset']
    limit = params['limit']

    presenter = GetFilteredTasksOverviewForUserPresenterImplementation()
    stage_storage = StagesStorageImplementation()
    task_storage = TasksStorageImplementation()
    field_storage = FieldsStorageImplementation()
    action_storage = ActionsStorageImplementation()
    from ib_tasks.storages.filter_storage_implementation import \
        FilterStorageImplementation
    filter_storage = FilterStorageImplementation()
    from ib_tasks.storages.elasticsearch_storage_implementation import \
        ElasticSearchStorageImplementation
    elasticsearch_storage = ElasticSearchStorageImplementation()
    task_stage_storage = TaskStageStorageImplementation()

    from ib_tasks.interactors.get_filtered_tasks_details_interactor import \
        GetTaskDetailsByFilterInteractor
    interactor = GetTaskDetailsByFilterInteractor(
        stage_storage=stage_storage,
        task_storage=task_storage,
        field_storage=field_storage,
        action_storage=action_storage,
        elasticsearch_storage=elasticsearch_storage,
        filter_storage=filter_storage,
        task_stage_storage=task_stage_storage
    )
    response = interactor.get_filtered_tasks_overview_for_user_wrapper(
        presenter=presenter,
        user_id=user_id,
        limit=limit,
        offset=offset,
        view_type=ViewType.KANBAN.value
    )
    return response
