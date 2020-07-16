from django.http import response
from typing import List

from ib_boards.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import TaskFieldsDTO, TaskActionsDTO


class PresenterImplementation(PresenterInterface):
    def get_response_for_task_details(self,
                                      task_fields_dto: List[TaskFieldsDTO],
                                      task_actions_dto: List[TaskActionsDTO],
                                      task_ids: List[str]) -> response.HttpResponse:

        task_details_list = self._convert_task_details_into_list_of_dicts(
            task_ids=task_ids, task_fields_dto=task_fields_dto,
            task_actions_dto=task_actions_dto
        )
        import json
        data = json.dumps(task_details_list)
        response_object = response.HttpResponse(
            data, status=200
        )
        return response_object

    def _convert_task_details_into_list_of_dicts(self,
                                                 task_fields_dto: List[TaskFieldsDTO],
                                                 task_actions_dto: List[TaskActionsDTO],
                                                 task_ids: List[str]
                                                 ):
        return {}


    def _convert_task_actions_dtos_into_list_of_dict(self,
                                                     task_actions_dto: List[TaskActionsDTO]):
        list_of_task_actions = []
        for action_dto in task_actions_dto:
            list_of_task_actions.append(
                {
                    "action_id": action_dto.action_id,
                    "name": action_dto.name,
                    "button_text": action_dto.button_text,
                    "button_color": action_dto.button_color
            }
            )
        return list_of_task_actions


    def _convert_task_fields_dtos_into_list_of_dict(self,
                                                    task_fields_dto: List[TaskFieldsDTO]):
        list_of_task_fields = []
        for field_dto in task_fields_dto:
            list_of_task_fields.append(
                {
                    "field_type": field_dto.field_type,
                    "key": field_dto.key,
                    "value": field_dto.value
            }
            )
        return list_of_task_fields