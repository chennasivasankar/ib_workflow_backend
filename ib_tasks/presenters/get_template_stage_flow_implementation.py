from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateDBId
from ib_tasks.interactors.presenter_interfaces.get_template_stage_flow_presenter_interface import \
    GetTemplateStageFlowPresenterInterface, StageFlowCompleteDetailsDTO
from ib_tasks.interactors.stages_dtos import StageMinimalDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageFlowDTO


class GetTemplateStageFlowPresenterImplementation(
        GetTemplateStageFlowPresenterInterface, HTTPResponseMixin):

    def raise_invalid_task_template_id(self, err: InvalidTaskTemplateDBId):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_TEMPLATE_DB_ID
        response_message = INVALID_TASK_TEMPLATE_DB_ID[0].format(
            err.task_template_id)
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_TASK_TEMPLATE_DB_ID[1]
        }
        return self.prepare_404_not_found_response(data)

    def get_response_for_invalid_project_id(
            self, err: InvalidProjectIdsException):
        from ib_tasks.constants.exception_messages import INVALID_PROJECT_ID
        project_id = err.invalid_project_ids[0]
        message = INVALID_PROJECT_ID[0].format(project_id)
        response_dict = {
            "response": message,
            "http_status_code": 404,
            "res_status": INVALID_PROJECT_ID[1]
        }

        response_object = self.prepare_404_not_found_response(response_dict)
        return response_object

    def get_response_for_user_not_in_project(self):
        from ib_tasks.constants.exception_messages import USER_NOT_IN_PROJECT
        response_dict = {
            "response": USER_NOT_IN_PROJECT[0],
            "http_status_code": 404,
            "res_status": USER_NOT_IN_PROJECT[1]
        }

        response_object = self.prepare_403_forbidden_response(response_dict)
        return response_object
    
    def get_response_for_template_stage_flow(
            self, stage_flow_complete_details_dto: StageFlowCompleteDetailsDTO
    ):

        stage_dtos = stage_flow_complete_details_dto.stage_dtos
        stage_flow_dtos = stage_flow_complete_details_dto.stage_flow_dtos
        response_dict = {
            "stages": self._convert_stage_dtos_to_stages_dict(stage_dtos),
            "actions": self._convert_stage_flow_dtos_to_stage_flows_dict(stage_flow_dtos)
        }
        response_object = self.prepare_200_success_response(response_dict)
        return response_object

    @staticmethod
    def _convert_stage_flow_dtos_to_stage_flows_dict(
            stage_flow_dtos: List[StageFlowDTO]):
        return [
            {
                "previous_stage": stage_flow_dto.previous_stage_id,
                "action_name": stage_flow_dto.action_name,
                "next_stage": stage_flow_dto.next_stage_id
            }
            for stage_flow_dto in stage_flow_dtos
        ]

    @staticmethod
    def _convert_stage_dtos_to_stages_dict(
            stage_dtos: List[StageMinimalDTO]
    ):

        return [
            {
                "stage_id": stage_dto.stage_id,
                "name": stage_dto.name,
                "color": stage_dto.color
            }
            for stage_dto in stage_dtos
        ]