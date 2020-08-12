from dataclasses import dataclass
from typing import List

from ib_tasks.adapters.dtos import UserDetailsDTO
from ib_tasks.exceptions.fields_custom_exceptions import \
    LimitShouldBeGreaterThanZeroException, \
    OffsetShouldBeGreaterThanZeroException
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces. \
    get_stage_searchable_possible_assignees_presenter_interface \
    import GetStageSearchablePossibleAssigneesPresenterInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface


@dataclass
class SearchQueryWithPaginationDTO:
    limit: int
    offset: int
    search_query: str


class GetStageSearchablePossibleAssigneesInteractor(
        ValidationMixin, GetTaskIdForTaskDisplayIdMixin):
    def __init__(self, stage_storage: StageStorageInterface):
        self.stage_storage = stage_storage

    def get_stage_searchable_possible_assignees_of_a_task_wrapper(
            self, stage_id: int,
            search_query_with_pagination_dto:
            SearchQueryWithPaginationDTO,
            presenter: GetStageSearchablePossibleAssigneesPresenterInterface):
        try:
            user_details_dtos = \
                self.get_stage_searchable_possible_assignees_of_a_task(
                    search_query_with_pagination_dto=
                    search_query_with_pagination_dto,
                    stage_id=stage_id)

        except InvalidStageId as err:
            return presenter.raise_invalid_stage_id_exception(err)
        except LimitShouldBeGreaterThanZeroException as err:
            return presenter.raise_invalid_limit_exception(err)
        except OffsetShouldBeGreaterThanZeroException as err:
            return presenter.raise_invalid_offset_exception(err)

        return presenter.get_stage_assignee_details_response(
            user_details_dtos=user_details_dtos)

    def get_stage_searchable_possible_assignees_of_a_task(
            self, stage_id: int,
            search_query_with_pagination_dto: SearchQueryWithPaginationDTO
            ) -> List[UserDetailsDTO]:

        self.validate_stage_id(stage_id=stage_id)
        self._validations_of_limit_and_offset(
            limit=search_query_with_pagination_dto.limit,
            offset=search_query_with_pagination_dto.offset)

        stage_permitted_user_roles = \
            self.stage_storage.get_stage_permitted_user_roles(
                stage_id=stage_id)

        from ib_tasks.adapters.auth_service import AuthService
        auth_service_adapter = AuthService()

        permitted_user_details_dtos = auth_service_adapter.\
            get_user_details_for_the_given_role_ids_based_on_query(
                role_ids=stage_permitted_user_roles,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto)

        return permitted_user_details_dtos

    @staticmethod
    def _validations_of_limit_and_offset(offset: int, limit: int):
        if limit < 1:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                LimitShouldBeGreaterThanZeroException
            raise LimitShouldBeGreaterThanZeroException

        if offset < -1:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                OffsetShouldBeGreaterThanOrEqualToMinusOneException
            raise OffsetShouldBeGreaterThanOrEqualToMinusOneException
