from typing import Optional, List

from ib_discussions.exceptions.custom_exceptions import DiscussionIdNotFound
from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentIdWithEditableStatusDTO, CommentWithRepliesCountDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    CreateCommentPresenterInterface
from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from ib_discussions.interactors.storage_interfaces.dtos import CommentDTO, \
    CommentIdWithRepliesCountDTO


class CommentInteractor:

    def __init__(self, storage: CommentStorageInterface):
        self.storage = storage

    def create_comment_for_discussion_wrapper(
            self, presenter: CreateCommentPresenterInterface,
            user_id: str, discussion_id: str, comment_content: str,
    ):
        try:
            # comment_with_replies_count_and_reaction_details_dto, \
            # author_details_with_verified_moderator_status_dto, \
            # user_comment_reaction_dto, comment_editable_status_dto = \
            self.create_comment_for_discussion(
                user_id=user_id, discussion_id=discussion_id,
                comment_content=comment_content,
            )

            # response = presenter.get_comment_details_response(
            #     comment_with_replies_count_and_reaction_details_dto,
            #     author_details_with_verified_moderator_status_dto,
            #     user_comment_reaction_dto, comment_editable_status_dto)
            # return response
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

        comment_with_replies_count_and_reaction_details_dto, \
        author_details_with_verified_moderator_status_dto, \
        user_comment_reaction_dto, comment_editable_status_dto = \
            self.get_comment_details(comment_id, user_id)
        #
        # return comment_with_replies_count_and_reaction_details_dto, \
        #        author_details_with_verified_moderator_status_dto, \
        #        user_comment_reaction_dto, comment_editable_status_dto

    def get_comment_details(self, comment_id: str, user_id: str):
        comment_dto = self.storage.get_comment_details_dto(comment_id)

        comment_with_replies_count_and_reaction_details_dtos, \
        overall_author_details_dtos, \
        user_comment_reaction_dtos, comment_editable_status_dtos = \
            self._get_comments_for_discussion([comment_dto], user_id)

        comment_with_replies_count_and_reaction_details_dto, \
        author_details_with_verified_moderator_status_dto, \
        user_comment_reaction_dto, comment_editable_status_dto \
            = comment_with_replies_count_and_reaction_details_dtos[0], \
              overall_author_details_dtos[0], \
              user_comment_reaction_dtos[0], comment_editable_status_dtos[0]

        return comment_with_replies_count_and_reaction_details_dto, \
               author_details_with_verified_moderator_status_dto, \
               user_comment_reaction_dto, comment_editable_status_dto

    def _get_comments_for_discussion(self, comment_dtos: List[CommentDTO],
                                     user_id):
        comment_ids = [comment.comment_id for comment in comment_dtos]

        user_ids = list(set(comment.user_id for comment in comment_dtos))

        user_profile_dtos = self._get_user_profile_dtos(user_ids=user_ids)

        comment_editable_status_dtos = \
            self._prepare_comment_editable_status_dtos(
                comment_dtos=comment_dtos, user_id=user_id)

        comment_id_with_replies_count_dtos = self.storage.get_replies_count_for_comments(
            comment_ids=comment_ids
        )
        comment_with_replies_count_dtos \
            = self._prepare_comment_with_replies_count_and_editable_dtos(
            comment_dtos=comment_dtos,
            comment_id_with_replies_count_dtos \
                =comment_id_with_replies_count_dtos,
            comment_editable_status_dtos=comment_editable_status_dtos
        )

        return comment_with_replies_count_and_reaction_details_dtos, \
               overall_author_details_dtos, \
               user_comment_reaction_dtos, comment_editable_status_dtos

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
            CommentInteractor._prepare_comment_editable_status_dto(
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
        comment_id_wise_comment_replies_count_dto_dict \
            = self._prepare_comment_id_wise_comment_replies_count_dto_dict(
            comment_id_with_replies_count_dtos=comment_id_with_replies_count_dtos)

        comment_id_wise_editable_status_dto_dict \
            = self._prepare_comment_id_wise_editable_status_dto_dict(
            comment_editable_status_dtos=comment_editable_status_dtos
        )

        comment_with_replies_count_dtos = [
            CommentWithRepliesCountDTO(
                comment_id=comment_dto.comment_id,
                comment_content=comment_dto.comment_content,
                user_id=comment_dto.user_id,
                created_at=comment_dto.user_id,
                replies_count=comment_id_wise_comment_replies_count_dto_dict[
                    comment_dto.comment_id
                ].replies_count
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

    def _prepare_comment_id_wise_editable_status_dto_dict(
            self,
            comment_editable_status_dtos: List[CommentIdWithEditableStatusDTO]):
        comment_id_wise_editable_status_dto_dict = {

        }
