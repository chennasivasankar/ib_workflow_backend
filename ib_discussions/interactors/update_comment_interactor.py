from typing import List

from ib_discussions.interactors.dtos.dtos import MultiMediaDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    UpdateCommentPresenterInterface
from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface


class UpdateCommentInteractor:

    def __init__(self, comment_storage: CommentStorageInterface):
        self.comment_storage = comment_storage

    def update_comment_wrapper(self, presenter: UpdateCommentPresenterInterface,
                               user_id: str, comment_id: str,
                               mention_user_ids: List[str],
                               multimedia_dtos: List[MultiMediaDTO]):
        from ib_discussions.exceptions.custom_exceptions import \
            CommentIdNotFound
        try:
            response = self.update_comment(
                user_id=user_id, mention_user_ids=mention_user_ids,
                comment_id=comment_id, multimedia_dtos=multimedia_dtos,
            )
        except CommentIdNotFound:
            response = presenter.prepare_response_for_comment_id_not_found()
        return response

    def update_comment(
            self, user_id: str, comment_id: str, mention_user_ids: List[str],
            multimedia_dtos: List[MultiMediaDTO]
    ):
        is_comment_id_not_exists = \
            not self.comment_storage.is_comment_id_exists(comment_id=comment_id)
        if is_comment_id_not_exists:
            from ib_discussions.exceptions.custom_exceptions import \
                CommentIdNotFound
            raise CommentIdNotFound
