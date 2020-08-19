from typing import List

from ib_tasks.adapters.dtos import AssigneeDetailsDTO
from ib_tasks.constants.constants import STAGE_TYPE
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException, \
    InvalidTaskDisplayId
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin \
    import GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.presenter_interfaces\
    .get_task_stages_history_presenter_interface \
    import GetTaskStagePresenterInterface
from ib_tasks.interactors.stages_dtos import TaskStageHistoryDTO, EntityTypeDTO, \
    LogDurationDTO, TaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface


class GetTaskStagesHistory(GetTaskIdForTaskDisplayIdMixin):

    def __init__(self, stage_storage: TaskStageStorageInterface,
                 task_storage: TaskStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def get_task_stages_history_wrapper(
            self, task_display_id: str, presenter: GetTaskStagePresenterInterface
    ):

        try:
            task_id = self.get_task_id_for_task_display_id(
                task_display_id=task_display_id)
            task_stages_details = \
                self._get_task_stages_log_history(task_id=task_id)
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_task_display_id(err)
        except InvalidTaskIdException as err:
            return presenter.raise_exception_for_invalid_task_id(err=err)
        return presenter.get_task_stages_history_response(
            task_stages_details_dto=task_stages_details
        )

    def _get_task_stages_log_history(self, task_id: int):

        self._validate_task_id(task_id=task_id)
        task_stages_dto = \
            self._get_task_stages_history(task_id)
        stage_ids = self._get_stage_ids(task_stages_dto)
        stage_dtos = self.stage_storage.get_stage_details(stage_ids)
        log_duration_dtos = self._get_log_duration_dtos(task_stages_dto)
        updated_task_stage_dtos = \
            self._get_updated_task_stage_dtos(task_stages_dto)
        user_ids = self._get_user_ids(task_stages_dto)
        user_dtos = self._get_user_details_dtos(user_ids)
        return TaskStageCompleteDetailsDTO(
            stage_dtos=stage_dtos,
            task_stage_dtos=updated_task_stage_dtos,
            log_duration_dtos=log_duration_dtos,
            assignee_details=user_dtos
        )

    @staticmethod
    def _get_stage_ids(task_stages_dto: List[TaskStageHistoryDTO]
                       ) -> List[int]:

        return list({
            task_stage.stage_id
            for task_stage in task_stages_dto
        })

    @staticmethod
    def _get_user_details_dtos(
            user_ids: List[str]) -> List[AssigneeDetailsDTO]:

        from ib_tasks.adapters.service_adapter import get_service_adapter
        adapter = get_service_adapter()
        log_duration_dtos = adapter.assignee_details_service \
            .get_assignees_details_dtos(assignee_ids=user_ids)
        return log_duration_dtos

    @staticmethod
    def _get_user_ids(
            task_stage_dtos: List[TaskStageHistoryDTO]
    ) -> List[str]:

        return list({
            task_stage_dto.assignee_id
            for task_stage_dto in task_stage_dtos
        })

    def _get_updated_task_stage_dtos(
            self, task_stage_dtos: List[TaskStageHistoryDTO]
    ) -> List[TaskStageHistoryDTO]:

        updated_dtos = []
        for task_stage_dto in task_stage_dtos:
            if task_stage_dto.left_at is None:
                updated_dtos.append(self._differ_current_datetime(task_stage_dto))
            else:
                updated_dtos.append(self._differ_left_at_datetime(task_stage_dto))
        return updated_dtos

    @staticmethod
    def _differ_current_datetime(task_stage_dto: TaskStageHistoryDTO):

        from datetime import datetime
        current_datetime = datetime.now()
        differ_time = current_datetime - task_stage_dto.started_at
        task_stage_dto.stage_duration = differ_time
        return task_stage_dto

    @staticmethod
    def _differ_left_at_datetime(task_stage_dto: TaskStageHistoryDTO):

        differ_time = task_stage_dto.left_at - task_stage_dto.started_at
        task_stage_dto.stage_duration = differ_time
        return task_stage_dto

    @staticmethod
    def _get_log_duration_dict(log_duration_dtos: List[LogDurationDTO]):

        from collections import defaultdict
        log_duration_dict = defaultdict()

        for log_duration_dto in log_duration_dtos:
            log_id = log_duration_dto.entity_id
            duration = log_duration_dto.duration
            log_duration_dict[log_id] = duration
        return log_duration_dict

    @staticmethod
    def _get_log_duration_dtos(
            task_stages_dto: List[TaskStageHistoryDTO]
    ) -> List[LogDurationDTO]:

        entity_dtos = [
            EntityTypeDTO(
                entity_id=task_stage_dto.log_id,
                entity_type=STAGE_TYPE
            )
            for task_stage_dto in task_stages_dto
        ]
        from ib_tasks.adapters.service_adapter import get_service_adapter
        adapter = get_service_adapter()
        log_duration_dtos = adapter.assignee_details_service\
            .get_log_duration_dtos(entity_dtos=entity_dtos)
        return log_duration_dtos

    def _get_task_stages_history(
            self, task_id: int) -> List[TaskStageHistoryDTO]:

        return self.stage_storage.get_task_stage_dtos(task_id=task_id)

    def _validate_task_id(self, task_id: int):

        is_invalid_task = \
            not self.task_storage.check_is_task_exists(task_id=task_id)
        if is_invalid_task:
            raise InvalidTaskIdException(task_id=task_id)