import json
from django.http import response
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import GetTaskPresenterInterface


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

    def get_task_response(self, task_details_dto):
        pass