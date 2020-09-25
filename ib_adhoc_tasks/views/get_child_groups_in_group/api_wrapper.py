from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    query_params = kwargs["query_params"]
    user = kwargs["user"]
    request_data = kwargs["request_data"]

    project_id = query_params["project_id"]
    limit = query_params["limit"]
    offset = query_params["offset"]
    group_limit = query_params["group_limit"]
    group_offset = query_params["group_offset"]
    user_id = user.user_id
    group_by_value = request_data["group_by_value"]

    from ib_adhoc_tasks.interactors.dtos.dtos import \
        GetChildGroupsInGroupInputDTO
    get_child_groups_in_group_input_dto = GetChildGroupsInGroupInputDTO(
        user_id=user_id, project_id=project_id, limit=limit, offset=offset,
        group_limit=group_limit, group_offset=group_offset,
        group_by_value=group_by_value
    )

    from ib_adhoc_tasks.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()

    from ib_adhoc_tasks.storages.elastic_storage_implementation import \
        ElasticStorageImplementation
    elastic_storage = ElasticStorageImplementation()

    from ib_adhoc_tasks.interactors.get_child_groups_in_group_interactor import \
        GetChildGroupsInGroupInteractor
    interactor = GetChildGroupsInGroupInteractor(
        storage=storage, elastic_storage=elastic_storage
    )

    from ib_adhoc_tasks.presenters.get_child_groups_in_group_presenter_implementation import \
        GetChildGroupsInGroupPresenterImplementation
    presenter = GetChildGroupsInGroupPresenterImplementation()

    response = interactor.get_child_groups_in_group_wrapper(
        get_child_groups_in_group_input_dto=get_child_groups_in_group_input_dto,
        presenter=presenter
    )
    return response
