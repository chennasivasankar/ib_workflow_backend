import pytest


@pytest.fixture()
def comment_storage():
    from ib_discussions.storages.comment_storage_implementaion import \
        CommentStorageImplementation
    comment_storage = CommentStorageImplementation()
    return comment_storage


@pytest.fixture()
def create_comments():
    discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
    from ib_discussions.tests.factories.models import DiscussionFactory
    DiscussionFactory(id=discussion_id)

    user_ids = [
        "31be920b-7b4c-49e7-8adb-41a0c18da848",
        "01be920b-7b4c-49e7-8adb-41a0c18da848",
        "77be920b-7b4c-49e7-8adb-41a0c18da848"
    ]
    comments_list = [
        {
            "id": "91be920b-7b4c-49e7-8adb-41a0c18da848",
            "discussion_id": discussion_id,
            "user_id": user_ids[0]
        },
        {
            "id": "11be920b-7b4c-49e7-8adb-41a0c18da848",
            "discussion_id": discussion_id,
            "user_id": user_ids[1]
        },
        {
            "id": "21be920b-7b4c-49e7-8adb-41a0c18da848",
            "discussion_id": discussion_id,
            "user_id": user_ids[2]
        }
    ]
    from ib_discussions.tests.factories.models import CommentFactory
    CommentFactory.created_at.reset()
    comment_objects = [
        CommentFactory(
            id=comment_dict["id"],
            discussion_id=comment_dict["discussion_id"],
            user_id=comment_dict["user_id"]
        )
        for comment_dict in comments_list
    ]

    replies_list = [
        {
            "id": "19be920b-7b4c-49e7-8adb-41a0c18da848",
            "discussion_id": discussion_id,
            "user_id": user_ids[1]
        },
        {
            "id": "12be920b-7b4c-49e7-8adb-41a0c18da848",
            "discussion_id": discussion_id,
            "user_id": user_ids[2]
        },
        {
            "id": "13be920b-7b4c-49e7-8adb-41a0c18da848",
            "discussion_id": discussion_id,
            "user_id": user_ids[0]
        }
    ]
    from ib_discussions.tests.factories.models import ReplyToCommentFactory
    ReplyToCommentFactory.created_at.reset()
    ReplyToCommentFactory(
        id=replies_list[0]["id"],
        parent_comment=comment_objects[0],
        discussion_id=replies_list[0]["discussion_id"],
        user_id=replies_list[0]["user_id"]
    )
    ReplyToCommentFactory(
        id=replies_list[1]["id"],
        parent_comment=comment_objects[0],
        discussion_id=replies_list[1]["discussion_id"],
        user_id=replies_list[1]["user_id"]
    )
    ReplyToCommentFactory(
        id=replies_list[2]["id"],
        parent_comment=comment_objects[1],
        discussion_id=replies_list[2]["discussion_id"],
        user_id=replies_list[2]["user_id"]
    )
