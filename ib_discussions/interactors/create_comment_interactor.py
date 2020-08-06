from typing import Optional, List

from ib_discussions.exceptions.custom_exceptions import DiscussionIdNotFound
from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentIdWithEditableStatusDTO, CommentWithRepliesCountAndEditableDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    CreateCommentPresenterInterface
from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from ib_discussions.interactors.storage_interfaces.dtos import CommentDTO, \
    CommentIdWithRepliesCountDTO


class CreateCommentInteractor:

    def __init__(self, storage: CommentStorageInterface):
        self.storage = storage

    def create_comment_for_discussion_wrapper(
            self, presenter: CreateCommentPresenterInterface,
            user_id: str, discussion_id: str, comment_content: str,
    ):
        try:
            comment_with_replies_count_and_editable_dto, user_profile_dto = \
                self.create_comment_for_discussion(
                    user_id=user_id, discussion_id=discussion_id,
                    comment_content=comment_content,
                )
            response = presenter.prepare_response_for_comment(
                comment_with_replies_count_and_editable_dto \
                    =comment_with_replies_count_and_editable_dto,
                user_profile_dto=user_profile_dto
            )
        except DiscussionIdNotFound:
            response = presenter.response_for_discussion_id_not_found()
        return response

    def create_comment_for_discussion(
            self, user_id: str, discussion_id: str,
            comment_content: Optional[str],
    ):
        is_discussion_id_not_exists = not self.storage. \
            is_discussion_id_exists(discussion_id=discussion_id)

        if is_discussion_id_not_exists:
            raise DiscussionIdNotFound

        comment_id = self.storage.create_comment_for_discussion(
            user_id=user_id, discussion_id=discussion_id,
            comment_content=comment_content,
        )

        comment_with_replies_count_and_editable_dto, user_profile_dto = \
            self.get_comment_details(comment_id=comment_id,
                                     user_id=user_id)

        return comment_with_replies_count_and_editable_dto, user_profile_dto

    def get_comment_details(self, comment_id: str, user_id: str):
        comment_dto = self.storage.get_comment_details_dto(comment_id)

        comment_with_replies_count_and_editable_dtos, user_profile_dtos = \
            self.get_comments_for_discussion([comment_dto], user_id)

        return comment_with_replies_count_and_editable_dtos[0], \
            user_profile_dtos[0]

    def get_comments_for_discussion(self, comment_dtos: List[CommentDTO],
                                    user_id: str):
        comment_ids = [comment.comment_id for comment in comment_dtos]

        user_ids = list(set(comment.user_id for comment in comment_dtos))

        user_profile_dtos = self._get_user_profile_dtos(user_ids=user_ids)

        comment_editable_status_dtos = \
            self._prepare_comment_editable_status_dtos(
                comment_dtos=comment_dtos, user_id=user_id)

        comment_id_with_replies_count_dtos = \
            self.storage.get_replies_count_for_comments(
                comment_ids=comment_ids
            )
        comment_with_replies_count_and_editable_dtos = \
            self._prepare_comment_with_replies_count_and_editable_dtos(
                comment_dtos=comment_dtos,
                comment_id_with_replies_count_dtos \
                    =comment_id_with_replies_count_dtos,
                comment_editable_status_dtos=comment_editable_status_dtos
            )

        return comment_with_replies_count_and_editable_dtos, \
            user_profile_dtos

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
            CreateCommentInteractor._prepare_comment_editable_status_dto(
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
        if user_id == comment_dto.user_id:
            is_editable = True
        comment_editable_status_dto = CommentIdWithEditableStatusDTO(
            comment_id=comment_dto.comment_id,
            is_editable=is_editable
        )
        return comment_editable_status_dto

    def _prepare_comment_with_replies_count_and_editable_dtos(
            self, comment_dtos: List[CommentDTO],
            comment_id_with_replies_count_dtos: List[
                CommentIdWithRepliesCountDTO],
            comment_editable_status_dtos: List[CommentIdWithEditableStatusDTO]
    ):
        comment_id_wise_comment_replies_count_dto_dict = \
            self._prepare_comment_id_wise_comment_replies_count_dto_dict(
                comment_id_with_replies_count_dtos= \
                    comment_id_with_replies_count_dtos
            )

        comment_id_wise_editable_status_dto_dict = \
            self._prepare_comment_id_wise_editable_status_dto_dict(
                comment_editable_status_dtos=comment_editable_status_dtos
            )

        comment_with_replies_count_dtos = [
            CommentWithRepliesCountAndEditableDTO(
                comment_id=comment_dto.comment_id,
                comment_content=comment_dto.comment_content,
                user_id=comment_dto.user_id,
                created_at=comment_dto.created_at,
                replies_count=comment_id_wise_comment_replies_count_dto_dict[
                    comment_dto.comment_id
                ].replies_count,
                is_editable=comment_id_wise_editable_status_dto_dict[
                    comment_dto.comment_id
                ].is_editable
            )
            for comment_dto in comment_dtos
        ]
        return comment_with_replies_count_dtos

    @staticmethod
    def _prepare_comment_id_wise_comment_replies_count_dto_dict(
            comment_id_with_replies_count_dtos: List[
                CommentIdWithRepliesCountDTO]):
        comment_id_wise_comment_replies_count_dto_dict = {
            comment_replies_count_dto.comment_id: comment_replies_count_dto
            for comment_replies_count_dto in comment_id_with_replies_count_dtos
        }
        return comment_id_wise_comment_replies_count_dto_dict

    @staticmethod
    def _prepare_comment_id_wise_editable_status_dto_dict(
            comment_editable_status_dtos: List[CommentIdWithEditableStatusDTO]):
        comment_id_wise_editable_status_dto_dict = {
            comment_editable_status_dto.comment_id: comment_editable_status_dto
            for comment_editable_status_dto in comment_editable_status_dtos
        }
        return comment_id_wise_editable_status_dto_dict
