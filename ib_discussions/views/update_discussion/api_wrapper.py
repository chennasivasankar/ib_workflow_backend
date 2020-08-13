from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = user_object.user_id

    path_params = kwargs["path_params"]
    discussion_id = path_params["discussion_id"]

    request_data = kwargs["request_data"]
    title = request_data["title"]
    description = request_data["description"]

    from ib_discussions.interactors.dtos.dtos import \
        DiscussionIdWithTitleAndDescriptionDTO
    discussion_id_with_title_and_description_dto \
        = DiscussionIdWithTitleAndDescriptionDTO(discussion_id=discussion_id,
                                                 title=title,
                                                 description=description)

    from ib_discussions.presenters.update_discussion_presenter_implementation import \
        UpdateDiscussionPresenterImplementation
    presenter = UpdateDiscussionPresenterImplementation()

    from ib_discussions.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()

    from ib_discussions.interactors.discussion_interactor import \
        DiscussionInteractor
    interactor = DiscussionInteractor(storage=storage)

    response = interactor.update_discussion_wrapper(
        discussion_id_with_title_and_description_dto \
            =discussion_id_with_title_and_description_dto,
        user_id=user_id, presenter=presenter
    )

    return response
