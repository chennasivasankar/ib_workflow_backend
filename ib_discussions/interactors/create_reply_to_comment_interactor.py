from typing import List

from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentIdWithEditableStatusDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    CreateReplyPresenterInterface
from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from ib_discussions.interactors.storage_interfaces.dtos import CommentDTO


class CreateReplyToCommentInteractor:

    def __init__(self, storage: CommentStorageInterface):
        self.storage = storage

    def reply_to_comment_wrapper(
            self, presenter: CreateReplyPresenterInterface, user_id: str,
            comment_id: str, comment_content: str,
    ):
        from ib_discussions.exceptions.custom_exceptions import \
            CommentIdNotFound
        try:
            response = self._reply_to_comment_response(
                comment_content=comment_content, comment_id=comment_id,
                presenter=presenter, user_id=user_id)
        except CommentIdNotFound:
            response = presenter.response_for_comment_id_not_found()
        return response

    def _reply_to_comment_response(self, comment_content, comment_id, presenter,
                                   user_id):
        comment_dto, comment_with_editable_status_dto, user_profile_dto = \
            self.reply_to_comment(
                user_id=user_id, comment_id=comment_id,
                comment_content=comment_content,
            )
        response = presenter.prepare_response_for_reply(
            comment_dto=comment_dto, user_profile_dto=user_profile_dto,
            comment_with_editable_status_dto \
                =comment_with_editable_status_dto
        )
        return response

    def reply_to_comment(
            self, user_id: str, comment_id: str, comment_content: str
    ):
        is_comment_id_not_exists = not self.storage.is_comment_id_exists(
            comment_id=comment_id
        )

        from ib_discussions.exceptions.custom_exceptions import \
            CommentIdNotFound
        if is_comment_id_not_exists:
            raise CommentIdNotFound

        parent_comment_id = self.storage.get_parent_comment_id(
            comment_id=comment_id)
        if parent_comment_id is None:
            parent_comment_id = comment_id
        discussion_id = self.storage.get_discussion_id(
            comment_id=comment_id)

        reply_comment_id = self.storage.create_reply_to_comment(
            parent_comment_id=parent_comment_id,
            comment_content=comment_content,
            user_id=user_id, discussion_id=discussion_id
        )
        comment_dto, comment_with_editable_status_dto, user_profile_dto = \
            self.get_reply_details(reply_comment_id, user_id)
        return comment_dto, comment_with_editable_status_dto, user_profile_dto

    def get_reply_details(self, reply_comment_id: str, user_id: str):
        comment_dto = self.storage.get_comment_details_dto(
            comment_id=reply_comment_id)

        comment_with_editable_status_dtos, user_profile_dtos = \
            self.get_replies_for_comment([comment_dto], user_id)

        return comment_dto, comment_with_editable_status_dtos[0], \
               user_profile_dtos[0]

    def get_replies_for_comment(
            self, reply_dtos: List[CommentDTO], user_id: str):
        user_ids = list(set(comment_dto.user_id for comment_dto in reply_dtos))

        user_profile_dtos = self._get_user_profile_dtos(user_ids=user_ids)

        comment_with_editable_status_dtos = \
            self._prepare_comment_editable_status_dtos(
                comment_dtos=reply_dtos, user_id=user_id)

        return comment_with_editable_status_dtos, user_profile_dtos

    @staticmethod
    def _get_user_profile_dtos(user_ids: List[str]):
        from ib_discussions.adapters.service_adapter import get_service_adapter
        adapter = get_service_adapter()
        user_profile_dtos = adapter.auth_service.get_user_profile_dtos(
            user_ids=user_ids
        )
        return user_profile_dtos

    @staticmethod
    def _prepare_comment_editable_status_dtos(comment_dtos: List[CommentDTO],
                                              user_id):
        comment_editable_status_dtos = [
            CreateReplyToCommentInteractor._prepare_comment_editable_status_dto(
                comment_dto=comment_dto, user_id=user_id
            )
            for comment_dto in comment_dtos
        ]
        return comment_editable_status_dtos

    @staticmethod
    def _prepare_comment_editable_status_dto(
            comment_dto: CommentDTO, user_id: str
    ) -> CommentIdWithEditableStatusDTO:
        is_editable = False
        if str(user_id) == str(comment_dto.user_id):
            is_editable = True
        comment_editable_status_dto = CommentIdWithEditableStatusDTO(
            comment_id=comment_dto.comment_id,
            is_editable=is_editable
        )
        return comment_editable_status_dto
