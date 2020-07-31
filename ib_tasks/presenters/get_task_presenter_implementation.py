import json
from django.http import response
from typing import List
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import GetTaskPresenterInterface
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import TaskCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskGoFFieldDTO, TaskGoFDTO
from ib_tasks.interactors.task_dtos import TaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO


class GetTaskPresenterImplementation(GetTaskPresenterInterface, HTTPResponseMixin):

    def raise_exception_for_invalid_task_id(self, err: InvalidTaskIdException):
        from ib_tasks.constants.exception_messages import INVALID_TASK_ID
        task_id = err.task_id
        print("task_uid = ", task_id)
        response_message = INVALID_TASK_ID[0].format(task_id)
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_TASK_ID[1]
        }
        response_object = self.prepare_404_not_found_response(response_dict=data)
        return response_object

    def get_task_response(self, task_complete_details_dto: TaskCompleteDetailsDTO):
        task_details_dto = task_complete_details_dto.task_details_dto
        task_gof_dtos = task_details_dto.task_gof_dtos
        task_gof_field_dtos = task_details_dto.task_gof_field_dtos
        gofs = self._get_task_gofs(task_gof_dtos, task_gof_field_dtos)
        task_stage_complete_details_dtos = \
            task_complete_details_dto.task_stages_complete_details_dtos
        stages_with_actions = self._get_task_satges_with_actions_details(
            task_stage_complete_details_dtos
        )
        task_details_dict = {
            "task_id": task_complete_details_dto.task_id,
            "template_id": task_details_dto.template_id,
            "gofs": gofs,
            "stages_with_actions": stages_with_actions
        }
        response_object = self.prepare_200_success_response(response_dict=task_details_dict)
        return response_object

    def _get_task_satges_with_actions_details(
            self,
            task_stage_complete_details_dtos: List[TaskStageCompleteDetailsDTO]
    ):
        stages_with_actions = []
        for task_stage_complete_details_dto in task_stage_complete_details_dtos:
            stage_details_dto = task_stage_complete_details_dto.stage_details_dto
            actions_dtos = task_stage_complete_details_dto.actions_dtos
            actions = self._get_action_details(actions_dtos)
            stage_details_dict = {
                "stage_id": stage_details_dto.stage_id,
                "stage_display_name": stage_details_dto.name,
                "actions": actions
            }
            stages_with_actions.append(stage_details_dict)
        return stages_with_actions

    def _get_action_details(self, actions_dtos: List[ActionDTO]):
        actions = []
        for actions_dto in actions_dtos:
            action = {
                "action_id": actions_dto.action_id,
                "button_text": actions_dto.button_text,
                "button_color": actions_dto.button_color
            }
            actions.append(action)
        return actions

    def _get_task_gofs(
            self, task_gof_dtos: List[TaskGoFDTO], task_gof_field_dtos: List[TaskGoFFieldDTO]
    ):
        gofs = []
        for task_gof_dto in task_gof_dtos:
            task_gof_id = task_gof_dto.task_gof_id
            gof_fields = self._get_gof_fields(task_gof_id, task_gof_field_dtos)
            gof = {
                "gof_id": task_gof_dto.gof_id,
                "same_gof_order": task_gof_dto.same_gof_order,
                "gof_fields": gof_fields
            }
            gofs.append(gof)
        return gofs

    def _get_gof_fields(
            self, task_gof_id: int, task_gof_field_dtos: List[TaskGoFFieldDTO]
    ):
        gof_fields = []
        for task_gof_field_dto in task_gof_field_dtos:
            if task_gof_id == task_gof_field_dto.task_gof_id:
                field_dict = {
                    "field_id": task_gof_field_dto.field_id,
                    "field_response": task_gof_field_dto.field_response
                }
                gof_fields.append(field_dict)
        return gof_fields
