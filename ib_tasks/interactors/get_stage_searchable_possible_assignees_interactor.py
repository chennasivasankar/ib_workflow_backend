from typing import List

from ib_tasks.exceptions.fields_custom_exceptions import \
    LimitShouldBeGreaterThanZeroException, \
    OffsetShouldBeGreaterThanOrEqualToZeroException
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskDisplayId
from ib_tasks.interactors.filter_dtos import SearchQueryWithPaginationDTO
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces. \
    get_stage_searchable_possible_assignees_presenter_interface \
    import GetStageSearchablePossibleAssigneesPresenterInterface
from ib_tasks.interactors.stages_dtos import UserDetailsWithTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class GetStageSearchablePossibleAssigneesInteractor(
        ValidationMixin, GetTaskIdForTaskDisplayIdMixin):
    def __init__(self,
                 stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def get_stage_searchable_possible_assignees_of_a_task_wrapper(
            self, stage_id: int, task_id: str,
            search_query_with_pagination_dto:
            SearchQueryWithPaginationDTO,
            presenter: GetStageSearchablePossibleAssigneesPresenterInterface):
        try:
            user_details_with_team_details_dto = \
                self.get_stage_searchable_possible_assignees_of_a_task(
                    search_query_with_pagination_dto=
                    search_query_with_pagination_dto,
                    stage_id=stage_id, task_id=task_id)
        except InvalidStageId as err:
            return presenter.raise_invalid_stage_id_exception(err)
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_task_display_id_exception(err)
        except LimitShouldBeGreaterThanZeroException:
            return presenter.raise_invalid_limit_exception()
        except OffsetShouldBeGreaterThanOrEqualToZeroException:
            return presenter.raise_invalid_offset_exception()

        return presenter.get_stage_assignee_details_response(
            user_details_with_team_details_dto=
            user_details_with_team_details_dto)

    def get_stage_searchable_possible_assignees_of_a_task(
            self, stage_id: int, task_id: str,
            search_query_with_pagination_dto: SearchQueryWithPaginationDTO
    ) -> UserDetailsWithTeamDetailsDTO:
        self._make_validations(
            stage_id=stage_id, task_id=task_id,
            search_query_with_pagination_dto=search_query_with_pagination_dto)

        stage_permitted_user_roles = \
            self.stage_storage.get_stage_permitted_user_roles(
                stage_id=stage_id)
        is_no_stage_permitted_users = not stage_permitted_user_roles
        if is_no_stage_permitted_users:
            permitted_user_details_dtos = []
            user_id_with_team_details_dtos = []
            user_details_with_team_details_dto = UserDetailsWithTeamDetailsDTO(
                user_id_with_team_details_dtos=user_id_with_team_details_dtos,
                user_details_dtos=permitted_user_details_dtos)
            return user_details_with_team_details_dto

        user_details_with_team_details_dto = \
            self._get_user_details_with_team_details_dto_for_user_roles(
                user_roles=stage_permitted_user_roles, task_id=task_id,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto
            )
        return user_details_with_team_details_dto

    def _get_user_details_with_team_details_dto_for_user_roles(
            self, user_roles: List[str], task_id: str,
            search_query_with_pagination_dto: SearchQueryWithPaginationDTO
    ) -> UserDetailsWithTeamDetailsDTO:

        project_id = self.task_storage.get_project_id_for_task_display_id(
            task_display_id=task_id)

        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()

        permitted_user_details_dtos = service_adapter.auth_service. \
            get_user_details_for_the_given_role_ids_based_on_query(
                role_ids=user_roles, project_id=project_id,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto)
        permitted_user_ids = [permitted_user_details_dto.user_id
                              for permitted_user_details_dto in
                              permitted_user_details_dtos]

        user_id_with_team_details_dtos = service_adapter.auth_service. \
            get_team_info_for_given_user_ids(
                user_ids=permitted_user_ids, project_id=project_id)
        user_details_with_team_details_dto = UserDetailsWithTeamDetailsDTO(
            user_id_with_team_details_dtos=user_id_with_team_details_dtos,
            user_details_dtos=permitted_user_details_dtos)
        return user_details_with_team_details_dto

    def _make_validations(
            self, stage_id: int, task_id: str,
            search_query_with_pagination_dto: SearchQueryWithPaginationDTO):

        self._validations_of_limit_and_offset(
            limit=search_query_with_pagination_dto.limit,
            offset=search_query_with_pagination_dto.offset)

        is_valid_task_display_id = \
            self.task_storage.check_is_valid_task_display_id(
                task_display_id=task_id)
        is_invalid_task_display_id = not is_valid_task_display_id
        if is_invalid_task_display_id:
            raise InvalidTaskDisplayId(task_display_id=task_id)

        is_valid_stage_id = self.check_is_valid_stage_id(stage_id=stage_id)
        is_invalid_stage_id = not is_valid_stage_id
        if is_invalid_stage_id:
            raise InvalidStageId(stage_id)

    @staticmethod
    def _validations_of_limit_and_offset(offset: int, limit: int):
        is_invalid_limit = limit < 1
        if is_invalid_limit:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                LimitShouldBeGreaterThanZeroException
            raise LimitShouldBeGreaterThanZeroException

        is_invalid_offset = offset < 0
        if is_invalid_offset:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                OffsetShouldBeGreaterThanOrEqualToZeroException
            raise OffsetShouldBeGreaterThanOrEqualToZeroException
