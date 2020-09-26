from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.dtos.dtos import GroupByInfoKanbanViewDTO, OffsetLimitDTO, \
    GroupBYKeyDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    query_params = kwargs['query_params']

    user_id = user.user_id
    project_id = query_params["project_id"]
    limit = query_params["limit"]
    offset = query_params["offset"]
    group1_limit = query_params["group1_limit"]
    group1_offset = query_params["group1_offset"]
    group2_limit = query_params["group2_limit"]
    group2_offset = query_params["group2_offset"]
    request_data = kwargs.get('request_data')
    group_by_keys = None
    if request_data:
        group_by_keys = request_data.get('group_by_keys')
    group_by_details = []
    if group_by_keys:
        group_by_details = [
            GroupBYKeyDTO(
                group_by_key=group_by.get('group_by_key'),
                order=group_by.get('group_by_key')
            )
            for group_by in group_by_keys
        ]

    task_offset_limit_dto = OffsetLimitDTO(offset=offset, limit=limit)
    group1_offset_limit_dto = OffsetLimitDTO(
        offset=group1_offset, limit=group1_limit
    )
    group2_offset_limit_dto = OffsetLimitDTO(
        offset=group2_offset, limit=group2_limit
    )
    group_by_info_kanban_view_dto = GroupByInfoKanbanViewDTO(
        project_id=project_id, user_id=user_id,
        group_by_details=group_by_details,
        task_offset_limit_dto=task_offset_limit_dto,
        group1_offset_limit_dto=group1_offset_limit_dto,
        group2_offset_limit_dto=group2_offset_limit_dto
    )

    from ib_adhoc_tasks.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()

    from ib_adhoc_tasks.storages.elastic_storage_implementation import \
        ElasticStorageImplementation
    elastic_storage = ElasticStorageImplementation()

    from ib_adhoc_tasks.presenters\
        .get_tasks_for_kanban_view_presenter_implementation import \
        GetTasksForKanbanViewPresenterImplementation
    presenter = GetTasksForKanbanViewPresenterImplementation()

    from ib_adhoc_tasks.interactors.get_tasks_for_kanban_view_interactor \
        import \
        GetTasksForKanbanViewInteractor
    interactor = GetTasksForKanbanViewInteractor(
        storage=storage, elastic_storage=elastic_storage
    )
    response = interactor.get_tasks_for_kanban_view_wrapper(
        group_by_info_kanban_view_dto=group_by_info_kanban_view_dto,
        presenter=presenter
    )
    return response

