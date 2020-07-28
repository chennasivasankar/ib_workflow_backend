from dataclasses import dataclass
from typing import List

from ib_tasks.exceptions.fields_custom_exceptions import \
    LimitShouldBeGreaterThanZeroException, \
    OffsetShouldBeGreaterThanOrEqualToMinusOneException
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsListEmptyException, InvalidStageIdsListException
from ib_tasks.interactors.presenter_interfaces.get_all_tasks_overview_for_user_presenter_interface import \
    GetAllTasksOverviewForUserPresenterInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


@dataclass
class UserIdPaginationDTO:
    user_id: str
    limit: int
    offset: int


class GetAllTasksOverviewForUserInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def get_all_tasks_overview_for_user_wrapper(
            self, user_id_with_pagination_dto: UserIdPaginationDTO,
            presenter: GetAllTasksOverviewForUserPresenterInterface):
        try:
            self.get_all_tasks_overview_for_user(user_id_with_pagination_dto)
        except StageIdsListEmptyException:
            return presenter.raise_stage_ids_empty_exception()

        except LimitShouldBeGreaterThanZeroException:
            return presenter.raise_limit_should_be_greater_than_zero_exception(
            )

        except OffsetShouldBeGreaterThanOrEqualToMinusOneException:
            return presenter. \
                raise_offset_should_be_greater_than_or_equal_to_minus_one_exception(
            )

        except InvalidStageIdsListException as exception:
            return presenter.raise_invalid_stage_ids(
                invalid_stage_ids=exception.invalid_stage_ids)

    def get_all_tasks_overview_for_user(
            self, user_id_with_pagination_dto: UserIdPaginationDTO):
        user_id = user_id_with_pagination_dto.user_id
        stage_ids = self._get_allowed_stage_ids_of_user(user_id=user_id)
        from ib_tasks.interactors.stages_dtos import \
            UserStagesWithPaginationDTO
        user_stages_with_pagination_dto = UserStagesWithPaginationDTO(
            stage_ids=stage_ids,
            user_id=user_id,
            limit=user_id_with_pagination_dto.limit,
            offset=user_id_with_pagination_dto.offset)
        task_id_with_stage_details_dtos = self._get_task_ids_of_user(
            user_stages_with_pagination_dto)

    def _get_allowed_stage_ids_of_user(self, user_id: str) -> List[str]:
        from ib_tasks.interactors.get_allowed_stage_ids_of_user_interactor \
            import \
            GetAllowedStageIdsOfUserInteractor
        get_allowed_stage_ids_of_user_interactor \
            = GetAllowedStageIdsOfUserInteractor(storage=self.stage_storage)
        stage_ids = get_allowed_stage_ids_of_user_interactor.get_allowed_stage_ids_of_user(
            user_id=user_id)
        return stage_ids

    def _get_task_ids_of_user(
            self, user_stages_with_pagination_dto
    ) -> List[TaskIdWithStageDetailsDTO]:
        from ib_tasks.interactors. \
            get_task_ids_of_user_based_on_stage_ids_interactor import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        get_task_ids_of_user_based_on_stage_ids_interactor = \
            GetTaskIdsOfUserBasedOnStagesInteractor(
                stage_storage=self.stage_storage,
                task_storage=self.task_storage)
        task_id_with_stage_details_dtos = \
            get_task_ids_of_user_based_on_stage_ids_interactor. \
                get_task_ids_of_user_based_on_stage_ids(
                user_stages_with_pagination_dto=
                user_stages_with_pagination_dto)
        return task_id_with_stage_details_dtos
