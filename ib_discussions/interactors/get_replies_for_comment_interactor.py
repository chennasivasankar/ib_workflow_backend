from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetRepliesForCommentPresenterInterface
from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface


class GetRepliesForCommentInteractor:

    def __init__(self, storage: CommentStorageInterface):
        self.storage = storage

    def get_replies_for_comment_wrapper(
            self, comment_id: str, user_id: str,
            presenter: GetRepliesForCommentPresenterInterface):
        from ib_discussions.exceptions.custom_exceptions import \
            CommentIdNotFound
        try:
            response = self._get_replies_for_comment(
                comment_id=comment_id, presenter=presenter, user_id=user_id)
        except CommentIdNotFound:
            response = presenter.response_for_comment_id_not_found()
        return response

    def _get_replies_for_comment(
            self, comment_id: str, user_id: str,
            presenter: GetRepliesForCommentPresenterInterface):
        reply_dtos, comment_with_editable_status_dtos, user_profile_dtos, \
        comment_id_with_mention_user_id_dtos, comment_id_with_multimedia_dtos = \
            self.get_replies_for_comment(
                comment_id=comment_id, user_id=user_id,
            )
        return presenter.prepare_response_for_replies_with_users_dtos(
            comment_with_editable_status_dtos=comment_with_editable_status_dtos,
            user_profile_dtos=user_profile_dtos,
            comment_dtos=reply_dtos,
            comment_id_with_mention_user_id_dtos=comment_id_with_mention_user_id_dtos,
            comment_id_with_multimedia_dtos=comment_id_with_multimedia_dtos
        )

    def get_replies_for_comment(
            self, comment_id: str, user_id: str):

        is_comment_id_not_exists = not self.storage.is_comment_id_exists(
            comment_id=comment_id
        )

        from ib_discussions.exceptions.custom_exceptions import \
            CommentIdNotFound
        if is_comment_id_not_exists:
            raise CommentIdNotFound

        reply_dtos = self.storage.get_replies_dtos(
            comment_id=comment_id)

        from ib_discussions.interactors.create_reply_to_comment_interactor import \
            CreateReplyToCommentInteractor
        interactor = CreateReplyToCommentInteractor(storage=self.storage)

        comment_with_editable_status_dtos, user_profile_dtos, \
        comment_id_with_mention_user_id_dtos, comment_id_with_multimedia_dtos = \
            interactor.get_replies_for_comment(
                reply_dtos=reply_dtos, user_id=user_id)

        return reply_dtos, comment_with_editable_status_dtos, user_profile_dtos, \
               comment_id_with_mention_user_id_dtos, comment_id_with_multimedia_dtos
