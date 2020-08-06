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
        presenter=presenter, user_id=user_id, comment_id=comment_id,
        comment_content=comment_content
    )
    return response
