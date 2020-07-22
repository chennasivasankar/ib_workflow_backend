from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    request_data = kwargs["request_data"]

    from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO
    discussion_dto = DiscussionDTO(
        user_id=user_object.user_id,
        entity_type=request_data["entity_type"],
        entity_id=request_data["entity_id"],
        title=request_data["title"],
        description=request_data["description"],
    )

    from ib_discussions.presenters.create_discussion_presenter_implementation import \
        CreateDiscussionPresenterImplementation
    presenter = CreateDiscussionPresenterImplementation()

    from ib_discussions.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()

    from ib_discussions.interactors.discussion_interactor import \
        DiscussionInteractor
    interactor = DiscussionInteractor(storage=storage)

    response = interactor.create_discussion_wrapper(
        discussion_dto=discussion_dto, presenter=presenter
    )
    return response
