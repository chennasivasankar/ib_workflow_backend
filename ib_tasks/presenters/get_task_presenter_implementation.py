import json
from django.http import response
from typing import List
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import GetTaskPresenterInterface
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import TaskCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskGoFFieldDTO


class GetTaskPresenterImplementation(GetTaskPresenterInterface):

    def raise_exception_for_invalid_task_id(self, err: InvalidTaskIdException):
        from ib_tasks.constants.exception_messages import INVALID_TASK_ID
        task_id = err.task_id
        response_message = INVALID_TASK_ID[0].format(task_id)
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 404,
                "res_status": INVALID_TASK_ID[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object

    def get_task_response(self, task_complete_details_dto: TaskCompleteDetailsDTO):
        task_details_dict = {}
        task_details_dto = task_complete_details_dto.task_details_dto
        task_details_dict["task_id"] = task_complete_details_dto.task_id
        task_details_dict["template_id"] = task_details_dto.template_id
        task_gof_dtos = task_details_dto.task_gof_dtos
        task_gof_field_dtos = task_details_dto.task_gof_field_dtos
        gofs = []
        for task_gof_dto in task_gof_dtos:
            task_gof_id = task_gof_dto.task_gof_id
            gof_fields = self._get_gof_fields(task_gof_id, task_gof_field_dtos)
            gofs.append(gof_fields)
        task_details_dict["gofs"] = gofs
        data = json.dumps(task_details_dict)
        response_object = response.HttpResponse(data)
        return response_object

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
