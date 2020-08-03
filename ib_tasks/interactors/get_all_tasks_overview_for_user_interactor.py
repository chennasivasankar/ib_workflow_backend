from dataclasses import dataclass
from typing import List

from ib_tasks.exceptions.fields_custom_exceptions import \
    LimitShouldBeGreaterThanZeroException, \
    OffsetShouldBeGreaterThanZeroException
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsListEmptyException
from ib_tasks.interactors.presenter_interfaces.get_all_tasks_overview_for_user_presenter_interface import \
    GetAllTasksOverviewForUserPresenterInterface
from ib_tasks.interactors.stages_dtos import UserStagesWithPaginationDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageDetailsDTO, GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


@dataclass
class UserIdPaginationDTO:
    user_id: str
    limit: int
    offset: int


class GetAllTasksOverviewForUserInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 field_storage: FieldsStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.field_storage = field_storage

    def get_all_tasks_overview_for_user_wrapper(
            self, user_id_with_pagination_dto: UserIdPaginationDTO,
            presenter: GetAllTasksOverviewForUserPresenterInterface):
        try:
            all_tasks_overview_details_dto = self.get_all_tasks_overview_for_user(
                user_id_with_pagination_dto)
        except StageIdsListEmptyException:
            return presenter.raise_stage_ids_empty_exception()

        except LimitShouldBeGreaterThanZeroException:
            return presenter.raise_limit_should_be_greater_than_zero_exception(
            )

        except OffsetShouldBeGreaterThanZeroException:
            return presenter. \
                raise_offset_should_be_greater_than_zero_exception(
            )
        return presenter.all_tasks_overview_details_response(
            all_tasks_overview_details_dto)

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
        from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
        task_id_with_stage_id_dtos = [
            GetTaskDetailsDTO(
                stage_id=each_task_id_with_stage_details_dto.stage_id,
                task_id=each_task_id_with_stage_details_dto.task_id)
            for each_task_id_with_stage_details_dto in
            task_id_with_stage_details_dtos
        ]

        task_fields_and_action_details_dtos = self._get_task_fields_and_action(
            task_id_with_stage_id_dtos, user_id)
        from ib_tasks.interactors.presenter_interfaces.dtos import \
            AllTasksOverviewDetailsDTO
        all_tasks_overview_details_dto = AllTasksOverviewDetailsDTO(
            task_id_with_stage_details_dtos=task_id_with_stage_details_dtos,
            task_fields_and_action_details_dtos=
            task_fields_and_action_details_dtos)
        return all_tasks_overview_details_dto

    def _get_allowed_stage_ids_of_user(self, user_id: str) -> List[str]:
        from ib_tasks.interactors.get_allowed_stage_ids_of_user_interactor \
            import \
            GetAllowedStageIdsOfUserInteractor
        get_allowed_stage_ids_of_user_interactor \
            = GetAllowedStageIdsOfUserInteractor(storage=self.stage_storage)
        stage_ids = get_allowed_stage_ids_of_user_interactor. \
            get_allowed_stage_ids_of_user(user_id=user_id)
        return stage_ids

    def _get_task_ids_of_user(
            self, user_stages_with_pagination_dto: UserStagesWithPaginationDTO
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

    def _get_task_fields_and_action(
            self, task_id_with_stage_id_dtos: List[GetTaskDetailsDTO],
            user_id: str
    ) -> List[GetTaskStageCompleteDetailsDTO]:
        from ib_tasks.interactors.get_task_fields_and_actions import \
            GetTaskFieldsAndActionsInteractor
        get_task_fields_and_actions_interactor = \
            GetTaskFieldsAndActionsInteractor(stage_storage=self.stage_storage,
                                              storage=self.field_storage)
        task_details_dtos = get_task_fields_and_actions_interactor. \
            get_task_fields_and_action(task_dtos=task_id_with_stage_id_dtos,
                                       user_id=user_id)

        return task_details_dtos
