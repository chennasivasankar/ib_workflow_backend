from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    print("****************")

    user_object = kwargs["user"]
    user_id = str(user_object.user_id)

    path_params = kwargs["path_params"]
    comment_id = path_params["comment_id"]

    request_data = kwargs["request_data"]
    comment_content = request_data["comment_content"]
    mention_user_ids = request_data["mention_user_ids"]
    multimedia_list = request_data["multimedia"]

    from ib_discussions.tests.factories.interactor_dtos import \
        MultiMediaDTOFactory
    multimedia_dtos = [
        MultiMediaDTOFactory(
            format_type=multimedia_dict["format_type"],
            url=multimedia_dict["url"],
            thumbnail_url=multimedia_dict["thumbnail_url"]
        )
        for multimedia_dict in multimedia_list
    ]

    from ib_discussions.storages.comment_storage_implementaion import \
        CommentStorageImplementation
    comment_storage = CommentStorageImplementation()

    from ib_discussions.presenters.update_comment_presenter_implementaion import \
        UpdateCommentPresenterImplementation
    presenter = UpdateCommentPresenterImplementation()

    from ib_discussions.interactors.update_comment_interactor import \
        UpdateCommentInteractor
    interactor = UpdateCommentInteractor(comment_storage=comment_storage)

    response = interactor.update_comment_wrapper(
        presenter=presenter, user_id=user_id, comment_id=comment_id,
        comment_content=comment_content, mention_user_ids=mention_user_ids,
        multimedia_dtos=multimedia_dtos
    )
    return response
