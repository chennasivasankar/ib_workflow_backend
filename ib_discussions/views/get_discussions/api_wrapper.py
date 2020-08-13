from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    query_params = kwargs["query_params"]
    user_object = kwargs["user"]
    user_id = str(user_object.user_id)

    entity_id_and_entity_type_dto = _prepare_entity_id_and_entity_type_dto(
        request_data)

    offset_and_limit_dto = _prepare_offset_and_limit_dto(query_params)

    filter_by_dto = _prepare_filter_by_dto(kwargs, request_data)

    sort_by_dto = _prepare_sort_by_dto(request_data)

    from ib_discussions.presenters.get_discussion_presenter_implementation import \
        GetDiscussionPresenterImplementation
    presenter = GetDiscussionPresenterImplementation()

    from ib_discussions.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()

    from ib_discussions.interactors.get_discussions_interactor import \
        GetDiscussionInteractor
    interactor = GetDiscussionInteractor(storage=storage)

    response = interactor.get_discussions_wrapper(
        entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
        offset_and_limit_dto=offset_and_limit_dto,
        filter_by_dto=filter_by_dto, sort_by_dto=sort_by_dto,
        presenter=presenter, user_id=user_id
    )
    return response


def _prepare_sort_by_dto(request_data):
    from ib_discussions.constants.enum import SortByEnum
    from ib_discussions.constants.enum import OrderByEnum
    from ib_discussions.interactors.dtos.dtos import SortByDTO

    sort_by = request_data["sort_by"]
    order = OrderByEnum.ASC.value
    if sort_by == SortByEnum.LATEST.value:
        order = OrderByEnum.ASC.value
    sort_by_dto = SortByDTO(
        sort_by=sort_by,
        order=order
    )
    return sort_by_dto


def _prepare_filter_by_dto(kwargs, request_data):
    from ib_discussions.constants.enum import FilterByEnum
    from ib_discussions.interactors.dtos.dtos import FilterByDTO

    filter_by = request_data["filter_by"]
    value = None
    if filter_by == FilterByEnum.ALL.value:
        value = FilterByEnum.ALL.value
    if filter_by == FilterByEnum.POSTED_BY_ME.value:
        user = kwargs["user"]
        value = user.user_id
    if filter_by == FilterByEnum.CLARIFIED.value:
        value = True
    if filter_by == FilterByEnum.NOT_CLARIFIED.value:
        value = False
    filter_by_dto = FilterByDTO(
        filter_by=filter_by,
        value=value
    )
    return filter_by_dto


def _prepare_offset_and_limit_dto(query_params):
    from ib_discussions.interactors.dtos.dtos import \
        OffsetAndLimitDTO

    offset_and_limit_dto = OffsetAndLimitDTO(
        offset=query_params["offset"],
        limit=query_params["limit"]
    )
    return offset_and_limit_dto


def _prepare_entity_id_and_entity_type_dto(request_data):
    from ib_discussions.interactors.dtos.dtos import \
        EntityIdAndEntityTypeDTO

    entity_id_and_entity_type_dto = EntityIdAndEntityTypeDTO(
        entity_id=request_data["entity_id"],
        entity_type=request_data["entity_type"]
    )
    return entity_id_and_entity_type_dto
