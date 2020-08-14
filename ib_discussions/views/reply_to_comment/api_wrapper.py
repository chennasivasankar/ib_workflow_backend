from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = user_object.user_id

    path_params = kwargs["path_params"]
    comment_id = path_params["comment_id"]

    request_data = kwargs["request_data"]
    comment_content = request_data["comment_content"]
    mention_user_ids = request_data["mention_user_ids"]
    multimedia_list = request_data["multimedia"]

    from ib_discussions.tests.factories.interactor_dtos import \
        MultimediaDTOFactory
    multimedia_dtos = [
        MultimediaDTOFactory(
            format_type=multimedia_dict["format_type"],
            url=multimedia_dict["url"],
            thumbnail_url=multimedia_dict["thumbnail_url"]
        )
        for multimedia_dict in multimedia_list
    ]

    from ib_discussions.interactors.dtos.dtos import \
        CreateCompleteReplyToCommentDTO
    create_complete_reply_to_comment_dto = CreateCompleteReplyToCommentDTO(
        comment_id=comment_id,
        user_id=user_id,
        comment_content=comment_content,
        mention_user_ids=mention_user_ids,
        multimedia_dtos=multimedia_dtos
    )

    from ib_discussions.storages.comment_storage_implementaion import \
        CommentStorageImplementation
    comment_storage = CommentStorageImplementation()

    from ib_discussions.presenters.create_reply_presenter_implementation import \
        CreateReplyPresenterImplementation
    presenter = CreateReplyPresenterImplementation()

    from ib_discussions.interactors.create_reply_to_comment_interactor import \
        CreateReplyToCommentInteractor
    interactor = CreateReplyToCommentInteractor(storage=comment_storage)

    response = interactor.reply_to_comment_wrapper(
        presenter=presenter,
        create_complete_reply_to_comment_dto=create_complete_reply_to_comment_dto
    )
    return response
