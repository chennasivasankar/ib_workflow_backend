from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...constants.enum import ViewType
from ...interactors.get_tasks_to_relevant_search_query \
    import GetTasksToRelevantSearchQuery, SearchQueryDTO
from ...presenters.get_all_tasks_overview_for_user_presenter_impl \
    import GetFilteredTasksOverviewForUserPresenterImplementation
from ...storages.action_storage_implementation import ActionsStorageImplementation
from ...storages.elasticsearch_storage_implementation import ElasticSearchStorageImplementation
from ...storages.fields_storage_implementation import FieldsStorageImplementation
from ...storages.storage_implementation import StagesStorageImplementation
from ...storages.task_stage_storage_implementation import TaskStageStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs['request_query_params']
    user_obj = kwargs['user']
    search_query_dto = get_search_query_dto(request_data, user_obj.user_id)
    stage_storage = StagesStorageImplementation()
    task_storage = TasksStorageImplementation()
    field_storage = FieldsStorageImplementation()
    action_storage = ActionsStorageImplementation()
    elastic_storage = ElasticSearchStorageImplementation()
    presenter = GetFilteredTasksOverviewForUserPresenterImplementation()
    task_stage_storage = TaskStageStorageImplementation()
    interactor = GetTasksToRelevantSearchQuery(
        stage_storage=stage_storage, task_storage=task_storage,
        field_storage=field_storage, action_storage=action_storage,
        elasticsearch_storage=elastic_storage,
        task_stage_storage=task_stage_storage
    )
    response = interactor.get_all_tasks_overview_for_user_wrapper(
        search_query_dto=search_query_dto, presenter=presenter
    )
    return response


def get_search_query_dto(request_data, user_id: str):
    return SearchQueryDTO(
        offset=request_data.offset,
        limit=request_data.limit,
        user_id=user_id,
        query_value=request_data.search_query,
        view_type=ViewType.KANBAN.value
    )