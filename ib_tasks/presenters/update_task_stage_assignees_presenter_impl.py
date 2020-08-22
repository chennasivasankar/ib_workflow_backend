from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.interactors.presenter_interfaces \
    .update_task_stage_assignees_presenter_interface import \
    UpdateTaskStageAssigneesPresenterInterface


class UpdateTaskStageAssigneesPresenterImplementation(
    UpdateTaskStageAssigneesPresenterInterface, HTTPResponseMixin
):

    def raise_invalid_task_display_id(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_DISPLAY_ID
        message = INVALID_TASK_DISPLAY_ID[0].format(err.task_display_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_DISPLAY_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_duplicate_stage_ids_not_valid(self,
                                            duplicate_stage_ids: List[int]):
        from ib_tasks.constants.exception_messages import DUPLICATE_STAGE_IDS
        response_dict = {
            "response": DUPLICATE_STAGE_IDS[0].format(duplicate_stage_ids),
            "http_status_code": 400,
            "res_status": DUPLICATE_STAGE_IDS[1]
        }
        response_object = self.prepare_400_bad_request_response(response_dict)
        return response_object

    def raise_invalid_task_id_exception(self, task_id: int):
        from ib_tasks.constants.exception_messages import INVALID_TASK_ID
        response_dict = {
            "response": INVALID_TASK_ID[0].format(task_id),
            "http_status_code": 404,
            "res_status": INVALID_TASK_ID[1]
        }
        response_object = self.prepare_404_not_found_response(response_dict)
        return response_object

    def raise_invalid_stage_ids_exception(self,
                                          invalid_stage_ids: List[int]):
        from ib_tasks.constants.exception_messages import INVALID_STAGE_IDS
        response_dict = {
            "response": INVALID_STAGE_IDS[0].format(invalid_stage_ids),
            "http_status_code": 404,
            "res_status": INVALID_STAGE_IDS[1]
        }
        response_object = self.prepare_404_not_found_response(response_dict)
        return response_object

    def raise_virtual_stage_ids_exception(self, virtual_stage_ids: List[int]):
        from ib_tasks.constants.exception_messages import VIRTUAL_STAGE_IDS
        response_dict = {
            "response": VIRTUAL_STAGE_IDS[0].format(virtual_stage_ids),
            "http_status_code": 400,
            "res_status": VIRTUAL_STAGE_IDS[1]
        }
        response_object = self.prepare_400_bad_request_response(response_dict)
        return response_object

    def raise_invalid_user_id_exception(self, user_id: str):
        from ib_tasks.constants.exception_messages import INVALID_USER_ID
        response_dict = {
            "response": INVALID_USER_ID[0].format(user_id),
            "http_status_code": 404,
            "res_status": INVALID_USER_ID[1]
        }
        response_object = self.prepare_404_not_found_response(response_dict)
        return response_object

    def raise_stage_ids_with_invalid_permission_for_assignee_exception(
            self, invalid_stage_ids: List[int]):
        from ib_tasks.constants.exception_messages import \
            STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE
        response_dict = {
            "response": STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE[0].
                format(invalid_stage_ids),
            "http_status_code": 400,
            "res_status": STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE[1]
        }
        response_object = self.prepare_400_bad_request_response(response_dict)
        return response_object
