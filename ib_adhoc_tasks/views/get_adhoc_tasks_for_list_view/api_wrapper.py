from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    query_params = kwargs['query_params']
    request_body = kwargs.get('request_body')
    user_id = user.user_id
    project_id = query_params["project_id"]
    limit = query_params["limit"]
    offset = query_params["offset"]
    group_limit = query_params["group_limit"]
    group_offset = query_params["group_offset"]
    group_by_key = None
    if request_body:
        group_by_key = request_body.get('group_by_key')

    from ib_adhoc_tasks.interactors.get_tasks_for_list_view_interactor import \
        GetTasksForListViewInteractor

    from ib_adhoc_tasks.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()

    from ib_adhoc_tasks.storages.elastic_storage_implementation import \
        ElasticStorageImplementation
    elastic_storage = ElasticStorageImplementation()

    from ib_adhoc_tasks.presenters\
        .get_tasks_for_list_view_presenter_implementation import \
        GetTasksForListViewPresenterImplementation
    presenter = GetTasksForListViewPresenterImplementation()

    interactor = GetTasksForListViewInteractor(
        storage=storage, elastic_storage=elastic_storage
    )

    from ib_adhoc_tasks.interactors.dtos.dtos import OffsetLimitDTO
    task_offset_limit_dto = OffsetLimitDTO(
        offset=offset, limit=limit
    )

    group_offset_limit_dto = OffsetLimitDTO(
        offset=group_offset, limit=group_limit
    )

    from ib_adhoc_tasks.interactors.dtos.dtos import GroupByInfoListViewDTO
    group_by_info_list_view_dto = GroupByInfoListViewDTO(
        project_id=project_id,
        user_id=user_id,
        group_by_key=group_by_key,
        task_offset_limit_dto=task_offset_limit_dto,
        group_offset_limit_dto=group_offset_limit_dto
    )

    response = interactor.get_tasks_for_list_view_wrapper(
        presenter=presenter,
        group_by_info_list_view_dto=group_by_info_list_view_dto
    )
    return response
