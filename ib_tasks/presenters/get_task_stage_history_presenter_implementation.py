from datetime import datetime
from typing import List
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from ib_tasks.adapters.dtos import AssigneeDetailsDTO
from ib_tasks.constants.constants import DATETIME_FORMAT
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.presenter_interfaces.get_task_stages_history_presenter_interface import \
    GetTaskStagePresenterInterface
from ib_tasks.interactors.stages_dtos import TaskStageCompleteDetailsDTO, StageMinimalDTO, LogDurationDTO


class GetTaskStageHistoryPresenterImplementation(
        GetTaskStagePresenterInterface, HTTPResponseMixin):

    def raise_exception_for_invalid_task_id(self, err: InvalidTaskIdException):
        from ib_tasks.constants.exception_messages import INVALID_TASK_ID
        task_id = err.task_id
        response_message = INVALID_TASK_ID[0].format(task_id)
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_TASK_ID[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object


    def get_task_stages_history_response(
            self, task_stages_details_dto: TaskStageCompleteDetailsDTO):

        stage_dtos = task_stages_details_dto.stage_dtos
        assignee_dtos = task_stages_details_dto.assignee_details
        log_duration_dtos = task_stages_details_dto.log_duration_dtos
        task_stage_dtos = task_stages_details_dto.task_stage_dtos
        stages_details = self._get_stage_details(stage_dtos)
        assignee_dto_dict = self._get_assignee_dto_dict(assignee_dtos)
        log_duration_dict = self._get_log_duration_dict(log_duration_dtos)

        task_stages_dict = {
          "stages_details": stages_details,
          "stages_history": [
            {
              "stage_id": task_stage_dto.stage_id,
              "created_at": str(task_stage_dto.started_at),
              "time_spent_by_user": log_duration_dict[task_stage_dto.log_id],
              "stage_time": task_stage_dto.stage_duration.total_seconds(),
              "user_details": self._get_assignee_dict(
                  assignee_dto_dict[task_stage_dto.assignee_id]
              )
            }
            for task_stage_dto in task_stage_dtos
          ]
        }
        response_object = self.prepare_200_success_response(
            response_dict=task_stages_dict
        )
        return response_object

    @staticmethod
    def _get_assignee_dict(assignee_dto: AssigneeDetailsDTO):

        return {
            "user_id": assignee_dto.assignee_id,
            "profile_pic_url": assignee_dto.profile_pic_url,
            "name": assignee_dto.name
        }

    @staticmethod
    def _get_log_duration_dict(log_duration_dtos: List[LogDurationDTO]):

        from collections import defaultdict
        log_duration_dict = defaultdict()

        for log_duration in log_duration_dtos:
            log_id = log_duration.entity_id
            stage_duration = log_duration.duration
            log_duration_dict[log_id] = stage_duration.total_seconds()
        return log_duration_dict

    @staticmethod
    def _get_assignee_dto_dict(
            assignee_dtos: List[AssigneeDetailsDTO]):

        from collections import defaultdict
        assignee_dto_dict = defaultdict()

        for assignee_dto in assignee_dtos:
            assignee_id = assignee_dto.assignee_id
            assignee_dto_dict[assignee_id] = assignee_dto
        return assignee_dto_dict

    @staticmethod
    def _get_stage_details(stage_dtos: List[StageMinimalDTO]):

        return [
            {
                "stage_id": stage_dto.stage_id,
                "name": stage_dto.name,
                "color": stage_dto.color
            }
            for stage_dto in stage_dtos
        ]


