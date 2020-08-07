from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = user_object.user_id

    path_params = kwargs["path_params"]
    comment_id = path_params["comment_id"]

    from ib_discussions.storages.comment_storage_implementaion import \
        CommentStorageImplementation
    comment_storage = CommentStorageImplementation()

    from ib_discussions.presenters.get_replies_for_comment_presenter_implementation import \
        GetRepliesForCommentPresenterImplementation
    presenter = GetRepliesForCommentPresenterImplementation()

    from ib_discussions.interactors.get_replies_for_comment_interactor import \
        GetRepliesForCommentInteractor
    interactor = GetRepliesForCommentInteractor(storage=comment_storage)

    response = interactor.get_replies_for_comment_wrapper(
        presenter=presenter, user_id=user_id, comment_id=comment_id,
    )
    return response
