import pytest


@pytest.fixture()
def prepare_discussion_with_comment_setup():
    discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
    comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
    from ib_discussions.tests.factories.models import CommentFactory
    CommentFactory.created_at.reset()
    CommentFactory(
        id=comment_id,
        discussion_id=discussion_id,
        user_id="31be920b-7b4c-49e7-8adb-41a0c18da848"
    )
    from ib_discussions.tests.factories.models import DiscussionFactory
    DiscussionFactory(id=discussion_id)


@pytest.fixture()
def prepare_mock_setup(mocker):
    comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
    from ib_discussions.tests.common_fixtures.adapters import \
        prepare_validate_user_ids_mock
    prepare_validate_user_ids_mock(mocker=mocker)

    from ib_discussions.tests.common_fixtures.storages import \
        prepare_create_comment_for_discussion_mock
    create_comment_for_discussion_mock = \
        prepare_create_comment_for_discussion_mock(mocker)
    create_comment_for_discussion_mock.return_value = comment_id


@pytest.fixture()
def prepare_users_setup(mocker):
    user_ids = [
        "31be920b-7b4c-49e7-8adb-41a0c18da848"
    ]
    mention_user_ids = [
        "10be920b-7b4c-49e7-8adb-41a0c18da848",
        "20be920b-7b4c-49e7-8adb-41a0c18da848"
    ]
    from ib_discussions.tests.common_fixtures.adapters import \
        prepare_get_user_profile_dtos_mock
    get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
    from ib_discussions.tests.factories.adapter_dtos import \
        UserProfileDTOFactory
    user_profile_dtos = [
        UserProfileDTOFactory(user_id=user_id)
        for user_id in (user_ids + mention_user_ids)
    ]
    get_user_profile_dtos_mock.return_value = user_profile_dtos
    return mention_user_ids


@pytest.fixture()
def prepare_multimedia_setup(mocker):
    comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
    from ib_discussions.constants.enum import MultiMediaFormatEnum
    multimedia = [
        {
            "format_type": MultiMediaFormatEnum.IMAGE.value,
            "url": "https://picsum.photos/200",
            "thumbnail_url": "https://picsum.photos/200"
        },
        {
            "format_type": MultiMediaFormatEnum.VIDEO.value,
            "url": "https://picsum.photos/200",
            "thumbnail_url": "https://picsum.photos/200"
        }
    ]
    multimedia_ids = [
        "97be920b-7b4c-49e7-8adb-41a0c18da848",
        "92be920b-7b4c-49e7-8adb-41a0c18da848",
    ]
    from ib_discussions.tests.factories.storage_dtos import \
        CommentIdWithMultiMediaDTOFactory
    multimedia_dtos = [
        CommentIdWithMultiMediaDTOFactory(
            comment_id=comment_id,
            multimedia_id=multimedia_ids[0],
            format_type=multimedia[0]["format_type"],
            url=multimedia[0]["url"]
        ),
        CommentIdWithMultiMediaDTOFactory(
            comment_id=comment_id,
            multimedia_id=multimedia_ids[1],
            format_type=multimedia[1]["format_type"],
            url=multimedia[1]["url"]
        )
    ]
    from ib_discussions.tests.common_fixtures.storages import \
        prepare_get_multimedia_dtos_mock
    multimedia_mock = prepare_get_multimedia_dtos_mock(mocker)
    multimedia_mock.return_value = multimedia_dtos
    return multimedia
