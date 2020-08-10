from typing import List

from ib_discussions.exceptions.custom_exceptions import InvalidOffset, \
    InvalidLimit, InvalidUserId, DiscussionSetNotFound
from ib_discussions.interactors.dtos.dtos import OffsetAndLimitDTO, \
    FilterByDTO, SortByDTO, EntityIdAndEntityTypeDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetDiscussionsPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import DiscussionDTO
from ib_discussions.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetDiscussionInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_discussions_wrapper(
            self, entity_id_and_entity_type_dto: EntityIdAndEntityTypeDTO,
            offset_and_limit_dto: OffsetAndLimitDTO, user_id: str,
            filter_by_dto: FilterByDTO, sort_by_dto: SortByDTO,
            presenter: GetDiscussionsPresenterInterface
    ):
        from ib_discussions.exceptions.custom_exceptions import \
            EntityIdNotFound, InvalidEntityTypeForEntityId
        try:
            response = self._get_discussions_response(
                entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
                offset_and_limit_dto=offset_and_limit_dto, presenter=presenter,
                filter_by_dto=filter_by_dto, sort_by_dto=sort_by_dto,
                user_id=user_id
            )
        except InvalidOffset:
            response = presenter.raise_exception_for_invalid_offset()
        except InvalidLimit:
            response = presenter.raise_exception_for_invalid_limit()
        except EntityIdNotFound:
            response = presenter.raise_exception_for_entity_id_not_found()
        except InvalidEntityTypeForEntityId:
            response = presenter. \
                raise_exception_for_invalid_entity_type_for_entity_id()
        except InvalidUserId:
            response = presenter.raise_exception_for_invalid_user_id()
        return response

    def _get_discussions_response(
            self, entity_id_and_entity_type_dto: EntityIdAndEntityTypeDTO,
            offset_and_limit_dto: OffsetAndLimitDTO, user_id: str,
            filter_by_dto: FilterByDTO, sort_by_dto: SortByDTO,
            presenter: GetDiscussionsPresenterInterface
    ):
        discussions_with_users_and_discussion_count_dto, \
        discussion_id_with_editable_status_dtos, discussion_id_with_comments_count_dtos \
            = self.get_discussions_details_dto(
            entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
            offset_and_limit_dto=offset_and_limit_dto, user_id=user_id,
            filter_by_dto=filter_by_dto, sort_by_dto=sort_by_dto
        )
        return presenter.prepare_response_for_discussions_details_dto(
            discussions_with_users_and_discussion_count_dto=discussions_with_users_and_discussion_count_dto,
            discussion_id_with_editable_status_dtos \
                =discussion_id_with_editable_status_dtos,
            discussion_id_with_comments_count_dtos=discussion_id_with_comments_count_dtos
        )

    def get_discussions_details_dto(
            self, entity_id_and_entity_type_dto: EntityIdAndEntityTypeDTO,
            offset_and_limit_dto: OffsetAndLimitDTO, user_id: str,
            filter_by_dto: FilterByDTO, sort_by_dto: SortByDTO,
    ):
        self._validate_limit_offset_entity_id_and_entity_type(
            offset_and_limit_dto)
        discussion_set_id = self._get_discussion_set_id(
            entity_id=entity_id_and_entity_type_dto.entity_id,
            entity_type=entity_id_and_entity_type_dto.entity_type
        )
        discussion_dtos = self.storage.get_discussion_dtos(
            discussion_set_id=discussion_set_id,
            offset_and_limit_dto=offset_and_limit_dto,
            filter_by_dto=filter_by_dto, sort_by_dto=sort_by_dto
        )
        total_discussions_count = self.storage.get_total_discussion_count(
            discussion_set_id=discussion_set_id, filter_by_dto=filter_by_dto
        )
        user_profile_dtos = self._get_user_profile_dtos(
            discussion_dtos=discussion_dtos
        )
        discussion_id_with_comments_count_dtos = \
            self.storage.get_comments_count_for_discussions(
                discussion_set_id=discussion_set_id
            )
        discussion_id_with_editable_status_dtos = \
            self._prepare_discussion_id_with_editable_status_dtos(
                discussion_dtos=discussion_dtos, user_id=user_id
            )
        from ib_discussions.interactors.presenter_interfaces.dtos import \
            DiscussionsWithUsersAndDiscussionCountDTO
        discussions_with_users_and_discussion_count_dto = DiscussionsWithUsersAndDiscussionCountDTO(
            discussion_dtos=discussion_dtos,
            user_profile_dtos=user_profile_dtos,
            total_count=total_discussions_count
        )
        return discussions_with_users_and_discussion_count_dto, discussion_id_with_editable_status_dtos, \
               discussion_id_with_comments_count_dtos

    def _validate_limit_offset_entity_id_and_entity_type(
            self, offset_and_limit_dto
    ):
        self._validate_offset(offset_and_limit_dto.offset)
        self._validate_limit(offset_and_limit_dto.limit)

    @staticmethod
    def _validate_offset(offset):
        is_invalid_offset = offset < 0
        if is_invalid_offset:
            raise InvalidOffset

    @staticmethod
    def _validate_limit(limit):
        is_invalid_limit = limit < 0
        if is_invalid_limit:
            raise InvalidLimit

    @staticmethod
    def _get_user_profile_dtos(
            discussion_dtos: List[DiscussionDTO]
    ):
        user_ids = [
            complete_discussion_dto.user_id
            for complete_discussion_dto in discussion_dtos
        ]
        from ib_discussions.adapters.service_adapter import get_service_adapter
        auth_service = get_service_adapter().auth_service
        user_profile_dtos = auth_service.get_user_profile_dtos(
            user_ids=user_ids
        )
        return user_profile_dtos

    def _get_discussion_set_id(self, entity_id, entity_type):
        try:
            discussion_set_id = self.storage.get_discussion_set_id_if_exists(
                entity_id=entity_id, entity_type=entity_type
            )
        except DiscussionSetNotFound:
            discussion_set_id = self.storage.create_discussion_set_return_id(
                entity_id=entity_id, entity_type=entity_type
            )
        return discussion_set_id

    def _prepare_discussion_id_with_editable_status_dtos(
            self, discussion_dtos: List[DiscussionDTO], user_id: str):
        discussion_id_with_editable_status_dtos = [
            self._prepare_discussion_id_with_editable_status_dto(
                discussion_dto=discussion_dto, user_id=user_id)
            for discussion_dto in discussion_dtos
        ]
        return discussion_id_with_editable_status_dtos

    @staticmethod
    def _prepare_discussion_id_with_editable_status_dto(
            discussion_dto: DiscussionDTO, user_id):
        is_editable = False
        id_discussion_owner_can_edit = discussion_dto.user_id == user_id
        if id_discussion_owner_can_edit:
            is_editable = True
        from ib_iam.interactors.presenter_interfaces.dtos import \
            DiscussionIdWithEditableStatusDTO
        discussion_id_with_editable_status_dto = \
            DiscussionIdWithEditableStatusDTO(
                discussion_id=discussion_dto.discussion_id,
                is_editable=is_editable
            )
        return discussion_id_with_editable_status_dto
