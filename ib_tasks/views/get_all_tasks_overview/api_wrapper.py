from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_tasks.interactors.get_all_tasks_overview_for_user_interactor import \
    GetAllTasksOverviewForUserInteractor, UserIdPaginationDTO
from .validator_class import ValidatorClass
from ib_tasks.presenters.get_all_tasks_overview_for_user_presenter_impl import \
    GetAllTasksOverviewForUserPresenterImpl
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.storages.fields_storage_implementation import \
    FieldsStorageImplementation
from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.storages.task_stage_storage_implementation import \
    TaskStageStorageImplementation
from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_account_obj = kwargs['user']
    user_id = user_account_obj.user_id
    params = kwargs['query_params']
    offset = params['offset']
    limit = params['limit']

    user_id_with_pagination_dto = UserIdPaginationDTO(user_id=user_id,
                                                      offset=offset,
                                                      limit=limit)
    presenter = GetAllTasksOverviewForUserPresenterImpl()
    stage_storage = StagesStorageImplementation()
    task_storage = TasksStorageImplementation()
    field_storage = FieldsStorageImplementation()
    action_storage = ActionsStorageImplementation()
    task_stage_storage = TaskStageStorageImplementation()

    interactor = GetAllTasksOverviewForUserInteractor(
        stage_storage=stage_storage,
        task_storage=task_storage,
        field_storage=field_storage, action_storage=action_storage,
        task_stage_storage=task_stage_storage
    )
    response = interactor. \
        get_all_tasks_overview_for_user_wrapper(presenter=presenter,
                                                user_id_with_pagination_dto=
                                                user_id_with_pagination_dto)
    return response
