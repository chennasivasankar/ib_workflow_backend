from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = user_object.user_id

    path_params = kwargs["path_params"]
    discussion_id = path_params["discussion_id"]

    from ib_discussions.storages.comment_storage_implementaion import \
        CommentStorageImplementation
    comment_storage = CommentStorageImplementation()

    from ib_discussions.presenters.get_comments_for_discussion_presenter_implementation import \
        GetCommentsForDiscussionPresenterImplementation
    presenter = GetCommentsForDiscussionPresenterImplementation()

    from ib_discussions.interactors.get_comments_for_discussion_interactor import \
        GetCommentsForDiscussionInteractor
    interactor = GetCommentsForDiscussionInteractor(storage=comment_storage)

    response = interactor.get_comments_for_discussion_wrapper(
        presenter=presenter, user_id=user_id, discussion_id=discussion_id
    )
    return response
