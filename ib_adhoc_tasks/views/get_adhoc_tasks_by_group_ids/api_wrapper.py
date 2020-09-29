from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    query_params = kwargs["query_params"]
    user = kwargs["user"]
    request_data = kwargs["request_data"]

    project_id = query_params["project_id"]
    view_type = request_data["view_type"]
    limit = query_params["limit"]
    offset = query_params["offset"]
    group_by_values = request_data["group_by_values"]
    user_id = user.user_id

    from ib_adhoc_tasks.interactors.dtos.dtos import \
        GetTaskDetailsInGroupInputDTO
    get_task_details_in_group_input_dto = GetTaskDetailsInGroupInputDTO(
        project_id=project_id,
        view_type=view_type,
        limit=limit,
        offset=offset,
        group_by_values=group_by_values,
        user_id=user_id
    )

    from ib_adhoc_tasks.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()

    from ib_adhoc_tasks.storages.elastic_storage_implementation import \
        ElasticStorageImplementation
    elastic_storage = ElasticStorageImplementation()

    from ib_adhoc_tasks.interactors.get_task_details_in_group_interactor import \
        GetTaskDetailsInGroupInteractor
    interactor = GetTaskDetailsInGroupInteractor(
        storage=storage, elastic_storage=elastic_storage
    )

    from ib_adhoc_tasks.presenters.get_task_details_in_group_presenter_implementation import \
        GetTaskDetailsInGroupPresenterImplementation
    presenter = GetTaskDetailsInGroupPresenterImplementation()

    response = interactor.get_task_details_in_group_wrapper(
        get_task_details_in_group_input_dto=get_task_details_in_group_input_dto,
        presenter=presenter
    )
    return response
