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
                               comment_content: str,
                               mention_user_ids: List[str],
                               multimedia_dtos: List[MultiMediaDTO]):
        from ib_discussions.exceptions.custom_exceptions import \
            CommentIdNotFound, UserCannotEditComment
        from ib_discussions.adapters.auth_service import InvalidUserIds
        try:
            response = self._update_comment_response(
                comment_content=comment_content, comment_id=comment_id,
                mention_user_ids=mention_user_ids,
                multimedia_dtos=multimedia_dtos, presenter=presenter,
                user_id=user_id)
        except CommentIdNotFound:
            response = presenter.prepare_response_for_comment_id_not_found()
        except InvalidUserIds as err:
            response = presenter.response_for_invalid_user_ids(err)
        except UserCannotEditComment:
            response = presenter.response_for_user_cannot_edit_comment()
        return response

    def _update_comment_response(self, comment_content, comment_id,
                                 mention_user_ids, multimedia_dtos, presenter,
                                 user_id):
        comment_with_replies_count_and_editable_dto, user_profile_dtos, \
        comment_id_with_mention_user_id_dtos, comment_id_with_multimedia_dtos = \
            self.update_comment(
                user_id=user_id, mention_user_ids=mention_user_ids,
                comment_id=comment_id, multimedia_dtos=multimedia_dtos,
                comment_content=comment_content
            )
        response = presenter.prepare_response_for_comment(
            comment_with_replies_count_and_editable_dto \
                =comment_with_replies_count_and_editable_dto,
            user_profile_dtos=user_profile_dtos,
            comment_id_with_mention_user_id_dtos=comment_id_with_mention_user_id_dtos,
            comment_id_with_multimedia_dtos=comment_id_with_multimedia_dtos
        )
        return response

    def update_comment(
            self, user_id: str, comment_id: str, mention_user_ids: List[str],
            multimedia_dtos: List[MultiMediaDTO], comment_content: str
    ):
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

        from ib_discussions.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        service_adapter.auth_service.validate_user_ids(
            user_ids=mention_user_ids)

        self.comment_storage.update_comment(
            comment_id=comment_id, comment_content=comment_content)
        self.comment_storage.add_mention_users_to_comment(
            comment_id=comment_id, mention_user_ids=mention_user_ids)
        self.comment_storage.add_multimedia_to_comment(
            comment_id=comment_id, multimedia_dtos=multimedia_dtos
        )

        from ib_discussions.interactors.create_comment_interactor import \
            CreateCommentInteractor
        interactor = CreateCommentInteractor(storage=self.comment_storage)
        comment_with_replies_count_and_editable_dto, user_profile_dtos, \
        comment_id_with_mention_user_id_dtos, comment_id_with_multimedia_dtos = \
            interactor.get_comment_details(
                user_id=user_id, comment_id=comment_id
            )
        return comment_with_replies_count_and_editable_dto, user_profile_dtos, \
               comment_id_with_mention_user_id_dtos, comment_id_with_multimedia_dtos
