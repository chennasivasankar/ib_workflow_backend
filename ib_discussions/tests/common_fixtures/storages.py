def prepare_create_comment_for_discussion_mock(mocker):
    mock = mocker.patch(
        "ib_discussions.storages.comment_storage_implementaion.CommentStorageImplementation.create_comment_for_discussion"
    )
    return mock


def prepare_create_reply_to_comment_mock(mocker):
    mock = mocker.patch(
        "ib_discussions.storages.comment_storage_implementaion.CommentStorageImplementation.create_reply_to_comment"
    )
    return mock


def prepare_get_multi_media_dtos_mock(mocker):
    mock = mocker.patch(
        "ib_discussions.storages.comment_storage_implementaion.CommentStorageImplementation.get_multi_media_dtos"
    )
    return mock