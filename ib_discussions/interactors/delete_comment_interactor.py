from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    DeleteCommentPresenterInterface
from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface


class DeleteCommentInteractor:

    def __init__(self, comment_storage: CommentStorageInterface):
        self.comment_storage = comment_storage

    def delete_comment_wrapper(self, comment_id: str, user_id: str,
                               presenter: DeleteCommentPresenterInterface):
        from ib_discussions.exceptions.custom_exceptions import \
            CommentIdNotFound, UserCannotEditComment

        try:
            self.delete_comment(comment_id=comment_id,
                                user_id=user_id)
            response = presenter.prepare_response_for_delete_comment()
        except CommentIdNotFound:
            response = presenter.prepare_response_for_comment_id_not_found()
        except UserCannotEditComment:
            response = presenter.response_for_user_cannot_edit_comment()
        return response

    def delete_comment(self, comment_id: str, user_id: str):
        from ib_discussions.exceptions.custom_exceptions import \
            CommentIdNotFound, UserCannotEditComment

        is_comment_id_not_exists = \
            not self.comment_storage.is_comment_id_exists(comment_id=comment_id)
        if is_comment_id_not_exists:
            raise CommentIdNotFound

        comment_creator_id = self.comment_storage.get_comment_creator_id(
            comment_id=comment_id
        )
        is_not_comment_creator = not comment_creator_id == user_id
        if is_not_comment_creator:
            raise UserCannotEditComment

        self.comment_storage.delete_comment(comment_id=comment_id)
        return
