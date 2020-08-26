from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs['path_params']
    query_params = kwargs['query_params']
    stage_id = path_params['stage_id']
    task_id = query_params['task_id']
    search_query = query_params['search_query']
    offset = query_params['offset']
    limit = query_params['limit']

    from ib_iam.adapters.dtos import SearchQueryWithPaginationDTO
    search_query_with_pagination_dto = SearchQueryWithPaginationDTO(
        limit=limit, offset=offset, search_query=search_query
    )

    from ib_tasks.storages.storage_implementation import \
        StagesStorageImplementation
    stage_storage = StagesStorageImplementation()

    from ib_tasks.storages.tasks_storage_implementation import \
        TasksStorageImplementation
    task_storage = TasksStorageImplementation()

    from ib_tasks.presenters.\
        get_stage_searchable_possible_assignees_presenter_implementation \
        import GetStageSearchablePossibleAssigneesPresenterImplementation
    presenter = GetStageSearchablePossibleAssigneesPresenterImplementation()

    from ib_tasks.interactors.\
        get_stage_searchable_possible_assignees_interactor import \
        GetStageSearchablePossibleAssigneesInteractor
    interactor = GetStageSearchablePossibleAssigneesInteractor(
        stage_storage=stage_storage, task_storage=task_storage
    )

    response = \
        interactor.get_stage_searchable_possible_assignees_of_a_task_wrapper(
            search_query_with_pagination_dto=search_query_with_pagination_dto,
            stage_id=stage_id, task_id=task_id, presenter=presenter)

    return response
