from ib_discussions.exceptions.custom_exceptions import DiscussionIdNotFound
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetCommentsForDiscussionPresenterInterface
from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface


class GetCommentsForDiscussionInteractor:

    def __init__(self, storage: CommentStorageInterface):
        self.storage = storage

    def get_comments_for_discussion_wrapper(
            self, presenter: GetCommentsForDiscussionPresenterInterface,
            discussion_id: str, user_id: str,
    ):
        try:
            response = self._get_comments_for_discussion_response(
                discussion_id=discussion_id, user_id=user_id,
                presenter=presenter
            )
        except DiscussionIdNotFound:
            response = presenter.response_for_discussion_id_not_found()
        return response

    def _get_comments_for_discussion_response(
            self, discussion_id: str, user_id: str,
            presenter: GetCommentsForDiscussionPresenterInterface
    ):
        comment_with_replies_count_and_editable_dtos, user_profile_dtos = \
            self.get_comments_for_discussion(
                discussion_id=discussion_id, user_id=user_id,
            )
        return presenter.return_response_for_comments_with_users_dtos(
            comment_with_replies_count_and_editable_dtos \
                =comment_with_replies_count_and_editable_dtos,
            user_profile_dtos=user_profile_dtos
        )

    def get_comments_for_discussion(
            self, discussion_id: str, user_id: str,
    ):
        is_discussion_id_not_exists = not self.storage. \
            is_discussion_id_exists(discussion_id=discussion_id)

        if is_discussion_id_not_exists:
            raise DiscussionIdNotFound

        comment_dtos = self.storage.get_comments_for_discussion(
            discussion_id=discussion_id
        )

        from ib_discussions.interactors.create_comment_interactor import \
            CommentInteractor
        interactor = CommentInteractor(storage=self.storage)

        comment_with_replies_count_and_editable_dtos, user_profile_dtos = \
            interactor.get_comments_for_discussion(comment_dtos=comment_dtos,
                                                   user_id=user_id)
        return comment_with_replies_count_and_editable_dtos, user_profile_dtos
