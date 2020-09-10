from typing import Dict, List, Any

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...constants.enum import ViewType
from ...interactors.get_tasks_to_relevant_search_query \
    import GetTasksToRelevantSearchQuery
from ...interactors.task_dtos import SearchQueryDTO
from ...presenters.get_all_tasks_overview_for_user_presenter_impl \
    import GetFilteredTasksOverviewForUserPresenterImplementation
from ...storages.action_storage_implementation import ActionsStorageImplementation
from ...storages.elasticsearch_storage_implementation import ElasticSearchStorageImplementation
from ...storages.fields_storage_implementation import FieldsStorageImplementation
from ...storages.filter_storage_implementation import FilterStorageImplementation
from ...storages.storage_implementation import StagesStorageImplementation
from ...storages.task_stage_storage_implementation import TaskStageStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_query_params']
    user_obj = kwargs['user']
    request_body = kwargs['request_data']
    templates_conditions = request_body.get('templates_conditions', [])
    project_id = request_body.get('project_id')
    apply_filters_dto = \
        get_apply_filters_dto(templates_conditions, project_id)
    search_query_dto = get_search_query_dto(
        request_data, user_obj.user_id, project_id
    )
    stage_storage = StagesStorageImplementation()
    task_storage = TasksStorageImplementation()
    field_storage = FieldsStorageImplementation()
    action_storage = ActionsStorageImplementation()
    elastic_storage = ElasticSearchStorageImplementation()
    presenter = GetFilteredTasksOverviewForUserPresenterImplementation()
    task_stage_storage = TaskStageStorageImplementation()
    filter_storage = FilterStorageImplementation()
    interactor = GetTasksToRelevantSearchQuery(
        stage_storage=stage_storage, task_storage=task_storage,
        field_storage=field_storage, action_storage=action_storage,
        elasticsearch_storage=elastic_storage,
        task_stage_storage=task_stage_storage,
        filter_storage=filter_storage
    )
    response = interactor.get_all_tasks_overview_for_user_wrapper(
        search_query_dto=search_query_dto, presenter=presenter,
        apply_filters_dto=apply_filters_dto
    )
    return response


def get_apply_filters_dto(
        templates_conditions: List[Dict[str, Any]], project_id: str):
    from ib_tasks.interactors.storage_interfaces.elastic_storage_interface \
        import ApplyFilterDTO

    apply_filters = []
    for template_conditions in templates_conditions:
        for condition in template_conditions['conditions']:
            apply_filters.append(ApplyFilterDTO(
                template_id=template_conditions['template_id'],
                field_id=condition['field_id'],
                operator=condition['operator'],
                value=condition['value'],
                project_id=project_id
            ))
    return apply_filters


def get_search_query_dto(request_data, user_id: str, project_id: str):
    return SearchQueryDTO(
        offset=request_data.offset,
        limit=request_data.limit,
        user_id=user_id,
        query_value=request_data.search_query,
        view_type=ViewType.KANBAN.value,
        project_id=project_id
    )
